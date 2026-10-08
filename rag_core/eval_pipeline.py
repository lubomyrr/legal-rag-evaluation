"""Core RAG pipeline for retrieval, context assembly, and grounded generation."""
from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from openai import OpenAI, RateLimitError

from rag_core.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_DIR,
    CHROMA_HTTP_HOST,
    CHROMA_HTTP_PORT,
    CHROMA_USE_HTTP,
    EMBEDDING_BASE_URL,
    EMB_MODEL,
    LLM_API_KEY,
    LLM_BASE_URL,
    LLM_MODEL,
)
from rag_core.deterministic_core import normalize_zakon_id, safe_str
from rag_core.prompts import (
    JSON_RESPONSE_FORMAT,
    JSON_SCHEMA,
    SYSTEM_PROMPT_JSON,
    SYSTEM_PROMPT_JSON_COMPOSE,
    USER_TEMPLATE_JSON,
    USER_TEMPLATE_JSON_COMPOSE,
    ZAKON_ID_RE,
)

LOG = logging.getLogger(__name__)

_RE_DOTLINE = re.compile(r"(?m)^\s*\.\s*$")
_RE_ELLIPSIS = re.compile(r"(?:\u2026|\.{3,})")
_RE_HEADING_ANSWER = re.compile(r"^Odpoved\s*\n?", re.IGNORECASE)
_RE_LEGAL_BASIS_BLOCK = re.compile(r"\n+\s*Pravny zaklad\s*\n[\s\S]*\Z", re.IGNORECASE)


class StructuredOutputError(ValueError):
    def __init__(self, raw_answer: str, message: str):
        super().__init__(message)
        self.raw_answer = raw_answer


def _mlflow_trace(name: str):
    # Tracing decorator for MLflow.
    try:
        import mlflow

        return mlflow.trace(name=name)
    except Exception:
        def _noop(fn):
            return fn
        return _noop


# Small helpers for safe parsing and text cleanup.
def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def build_citation_law_id(law_name: Any, paragraph: Any) -> str:
    law_s = re.sub(r"\s+", "", safe_str(law_name).strip())
    par_s = re.sub(r"\s+", "", safe_str(paragraph).strip().lower())
    if par_s.startswith("paragraf-"):
        par_s = par_s[len("paragraf-"):]
    if not law_s or not par_s:
        return ""
    return f"{law_s}/paragraf-{par_s}"


def provision_doc_id_from_meta(meta: Optional[Dict[str, Any]]) -> str:
    meta = meta or {}
    raw_doc_id = safe_str(meta.get("doc_id")).strip()
    if ZAKON_ID_RE.fullmatch(raw_doc_id):
        return raw_doc_id
    return build_citation_law_id(meta.get("law_name"), meta.get("paragraph"))


def _normalize_citacie_json_items(payload: Any) -> List[Dict[str, str]]:
    if not isinstance(payload, list):
        raise ValueError("citacie_json output must be a JSON array")

    normalized: List[Dict[str, str]] = []
    seen: set[Tuple[str, str]] = set()
    required_keys = {"zakon", "odpoved_vygenerovana"}

    for item in payload:
        if not isinstance(item, dict):
            raise ValueError("Each citacie_json item must be an object")
        if set(item) != required_keys:
            raise ValueError(
                "Each citacie_json item must contain only zakon and odpoved_vygenerovana"
            )

        zakon = safe_str(item.get("zakon")).strip()
        odpoved = safe_str(item.get("odpoved_vygenerovana")).strip()

        if not ZAKON_ID_RE.fullmatch(zakon):
            raise ValueError(f"Invalid zakon value: {zakon}")
        if not odpoved:
            raise ValueError("odpoved_vygenerovana must not be empty")
        if len(odpoved) > 500:
            raise ValueError("odpoved_vygenerovana is too long")

        dedup_key = (zakon, odpoved)
        if dedup_key in seen:
            continue
        seen.add(dedup_key)
        normalized.append(
            {
                "zakon": zakon,
                "odpoved_vygenerovana": odpoved,
            }
        )

    return normalized


