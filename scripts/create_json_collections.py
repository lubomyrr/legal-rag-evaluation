from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import List, Dict, Any, Iterator, Optional
from datetime import datetime, timedelta

import requests
import ftfy
from dotenv import load_dotenv

#Progress bar
try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    print("💡 Tip: Install tqdm for progress bar: pip install tqdm")

# Streaming JSON parser for large files
try:
    import ijson
    HAS_IJSON = True
except ImportError:
    HAS_IJSON = False
    print("⚠️ ijson not installed. Will use json.load() (high memory for large files)")
    print("   Install with: pip install ijson")

# Optional: LangChain splitter for chunking
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    HAS_LANGCHAIN_SPLITTER = True
except ImportError:
    HAS_LANGCHAIN_SPLITTER = False

from chromadb import PersistentClient

# ----------------------------
# Config
# ----------------------------
load_dotenv()

EMBEDDING_BASE_URL = os.getenv("EMBEDDING_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
EMB_MODEL = os.getenv("EMB_MODEL", "qwen3-embedding:4b")

# Chunking settings
CHUNK_SIZE = int(os.getenv("INGEST_CHUNK_SIZE", "2000"))
CHUNK_OVERLAP = int(os.getenv("INGEST_CHUNK_OVERLAP", "200"))

# Default to "never auto-chunk by length" unless explicitly overridden.
MAX_TEXT_LENGTH_FOR_SINGLE_DOC = int(os.getenv("MAX_SINGLE_DOC_LENGTH", "100000000"))

# Embedding settings
BATCH_SIZE = int(os.getenv("INGEST_BATCH_SIZE", "32"))
EMBEDDING_TIMEOUT = int(os.getenv("EMBEDDING_TIMEOUT", "180"))

# Slovak-specific fixes are optional (OFF by default to avoid altering Czech/other texts)
APPLY_SLOVAK_FIXES = os.getenv("APPLY_SLOVAK_FIXES", "0").strip().lower() in ("1", "true", "yes")

# ----------------------------
# Checkpoint (resume) helpers
# ----------------------------
def get_checkpoint_path(chroma_dir: Path, collection_name: str) -> Path:
    # one checkpoint per collection + db dir
    return chroma_dir / f".ingest_checkpoint_{collection_name}.json"

def load_checkpoint(path: Path) -> Dict[str, int]:
    """
    Returns mapping: { "<json_filename>": last_obj_index_done }
    """
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            out: Dict[str, int] = {}
            for k, v in data.items():
                try:
                    out[str(k)] = int(v)
                except Exception:
                    continue
            return out
    except Exception:
        return {}
    return {}

def save_checkpoint(path: Path, state: Dict[str, int]) -> None:
    """
    Atomic-ish write: write temp then replace.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False)
    tmp.replace(path)


# ----------------------------
# 1. Streaming JSON Parser
# ----------------------------
def iter_json_objects(json_path: Path) -> Iterator[Dict[str, Any]]:
    """
    Stream JSON objects one by one without loading entire file into memory.

    Uses ijson for streaming if available, otherwise falls back to json.load().
    For 300MB+ files, ijson is strongly recommended.
    """
    if HAS_IJSON:
        print(f"   📖 Using streaming parser (ijson)")
        with open(json_path, "rb") as f:
            for obj in ijson.items(f, "item"):
                if isinstance(obj, dict):
                    yield obj
    else:
        print(f"   ⚠️ Loading entire JSON into memory (no ijson)")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            for obj in data:
                if isinstance(obj, dict):
                    yield obj


# ----------------------------
# 4. Text Cleaning (Safe)
# ----------------------------
_SLOVAK_CONTEXT_PATTERNS = [
    (re.compile(r"(?<=[a-záäčďéíľĺňóôŕšťúýž])>(?=[a-záäčďéíľĺňóôŕšťúýž])", re.IGNORECASE), "ľ"),
    (re.compile(r"(?<=[a-záäčďéíľĺňóôŕšťúýž])~(?=[a-záäčďéíľĺňóôŕšťúýž])", re.IGNORECASE), "ž"),
    (re.compile(r"\bdHa\b"), "dňa"),
    (re.compile(r"peHažn"), "peňažn"),
]
_ASPI_LINK = re.compile(r"aspi://[^\s'\"]+", re.IGNORECASE)


def clean_text(text: str) -> str:
    """
    Cleans text artifacts with optional context-aware Slovak fixes.
    """
    if not text:
        return ""

    t = ftfy.fix_text(text)
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    t = _ASPI_LINK.sub("", t)

    if APPLY_SLOVAK_FIXES:
        for pattern, replacement in _SLOVAK_CONTEXT_PATTERNS:
            t = pattern.sub(replacement, t)

    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


# ----------------------------
# 5. Document Normalization
# ----------------------------
def normalize_json_object(
    obj: Dict[str, Any],
    source_file: str,
    obj_index: int = 0
) -> List[Dict[str, Any]]:
    """
    Normalize one QA JSON object into LAW-ONLY documents.

    Important:
    - question/expected are NOT indexed into Chroma
    - only provisions[].text are indexed
    - objects without provisions text are skipped
    """
    docs: List[Dict[str, Any]] = []

    doc_id = str(obj.get("_id", "") or "").strip()
    if not doc_id:
        return []

    title = clean_text(str(obj.get("title", "") or ""))
    qa_type = clean_text(str(obj.get("type", "") or ""))
    url = str(obj.get("url", "") or "")
    date = str(obj.get("date", "") or "")

    provisions = obj.get("provisions", []) or []

    for i, p in enumerate(provisions):
        if not isinstance(p, dict):
            continue

        law_name = clean_text(str(p.get("law", "") or ""))
        law_version = str(p.get("version", "") or "")
        paragraph = clean_text(str(p.get("paragraph", "") or ""))
        nadpis = clean_text(str(p.get("nadpis", "") or ""))
        p_text = clean_text(str(p.get("text", "") or ""))
        fragment = str(p.get("fragment", "") or "")
        provision_url = str(p.get("url", "") or "")

        if not p_text:
            continue

        parts: List[str] = []
        if law_name:
            parts.append(f"LAW: {law_name}")
        if law_version:
            parts.append(f"VERSION: {law_version}")
        if paragraph:
            parts.append(f"PARAGRAPH: {paragraph}")
        if nadpis:
            parts.append(f"TITLE: {nadpis}")
        parts.append(f"TEXT:\n{p_text}")

        prov_text = "\n\n".join(parts).strip()

        docs.append({
            "doc_id": doc_id,
            "version": f"prov_{i}",
            "page_content": prov_text,
            "headline_prefix": nadpis or paragraph or law_name,
            "metadata": {
                "doc_id": doc_id,
                "version": f"prov_{i}",
                "source_file": source_file,
                "obj_index": obj_index,
                "doc_kind": "law_provision",
                "parent_qa_id": doc_id,
                "title": title,
                "type": qa_type,
                "url": url,
                "date": date,
                "law_name": law_name,
                "law_version": law_version,
                "paragraph": paragraph,
                "nadpis": nadpis,
                "fragment": fragment,
                "provision_url": provision_url,
                "headlines": nadpis or paragraph or law_name,
                "title_path": " > ".join(x for x in [law_name, paragraph, nadpis] if x),
            },
            "chroma_id": f"prov::{doc_id}::{i}",
        })

    return docs

# ----------------------------
# 6. Chunking (Default: 1 object = 1 doc)
# ----------------------------
def chunk_document(doc: Dict[str, Any], always_chunk: bool = False) -> List[Dict[str, Any]]:
    """
    Chunk a document for better retrieval precision (optional).
    Default behavior with MAX_SINGLE_DOC_LENGTH very large:
    - Returns [doc] for almost all inputs.
    """
    page_content = doc["page_content"]
    headline_prefix = doc.get("headline_prefix", "")

    if not always_chunk and len(page_content) <= MAX_TEXT_LENGTH_FOR_SINGLE_DOC:
        return [doc]

    if not HAS_LANGCHAIN_SPLITTER:
        print(f"   ⚠️ Text too long ({len(page_content)} chars) but no splitter available")
        return [doc]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    text_to_split = page_content
    if headline_prefix and page_content.startswith(headline_prefix):
        text_to_split = page_content[len(headline_prefix):].lstrip("\n")

    chunks = splitter.split_text(text_to_split)
    if len(chunks) <= 1:
        return [doc]

    result: List[Dict[str, Any]] = []
    for i, chunk_text in enumerate(chunks):
        if headline_prefix:
            chunk_content = headline_prefix + "\n\n" + chunk_text
        else:
            chunk_content = chunk_text

        chunk_doc = {
            "doc_id": doc["doc_id"],
            "version": doc["version"],
            "page_content": chunk_content,
            "metadata": {
                **doc["metadata"],
                "chunk_index": i,
                "chunk_total": len(chunks),
            },
            "chroma_id": f"{doc['chroma_id']}::chunk{i}",
        }
        result.append(chunk_doc)

    return result


def fallback_split_text(text: str) -> List[str]:
    """
    Fallback splitting used only when embedding a full document fails.
    Prefers LangChain splitter if available; otherwise uses a simple slicing strategy.
    """
    if not text:
        return [""]

    if HAS_LANGCHAIN_SPLITTER:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", ". ", " ", ""],
        )
        chunks = splitter.split_text(text)
        return chunks if chunks else [text]

    chunks: List[str] = []
    step = max(1, CHUNK_SIZE - CHUNK_OVERLAP)
    for i in range(0, len(text), step):
        chunks.append(text[i:i + CHUNK_SIZE])
    return chunks if chunks else [text]


# ----------------------------
# 7. Embedding Client (Adaptive)
# ----------------------------
class OllamaEmbedder:
    """Ollama API client with adaptive batching and retry."""

    def __init__(self, base_url: str, model: str, timeout: int = EMBEDDING_TIMEOUT):
        self.url = f"{base_url.rstrip('/')}/api/embed"
        self.model = model
        self.timeout = timeout

    def embed(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        """
        Generate embeddings with adaptive batch sizing.
        If a batch fails, retries with smaller batch size.
        """
        all_embeddings: List[List[float]] = []
        batch_size = batch_size or BATCH_SIZE

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            embeddings = self._embed_batch(batch)
            if embeddings is None:
                embeddings = self._embed_batch_with_retry(batch)

            if embeddings:
                all_embeddings.extend(embeddings)
            else:
                print(f"   ❌ Failed to embed batch {i//batch_size + 1}")
                return []

        return all_embeddings

    def _embed_batch(self, texts: List[str], timeout_override: int = None) -> Optional[List[List[float]]]:
        try:
            resp = requests.post(
                self.url,
                json={"model": self.model, "input": texts},
                timeout=timeout_override or self.timeout
            )
            resp.raise_for_status()
            return resp.json().get("embeddings", [])
        except Exception as e:
            print(f"   ⚠️ Embedding batch error: {e}")
            return None

    def _embed_batch_with_retry(self, texts: List[str]) -> Optional[List[List[float]]]:
        for retry_batch_size in [16, 8, 4, 2, 1]:
            if len(texts) < retry_batch_size:
                continue

            print(f"   🔄 Retrying with batch_size={retry_batch_size}")
            all_embs: List[List[float]] = []
            success = True

            for i in range(0, len(texts), retry_batch_size):
                batch = texts[i:i + retry_batch_size]
                embs = self._embed_batch(batch, timeout_override=self.timeout * 2)
                if embs:
                    all_embs.extend(embs)
                else:
                    success = False
                    break

            if success and len(all_embs) == len(texts):
                return all_embs

        return None

# ----------------------------
# 9. Main Ingest Logic (Idempotent & Resumable)
# ----------------------------
def ingest_json(
    source_dir: Path,
    chroma_dir: Path,
    collection_name: str,
    reset: bool = False,
    always_chunk: bool = False,
    batch_size: int = BATCH_SIZE,
) -> Dict[str, Any]:
    start_time = time.time()

    print(f"\n{'='*60}")
    print(f"🚀 JSON INGEST PIPELINE v2")
    print(f"{'='*60}")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📂 Source:       {source_dir}")
    print(f"💾 DB:           {chroma_dir}")
    print(f"📦 Collection:   {collection_name}")
    print(f"🔄 Reset:        {reset}")
    print(f"✂️  Always chunk: {always_chunk}")
    print(f"📊 Batch size:   {batch_size}")
    print(f"📏 Chunk size:   {CHUNK_SIZE} (overlap: {CHUNK_OVERLAP})")
    print(f"🧱 Max single doc length: {MAX_TEXT_LENGTH_FOR_SINGLE_DOC}")
    print(f"🔗 Embedding:    {EMB_MODEL} @ {EMBEDDING_BASE_URL}")
    print(f"{'='*60}\n")

    client = PersistentClient(path=str(chroma_dir))

    if reset:
        try:
            client.delete_collection(name=collection_name)
            print(f"🗑️  Deleted collection: {collection_name}")
            # Also remove checkpoint file if resetting
            ckpt_path = get_checkpoint_path(chroma_dir, collection_name)
            if ckpt_path.exists():
                os.remove(ckpt_path)
                print(f"🗑️  Deleted checkpoint file: {ckpt_path.name}")
        except Exception as e:
            print(f"   ℹ️ Collection didn't exist or error: {e}")

    coll = client.get_or_create_collection(name=collection_name)
    embedder = OllamaEmbedder(EMBEDDING_BASE_URL, EMB_MODEL)

    # Checkpoint initialization
    ckpt_path = get_checkpoint_path(chroma_dir, collection_name)
    processed_state = {}
    if not reset:
        processed_state = load_checkpoint(ckpt_path)
        if processed_state:
            print(f"🔄 Loaded checkpoint state: {processed_state}")
    
    json_files = list(source_dir.rglob("*.json"))
    if not json_files:
        print("❌ No .json files found!")
        return {"error": "no_json_files"}

    print(f"📁 Found {len(json_files)} JSON file(s)")

    stats: Dict[str, Any] = {
        "files_processed": 0,
        "objects_read": 0,
        "objects_normalized": 0,
        "chunks_created": 0,
        "chunks_indexed": 0,
        "unique_doc_ids_count": 0,
        "skipped_objects": 0,
        "batches_failed": 0,
        "docs_fallback_chunked": 0,
        "chunks_failed": 0,
    }
    unique_doc_ids = set()

    batch_ids: List[str] = []
    batch_docs: List[str] = []
    batch_metas: List[Dict[str, Any]] = []

    def bump_checkpoint_from_metas(metas_list: List[Dict[str, Any]]):
        """Update global processed_state based on max obj_index in batch."""
        if not metas_list:
            return
        
        updates = {}
        for m in metas_list:
            fname = m.get("source_file")
            idx = m.get("obj_index")
            if fname and idx is not None:
                try:
                    idx_int = int(idx)
                    cur_max = updates.get(fname, -1)
                    if idx_int > cur_max:
                        updates[fname] = idx_int
                except:
                    pass
        
        changed = False
        for fname, max_idx in updates.items():
            old_val = processed_state.get(fname, -1)
            if max_idx > old_val:
                processed_state[fname] = max_idx
                changed = True
        
        if changed:
            save_checkpoint(ckpt_path, processed_state)

    def flush_batch():
        nonlocal batch_ids, batch_docs, batch_metas
        if not batch_ids:
            return

        ids = batch_ids
        docs = batch_docs
        metas = batch_metas

        embs = embedder.embed(docs, batch_size=batch_size)
        if embs and len(embs) == len(ids):
            coll.upsert(ids=ids, documents=docs, metadatas=metas, embeddings=embs)
            stats["chunks_indexed"] += len(ids)
            
            # CHECKPOINT UPDATE
            bump_checkpoint_from_metas(metas)
            
            batch_ids, batch_docs, batch_metas = [], [], []
            return

        stats["batches_failed"] += 1



        print("   ⚠️ Batch embedding mismatch/failure. Salvaging docs one-by-one...")

        ok_ids: List[str] = []
        ok_docs: List[str] = []
        ok_metas: List[Dict[str, Any]] = []
        ok_embs: List[List[float]] = []
        failed_docs: List[tuple[str, str, Dict[str, Any]]] = []

        for _id, _doc, _meta in zip(ids, docs, metas):
            one = embedder.embed([_doc], batch_size=1)
            if one and len(one) == 1:
                ok_ids.append(_id)
                ok_docs.append(_doc)
                ok_metas.append(_meta)
                ok_embs.append(one[0])
            else:
                failed_docs.append((_id, _doc, _meta))

        if ok_ids:
            coll.upsert(ids=ok_ids, documents=ok_docs, metadatas=ok_metas, embeddings=ok_embs)
            stats["chunks_indexed"] += len(ok_ids)
            
            # CHECKPOINT UPDATE (partial batch success)
            bump_checkpoint_from_metas(ok_metas)


        if not failed_docs:
            batch_ids, batch_docs, batch_metas = [], [], []
            return

        for base_id, full_text, base_meta in failed_docs:
            chunks = fallback_split_text(full_text)

            if not chunks:
                stats["chunks_failed"] += 1
                print(f"   ❌ Failed to embed doc even after fallback split: {base_id}")
                continue

            # If splitter returns one chunk identical in size, splitting did not help;
            # but still try embedding that single chunk as "fallback" once.
            if len(chunks) == 1:
                one = embedder.embed([chunks[0]], batch_size=1)
                if one and len(one) == 1:
                    meta = dict(base_meta)
                    meta["fallback_chunk"] = True
                    meta["parent_id"] = base_id
                    meta["chunk_index"] = 0
                    meta["chunk_total"] = 1
                    coll.upsert(
                        ids=[f"{base_id}::fbchunk0"],
                        documents=[chunks[0]],
                        metadatas=[meta],
                        embeddings=[one[0]],
                    )
                    stats["chunks_indexed"] += 1
                    stats["docs_fallback_chunked"] += 1
                    
                    # CHECKPOINT UPDATE
                    bump_checkpoint_from_metas([meta])
                    continue

                stats["chunks_failed"] += 1
                print(f"   ❌ Failed to embed doc even after fallback single-chunk retry: {base_id}")
                continue

            stats["docs_fallback_chunked"] += 1

            chunk_ids = [f"{base_id}::fbchunk{i}" for i in range(len(chunks))]
            chunk_metas: List[Dict[str, Any]] = []
            for i in range(len(chunks)):
                m = dict(base_meta)
                m["fallback_chunk"] = True
                m["parent_id"] = base_id
                m["chunk_index"] = i
                m["chunk_total"] = len(chunks)
                chunk_metas.append(m)

            chunk_embs = embedder.embed(chunks, batch_size=min(batch_size, len(chunks)))
            if not chunk_embs or len(chunk_embs) != len(chunks):
                fixed_embs: List[List[float]] = []
                success = True
                for ch in chunks:
                    one = embedder.embed([ch], batch_size=1)
                    if one and len(one) == 1:
                        fixed_embs.append(one[0])
                    else:
                        success = False
                        break

                if not success:
                    stats["chunks_failed"] += len(chunks)
                    print(f"   ❌ Failed to embed fallback chunks for: {base_id}")
                    continue

                chunk_embs = fixed_embs

            coll.upsert(ids=chunk_ids, documents=chunks, metadatas=chunk_metas, embeddings=chunk_embs)
            stats["chunks_indexed"] += len(chunk_ids)

            # CHECKPOINT UPDATE (fallback chunks success)
            bump_checkpoint_from_metas(chunk_metas)



        batch_ids, batch_docs, batch_metas = [], [], []

    for json_path in json_files:
        file_start = time.time()
        file_size_mb = json_path.stat().st_size / (1024 * 1024)
        print(f"\n{'─'*60}")
        print(f"📄 Processing: {json_path.name} ({file_size_mb:.1f} MB)")
        print(f"{'─'*60}")
        stats["files_processed"] += 1
        current_source_file = json_path.name
        resume_from = int(processed_state.get(current_source_file, -1))
        print(f"   ↪️ Resume from checkpoint: obj_index > {resume_from}")

        obj_index = 0
        last_log_time = time.time()

        for obj in iter_json_objects(json_path):
            stats["objects_read"] += 1
            obj_index += 1

            if obj_index <= resume_from:
                continue

            docs = normalize_json_object(obj, json_path.name, obj_index)
            if not docs:
                stats["skipped_objects"] += 1
                continue

            stats["objects_normalized"] += 1

            for doc in docs:
                unique_doc_ids.add(doc["doc_id"])

                doc_chunks = chunk_document(doc, always_chunk=always_chunk)
                stats["chunks_created"] += len(doc_chunks)

                for chunk in doc_chunks:
                    batch_ids.append(chunk["chroma_id"])
                    batch_docs.append(chunk["page_content"])
                    batch_metas.append(chunk["metadata"])

                    if len(batch_ids) >= batch_size:
                        flush_batch()

            now = time.time()
            if now - last_log_time >= 5 or obj_index % 1000 == 0:
                elapsed = now - file_start
                rate = obj_index / elapsed if elapsed > 0 else 0
                print(
                    f"   📊 Objects: {obj_index:,} | Chunks: {stats['chunks_created']:,} | "
                    f"Indexed: {stats['chunks_indexed']:,} | Rate: {rate:.0f} obj/s"
                )
                last_log_time = now

        file_elapsed = time.time() - file_start
        print(f"   ✅ Completed: {obj_index:,} objects in {file_elapsed:.1f}s")

    flush_batch()

    stats["unique_doc_ids_count"] = len(unique_doc_ids)
    total_elapsed = time.time() - start_time

    print(f"\n{'='*60}")
    print(f"✅ INGEST COMPLETE")
    print(f"{'='*60}")
    print(f"⏰ Finished at:          {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️  Total time:           {timedelta(seconds=int(total_elapsed))}")
    print(f"{'─'*60}")
    print(f"📁 Files processed:      {stats['files_processed']:,}")
    print(f"📊 Objects read:         {stats['objects_read']:,}")
    print(f"📝 Objects normalized:   {stats['objects_normalized']:,}")
    print(f"✂️  Chunks created:       {stats['chunks_created']:,}")
    print(f"🗄️  Chunks indexed:       {stats['chunks_indexed']:,}")
    print(f"🆔 Unique doc_ids:       {stats['unique_doc_ids_count']:,}")
    print(f"⏭️  Skipped objects:      {stats['skipped_objects']:,}")
    print(f"🧪 Batch embed failures:  {stats['batches_failed']:,}")
    print(f"🪓 Docs fallback-chunked: {stats['docs_fallback_chunked']:,}")
    print(f"❌ Failed docs/chunks:    {stats['chunks_failed']:,}")
    print(f"{'─'*60}")

    if total_elapsed > 0:
        obj_per_sec = stats["objects_read"] / total_elapsed
        chunks_per_sec = stats["chunks_indexed"] / total_elapsed
        print(f"⚡ Performance:          {obj_per_sec:.1f} obj/s, {chunks_per_sec:.1f} chunks/s")

    if stats["chunks_indexed"] == 0:
        print(f"\n⚠️  WARNING: No chunks were indexed! Check embedding server.")
    if stats["chunks_failed"] > 0:
        print(f"\n⚠️  WARNING: {stats['chunks_failed']:,} docs/chunks failed to embed/index.")
    if stats["batches_failed"] > 0:
        print(f"\nℹ️  Note: {stats['batches_failed']:,} batch embedding attempts required salvage/fallback.")
    if stats["chunks_indexed"] > 0 and stats["chunks_failed"] == 0:
        print(f"\n🎉 Indexing completed without embedding/index failures!")

    print(f"{'='*60}\n")
    return stats


# ----------------------------
# 10. CLI Entry
# ----------------------------
def validate_json_files(source_dir: Path):
    print(f"🔍 Validating JSON files in: {source_dir}")

    json_files = list(source_dir.rglob("*.json"))
    if not json_files:
        print("❌ No .json files found!")
        return

    for json_path in json_files:
        print(f"\n📄 {json_path.name}")
        try:
            obj_count = 0
            sample_obj = None

            for obj in iter_json_objects(json_path):
                obj_count += 1
                if sample_obj is None:
                    sample_obj = obj

            print(f"   ✅ Valid JSON with {obj_count} objects")

            if sample_obj:
                print(f"   📋 Keys: {list(sample_obj.keys())}")

                if "_id" in sample_obj:
                    print(f"   🆔 Sample _id: {sample_obj['_id']}")

                question = str(sample_obj.get("question", "") or "")
                expected = str(sample_obj.get("expected", "") or "")
                laws = sample_obj.get("laws", []) or []
                provisions = sample_obj.get("provisions", []) or []

                print(f"   ❓ Question length: {len(question)}")
                print(f"   ✅ Expected length: {len(expected)}")
                print(f"   ⚖️ Laws count: {len(laws)}")
                print(f"   📜 Provisions count: {len(provisions)}")

        except Exception as e:
            print(f"   ❌ Error: {e}")


def show_collection_stats(chroma_dir: Path, collection_name: str):
    print(f"📊 Collection stats: {collection_name}")
    print(f"📂 DB path: {chroma_dir}")

    try:
        client = PersistentClient(path=str(chroma_dir))
        coll = client.get_collection(name=collection_name)

        count = coll.count()
        print(f"\n✅ Collection exists")
        print(f"📚 Total documents: {count}")

        if count > 0:
            sample = coll.peek(limit=3)
            print(f"\n📋 Sample documents:")
            for i, (doc_id, doc, meta) in enumerate(
                zip(sample.get("ids", []), sample.get("documents", []), sample.get("metadatas", []))
            ):
                print(f"\n   [{i+1}] ID: {doc_id}")
                print(f"       Metadata: {meta}")
                print(f"       Text preview: {doc[:200] if doc else 'N/A'}...")

    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    ap = argparse.ArgumentParser(
        description="JSON-based RAG Ingest Pipeline (v2)"
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    cnt = sub.add_parser("count", help="Count objects in JSON files (streaming, no embeddings)")
    cnt.add_argument("--source", default="kb/documents")

    ing = sub.add_parser("ingest", help="Ingest JSON documents into ChromaDB")
    ing.add_argument("--source", default="kb/documents")
    ing.add_argument("--chroma_dir", default="kb/chroma_json")
    ing.add_argument("--collection", default="chroma_json")
    ing.add_argument("--reset", action="store_true")
    ing.add_argument("--always-chunk", action="store_true")
    ing.add_argument("--batch-size", type=int, default=BATCH_SIZE)

    val = sub.add_parser("validate", help="Validate JSON files without ingesting")
    val.add_argument("--source", default="kb/documents")

    stats_p = sub.add_parser("stats", help="Show collection statistics")
    stats_p.add_argument("--chroma_dir", default="kb/chroma_json")
    stats_p.add_argument("--collection", default="chroma_json")

    args = ap.parse_args()

    if args.cmd == "ingest":
        ingest_json(
            Path(args.source),
            Path(args.chroma_dir),
            args.collection,
            args.reset,
            args.always_chunk,
            batch_size=args.batch_size,
        )
    elif args.cmd == "validate":
        validate_json_files(Path(args.source))
    elif args.cmd == "stats":
        show_collection_stats(Path(args.chroma_dir), args.collection)
    elif args.cmd == "count":
        total = 0
        src = Path(args.source)
        for jp in src.rglob("*.json"):
            c = 0
            for _ in iter_json_objects(jp):
                c += 1
            print(f"{jp.name}: {c:,} objects")
            total += c
        print(f"TOTAL: {total:,} objects")


if __name__ == "__main__":
    main()
