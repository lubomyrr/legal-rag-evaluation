from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH_ROOT = PROJECT_ROOT / "eval" / "batches"
DEFAULT_OUTPUT_DIR = DEFAULT_BATCH_ROOT / "summary_02"
DEFAULT_ENV = PROJECT_ROOT / ".env"
QUESTION_SECTION_RE = re.compile(r"^## ID (?P<id>\d+) \| Status: (?P<status>[^\n]+)\n(?P<body>.*?)(?=^## ID \d+ \| Status: |\Z)", re.M | re.S)
PROVISION_SECTION_RE = re.compile(r"^### Model-Selected Provision \d+\n(?P<body>.*?)(?=^### Model-Selected Provision \d+\n|\Z)", re.M | re.S)
SUMMARY_INT_RE = re.compile(r"^(?P<label>Questions with gold annotations|True positives|False positives|False negatives):\s*(?P<value>\d+)\s*$", re.M)
LIST_LINE_RE = re.compile(r"^\*\*(?P<label>True positives|False positives|False negatives):\*\*\s*(?P<value>\[[^\n]*\])\s*$", re.M)
VERDICT_ORDER = ("SUPPORTED", "PARTIALLY_SUPPORTED", "UNSUPPORTED")
VERDICT_LABELS = {
    "SUPPORTED": "SUPPORTED (odpoveď je vecne v súlade so zdrojom)",
    "PARTIALLY_SUPPORTED": "PARTIALLY_SUPPORTED (jadro sedí, ale odpoveď je neúplná alebo menej presná)",
    "UNSUPPORTED": "UNSUPPORTED (odpoveď nie je podložená zdrojom alebo ho skresľuje)",
}


def _load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _batch_sort_key(path: Path) -> Tuple[int, str]:
    match = re.search(r"(\d+)", path.name)
    return (int(match.group(1)) if match else 10**9, path.name.lower())


def _discover_batch_dirs(root: Path) -> List[Path]:
    candidates: List[Path] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        if (child / "metric1_statute_grounding.md").exists() and (child / "metric2_span_faithfulness.md").exists() and (child / "metric3_expected_alignment.md").exists():
            candidates.append(child)
    return sorted(candidates, key=_batch_sort_key)


def _extract_inline_value(body: str, label: str) -> str:
    match = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", body)
    return match.group(1).strip() if match else ""


def _extract_multiline_value(body: str, label: str) -> str:
    pattern = re.compile(rf"\*\*{re.escape(label)}:\*\*\s*\n(?P<value>.*?)(?=\n\*\*[^\n]+:\*\*|\Z)", re.S)
    match = pattern.search(body)
    return match.group("value").strip() if match else ""


def _clean_explanation(raw: str) -> str:
    text = str(raw or "").strip()
    if not text:
        return ""
    if text.startswith("```") and text.endswith("```"):
        lines = text.splitlines()[1:-1]
        text = "\n".join(lines).strip()
    if text.startswith("{"):
        try:
            parsed = json.loads(text)
        except Exception:
            parsed = None
        if isinstance(parsed, dict):
            text = str(parsed.get("explanation") or parsed.get("judge_explanation") or text).strip()
    return text


def _parse_json_list(raw: str) -> List[str]:
    value = str(raw or "").strip()
    if not value:
        return []
    try:
        parsed = json.loads(value)
    except Exception:
        return []
    return [str(item).strip() for item in parsed if str(item).strip()] if isinstance(parsed, list) else []


def _parse_metric1(batch_dirs: List[Path]) -> Dict[str, Any]:
    totals = dict.fromkeys(
        ("Questions with gold annotations", "True positives", "False positives", "False negatives"),
        0,
    )
    error_counts: Dict[str, Dict[str, int]] = {
        "False positives": {},
        "False negatives": {},
    }

    for batch_dir in batch_dirs:
        text = _load_text(batch_dir / "metric1_statute_grounding.md")
        for match in SUMMARY_INT_RE.finditer(text):
            label = match.group("label")
            totals[label] += int(match.group("value"))

        for question_match in QUESTION_SECTION_RE.finditer(text):
            body = question_match.group("body")
            for list_match in LIST_LINE_RE.finditer(body):
                counts = error_counts.get(list_match.group("label"))
                if counts is None:
                    continue
                for law_id in _parse_json_list(list_match.group("value")):
                    counts[law_id] = counts.get(law_id, 0) + 1

    tp = totals["True positives"]
    fp = totals["False positives"]
    fn = totals["False negatives"]
    precision = float(tp / (tp + fp)) if (tp + fp) else 0.0
    recall = float(tp / (tp + fn)) if (tp + fn) else 0.0
    f1 = float((2 * precision * recall) / (precision + recall)) if (precision + recall) else 0.0
    return {
        "questions_total": totals["Questions with gold annotations"],
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "most_common_false_positives": sorted(error_counts["False positives"].items(), key=lambda item: (-item[1], item[0]))[:10],
        "most_common_false_negatives": sorted(error_counts["False negatives"].items(), key=lambda item: (-item[1], item[0]))[:10],
    }


