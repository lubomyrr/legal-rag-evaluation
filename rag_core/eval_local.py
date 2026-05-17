"""Local evaluation runner for RAG pipeline"""
from __future__ import annotations

import argparse
import faulthandler
import json
import logging
import os
import re
import time
import traceback
import unicodedata
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

from dotenv import load_dotenv
from rag_core.eval_artifacts import (
    _log_triad_report,
    _write_core_artifacts,
    _write_metric1_selection_artifact,
    _write_metric2_span_faithfulness_artifact,
    _write_metric3_expected_alignment_artifact,
)

faulthandler.enable()
LOG = logging.getLogger("rag_core.eval")

EXTRA_INPUT_KEYS = (
    "case_number",
    "law_id",
    "paragraf_id",
    "effective_from",
    "effective_to",
    "jurisdiction",
    "language",
    "category",
    "type",
)

# General helpers
def _bool_env(name: str, default: bool = False) -> bool:
    """Parse boolean environment variables like 1/true/yes/on (case-insensitive)."""
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}



def _safe_mkdir(path: Path) -> None:
    """Create a directory if it doesn't exist (including parents)."""
    path.mkdir(parents=True, exist_ok=True)


def _resolve_env_path(env_file: str) -> Path:
    here = Path(__file__).resolve()
    root = here.parents[1]
    path = Path(env_file)
    if path.is_absolute():
        return path
    candidate = (root / path).resolve()
    return candidate if candidate.exists() else path


def _normalize_question_key(text: Any) -> str:
    raw = str(text or "")
    if not raw:
        return ""
    normalized = unicodedata.normalize("NFKC", raw)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized.lower()


def _parse_qid(value: Any, default: int = -1) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _format_context(docs: Any) -> str:
    if not isinstance(docs, list):
        return ""
    out: List[str] = []
    for i, doc in enumerate(docs, start=1):
        text = str(doc or "").strip().replace("\r", "")
        if not text:
            continue
        out.append(f"[{i}] {text}")
    return "\n\n".join(out)


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("mlflow.utils.git_utils").setLevel(logging.ERROR)
    logging.getLogger("git").setLevel(logging.ERROR)
    logging.getLogger("git.cmd").setLevel(logging.ERROR)
    os.environ.setdefault("GIT_PYTHON_REFRESH", "quiet")


# Dataset helpers
def _normalize_dataset_row(x: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "question": str(x.get("question") or "").strip(),
        "expected": str(x.get("expected") or "").strip(),
        "url": str(x.get("url") or "").strip(),
    }

def _load_questions_any(path: Path):
    import pandas as pd  # type: ignore

    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path, encoding="utf-8-sig")

    if suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        if isinstance(data, dict) and "data" in data:
            data = data["data"]
        if not isinstance(data, list):
            raise RuntimeError("JSON must be a list of objects")
        return pd.DataFrame([_normalize_dataset_row(x) for x in data if isinstance(x, dict)])

    if suffix == ".jsonl":
        rows = []
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            if isinstance(item, dict):
                rows.append(_normalize_dataset_row(item))
        return pd.DataFrame(rows)

    raise RuntimeError(f"Unsupported questions file type: {suffix}")


def _ensure_eval_columns(df) -> None:
    if "question" not in df.columns:
        raise RuntimeError(f"CSV must contain column: question. Got: {list(df.columns)}")
    if "expected" not in df.columns:
        df["expected"] = ""
    for key in EXTRA_INPUT_KEYS:
        if key not in df.columns:
            df[key] = ""

def _build_inputs_dict(row: Dict[str, Any], row_id: int) -> Dict[str, Any]:
    inputs = {
        "id": int(row_id),
        "question": str(row.get("question") or ""),
    }
    for key in EXTRA_INPUT_KEYS:
        inputs[key] = str(row.get(key) or "")
    return inputs

def _load_gold_provision_map(path: Path) -> Dict[str, Dict[str, Any]]:
    from rag_core.deterministic_core import build_zakon_id, extract_case_numbers, extract_gold_zakon_ids

    if not path.exists():
        return {}

    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict) and "data" in data:
        data = data["data"]
    if not isinstance(data, list):
        return {}

    out: Dict[str, Dict[str, Any]] = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        question = str(item.get("question") or "").strip()
        if not question:
            continue
        question_key = _normalize_question_key(question)
        provisions = item.get("provisions") or []
        expected = str(item.get("expected") or "")
        expected_statutes = sorted({
            str(p.get("paragraph")).strip()
            for p in provisions
            if isinstance(p, dict) and str(p.get("paragraph") or "").strip()
        })
        provisions_by_zakon: Dict[str, List[Dict[str, Any]]] = {}
        for provision in provisions:
            if not isinstance(provision, dict):
                continue
            zakon = build_zakon_id(provision.get("law"), provision.get("paragraph"))
            if not zakon:
                continue
            provisions_by_zakon.setdefault(zakon, []).append({
                "law": str(provision.get("law") or "").strip(),
                "paragraph": str(provision.get("paragraph") or "").strip(),
                "section": provision.get("section"),
                "fragment": str(provision.get("fragment") or "").strip(),
            })
        out[question_key] = {
            "gold_zakony": extract_gold_zakon_ids(provisions),
            "expected_statutes": expected_statutes,
            "expected_cases": extract_case_numbers(expected),
            "provisions_by_zakon": provisions_by_zakon,
        }
    return out
