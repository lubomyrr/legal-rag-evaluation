"""Deterministic scorers for legal RAG evaluation."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List, Tuple

_NUM_PAT = re.compile(r"[-+]?(?:\d{1,3}(?:[ \u00A0]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?)")
_STATUTE_RE = re.compile(r"(?:\u00A7|paragraf\w*)\s*(\d+[a-z]*)", re.IGNORECASE)
_CASE_NO_RE = re.compile(r"\b(\d{1,4}\s*[A-Za-z]+\s*(?:/|\s)\s*\d{1,6}\s*/\s*\d{4})\b")
_PARAGRAPH_ID_RE = re.compile(r"(\d+[a-z]*)", re.IGNORECASE)
_ZAKON_ID_RE = re.compile(r"^([1-9]\d{0,5}/(?:18|19|20)\d{2})/paragraf-(\d+[a-z]*)$", re.IGNORECASE)


# HELPER FUNCTIONS
def safe_str(v: Any) -> str:
    return str(v) if v is not None else ""


def normalize_question_key(text: Any) -> str:
    raw = safe_str(text)
    if not raw:
        return ""
    normalized = unicodedata.normalize("NFKC", raw)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized.lower()


def extract_decimals(text: str) -> List[Decimal]:
    out: List[Decimal] = []
    if not text:
        return out

    clean_text = safe_str(text).replace("*", "").replace("_", "")
    for raw in _NUM_PAT.findall(clean_text):
        clean = raw.replace(" ", "").replace("\u00A0", "").replace(",", ".")
        try:
            out.append(Decimal(clean))
        except InvalidOperation:
            pass
    return out


def extract_statute_refs(text: str) -> List[str]:
    if not text:
        return []
    clean_text = safe_str(text).replace("*", "").replace("_", "")
    return _STATUTE_RE.findall(clean_text)


def extract_case_numbers(text: str) -> List[str]:
    if not text:
        return []

    out: List[str] = []
    matches = _CASE_NO_RE.findall(safe_str(text))
    for match in matches:
        norm = re.sub(r"\s+", "", match).lower()
        norm = re.sub(r"^(\d{1,4}[a-z]+)(\d{1,6}/\d{4})$", r"\1/\2", norm)
        out.append(norm)
    return out


def _normalize_paragraph_id(paragraph: Any) -> str:
    raw = re.sub(r"\s+", "", safe_str(paragraph).strip().lower())
    if raw.startswith("paragraf-"):
        raw = raw[len("paragraf-") :]
    match = _PARAGRAPH_ID_RE.search(raw)
    return match.group(1).lower() if match else ""


def build_zakon_id(law: Any, paragraph: Any) -> str:
    law_s = re.sub(r"\s+", "", safe_str(law).strip())
    par_s = _normalize_paragraph_id(paragraph)
    if not law_s or not par_s:
        return ""
    return f"{law_s}/paragraf-{par_s}"


def normalize_zakon_id(zakon_id: Any) -> str:
    raw = re.sub(r"\s+", "", safe_str(zakon_id).strip())
    match = _ZAKON_ID_RE.fullmatch(raw)
    if not match:
        return ""
    return f"{match.group(1)}/paragraf-{match.group(2).lower()}"


def extract_gold_zakon_ids(provisions: List[Dict[str, Any]]) -> List[str]:
    keys = {
        build_zakon_id(item.get("law"), item.get("paragraph"))
        for item in (provisions or [])
        if isinstance(item, dict)
    }
    return sorted(key for key in keys if key)


def extract_predicted_zakon_ids(citacie_json: List[Dict[str, Any]]) -> List[str]:
    keys = {
        normalize_zakon_id(item.get("zakon"))
        for item in (citacie_json or [])
        if isinstance(item, dict)
    }
    return sorted(key for key in keys if key)


def _precision_recall_f1(
    true_positives: int,
    false_positives: int,
    false_negatives: int,
) -> Tuple[float, float, float]:
    precision = (
        float(true_positives / (true_positives + false_positives))
        if (true_positives + false_positives)
        else 0.0
    )
    recall = (
        float(true_positives / (true_positives + false_negatives))
        if (true_positives + false_negatives)
        else 0.0
    )
    f1 = float((2 * precision * recall) / (precision + recall)) if (precision + recall) else 0.0
    return precision, recall, f1


def compare_zakon_sets(predicted_ids: List[str], gold_ids: List[str]) -> Dict[str, Any]:
    predicted = {normalize_zakon_id(value) for value in (predicted_ids or []) if normalize_zakon_id(value)}
    gold = {normalize_zakon_id(value) for value in (gold_ids or []) if normalize_zakon_id(value)}

    true_positive_ids = sorted(predicted & gold)
    false_positive_ids = sorted(predicted - gold)
    false_negative_ids = sorted(gold - predicted)
    true_positives = len(true_positive_ids)
    false_positives = len(false_positive_ids)
    false_negatives = len(false_negative_ids)
    precision, recall, f1 = _precision_recall_f1(
        true_positives,
        false_positives,
        false_negatives,
    )

    return {
        "predicted_ids": sorted(predicted),
        "gold_ids": sorted(gold),
        "true_positive_ids": true_positive_ids,
        "false_positive_ids": false_positive_ids,
        "false_negative_ids": false_negative_ids,
        "true_positives": true_positives,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "exact_match": not false_positive_ids and not false_negative_ids,
    }


def summarize_statute_grounding_predictions(
    prediction_rows: List[Dict[str, Any]],
    gold_by_question: Dict[str, List[str]],
) -> Dict[str, Any]:
    total_tp = 0
    total_fp = 0
    total_fn = 0
    exact_match_questions = 0
    partial_match_questions = 0
    duplicate_questions = 0
    fp_counter: Counter[str] = Counter()
    fn_counter: Counter[str] = Counter()
    seen_questions: set[str] = set()
    rows: List[Dict[str, Any]] = []

    for index, row in enumerate(prediction_rows):
        question = safe_str(row.get("question")).strip()
        question_key = normalize_question_key(question)
        gold_ids = gold_by_question.get(question_key) or []
        predicted_ids = extract_predicted_zakon_ids(((row.get("outputs") or {}).get("citacie_json") or []))
        comparison = compare_zakon_sets(predicted_ids, gold_ids)

        total_tp += int(comparison["true_positives"])
        total_fp += int(comparison["false_positives"])
        total_fn += int(comparison["false_negatives"])
        fp_counter.update(comparison["false_positive_ids"])
        fn_counter.update(comparison["false_negative_ids"])

        if question_key in seen_questions:
            duplicate_questions += 1
        else:
            seen_questions.add(question_key)

        if comparison["exact_match"]:
            exact_match_questions += 1
        elif comparison["true_positive_ids"] or comparison["false_positive_ids"] or comparison["false_negative_ids"]:
            partial_match_questions += 1

        rows.append(
            {
                "id": int(row.get("global_question_id", index)),
                "batch_name": safe_str(row.get("batch_name")).strip(),
                "batch_question_id": row.get("batch_question_id"),
                "question": question,
                "gold_zakony": comparison["gold_ids"],
                "predicted_zakony": comparison["predicted_ids"],
                "tp": comparison["true_positive_ids"],
                "fp": comparison["false_positive_ids"],
                "fn": comparison["false_negative_ids"],
                "precision": comparison["precision"],
                "recall": comparison["recall"],
                "f1": comparison["f1"],
                "exact_match": comparison["exact_match"],
                "structured_output": ((row.get("outputs") or {}).get("citacie_json") or []),
            }
        )

    precision, recall, f1 = _precision_recall_f1(total_tp, total_fp, total_fn)
    return {
        "summary": {
            "questions_total": len(prediction_rows),
            "questions_with_gold": len(prediction_rows),
            "exact_match_questions": exact_match_questions,
            "partial_match_questions": partial_match_questions,
            "duplicate_questions_detected": duplicate_questions,
            "tp": total_tp,
            "fp": total_fp,
            "fn": total_fn,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "most_common_false_positives": fp_counter.most_common(10),
            "most_common_false_negatives": fn_counter.most_common(10),
        },
        "rows": rows,
    }