def _parse_metric_explanations(path: Path) -> List[Dict[str, Any]]:
    text = _load_text(path)
    entries: List[Dict[str, Any]] = []
    batch_name = path.parent.name

    for question_match in QUESTION_SECTION_RE.finditer(text):
        local_id = int(question_match.group("id"))
        q_body = question_match.group("body")
        question = _extract_inline_value(q_body, "Question")

        for provision_match in PROVISION_SECTION_RE.finditer(q_body):
            p_body = provision_match.group("body")
            provision_text = _extract_multiline_value(p_body, "Provision")
            provision = provision_text.splitlines()[0].strip() if provision_text else ""
            explanation = _clean_explanation(_extract_multiline_value(p_body, "Judge Explanation"))
            if not explanation:
                continue
            score_raw = _extract_inline_value(p_body, "Score")
            verdict = _extract_inline_value(p_body, "Verdict")
            try:
                score = float(score_raw)
            except Exception:
                score = None

            entries.append(
                {
                    "batch_name": batch_name,
                    "batch_question_id": local_id,
                    "question": question,
                    "provision": provision,
                    "score": score,
                    "verdict": verdict,
                    "judge_explanation": explanation,
                }
            )
    return entries


_METRIC_DESCRIPTIONS: Dict[str, str] = {
    "metric2_span_faithfulness": (
        "Metrika 2 hodnotí vecnú vernosť textu modelu voči citovanému právnemu ustanoveniu. "
        "Pre každý paragraf, ktorý model vybral, sa porovná stručné vysvetlenie modelu so skutočným znením paragrafu. "
        "SUPPORTED znamená, že text modelu zostáva pri obsahu zákona. "
        "PARTIALLY_SUPPORTED znamená, že jadro je správne, ale chýbajú podmienky, výnimky alebo je text príliš zovšeobecnený. "
        "UNSUPPORTED znamená, že text nie je opretý o dané ustanovenie alebo jeho význam skresľuje."
    ),
    "metric3_expected_alignment": (
        "Metrika 3 hodnotí zhodu textu modelu s referenčnou odbornou odpoveďou pre dané ustanovenie. "
        "Pre každý citovaný paragraf sa text modelu porovná s relevantným výrezom z expertnej odpovede. "
        "SUPPORTED znamená obsahovú zhodu s odborným referenčným textom. "
        "PARTIALLY_SUPPORTED znamená, že jadro sedí, ale výstup je neúplný alebo menej presný. "
        "UNSUPPORTED znamená, že model vystihol iný právny bod alebo uviedol vecne nesprávny obsah."
    ),
}

_METRIC_DISPLAY_NAMES: Dict[str, str] = {
    "metric2_span_faithfulness": "Faithfulness to Legal Text",
    "metric3_expected_alignment": "Alignment with Expert Expected Answer",
}


def _summary_prompt(metric_name: str, metric_description: str, entries: List[Dict[str, Any]]) -> str:
    verdict_counts = _count_verdicts(entries)
    display_name = _METRIC_DISPLAY_NAMES.get(metric_name, metric_name)

    lines = [
        f"Metrika: {display_name}",
        f"Popis metriky: {metric_description}",
        "",
        f"Celkový počet hodnotených záznamov: {len(entries)}",
        "Rozdelenie verdiktov:",
    ]
    for verdict, count in sorted(verdict_counts.items()):
        pct = round(100.0 * count / len(entries)) if entries else 0
        lines.append(f"- {verdict}: {count} ({pct} %)")
    lines.append("")
    lines.append("Vysvetlenia sudcu (judge explanations):")
    for entry in entries:
        lines.extend(
            [
                "---",
                f"Paragraf: {entry.get('provision')}",
                f"Verdikt: {entry.get('verdict')}",
                f"Skore: {entry.get('score')}",
                f"Otazka: {entry.get('question')}",
                str(entry.get("judge_explanation") or "").strip(),
            ]
        )
    return "\n".join(lines)


