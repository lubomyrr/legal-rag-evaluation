# legal-rag-reliability

Experimental prototype for a bachelor's thesis on evaluating the reliability of answers produced by a legal RAG system over Slovak legal texts.

## Repository contents

- `rag_core/` - retrieval, answer generation, and evaluation logic
- `scripts/` - dataset collection, indexing, and batch evaluation scripts
- `data/` - legal question dataset and prepared evaluation batches
- `eval/` - saved evaluation outputs used in the experiments

## Setup

1. Create a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a local `.env` file with the runtime settings required by `rag_core/config.py`.
4. Provide the local ChromaDB index used in the experiment before running the RAG pipeline.

## Main scripts

Collect legal Q&A data from Najpravo:

```bash
python scripts/scrape.py
```

Create or inspect the local JSON-based Chroma collection:

```bash
python scripts/create_json_collections.py --help
```

Prepare evaluation batches:

```bash
python scripts/run_eval_batches.py
```

Run local evaluation:

```bash
python -m rag_core.eval_local
```

Summarize saved batch outputs:

```bash
python scripts/summarize_eval_batches.py
```

## Notes

This repository is an academic prototype. Local secrets, virtual environments, MLflow runs, logs, and generated ChromaDB indexes are intentionally excluded from version control.