def _strip_json_code_fence(raw_answer: str) -> str:
    text = safe_str(raw_answer).strip()
    if not text.startswith("```"):
        return text
    lines = text.splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    text = "\n".join(lines).strip()
    if text.lower().startswith("json"):
        text = text[4:].lstrip()
    return text.strip()


def parse_citacie_json_payload(raw_answer: str) -> Dict[str, Any]:
    payload = json.loads(_strip_json_code_fence(raw_answer))
    if isinstance(payload, list):
        return {"citacie_json": _normalize_citacie_json_items(payload)}
    if not isinstance(payload, dict):
        raise ValueError("citacie_json output must be a JSON object")
    return {"citacie_json": _normalize_citacie_json_items(payload.get("citacie_json") or [])}


def is_refusal_text(answer: str) -> bool:
    answer_low = safe_str(answer).strip().lower()
    return (not answer_low) or (
        "insufficient data" in answer_low
        or "nedostatok" in answer_low
        or "neviem" in answer_low
    )


def sanitize_context_text(text: str) -> str:
    text = safe_str(text).replace("\r\n", "\n").replace("\r", "\n")
    text = _RE_DOTLINE.sub("", text)
    text = _RE_ELLIPSIS.sub(" ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def cleanup_text_answer(answer: str) -> str:
    cleaned = safe_str(answer).strip()
    cleaned = _RE_HEADING_ANSWER.sub("", cleaned, count=1)
    cleaned = _RE_LEGAL_BASIS_BLOCK.sub("", cleaned).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


# Embedding client used to encode the user question for retrieval.
@dataclass(frozen=True)
class LocalEmbeddingClient:
    base_url: str
    model: str
    timeout_s: int = 60

    @_mlflow_trace("embed_batch")
    def embed(self, texts: List[str]) -> List[List[float]]:
        payload = {"model": self.model, "input": texts if len(texts) != 1 else texts[0]}
        url = f"{self.base_url}/api/embed"

        try:
            import requests

            resp = requests.post(url, json=payload, timeout=self.timeout_s)
            resp.raise_for_status()
            data = resp.json()
        except Exception:
            import urllib.request

            req = urllib.request.Request(
                url=url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=self.timeout_s) as response:
                data = json.loads(response.read().decode("utf-8"))

        embeddings = data.get("embeddings")
        if not isinstance(embeddings, list) or not embeddings:
            raise ValueError(f"Unexpected embeddings response: {data}")

        output: List[List[float]] = []
        for vector in embeddings:
            if not isinstance(vector, list):
                raise ValueError(f"Unexpected embedding element type: {type(vector)}")
            output.append([float(value) for value in vector])
        return output


@lru_cache(maxsize=1)
def get_embedding_client() -> LocalEmbeddingClient:
    return LocalEmbeddingClient(base_url=EMBEDDING_BASE_URL, model=EMB_MODEL)


@_mlflow_trace("embed_query")
def embed_query(text: str) -> List[float]:
    return get_embedding_client().embed([safe_str(text)])[0]


# Chroma access and top-k retrieval.
@_mlflow_trace("chroma_client")
def get_chroma_client():
    import chromadb

    if CHROMA_USE_HTTP:
        print(f"[INFO] Opening Chroma HTTP client at http://{CHROMA_HTTP_HOST}:{CHROMA_HTTP_PORT}")
        return chromadb.HttpClient(host=CHROMA_HTTP_HOST, port=CHROMA_HTTP_PORT)

    chroma_path = Path(CHROMA_DIR)
    if not chroma_path.exists():
        raise RuntimeError(f"Chroma directory not found: {chroma_path}")

    print(f"[INFO] Opening Chroma client at {chroma_path}")
    return chromadb.PersistentClient(path=str(chroma_path))


@_mlflow_trace("chroma_collection")
def get_chroma_collection():
    client = get_chroma_client()
    return client.get_collection(name=CHROMA_COLLECTION_NAME, embedding_function=None)


@_mlflow_trace("retriever_init")
def get_retriever():
    return get_chroma_collection()


@_mlflow_trace("retriever_query")
def retrieve(question: str, collection, k: int) -> List[Dict[str, Any]]:
    q_emb = embed_query(question)

    result = collection.query(
        query_embeddings=[q_emb],
        n_results=int(k),
        include=["documents", "metadatas", "distances"],
    )

    docs = (result.get("documents") or [[]])[0] or []
    metas = (result.get("metadatas") or [[]])[0] or []
    dists = (result.get("distances") or [[]])[0] or []
    ids_ = (result.get("ids") or [[]])[0] or []

    hits: List[Dict[str, Any]] = []
    for index, doc in enumerate(docs):
        hits.append(
            {
                "text": safe_str(doc),
                "meta": metas[index] if index < len(metas) else {},
                "distance": dists[index] if index < len(dists) else None,
                "id": ids_[index] if index < len(ids_) else None,
            }
        )
    return hits


# Build one clean LLM context from retrieved laws/provisions.
@_mlflow_trace("build_context")
def build_context(
    hits: List[Dict[str, Any]],
    *,
    max_selected: int = 4,
) -> Tuple[str, List[str], List[Dict[str, Any]]]:
    selected_hits: List[Dict[str, Any]] = []

    # Keep retrieved hits in rank order and skip only empty texts.
    for hit in hits or []:
        text = sanitize_context_text(safe_str(hit.get("text")))
        if not text:
            continue

        selected_hits.append(hit)
        if len(selected_hits) >= max_selected:
            break

    llm_blocks: List[str] = []
    context_texts: List[str] = []
    context_metas: List[Dict[str, Any]] = []

    #build final context for the model.
    for hit in selected_hits:
        meta = hit.get("meta") or {}
        text = sanitize_context_text(safe_str(hit.get("text")))
        if not text:
            continue

        zakon_id = provision_doc_id_from_meta(meta)
        doc_id = safe_str(meta.get("doc_id")).strip() or safe_str(hit.get("id")).strip()

        if zakon_id:
            block = f"ZAKON: {zakon_id}\nTEXT:\n{text}"
        elif doc_id:
            block = f"DOC_ID: {doc_id}\nTEXT:\n{text}"
        else:
            block = f"TEXT:\n{text}"

        llm_blocks.append(block)
        context_texts.append(text)

        output_meta = dict(meta)
        output_meta["distance"] = hit.get("distance")
        if zakon_id:
            output_meta["zakon_id"] = zakon_id
        context_metas.append(output_meta)

    llm_context = "\n\n---\n\n".join(llm_blocks).strip()
    return llm_context, context_texts, context_metas


# Shared OpenAI-compatible LLM call wrapper with retry logic.
@lru_cache(maxsize=1)
def get_llm_client() -> OpenAI:
    return OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)