# MLflow genai fixes
def _patch_mlflow_genai_expectations_best_effort() -> None:
    try:
        import mlflow.genai.evaluation.harness as harness  # type: ignore
    except Exception:
        return

    orig = getattr(harness, "_get_new_expectations", None)
    if orig is None:
        return

    def _safe_get_new_expectations(eval_item):  # type: ignore[no-untyped-def]
        tr = getattr(eval_item, "trace", None)
        info = getattr(tr, "info", None) if tr is not None else None
        assessments = getattr(info, "assessments", None) if info is not None else None
        if not assessments:
            return []
        return orig(eval_item)

    harness._get_new_expectations = _safe_get_new_expectations  # type: ignore[attr-defined]


def _patch_mlflow_genai_log_trace_best_effort() -> None:
    try:
        import mlflow.genai.evaluation.harness as harness  # type: ignore
    except Exception:
        return

    candidates = [
        "_log_trace_and_assessments_to_mlflow",
        "_log_trace_and_assessments",
        "log_trace_and_assessments_to_mlflow",
    ]

    for name in candidates:
        orig = getattr(harness, name, None)
        if orig is None:
            continue

        def _safe(*args, **kwargs):  # type: ignore[no-untyped-def]
            try:
                return orig(*args, **kwargs)
            except Exception:
                return None

        try:
            setattr(harness, name, _safe)
            return
        except Exception:
            return


def _patch_mlflow_genai_trace_linking_best_effort() -> None:
    try:
        from mlflow.genai.utils import trace_utils  # type: ignore
    except Exception:
        return

    try:
        orig_batch_link = trace_utils.batch_link_traces_to_run  # type: ignore[attr-defined]
    except Exception:
        return

    def _safe_batch_link_traces_to_run(*, run_id: str, eval_results: list, **kwargs):  # type: ignore[no-untyped-def]
        safe_results = []
        for r in eval_results or []:
            try:
                ev_item = getattr(r, "eval_item", None)
                tr = getattr(ev_item, "trace", None)
                info = getattr(tr, "info", None) if tr is not None else None
                if info is None:
                    continue
                safe_results.append(r)
            except Exception:
                continue
        if not safe_results:
            return None
        return orig_batch_link(run_id=run_id, eval_results=safe_results, **kwargs)

    try:
        trace_utils.batch_link_traces_to_run = _safe_batch_link_traces_to_run  # type: ignore[attr-defined]
    except Exception:
        return

    try:
        import mlflow.genai.evaluation.harness as harness  # type: ignore

        harness.batch_link_traces_to_run = trace_utils.batch_link_traces_to_run  # type: ignore[attr-defined]
    except Exception:
        pass


