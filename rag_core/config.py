from __future__ import annotations
import os
from pathlib import Path

def _bool_env(name: str, default: bool = False) -> bool:
    """Parse boolean environment variables like 1/true/yes/on (case-insensitive)."""
    v = os.getenv(name)
    if v is None:
        return default
    return v.strip().lower() in {"1", "true", "yes", "y", "on"}

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ChromaDB
CHROMA_DIR = Path(os.getenv("CHROMA_DIR", str(PROJECT_ROOT / "kb" / "chroma_json_law")))
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "slovak_law_json")

# Evaluation
EVAL_OUT_DIR = Path(os.getenv("EVAL_OUT_DIR", str(PROJECT_ROOT / "eval")))
EVAL_QUESTIONS_CSV = os.getenv("EVAL_QUESTIONS_CSV", os.getenv("EVAL_CSV", "eval/questions.csv"))

# LLM for answer generation
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1:latest")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:11434/v1"))
LLM_API_KEY = os.getenv("LLM_API_KEY", os.getenv("OPENAI_API_KEY", "not-needed"))

# Embeddings
EMB_MODEL = os.getenv("EMB_MODEL", "qwen3-embedding:4b")
EMBEDDING_BASE_URL = os.getenv("EMBEDDING_BASE_URL", "http://127.0.0.1:11434").rstrip("/")

# Judge model
JUDGE_MODEL = os.getenv("JUDGE_MODEL", os.getenv("LLM_MODEL", "vertex-gemini"))
JUDGE_BASE_URL = os.getenv("JUDGE_BASE_URL", os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:4000/v1"))
JUDGE_API_KEY = os.getenv("JUDGE_API_KEY", os.getenv("OPENAI_API_KEY", "anything"))

# RAG runtime settings
RETRIEVE_K = int(os.getenv("RETRIEVE_K", "40"))

# Triad scorer settings
TRIAD_MAX_CHARS = int(os.getenv("TRIAD_MAX_CHARS", "14000"))

# Chroma client mode
CHROMA_USE_HTTP = os.getenv("CHROMA_USE_HTTP", "0") == "1"
CHROMA_HTTP_HOST = os.getenv("CHROMA_HTTP_HOST", "127.0.0.1")
CHROMA_HTTP_PORT = int(os.getenv("CHROMA_HTTP_PORT", "8000"))

# MLflow
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "")
MLFLOW_EXPERIMENT_NAME = os.getenv("MLFLOW_EXPERIMENT_NAME", "qa-eval-local")
MLFLOW_LOG_TRACES = _bool_env("MLFLOW_GENAI_EVAL_LOG_TRACES", default=False)

# Evaluation
EVAL_LIMIT = int(os.getenv("EVAL_LIMIT", "0") or 0)



