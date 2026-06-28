# Legal RAG Evaluation System

Academic bachelor thesis prototype for evaluating the reliability of answers produced by a legal RAG system over Slovak legal texts.

The project focuses on legal question answering, retrieval over legal documents, LLM-based answer generation, and evaluation of whether generated answers correctly use the retrieved legal sources.

## Project Goal

The goal of this project is not to build a production legal assistant, but to create an experimental system for testing how reliable legal RAG answers are.

The work focuses on:

- preparing a legal QA dataset,
- retrieving relevant legal documents,
- generating answers with an LLM,
- tracking experiments with MLflow,
- evaluating answer reliability using custom metrics.

## Main Features

- Legal QA dataset preparation
- Local retrieval pipeline over Slovak legal documents
- ChromaDB-based vector search
- OpenAI-compatible LLM client support
- MLflow experiment tracking
- Batch evaluation pipeline
- Custom evaluation metrics for legal RAG reliability

## Evaluation Focus

The evaluation is based on three main aspects:

1. Source selection  
   Whether the system selected relevant legal sources.

2. Groundedness / faithfulness  
   Whether the generated answer is supported by the cited legal text.

3. Correct use of legal references  
   Whether the answer uses the legal source correctly and aligns with the expert answer.

## Tech Stack

**Core:**

- Python
- RAG architecture
- ChromaDB
- MLflow / MLflow GenAI
- OpenAI-compatible LLM APIs
- pandas
- JSON dataset processing

**Secondary:**

- LangChain
- RAGAS
- Pydantic
- BeautifulSoup
- requests

## Repository Structure

```text
rag_core/     Core retrieval, generation, and evaluation logic
scripts/      Dataset preparation, indexing, and batch evaluation scripts
data/         Legal QA dataset and prepared evaluation batches
eval/         Saved evaluation outputs and experiment artifacts
config/       Local model/provider configuration examples