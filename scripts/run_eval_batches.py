from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "otazky-najpravo-doplnene.json"
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "data" / "eval_batches_10q"


def _load_items(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict) and "data" in data:
        data = data["data"]
    if not isinstance(data, list):
        raise RuntimeError("Input JSON must be a list of objects")
    return [item for item in data if isinstance(item, dict)]


def _has_provisions(item: Dict[str, Any]) -> bool:
    provisions = item.get("provisions")
    return isinstance(provisions, list) and len(provisions) > 0


def _normalize_item(item: Dict[str, Any]) -> Dict[str, str]:
    return {
        "question": str(item.get("question") or "").strip(),
        "expected": str(item.get("expected") or "").strip(),
        "type": str(item.get("type") or "").strip(),
    }


def _chunk(items: List[Dict[str, str]], size: int) -> List[List[Dict[str, str]]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def _prepare_batches(input_path: Path, batch_size: int) -> List[List[Dict[str, str]]]:
    items = _load_items(input_path)
    selected = [_normalize_item(item) for item in items if _has_provisions(item)]
    selected = [item for item in selected if item["question"] and item["expected"]]
    if not selected:
        raise RuntimeError("No questions with non-empty provisions were found")
    return _chunk(selected, batch_size)


def _clean_output_root(output_root: Path) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    for path in output_root.iterdir():
        if path.is_file() and (path.name.startswith("batch_") or path.name == "manifest.json"):
            path.unlink()


def _write_batches(batches: List[List[Dict[str, str]]], output_root: Path, input_path: Path, batch_size: int) -> None:
    _clean_output_root(output_root)

    for index, batch_items in enumerate(batches, start=1):
        batch_path = output_root / f"batch_{index:02d}.json"
        batch_path.write_text(json.dumps(batch_items, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest = {
        "input": str(input_path),
        "output_root": str(output_root),
        "batch_size": batch_size,
        "questions_total": sum(len(batch) for batch in batches),
        "batches_total": len(batches),
        "files": [f"batch_{index:02d}.json" for index in range(1, len(batches) + 1)],
    }
    (output_root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare eval batch JSON files from the original Najpravo dataset.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--batch-size", type=int, default=3)
    args = parser.parse_args()

    if args.batch_size <= 0:
        raise RuntimeError("batch-size must be > 0")

    input_path = args.input if args.input.is_absolute() else (PROJECT_ROOT / args.input).resolve()
    output_root = args.output_root if args.output_root.is_absolute() else (PROJECT_ROOT / args.output_root).resolve()

    batches = _prepare_batches(input_path, args.batch_size)
    _write_batches(batches, output_root, input_path, args.batch_size)

    print(f"Prepared {len(batches)} batch files in {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