def _chat_completion(messages: List[Dict[str, str]], *, format_schema: Optional[Dict[str, Any]] = None) -> str:
    import traceback
    last_err = None

    for attempt in range(4):
        try:
            client = get_llm_client()
            request_kwargs: Dict[str, Any] = {
                "model": LLM_MODEL,
                "messages": messages,
                "temperature": 0.0,
                "stop": None,
            }
            if format_schema is not None:
                request_kwargs["response_format"] = JSON_RESPONSE_FORMAT
            response = client.chat.completions.create(**request_kwargs)

            finish_reason = safe_str(response.choices[0].finish_reason).strip()
            if finish_reason:
                LOG.debug("LLM finish_reason: %s", finish_reason)

            return safe_str(response.choices[0].message.content).strip()
        except RateLimitError:
            time.sleep(4.0 * (attempt + 1))
        except Exception:
            last_err = traceback.format_exc()
            time.sleep(0.8 * (attempt + 1))
    raise RuntimeError(f"LLM call failed:\n{last_err}")

#one structured per-law answer block for each relevant retrieved provision
@_mlflow_trace("structured_generation")
def generate_structured_answer(question: str, context: str) -> Dict[str, Any]:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_JSON},
        {
            "role": "user",
            "content": USER_TEMPLATE_JSON.format(
                question=safe_str(question),
                context=safe_str(context),
            ),
        },
    ]
    raw_structured_answer = _chat_completion(messages, format_schema=JSON_SCHEMA)
    try:
        parsed_payload = parse_citacie_json_payload(raw_structured_answer)
    except (json.JSONDecodeError, ValueError) as exc:
        raise StructuredOutputError(raw_structured_answer, str(exc)) from exc
    return {
        "raw_structured_answer": raw_structured_answer,
        "citacie_json": parsed_payload.get("citacie_json") or [],
    }


