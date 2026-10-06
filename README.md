# Legal RAG Evaluation

A Python project for evaluating how a RAG system uses Slovak legal sources when answering questions. It retrieves legal provisions, generates an answer, and checks **which provisions the model chose, whether its explanations follow the legal text, and how they compare with an expert answer**.

I built this project for my bachelor's thesis. The repository contains the RAG pipeline, custom evaluation logic, a legal QA dataset, and saved experiment reports. It is an experimental system run through Python scripts.

## What is being evaluated?

A fluent answer can still cite the wrong paragraph or draw a conclusion that the source does not support. This project separates those problems into three metrics:

| Metric | What it checks | How it is measured |
| --- | --- | --- |
| **1. Statute grounding** | Did the model select the provisions listed in the reference annotations? | Deterministic comparison of provision IDs: true positives, extra citations, missing citations, precision, recall, and F1. |
| **2. Faithfulness to legal text** | Is the model's explanation for a selected provision supported by that provision's retrieved text? | An LLM judge compares the explanation with the source text. |
| **3. Alignment with the expert answer** | Does the explanation agree with the relevant part of the expert answer for the same provision? | An LLM judge compares the two text fragments. |

Metrics 2 and 3 use scores of **0, 0.5, or 1** for unsupported, partially supported, or fully supported explanations. Reports include the judge's reasoning and the texts being compared.

Metric 2 checks model-selected provisions. Metric 3 checks provisions that also occur in the reference annotations and can be located in the expert answer. Skipped cases are recorded, so the two metrics can cover different subsets of the data.

The pipeline also logs a separate **whole-answer groundedness** score through MLflow GenAI, comparing the final answer with the retrieved context. This is distinct from the provision-level metrics above.

## How the RAG pipeline works

```text
Indexing
Annotated JSON → legal provisions → embeddings via Ollama → ChromaDB

Answering
Question → query embedding → top-k vector search → legal context
         → structured explanations per provision → final answer

Evaluation
Generated output + retrieved sources + reference annotations / expert answer
         → deterministic checks + LLM judge → MLflow + JSON / Markdown reports
```

Retrieval uses **dense vector search** in ChromaDB. The default embedding model is `qwen3-embedding:4b`, served locally by Ollama. There is no BM25 combination or reranking stage in the current pipeline.

The index contains legal provision texts and their identifying information. Questions and expert answer bodies are excluded from the indexed text. Provisions are generally kept whole; optional chunking and fallback splitting handle longer inputs.

Generation has two LLM calls. The first produces structured explanations tied to provision IDs; the second combines those explanations into a readable answer. The intermediate format makes each explanation available for evaluation:

```json
{
  "citacie_json": [
    {
      "zakon": "513/1991/paragraf-122",
      "odpoved_vygenerovana": "An explanation supported by this provision."
    }
  ]
}
```

`zakon` identifies a law and paragraph; `odpoved_vygenerovana` contains the generated explanation. These Slovak field names are used throughout the code. The pipeline checks the output format and records statuses for missing context, invalid JSON, empty results, and generation failures.

## Repository map

```text
rag_core/                              Retrieval, generation, and evaluation
├── __init__.py                        Package version and lazy evaluation entry points
├── config.py                          Environment-based paths, models, APIs, and runtime settings
├── prompts.py                         Generation prompts and Pydantic / JSON output schema
├── eval_pipeline.py                   Query embedding, retrieval, context assembly, and generation
├── eval_local.py                      Experiment runner: load data, run RAG, calculate and log metrics
├── deterministic_core.py              Provision ID normalization and precision / recall / F1 calculations
├── scorers.py                         LLM judge prompts, scoring calls, and expert-fragment extraction
├── eval_artifacts.py                  Prediction JSON and per-metric Markdown report writers
└── batch_summary.py                   Aggregate metric reports and generate a summary

scripts/                               Data and index preparation utilities
├── scrape.py                          Collect questions and expert answers from najpravo.sk
├── create_json_collections.py          Clean provision texts, embed them, and upsert into ChromaDB
├── run_eval_batches.py                Prepare input batches and a manifest
└── summarize_eval_batches.py           Merge saved batch prediction JSON files

data/
├── otazky-najpravo-doplnene.json        Enriched source dataset: 90 QA records
└── eval_batches_10q/                   Saved evaluation inputs: 29 questions across 10 batches
    ├── batch_01.json … batch_10.json   Question, expert answer, and category
    └── manifest.json                  Input provenance, batch size, counts, and filenames

eval/batches/
├── batches_01/ … batches_10/           Three metric reports for each saved batch
│   ├── metric1_statute_grounding.md   Selected versus reference provisions
│   ├── metric2_span_faithfulness.md   Explanations versus legal source texts
│   └── metric3_expected_alignment.md  Explanations versus expert answer fragments
└── summary_02/summary.md               Combined results and interpretation

config/litellm_config.yaml              Example Gemini generation / judge routes through Vertex AI
requirements.txt                       Python dependencies from the experiment environment
.gitignore                             Excludes secrets, local indexes, MLflow data, and caches
```

Despite its name, `run_eval_batches.py` only prepares data; evaluation runs through `rag_core.eval_local`. Similarly, `summarize_eval_batches.py` merges predictions, while `rag_core.batch_summary` produces the written summary. The saved `eval_batches_10q` files contain two or three questions each.

## Technologies and their roles

| Technology | Role in this project |
| --- | --- |
| **Python** | Pipeline orchestration, data preparation, and evaluation logic. |
| **Ollama + Qwen3-Embedding-4B** | Local embeddings for both provisions and queries. The model is configurable. |
| **ChromaDB** | Persistent vector storage and top-k retrieval; local and HTTP client modes are supported. |
| **OpenAI Python SDK** | Calls generation and judge models through configurable OpenAI-compatible endpoints. |
| **LiteLLM / Vertex AI** | Provider routing illustrated by the included Gemini configuration. |
| **MLflow / MLflow GenAI** | Experiment runs, metrics, artifacts, evaluation, and optional tracing. |
| **Pydantic** | Structured citation output models and JSON Schema generation. |
| **pandas** | Evaluation input tables and prediction records. |
| **requests, BeautifulSoup, ftfy** | HTTP requests, QA page parsing, and text cleanup. |
| **LangChain Text Splitters** | Optional document splitting during indexing. |
| **python-dotenv** | Loading local experiment configuration from `.env` files. |

The active evaluation uses custom scorers. Packages such as RAGAS, datasets, and Groq remain in `requirements.txt` from the experiment environment but are not directly used by the current pipeline.