# Prediction helpers
def _predict_fn_factory(
    *,
    retriever: Any,
    retrieve_k: int,
) -> Tuple[Callable[..., Dict[str, Any]], Dict[int, Dict[str, Any]]]:
    from rag_core.eval_pipeline import generate_rag_answer  # type: ignore

    cache_by_id: Dict[int, Dict[str, Any]] = {}
    import mlflow

    def predict_fn(*args: Any, **kwargs: Any) -> Dict[str, Any]:
        row0 = args[0] if args else None
        if isinstance(row0, dict) and "inputs" in row0 and isinstance(row0.get("inputs"), dict):
            inp = row0.get("inputs") or {}
        elif isinstance(row0, dict):
            inp = row0
        else:
            inp = kwargs

        qid = _parse_qid(inp.get("id", -1))
        if qid >= 0 and qid in cache_by_id:
            return cache_by_id[qid]

        question = str(inp.get("question") or "").strip()

        @mlflow.trace(name="rag_predict")
        def _run_one() -> Dict[str, Any]:
            t0 = time.perf_counter()
            try:
                pkg = generate_rag_answer(
                    question=question,
                    retriever=retriever,
                    retrieve_k=int(retrieve_k),
                )
            except Exception:
                pkg = {
                    "answer": "Insufficient data to verify",
                    "citacie_json": [],
                    "raw_structured_answer": "",
                    "raw_answer": "",
                    "structured_response": "",
                    "context_texts": [],
                    "context_metas": [],
                    "llm_context": "",
                    "k_used": int(retrieve_k),
                    "status": "exception",
                    "exception": traceback.format_exc(),
                }

            latency_s = float(time.perf_counter() - t0)

            answer_text = str(pkg.get("answer") or "").strip() or "Insufficient data to verify"
            citacie_json = pkg.get("citacie_json") or []
            if not isinstance(citacie_json, list):
                citacie_json = []
            context_texts = pkg.get("context_texts") or []
            if not isinstance(context_texts, list):
                context_texts = []
            context_metas = pkg.get("context_metas") or []
            if not isinstance(context_metas, list):
                context_metas = []
            llm_context = pkg.get("llm_context") or ""

            k_requested = _parse_qid(pkg.get("k_requested", retrieve_k), int(retrieve_k))
            k_used = _parse_qid(pkg.get("k_used", retrieve_k), int(retrieve_k))
            status = str(pkg.get("status") or "ok")
            composed_answer_text = str(pkg.get("raw_answer") or "")
            raw_structured_answer = str(pkg.get("raw_structured_answer") or "")
            structured_response = str(pkg.get("structured_response") or json.dumps(citacie_json, ensure_ascii=False))
            context_text = _format_context(context_texts)

            outputs: Dict[str, Any] = {
                "response": answer_text,
                "citacie_json": citacie_json,
                "raw_answer": composed_answer_text,
                "raw_structured_answer": raw_structured_answer,
                "structured_response": structured_response,
            }

            out: Dict[str, Any] = {
                "answer": answer_text,
                "response": answer_text,
                "prediction": answer_text,
                "outputs": outputs,
                "context": context_text,
                "latency_s": latency_s,
                "retriever_k_requested": k_requested,
                "retriever_k_used": k_used,
                "context_docs": context_texts,
                "context_docs_n": int(len(context_texts)),
                "status": status,
                "contexts": context_texts,
                "context_metas": context_metas,
                "llm_context": llm_context,
                "citacie_json": citacie_json,
                "raw_answer": composed_answer_text,
                "raw_structured_answer": raw_structured_answer,
                "structured_response": structured_response,
                "context_preview": (llm_context[:500] if isinstance(llm_context, str) else ""),
            }
            if status == "exception":
                out["exception"] = str(pkg.get("exception") or "")
            return out

        out = _run_one()
        if qid >= 0:
            cache_by_id[qid] = out
        return out

    return predict_fn, cache_by_id

# Evaluation helpers
def _build_eval_data(df_q) -> List[Dict[str, Any]]:
    eval_data: List[Dict[str, Any]] = []
    for row_id, row in df_q.reset_index(drop=True).iterrows():
        inputs_dict = _build_inputs_dict(row, int(row_id))
        expected_text = str(row.get("expected") or "")
        eval_data.append(
            {
                "inputs": inputs_dict,
                "expectations": {"expected_response": expected_text},
            }
        )
    return eval_data


def _reset_judge_logs(_S) -> None:
    _S.TRIAD_JUDGE_LOG.clear()


def _run_mlflow_eval(eval_data: List[Dict[str, Any]], predict_fn, cache_by_id: Dict[int, Dict[str, Any]]):
    import mlflow  # type: ignore
    from rag_core import scorers as _S  # type: ignore

    _reset_judge_logs(_S)

    from rag_core.scorers import (  # type: ignore
        triad_groundedness_scorer,
    )

    eval_res = mlflow.genai.evaluate(
        data=eval_data,
        predict_fn=predict_fn,
        scorers=[
            triad_groundedness_scorer,
        ],
    )

    return eval_res, _S