# Composes one final user-facing answer from structured per-law blocks
@_mlflow_trace("final_answer_composition")
def compose_final_answer(question: str, citacie_json: List[Dict[str, str]]) -> str:
    blocks: List[str] = []
    for index, item in enumerate(citacie_json, start=1):
        text = safe_str(item.get("odpoved_vygenerovana")).strip()
        if text:
            blocks.append(f"[{index}] {text}")

    if not blocks:
        return "Insufficient data to verify"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_JSON_COMPOSE},
        {
            "role": "user",
            "content": USER_TEMPLATE_JSON_COMPOSE.format(
                question=safe_str(question).strip(),
                blocks="\n\n".join(blocks),
            ),
        },
    ]
    return _chat_completion(messages)



def _build_base_payload(
    llm_context: str,
    context_texts: List[str],
    context_metas: List[Dict[str, Any]],
    requested_k: int,
) -> Dict[str, Any]:
    # Payload fields consumed by eval_local.py and downstream scorers.
    return {
        "llm_context": llm_context,
        "context_texts": context_texts,
        "context_metas": context_metas,
        "k_requested": int(requested_k),
        "k_used": int(len(context_texts)),
    }


# Full prediction flow:
# retrieve -> build context -> structured generation -> final composition.
@_mlflow_trace("rag_pipeline")
def generate_rag_answer(
    *,
    question: str,
    retriever,
    retrieve_k: int,
) -> Dict[str, Any]:
    import traceback

    question_text = safe_str(question).strip()
    requested_k = max(1, safe_int(retrieve_k, 10))

    hits = retrieve(question_text, retriever, requested_k) or []
    llm_context, context_texts, context_metas = build_context(
        hits,
        max_selected=requested_k,
    )
    base_payload = _build_base_payload(llm_context, context_texts, context_metas, requested_k)
    empty_answer = "Insufficient data to verify"

    if not llm_context:
        return {
            "answer": empty_answer,
            "citacie_json": [],
            "raw_structured_answer": "",
            "raw_answer": "",
            "structured_response": json.dumps([], ensure_ascii=False),
            "status": "no_context",
            **base_payload,
        }

    raw_structured_answer = ""
    try:
        structured_pkg = generate_structured_answer(question_text, llm_context)
        raw_structured_answer = safe_str(structured_pkg.get("raw_structured_answer")).strip()
        citacie_json = structured_pkg.get("citacie_json") or []
        if not isinstance(citacie_json, list):
            citacie_json = []
    except StructuredOutputError as exc:
        raw_structured_answer = safe_str(exc.raw_answer).strip()
        return {
            "answer": empty_answer,
            "citacie_json": [],
            "raw_structured_answer": raw_structured_answer,
            "raw_answer": "",
            "structured_response": "",
            "status": "invalid_json",
            **base_payload,
        }
    except (json.JSONDecodeError, ValueError):
        return {
            "answer": empty_answer,
            "citacie_json": [],
            "raw_structured_answer": raw_structured_answer,
            "raw_answer": "",
            "structured_response": "",
            "status": "invalid_json",
            **base_payload,
        }
    except Exception:
        return {
            "answer": empty_answer,
            "citacie_json": [],
            "raw_structured_answer": raw_structured_answer,
            "raw_answer": "",
            "structured_response": "",
            "status": "exception",
            "exception": traceback.format_exc(),
            **base_payload,
        }

    if not citacie_json:
        return {
            "answer": empty_answer,
            "citacie_json": [],
            "raw_structured_answer": raw_structured_answer,
            "raw_answer": "",
            "structured_response": json.dumps([], ensure_ascii=False),
            "status": "empty_result",
            **base_payload,
        }

    composed_answer_text = ""
    status = "ok"
    try:
        composed_answer_text = compose_final_answer(question_text, citacie_json)
        answer = cleanup_text_answer(composed_answer_text) or empty_answer
        if is_refusal_text(answer):
            answer = empty_answer
            status = "compose_failed"
    except Exception:
        answer = empty_answer
        status = "compose_failed"

    return {
        "answer": answer,
        "citacie_json": citacie_json,
        "raw_structured_answer": raw_structured_answer,
        "raw_answer": composed_answer_text,
        "structured_response": json.dumps(citacie_json, ensure_ascii=False),
        "status": status,
        **base_payload,
    }