def _count_verdicts(entries: List[Dict[str, Any]]) -> Dict[str, int]:
    verdict_counts: Dict[str, int] = {}
    for entry in entries:
        verdict = str(entry.get("verdict") or "UNKNOWN").strip() or "UNKNOWN"
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
    return verdict_counts


def _format_count_pct(count: int, total: int) -> str:
    pct = round(100.0 * count / total) if total else 0
    return f"{count} ({pct} %)"


def _format_metric_overview(entries: List[Dict[str, Any]]) -> str:
    counts = _count_verdicts(entries)
    total = len(entries)
    lines = [
        "### Celkový obraz",
        "",
        f"- Hodnotených záznamov: {total}",
    ]
    for verdict in VERDICT_ORDER:
        lines.append(f"- {VERDICT_LABELS[verdict]}: {_format_count_pct(counts.get(verdict, 0), total)}")
    for verdict, count in sorted(counts.items()):
        if verdict not in VERDICT_ORDER:
            lines.append(f"- {verdict}: {_format_count_pct(count, total)}")
    return "\n".join(lines)


def _format_metric1_summary(metric1_summary: Dict[str, Any]) -> str:
    questions_total = int(metric1_summary.get("questions_total", 0))
    tp = int(metric1_summary.get("tp", 0))
    fp = int(metric1_summary.get("fp", 0))
    fn = int(metric1_summary.get("fn", 0))
    selected_total = tp + fp
    expected_total = tp + fn
    precision = float(metric1_summary.get("precision", 0.0))
    recall = float(metric1_summary.get("recall", 0.0))
    f1 = float(metric1_summary.get("f1", 0.0))

    return "\n".join(
        [
            f"- Počet hodnotených otázok: {questions_total}",
            f"- Správne nájdené paragrafy (zhoda s expertom): {tp}/{expected_total}",
            f"- Nesprávne pridané paragrafy (model vybral navyše): {fp}/{selected_total}",
            f"- Nenájdené paragrafy (model vynechal): {fn}/{expected_total}",
            f"- Presnosť (Precision - správne z modelom vybraných paragrafov): {tp}/{selected_total} = {precision:.3f}",
            f"- Pokrytie (Recall - nájdené z expertom očakávaných paragrafov): {tp}/{expected_total} = {recall:.3f}",
            f"- F1 skóre: {f1:.3f}",
            "",
            "F1 skóre je spoločné zhrnutie precision a recall. V tejto metrike teda ukazuje kompromis medzi tým, či model nevyberá paragrafy navyše, a tým, či nevynecháva paragrafy očakávané expertom.",
        ]
    )


def _remove_markdown_sections(text: str, blocked_titles: set[str]) -> str:
    lines = text.splitlines()
    kept: List[str] = []
    skip = False
    for line in lines:
        match = re.match(r"^###\s+(.+?)\s*$", line)
        if match:
            title = match.group(1).strip().lower()
            skip = title in blocked_titles
        if not skip:
            kept.append(line)
    return "\n".join(kept).strip()