def _build_output_rows(
    eval_data: List[Dict[str, Any]],
    cache_by_id: Dict[int, Dict[str, Any]],
    gold_provision_map: Dict[str, Dict[str, List[str]]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []

    for item in eval_data:
        inp = item["inputs"]
        qid = int(inp["id"])
        out = cache_by_id.get(qid, {})
        row = {
            "id": qid,
            "question": inp.get("question"),
            "expected": item["expectations"].get("expected_response"),
            "outputs": (out.get("outputs") if isinstance(out.get("outputs"), dict) else {"response": out.get("response")}),
            **out,
        }

        gold_info = gold_provision_map.get(_normalize_question_key(inp.get("question")), {})
        if isinstance(gold_info, dict):
            row["extracted_statutes"] = gold_info.get("expected_statutes", []) or []
            row["extracted_cases"] = gold_info.get("expected_cases", []) or []

        row.pop("response", None)
        row.pop("prediction", None)
        if "contexts" in row and "context_docs" in row:
            row.pop("context_docs", None)

        if "contexts" in row and "extracted_statutes" in row:
            reordered: Dict[str, Any] = {}
            for key, value in row.items():
                if key == "contexts":
                    reordered["extracted_statutes"] = row.get("extracted_statutes", [])
                    if "extracted_cases" in row:
                        reordered["extracted_cases"] = row.get("extracted_cases", [])
                if key not in {"extracted_statutes", "extracted_cases"}:
                    reordered[key] = value
            row = reordered

        rows.append(row)

    return rows

# JSON-mode metric builders
def _build_json_mode_metrics(
    df_out,
    gold_provision_map: Dict[str, Dict[str, Any]],
    mlflow,
    _S,
) -> Tuple[Dict[int, Dict[str, Any]], Dict[str, Any]]:
    from rag_core.deterministic_core import (
        compare_zakon_sets,
        extract_predicted_zakon_ids,
        safe_str,
    )
    from rag_core.scorers import (
        answer_span_faithfulness_batch_score,
        citation_expected_alignment_batch_score,
        extract_marked_statute_context,
        mark_target_zakon_refs,
    )
    def _items_by_zakon(citacie_json: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        out: Dict[str, Dict[str, Any]] = {}
        for item in citacie_json or []:
            if not isinstance(item, dict):
                continue
            zakon = safe_str(item.get("zakon")).strip()
            if zakon and zakon not in out:
                out[zakon] = item
        return out

    def _metric1_verdict(tp_ids: List[str], fp_ids: List[str], fn_ids: List[str], gold_count: int) -> str:
        if gold_count <= 0:
            return "no gold annotations"
        if not fp_ids and not fn_ids:
            return "exact match"
        if fp_ids and fn_ids:
            return "partial match"
        if fp_ids:
            return "extra citation"
        if fn_ids:
            return "missing annotated citations"
        return "partial match"
    def _normalize_half_score(score: float) -> float:
        value = float(score)
        if value <= 0.25:
            return 0.0
        if value >= 0.75:
            return 1.0
        return 0.5

    def _metric_verdict(score: float) -> str:
        normalized = _normalize_half_score(score)
        if normalized >= 1.0:
            return "SUPPORTED"
        if normalized <= 0.0:
            return "UNSUPPORTED"
        return "PARTIALLY_SUPPORTED"

    def _context_by_zakon(context_docs: List[Any], context_metas: List[Any], allowed_zakony: List[str]) -> Dict[str, str]:
        docs = context_docs if isinstance(context_docs, list) else [context_docs]
        metas = context_metas if isinstance(context_metas, list) else []
        allowed = {safe_str(item).strip() for item in (allowed_zakony or []) if safe_str(item).strip()}
        out: Dict[str, str] = {}

        for idx, doc in enumerate(docs):
            text_value = safe_str(doc).strip()
            if not text_value:
                continue
            meta = metas[idx] if idx < len(metas) and isinstance(metas[idx], dict) else {}
            zakon = safe_str(meta.get("zakon_id") or meta.get("doc_id")).strip()
            if zakon not in allowed:
                continue
            previous = out.get(zakon, "")
            if previous:
                if text_value in previous:
                    continue
                out[zakon] = f"{previous}\n\n---\n\n{text_value}"
            else:
                out[zakon] = text_value
        return out

    per_q_metrics: Dict[int, Dict[str, Any]] = {}
    metric1_rows: List[Dict[str, Any]] = []
    metric2_rows: List[Dict[str, Any]] = []
    metric3_rows: List[Dict[str, Any]] = []
    total_tp = 0
    total_fp = 0
    total_fn = 0
    applicable_questions = 0
    metric2_question_scores: List[float] = []
    metric2_claim_scores: List[float] = []
    metric3_question_scores: List[float] = []
    metric3_claim_scores: List[float] = []

    for _, row in df_out.iterrows():
        qid = _parse_qid(row.get("id"), -1)
        if qid < 0:
            continue

        question = safe_str(row.get("question")).strip()
        expected = safe_str(row.get("expected")).strip()
        status = str(row.get("status") or "ok")
        prediction_ok = status in {"ok", "compose_failed"}
        citacie_json = row.get("citacie_json")
        if not isinstance(citacie_json, list):
            citacie_json = []
        
        context_docs = row.get("context_docs")
        if context_docs is None:
            context_docs = row.get("contexts")
        if isinstance(context_docs, str):
            context_docs = [context_docs]
        if not isinstance(context_docs, list):
            context_docs = []

        context_metas = row.get("context_metas")
        if not isinstance(context_metas, list):
            context_metas = []

        per_q_metrics[qid] = {
            "latency_s": float(row.get("latency_s")) if isinstance(row.get("latency_s"), (int, float)) else 0.0,
            "retriever_k_used": float(row.get("retriever_k_used")) if isinstance(row.get("retriever_k_used"), (int, float)) else float(len(context_docs)),
            "context_docs_n": float(row.get("context_docs_n")) if isinstance(row.get("context_docs_n"), (int, float)) else float(len(context_docs)),
            "status": status,
            "metric2_span_faithfulness": 0.0,
            "metric2_tp_spans_n": 0.0,
            "metric2_applicable": False,
            "metric3_expected_alignment": 0.0,
            "metric3_tp_spans_n": 0.0,
            "metric3_applicable": False,
        }

        gold_info = gold_provision_map.get(_normalize_question_key(question), {})
        if not isinstance(gold_info, dict):
            gold_info = {}
        gold_zakony = gold_info.get("gold_zakony") or []
        predicted_zakony = extract_predicted_zakon_ids(citacie_json)

        tp_ids: List[str] = []
        fp_ids: List[str] = []
        fn_ids: List[str] = []
        if gold_zakony:
            result = compare_zakon_sets(predicted_zakony, gold_zakony)
            applicable_questions += 1
            total_tp += int(result["true_positives"])
            total_fp += int(result["false_positives"])
            total_fn += int(result["false_negatives"])
            tp_ids = list(result["true_positive_ids"])
            fp_ids = list(result["false_positive_ids"])
            fn_ids = list(result["false_negative_ids"])

            per_q_metrics[qid].update({
                "citation_tp": int(result["true_positives"]),
                "citation_fp": int(result["false_positives"]),
                "citation_fn": int(result["false_negatives"]),
                "citation_precision": float(result["precision"]),
                "citation_recall": float(result["recall"]),
                "citation_f1": float(result["f1"]),
                "citation_exact_match": bool(result["exact_match"]),
            })

            predicted_zakony = list(result["predicted_ids"])
            gold_zakony = list(result["gold_ids"])

        metric1_rows.append({
            "id": qid,
            "question": question,
            "status": status,
            "gold_zakony": gold_zakony,
            "predicted_zakony": predicted_zakony,
            "structured_output": citacie_json,
            "tp": tp_ids,
            "fp": fp_ids,
            "fn": fn_ids,
            "verdict": _metric1_verdict(tp_ids, fp_ids, fn_ids, len(gold_zakony)),
        })

        metric2_row: Dict[str, Any] = {
            "id": qid,
            "question": question,
            "status": status,
            "question_score": None,
            "claims": [],
            "applicable": False,
            "skip_reason": "",

            "evaluated_zakony": [],
        }
        metric3_row: Dict[str, Any] = {
            "id": qid,
            "question": question,
            "status": status,
            "question_score": None,
            "claims": [],
            "applicable": False,
            "skip_reason": "",

            "evaluated_zakony": [],
        }

        if not prediction_ok:
            metric2_row["skip_reason"] = f"prediction status: {status}"
            metric3_row["skip_reason"] = f"prediction status: {status}"
        elif not predicted_zakony:
            metric2_row["skip_reason"] = "no predicted citations in structured output"
            metric3_row["skip_reason"] = "no predicted citations in structured output"
        else:
            predicted_items_by_zakon = _items_by_zakon(citacie_json)
            provisions_by_zakon = gold_info.get("provisions_by_zakon") if isinstance(gold_info.get("provisions_by_zakon"), dict) else {}
            span_zakony = list(predicted_zakony)
            metric3_zakony = [zakon for zakon in span_zakony if zakon in set(gold_zakony)]
            metric2_row["evaluated_zakony"] = list(span_zakony)
            metric3_row["evaluated_zakony"] = list(metric3_zakony)

            span_source_map = _context_by_zakon(context_docs, context_metas, span_zakony)
            metric2_row["applicable"] = True
            metric2_claim_rows: List[Dict[str, Any]] = []
            metric2_judge_inputs: List[Dict[str, str]] = []
            for idx, zakon in enumerate(span_zakony, start=1):
                item = predicted_items_by_zakon.get(zakon) or {}
                structured_answer = safe_str(item.get("odpoved_vygenerovana")).strip()
                law_text = safe_str(span_source_map.get(zakon)).strip()

                score = 0.0
                reason = ""
                if not structured_answer:
                    reason = "V structured outpute chybalo odpoved_vygenerovana pre tento pravny predpis."
                elif not law_text:
                    reason = "Text pravneho predpisu nebol dostupny v retrieved contexte pre tento modelom zvoleny predpis."
                else:
                    metric2_judge_inputs.append({
                        "zakon": zakon,
                        "model_span": structured_answer,
                        "provision_text": law_text,
                    })

                metric2_claim_rows.append({
                    "index": idx,
                    "zakon": zakon,
                    "structured_answer": structured_answer,
                    "law_text": law_text,
                    "score": score,
                    "verdict": _metric_verdict(score),
                    "judge_reason": reason,
                })

            if metric2_judge_inputs:
                try:
                    metric2_judge_rows = answer_span_faithfulness_batch_score(question, metric2_judge_inputs)
                except Exception as e:
                    metric2_judge_rows = [{
                        "zakon": item["zakon"],
                        "score": 0.0,
                        "judge_explanation": f"JUDGE_ERROR: {type(e).__name__}: {e}",
                    } for item in metric2_judge_inputs]
                metric2_judge_by_zakon = {
                    safe_str(item.get("zakon")).strip(): item
                    for item in metric2_judge_rows
                    if isinstance(item, dict) and safe_str(item.get("zakon")).strip()
                }
                for claim_row in metric2_claim_rows:
                    judge_row = metric2_judge_by_zakon.get(claim_row["zakon"])
                    if not judge_row:
                        continue
                    score = _normalize_half_score(float(judge_row.get("score", 0.0)))
                    claim_row["score"] = score
                    claim_row["verdict"] = _metric_verdict(score)
                    claim_row["judge_reason"] = safe_str(judge_row.get("judge_explanation")).strip()

            metric2_question_score = float(sum(item["score"] for item in metric2_claim_rows) / len(metric2_claim_rows)) if metric2_claim_rows else 0.0
            metric2_row["question_score"] = metric2_question_score
            metric2_row["claims"] = metric2_claim_rows
            metric2_question_scores.append(metric2_question_score)
            metric2_claim_scores.extend(item["score"] for item in metric2_claim_rows)
            per_q_metrics[qid]["metric2_span_faithfulness"] = metric2_question_score
            per_q_metrics[qid]["metric2_tp_spans_n"] = float(len(metric2_claim_rows))
            per_q_metrics[qid]["metric2_applicable"] = True

            if not expected:
                metric3_row["skip_reason"] = "empty expected answer text"
            elif not metric3_zakony:
                metric3_row["skip_reason"] = "no model-selected provisions matched gold provisions"
            else:
                metric3_claim_rows: List[Dict[str, Any]] = []
                metric3_judge_inputs: List[Dict[str, str]] = []
                for idx, zakon in enumerate(metric3_zakony, start=1):
                    item = predicted_items_by_zakon.get(zakon) or {}
                    provision_hints = item.get("provision_hints") if isinstance(item.get("provision_hints"), list) else []
                    if not provision_hints:
                        provision_hints = provisions_by_zakon.get(zakon) or []
                    structured_answer = safe_str(item.get("odpoved_vygenerovana")).strip()
                    marked_expected = mark_target_zakon_refs(expected, zakon, provision_hints)
                    if "***" not in marked_expected:
                        continue

                    expected_pkg = extract_marked_statute_context(marked_expected, zakon)
                    expected_span = safe_str(expected_pkg.get("span")).strip()
                    expected_extract_reason = safe_str(expected_pkg.get("judge_explanation")).strip()

                    score = 0.0
                    reason = ""
                    if not structured_answer:
                        reason = "V structured outpute chybalo odpoved_vygenerovana pre tento pravny predpis."
                    elif not expected_span:
                        reason = f"Nepodarilo sa z expertnej expected odpovede vyrezat pouzitelny gold span pre tento pravny predpis. Detail: {expected_extract_reason or 'lokalna extrakcia vratila prazdny span.'}"
                    else:
                        metric3_judge_inputs.append({
                            "zakon": zakon,
                            "model_span": structured_answer,
                            "expected_span": expected_span,
                        })

                    metric3_claim_rows.append({
                        "index": idx,
                        "zakon": zakon,
                        "structured_answer": structured_answer,
                        "expected_span": expected_span,
                        "expected_extract_reason": expected_extract_reason,
                        "score": score,
                        "verdict": _metric_verdict(score),
                        "judge_reason": reason,
                    })

                if metric3_claim_rows:
                    if metric3_judge_inputs:
                        try:
                            metric3_judge_rows = citation_expected_alignment_batch_score(question, metric3_judge_inputs)
                        except Exception as e:
                            metric3_judge_rows = [{
                                "zakon": item["zakon"],
                                "score": 0.0,
                                "judge_explanation": f"JUDGE_ERROR: {type(e).__name__}: {e}",
                            } for item in metric3_judge_inputs]
                        metric3_judge_by_zakon = {
                            safe_str(item.get("zakon")).strip(): item
                            for item in metric3_judge_rows
                            if isinstance(item, dict) and safe_str(item.get("zakon")).strip()
                        }
                        for claim_row in metric3_claim_rows:
                            judge_row = metric3_judge_by_zakon.get(claim_row["zakon"])
                            if not judge_row:
                                continue
                            score = _normalize_half_score(float(judge_row.get("score", 0.0)))
                            claim_row["score"] = score
                            claim_row["verdict"] = _metric_verdict(score)
                            claim_row["judge_reason"] = safe_str(judge_row.get("judge_explanation")).strip()

                    metric3_row["applicable"] = True
                    metric3_question_score = float(sum(item["score"] for item in metric3_claim_rows) / len(metric3_claim_rows))
                    metric3_row["question_score"] = metric3_question_score
                    metric3_row["claims"] = metric3_claim_rows
                    metric3_question_scores.append(metric3_question_score)
                    metric3_claim_scores.extend(item["score"] for item in metric3_claim_rows)
                    per_q_metrics[qid]["metric3_expected_alignment"] = metric3_question_score
                    per_q_metrics[qid]["metric3_tp_spans_n"] = float(len(metric3_claim_rows))
                    per_q_metrics[qid]["metric3_applicable"] = True
                else:
                    metric3_row["skip_reason"] = "no model-selected provisions were found in expected answer"
        metric2_rows.append(metric2_row)
        metric3_rows.append(metric3_row)

    def _merge_log(log: List[Dict[str, Any]], *metric_keys: str) -> None:
        for metric_row in log or []:
            qid = _parse_qid(metric_row.get("id", -1), -1)
            if qid < 0 or qid not in per_q_metrics:
                continue
            for metric_key in metric_keys:
                value = metric_row.get(metric_key)
                if isinstance(value, (int, float)):
                    per_q_metrics[qid][metric_key] = float(value)

    _merge_log(getattr(_S, "TRIAD_JUDGE_LOG", []), "triad_groundedness")


    precision = float(total_tp / (total_tp + total_fp)) if (total_tp + total_fp) else 0.0
    recall = float(total_tp / (total_tp + total_fn)) if (total_tp + total_fn) else 0.0
    f1 = float((2 * precision * recall) / (precision + recall)) if (precision + recall) else 0.0
    if applicable_questions > 0:
        mlflow.log_metrics({
            "citation_tp": float(total_tp),
            "citation_fp": float(total_fp),
            "citation_fn": float(total_fn),
            "citation_precision": precision,
            "citation_recall": recall,
            "citation_f1": f1,
        })

    metric2_question_mean = (
        float(sum(metric2_question_scores) / len(metric2_question_scores)) if metric2_question_scores else 0.0
    )
    metric2_claim_mean = (
        float(sum(metric2_claim_scores) / len(metric2_claim_scores)) if metric2_claim_scores else 0.0
    )
    if metric2_question_scores or metric2_claim_scores:
        mlflow.log_metrics({
            "metric2_span_faithfulness_question_mean": metric2_question_mean,
            "metric2_span_faithfulness_claim_mean": metric2_claim_mean,
            "metric2_span_faithfulness_questions": float(len(metric2_question_scores)),
            "metric2_span_faithfulness_claims": float(len(metric2_claim_scores)),
        })

    metric3_question_mean = (
        float(sum(metric3_question_scores) / len(metric3_question_scores)) if metric3_question_scores else 0.0
    )
    metric3_claim_mean = (
        float(sum(metric3_claim_scores) / len(metric3_claim_scores)) if metric3_claim_scores else 0.0
    )
    if metric3_question_scores or metric3_claim_scores:
        mlflow.log_metrics({
            "metric3_expected_alignment_question_mean": metric3_question_mean,
            "metric3_expected_alignment_claim_mean": metric3_claim_mean,
            "metric3_expected_alignment_questions": float(len(metric3_question_scores)),
            "metric3_expected_alignment_claims": float(len(metric3_claim_scores)),
        })

    return per_q_metrics, {
        "metric1": {
            "summary": {
                "questions_with_gold": int(applicable_questions),
                "tp": int(total_tp),
                "fp": int(total_fp),
                "fn": int(total_fn),
                "precision": precision,
                "recall": recall,
                "f1": f1,
            },
            "rows": metric1_rows,
        },
        "metric2": {
            "summary": {
                "evaluated_questions": int(len(metric2_question_scores)),
                "evaluated_tp_spans": int(len(metric2_claim_scores)),
                "question_mean": metric2_question_mean,
                "claim_mean": metric2_claim_mean,
    
            },
            "rows": metric2_rows,
        },
        "metric3": {
            "summary": {
                "evaluated_questions": int(len(metric3_question_scores)),
                "evaluated_tp_spans": int(len(metric3_claim_scores)),
                "question_mean": metric3_question_mean,
                "claim_mean": metric3_claim_mean,
    
            },
            "rows": metric3_rows,
        },
    }

# MLflow summary metrics
def _log_eval_metrics(eval_res, mlflow) -> None:
    try:
        if eval_res is None:
            return
        eval_metrics = dict(getattr(eval_res, "metrics", {}) or {})
        mlflow.log_metrics({k: float(v) for k, v in eval_metrics.items() if isinstance(v, (int, float))})
    except Exception:
        pass

# Main evaluation flow
def run_eval(env_file: str) -> None:
    env_path = _resolve_env_path(env_file)
    load_dotenv(env_path, override=True)

    import mlflow  # type: ignore
    import pandas as pd  # type: ignore
    from rag_core.eval_pipeline import get_retriever  # type: ignore

    if os.getenv("MLFLOW_GENAI_EVAL_SKIP_TRACE_VALIDATION") is None:
        os.environ["MLFLOW_GENAI_EVAL_SKIP_TRACE_VALIDATION"] = "True"

    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    if not tracking_uri:
        root = Path(__file__).resolve().parents[1]
        tracking_uri = (root / "mlruns").resolve().as_uri()
        os.environ["MLFLOW_TRACKING_URI"] = tracking_uri

    experiment_name = os.getenv("MLFLOW_EXPERIMENT_NAME", "qa-eval-local")

    questions_file = Path(os.getenv("EVAL_QUESTIONS_FILE", os.getenv("EVAL_QUESTIONS_CSV", os.getenv("EVAL_CSV", "eval/questions.csv"))))
    if not questions_file.is_absolute():
        root = Path(__file__).resolve().parents[1]
        questions_file = (root / questions_file).resolve()

    gold_provisions_file = Path(os.getenv("EVAL_GOLD_PROVISIONS_FILE", "data/otazky-najpravo-doplnene.json"))
    if not gold_provisions_file.is_absolute():
        root = Path(__file__).resolve().parents[1]
        gold_provisions_file = (root / gold_provisions_file).resolve()
    gold_provision_map = _load_gold_provision_map(gold_provisions_file)

    out_dir = Path(os.getenv("EVAL_OUT_DIR", "eval"))
    if not out_dir.is_absolute():
        root = Path(__file__).resolve().parents[1]
        out_dir = (root / out_dir).resolve()

    limit = int(os.getenv("EVAL_LIMIT", "0") or 0)
    retrieve_k = int(os.getenv("RETRIEVE_K", "10") or 10)
    want_traces = _bool_env("MLFLOW_GENAI_EVAL_LOG_TRACES", default=False)

    try:
        mlflow.openai.autolog(log_traces=want_traces)
    except Exception:
        pass
    try:
        mlflow.litellm.autolog(log_traces=want_traces)
    except Exception:
        pass

    _patch_mlflow_genai_trace_linking_best_effort()
    _patch_mlflow_genai_expectations_best_effort()
    _patch_mlflow_genai_log_trace_best_effort()

    _safe_mkdir(out_dir)
    if not questions_file.exists():
        raise RuntimeError(f"Questions file not found: {questions_file}")

    df_q = _load_questions_any(questions_file)
    if limit > 0:
        df_q = df_q.head(limit)
    _ensure_eval_columns(df_q)

    eval_data = _build_eval_data(df_q)
    retriever = get_retriever()
    predict_fn, cache_by_id = _predict_fn_factory(
        retriever=retriever,
        retrieve_k=retrieve_k,
    )

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    LOG.info(
        "Eval config | experiment=%s | items=%d | k=%d",
        experiment_name,
        len(eval_data),
        retrieve_k,
    )

    LOG.info("Starting MLflow run")
    run = None
    try:
        run = mlflow.start_run(run_name="eval")
        LOG.info("MLflow run started | run_id=%s", run.info.run_id)

        eval_res, _S = _run_mlflow_eval(eval_data, predict_fn, cache_by_id)
        rows = _build_output_rows(eval_data, cache_by_id, gold_provision_map)
        df_out = pd.DataFrame(rows).sort_values("id").reset_index(drop=True)

        _write_core_artifacts(df_out, out_dir, mlflow)
        _log_triad_report(out_dir, mlflow, _S)
        _log_eval_metrics(eval_res, mlflow)
        _, citation_report = _build_json_mode_metrics(df_out, gold_provision_map, mlflow, _S)
        _write_metric1_selection_artifact(out_dir, mlflow, citation_report)
        _write_metric2_span_faithfulness_artifact(out_dir, mlflow, citation_report)
        _write_metric3_expected_alignment_artifact(out_dir, mlflow, citation_report)

        LOG.info("Evaluation completed | artifacts_dir=%s", str(out_dir))
        mlflow.end_run(status="FINISHED")
    except BaseException:
        print(traceback.format_exc())
        try:
            mlflow.end_run(status="FAILED")
        except Exception:
            pass
        raise
    finally:
        try:
            if mlflow.active_run() is not None:
                mlflow.end_run()
        except Exception:
            pass

# CLI
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", default=".env")
    args = parser.parse_args()
    _configure_logging()
    run_eval(args.env_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())