def SNAP(
    *,
    question: str,
    final_answer: str,
    retrieved_context: Any = None,
    citations: Any = None,
    llm_extract: Optional[Any] = None,
) -> Dict[str, Any]:
    """Minimal transferability snapshot for external legal RAG outputs.

    This is not part of the main experiment pipeline. It only documents the
    simple idea used in the thesis: another RAG output can be evaluated by the
    same metrics if it is converted to ``citacie_json``. If the external system
    has citations, they are normalized here. If it has no citations, an optional
    caller-provided ``llm_extract`` function may produce them.
    """
    raw_citations = citations
    if raw_citations is None and llm_extract is not None:
        raw_citations = llm_extract(question, final_answer, retrieved_context)

    if isinstance(raw_citations, dict):
        raw_citations = raw_citations.get("citacie_json") or raw_citations.get("citations") or []
    if not isinstance(raw_citations, list):
        raw_citations = []

    citacie_json: List[Dict[str, str]] = []
    seen: set[str] = set()
    for item in raw_citations:
        if not isinstance(item, dict):
            continue
        zakon = normalize_zakon_id(
            item.get("zakon")
            or item.get("zakon_id")
            or item.get("provision_id")
            or build_citation_law_id(item.get("law") or item.get("law_id"), item.get("paragraph") or item.get("paragraf"))
        )
        text = (
            safe_str(item.get("odpoved_vygenerovana")).strip()
            or safe_str(item.get("generated_text")).strip()
            or safe_str(item.get("answer_span")).strip()
            or safe_str(item.get("text")).strip()
        )
        if zakon and text and zakon not in seen:
            citacie_json.append({"zakon": zakon, "odpoved_vygenerovana": text})
            seen.add(zakon)

    context_docs: List[str] = []
    context_metas: List[Dict[str, Any]] = []
    raw_contexts = retrieved_context if isinstance(retrieved_context, list) else [retrieved_context]
    for item in raw_contexts:
        if item is None:
            continue
        if isinstance(item, dict):
            text = safe_str(item.get("text") or item.get("content") or item.get("document")).strip()
            meta = item.get("meta") or item.get("metadata") or {}
            meta_out = dict(meta) if isinstance(meta, dict) else {}
        else:
            text = safe_str(item).strip()
            meta_out = {}
        if text:
            context_docs.append(text)
            context_metas.append(meta_out)

    return {
        "question": safe_str(question).strip(),
        "answer": safe_str(final_answer).strip(),
        "citacie_json": citacie_json,
        "contexts": context_docs,
        "context_docs": context_docs,
        "context_metas": context_metas,
        "outputs": {
            "response": safe_str(final_answer).strip(),
            "citacie_json": citacie_json,
        },
        "status": "snap_external_rag",
    }