def _summarize_entries(metric_name: str, entries: List[Dict[str, Any]], model: str, base_url: str, api_key: str) -> str:
    client = OpenAI(base_url=base_url, api_key=api_key)
    metric_description = _METRIC_DESCRIPTIONS.get(metric_name, metric_name)
    system_prompt = (
        "Si analytik hodnotenia pre bakalársku prácu o slovenskom právnom RAG systéme. "
        f"Popis metriky, ktoru sumarizujes: {metric_description} "
        "Dostaneš štatistiku verdiktov a vysvetlenia LLM sudcu pre jednotlivé záznamy. "
        "Napíš stručné, vecné markdown zhrnutie vhodné do záverečnej prezentácie bakalárskej práce. "
        "Povinná sekcia: ### Vysvetlenie výsledku. "
        "Pravidla: "
        "(1) Uvádzaj iba to, čo priamo vyplýva z dodaných vysvetlení sudcu. "
        "(2) Nevytváraj sekciu 'Celkový obraz', tá bude doplnená deterministicky zo štatistík. "
        "(3) Nevytváraj sekciu 'Záver' ani odrážkový zoznam. "
        "(4) V sekcii 'Vysvetlenie výsledku' napíš jeden súvislý odsek s 2 až 4 vetami. "
        "(5) Opíš, čo z výsledkov metriky vidno pre tento experiment; nepíš odporúčania, čo treba ďalej preveriť alebo opraviť. "
        "(6) Môžeš pomenovať silné stránky aj slabiny, ale bez dlhých príkladov, bez citovania konkrétnych paragrafov a bez rozpisovania jednotlivých prípadov. "
        "(7) Nepoužívaj konverzačné formulácie typu 'Jasné, tu je zhrnutie'. "
        "(8) Nepoužívaj nadhodnotené formulácie ako 'exceluje' alebo 'drvivá väčšina', ak nie sú priamo podložené číslami. "
        "(9) Nepoužívaj slovo 'span' ani interné technické názvy metriky. "
        "(10) Štýl má byť akademický, stručný a obhájiteľný. "
        "(11) Používaj normálnu slovenčinu s diakritikou."
    )
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": _summary_prompt(metric_name, metric_description, entries)},
        ],
    )
    summary = (response.choices[0].message.content or "").strip()
    return _remove_markdown_sections(
        summary,
        {
            "celkovy obraz",
            "celkový obraz",
            "zaver",
            "záver",
            "opakujuce sa zistenia zo judge reasoning",
            "opakujúce sa zistenia zo judge reasoning",
        },
    )


def _cleanup_old_summary_files(output_dir: Path) -> None:
    if not output_dir.exists():
        return
    for path in output_dir.iterdir():
        if path.is_file():
            path.unlink()


def build_batch_summary_artifacts(*, batch_root: Path, output_dir: Path) -> Dict[str, Path]:
    batch_dirs = _discover_batch_dirs(batch_root)
    if not batch_dirs:
        raise RuntimeError(f"No batch metric directories found in {batch_root}")

    output_dir.mkdir(parents=True, exist_ok=True)
    _cleanup_old_summary_files(output_dir)

    metric1_summary = _parse_metric1(batch_dirs)

    metric2_entries: List[Dict[str, Any]] = []
    metric3_entries: List[Dict[str, Any]] = []
    for batch_dir in batch_dirs:
        metric2_entries.extend(_parse_metric_explanations(batch_dir / "metric2_span_faithfulness.md"))
        metric3_entries.extend(_parse_metric_explanations(batch_dir / "metric3_expected_alignment.md"))

    model = os.getenv("JUDGE_MODEL") or os.getenv("LLM_MODEL") or ""
    base_url = os.getenv("JUDGE_BASE_URL") or os.getenv("OPENAI_BASE_URL") or os.getenv("LLM_BASE_URL") or ""
    api_key = os.getenv("JUDGE_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY") or ""
    if not model or not base_url:
        raise RuntimeError("Missing judge/LLM configuration for batch summary")

    metric2_summary = _summarize_entries("metric2_span_faithfulness", metric2_entries, model, base_url, api_key)
    metric3_summary = _summarize_entries("metric3_expected_alignment", metric3_entries, model, base_url, api_key)

    summary_path = output_dir / "summary.md"
    lines = [
        "# Summary",
        "",
        "## Metric 1 - Statute Grounding",
        "",
        _format_metric1_summary(metric1_summary),
        "",
        "## Metric 2 - Faithfulness to Legal Text",
        "",
        _format_metric_overview(metric2_entries),
        "",
        metric2_summary.strip(),
        "",
        "## Metric 3 - Alignment with Expert Expected Answer",
        "",
        _format_metric_overview(metric3_entries),
        "",
        metric3_summary.strip(),
        "",
    ]
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    return {"summary_md": summary_path}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build one summary.md from batch metric reports.")
    parser.add_argument("--batch-root", type=Path, default=DEFAULT_BATCH_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    build_batch_summary_artifacts(
        batch_root=args.batch_root.resolve(),
        output_dir=args.output_dir.resolve(),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

