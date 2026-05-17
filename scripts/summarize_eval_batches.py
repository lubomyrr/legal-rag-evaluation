from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH_ROOT = PROJECT_ROOT / "eval" / "batches"
DEFAULT_OUTPUT_FILE = DEFAULT_BATCH_ROOT / "merged_predictions_30q.json"
DEFAULT_MANIFEST_FILE = DEFAULT_BATCH_ROOT / "merged_manifest.json"


def _batch_sort_key(path: Path) -> Tuple[int, str]:
    match = re.search(r"(\d+)", path.name)
    return (int(match.group(1)) if match else 10**9, path.name.lower())


def _discover_batch_dirs(root: Path) -> List[Path]:
    candidates = []
    for child in root.iterdir():
        if child.is_dir() and (child / "predictions_10q.json").exists():
            candidates.append(child)
    return sorted(candidates, key=_batch_sort_key)


def _load_predictions(path: Path) -> List[Dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise RuntimeError(f"Expected JSON list in {path}")
    return [item for item in payload if isinstance(item, dict)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge batch prediction files into one 30-question JSON.")
    parser.add_argument("--batch-root", type=Path, default=DEFAULT_BATCH_ROOT)
    parser.add_argument("--output-file", type=Path, default=DEFAULT_OUTPUT_FILE)
    parser.add_argument("--manifest-file", type=Path, default=DEFAULT_MANIFEST_FILE)
    args = parser.parse_args()

    batch_root = args.batch_root.resolve()
    output_file = args.output_file.resolve()
    manifest_file = args.manifest_file.resolve()

    batch_dirs = _discover_batch_dirs(batch_root)
    if not batch_dirs:
        raise RuntimeError(f"No batch directories with predictions_10q.json found in {batch_root}")

    merged: List[Dict[str, Any]] = []
    manifest_batches: List[Dict[str, Any]] = []
    for batch_dir in batch_dirs:
        rows = _load_predictions(batch_dir / "predictions_10q.json")
        manifest_batches.append({"batch_name": batch_dir.name, "questions": len(rows)})
        for row in rows:
            merged_row = dict(row)
            merged_row["batch_name"] = batch_dir.name
            merged_row["batch_question_id"] = int(row.get("id", -1))
            merged_row["global_question_id"] = len(merged)
            merged.append(merged_row)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest = {
        "batch_root": str(batch_root),
        "output_file": str(output_file),
        "questions_total": len(merged),
        "batches": manifest_batches,
    }
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
