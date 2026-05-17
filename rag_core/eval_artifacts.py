from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def _strip_markdown_code_fence(text: Any) -> str:
    raw = str(text or "").strip()
    if not raw.startswith("```"):
        return raw
    lines = raw.splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _extract_judge_explanation_text(reason: Any) -> str:
    raw = _strip_markdown_code_fence(reason)
    if raw in {"", "[]", "{}", "null", "None", "none"}:
        return ""
    if raw.startswith("{") or raw.startswith("["):
        try:
            parsed = json.loads(raw)
        except Exception:
            parsed = None
        if isinstance(parsed, dict):
            explanation = str(parsed.get("explanation") or parsed.get("judge_explanation") or parsed.get("reason") or "").strip()
            if explanation:
                return explanation
    return raw


def _collapse_nonempty_lines(value: Any) -> str:
    text_value = str(value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text_value:
        return ""
    return "\n".join(line.strip() for line in text_value.splitlines() if line.strip()).strip()


def _write_core_artifacts(df_out, out_dir: Path, mlflow) -> None:
    pred_json = out_dir / "predictions_10q.json"
    pred_json.write_text(json.dumps(df_out.to_dict(orient="records"), ensure_ascii=False, indent=2), encoding="utf-8")
    mlflow.log_artifact(str(pred_json), artifact_path="eval")


def _log_triad_report(out_dir: Path, mlflow, scorers_module) -> None:
    try:
        triad_report = sorted(getattr(scorers_module, "TRIAD_JUDGE_LOG", []) or [], key=lambda item: item.get("id", -1))
        triad_md = out_dir / "triad_groundedness_report.md"
        lines = ["# RAG Triad - Groundedness judge report", ""]
        for row in triad_report:
            lines.extend(
                [
                    f"## Question ID {row.get('id', -1)}",
                    f"**Question:** {row.get('question', '')}",
                    f"**Answer:** {row.get('answer', '')}",
                    f"**Groundedness score:** {float(row.get('triad_groundedness', 0.0)):.3f}",
                    "",
                    "**Judge explanation:**",
                    "",
                    _extract_judge_explanation_text(row.get("judge_explanation")) or "_(no explanation)_",
                    "",
                    "---",
                    "",
                ]
            )
        triad_md.write_text("\n".join(lines), encoding="utf-8")
        mlflow.log_artifact(str(triad_md), artifact_path="eval")
    except Exception:
        pass


def _write_metric1_selection_artifact(out_dir: Path, mlflow, report: Dict[str, Any]) -> None:
    metric1 = report.get("metric1") if isinstance(report, dict) else {}
    if not isinstance(metric1, dict):
        metric1 = {}
    rows = metric1.get("rows") if isinstance(metric1.get("rows"), list) else []
    summary = metric1.get("summary") if isinstance(metric1.get("summary"), dict) else {}

    path = out_dir / "metric1_statute_grounding.md"
    lines: List[str] = ["# Metric 1 - Statute Grounding", ""]

    def _append_values(label: str, values: List[Any]) -> None:
        lines.append(f"**{label}:**")
        if values:
            lines.extend(f"- {str(value).strip()}" for value in values)
        else:
            lines.append("- none")
        lines.append("")

    if summary:
        lines.extend([
            "## Summary",
            "",
            f"Questions with gold annotations: {int(summary.get('questions_with_gold', 0))}",
            f"True positives: {int(summary.get('tp', 0))}",
            f"False positives: {int(summary.get('fp', 0))}",
            f"False negatives: {int(summary.get('fn', 0))}",
            f"Precision: {float(summary.get('precision', 0.0)):.3f}",
            f"Recall: {float(summary.get('recall', 0.0)):.3f}",
            f"F1: {float(summary.get('f1', 0.0)):.3f}",
            "",
        ])

    for row in rows:
        lines.extend([
            f"## ID {int(row.get('id', -1))} | Status: {str(row.get('status') or '').strip().upper()}",
            "",
            f"**Question:** {str(row.get('question') or '').strip()}",
            "",
        ])
        _append_values("Expected Provisions", row.get("gold_zakony") or [])
        _append_values("Model-Selected Provisions", row.get("predicted_zakony") or [])
        lines.extend([
            "**Structured output:**",
            "",
            "```json",
            json.dumps(row.get("structured_output") or [], ensure_ascii=False, indent=2),
            "```",
            "",
            f"**True positives:** {json.dumps(row.get('tp') or [], ensure_ascii=False)}",
            f"**False positives:** {json.dumps(row.get('fp') or [], ensure_ascii=False)}",
            f"**False negatives:** {json.dumps(row.get('fn') or [], ensure_ascii=False)}",
            "",
            f"**Verdict:** {str(row.get('verdict') or '').strip()}",
            "",
            "---",
            "",
        ])

    path.write_text("\n".join(lines), encoding="utf-8")
    mlflow.log_artifact(str(path), artifact_path="eval")


def _render_metric_claims(
    *,
    path: Path,
    title: str,
    judge_task_text: str,
    summary_note: str,
    rows: List[Dict[str, Any]],
    summary: Dict[str, Any],
    empty_message: str,
    comparison_block_title: str,
    comparison_key: str,
    empty_comparison_message: str,
) -> None:
    applicable_rows = [row for row in rows if isinstance(row, dict) and bool(row.get("applicable"))]
    skipped_questions = max(0, len(rows) - len(applicable_rows))
    lines: List[str] = [title, ""]

    def _append_values(label: str, values: List[Any]) -> None:
        lines.append(f"**{label}:**")
        if values:
            lines.extend(f"- {str(value).strip()}" for value in values)
        else:
            lines.append("- none")
        lines.append("")

    if summary:
        lines.extend([
            "## Summary",
            "",
            f"Evaluated questions: {int(summary.get('evaluated_questions', 0))}",
            f"Evaluated model-selected provisions: {int(summary.get('evaluated_tp_spans', 0))}",
            f"Mean question score: {float(summary.get('question_mean', 0.0)):.3f}",
            f"Mean provision score: {float(summary.get('claim_mean', 0.0)):.3f}",
            f"Skipped questions: {int(skipped_questions)}",
            summary_note,
            "",
        ])

    if not applicable_rows:
        lines.extend([empty_message, ""])

    for row in applicable_rows:
        selected_zakony = [
            str(claim_row.get("zakon") or "").strip()
            for claim_row in (row.get("claims") or [])
            if isinstance(claim_row, dict) and str(claim_row.get("zakon") or "").strip()
        ]
        lines.extend([
            f"## ID {int(row.get('id', -1))} | Status: {str(row.get('status') or '').strip().upper()}",
            "",
            f"**Question:** {str(row.get('question') or '').strip()}",
            "",
        ])
        _append_values("Model-Selected Provisions", selected_zakony)
        lines.extend([
            f"**Question score:** {float(row.get('question_score', 0.0)):.3f}",
            "",
        ])

        for claim_row in row.get("claims") or []:
            if not isinstance(claim_row, dict):
                continue
            lines.extend([
                f"### Model-Selected Provision {int(claim_row.get('index', 0))}",
                "",
                "**Provision:**",
                str(claim_row.get('zakon') or '').strip(),
                "",
                "**Text written by the model for this provision:**",
                "",
                "```text",
                str(claim_row.get("structured_answer") or "").strip() or "Structured odpoved_vygenerovana nebola dostupna.",
                "```",
                "",
                f"**{comparison_block_title}:**",
                "",
                "```text",
                _collapse_nonempty_lines(claim_row.get(comparison_key)) or empty_comparison_message,
                "```",
                "",
                "**What the judge evaluated:**",
                judge_task_text,
                "",
                f"**Score:** {float(claim_row.get('score', 0.0)):.3f}",
                f"**Verdict:** {str(claim_row.get('verdict') or '').strip()}",
                "",
                "**Judge Explanation:**",
                _extract_judge_explanation_text(claim_row.get("judge_reason")) or "Sudca nevratil odovodnenie.",
                "",
            ])
        lines.extend(["---", ""])

    path.write_text("\n".join(lines), encoding="utf-8")


def _write_metric2_span_faithfulness_artifact(out_dir: Path, mlflow, report: Dict[str, Any]) -> None:
    metric2 = report.get("metric2") if isinstance(report, dict) else {}
    if not isinstance(metric2, dict):
        metric2 = {}
    path = out_dir / "metric2_span_faithfulness.md"
    _render_metric_claims(
        path=path,
        title="# Metric 2 - Structured Answer Faithfulness to Legal Text",
        judge_task_text="Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.",
        summary_note="Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.",
        rows=metric2.get("rows") if isinstance(metric2.get("rows"), list) else [],
        summary=metric2.get("summary") if isinstance(metric2.get("summary"), dict) else {},
        empty_message="No model-selected provisions were available for metric 2.",
        comparison_block_title="Text of legal provision",
        comparison_key="law_text",
        empty_comparison_message="Text pravneho predpisu nebol dostupny.",
    )
    mlflow.log_artifact(str(path), artifact_path="eval")


def _write_metric3_expected_alignment_artifact(out_dir: Path, mlflow, report: Dict[str, Any]) -> None:
    metric3 = report.get("metric3") if isinstance(report, dict) else {}
    if not isinstance(metric3, dict):
        metric3 = {}
    path = out_dir / "metric3_expected_alignment.md"
    _render_metric_claims(
        path=path,
        title="# Metric 3 - Expected Alignment",
        judge_task_text="Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.",
        summary_note="Metrika 3 porovnava text modelu s relevantnym vyrezom expertnej expected odpovede pre ten isty pravny predpis. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.",
        rows=metric3.get("rows") if isinstance(metric3.get("rows"), list) else [],
        summary=metric3.get("summary") if isinstance(metric3.get("summary"), dict) else {},
        empty_message="No model-selected provisions were available for metric 3.",
        comparison_block_title="Extracted expected span",
        comparison_key="expected_span",
        empty_comparison_message="Gold span nebol dostupny alebo dany predpis nebol v expected odpovedi oznaceny.",
    )
    mlflow.log_artifact(str(path), artifact_path="eval")
