"""Check the benchmark: every JSONL row has id, input, target, metadata; ids are unique; example items stay in example/."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
for f in sorted(ROOT.glob("data/v*/*.jsonl")) + sorted(ROOT.glob("example/*.jsonl")):
    seen = set()
    for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        where = f"{f.relative_to(ROOT)}:{n}"
        try:
            row = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: not valid JSON ({e})")
            continue
        missing = [k for k in ("id", "input", "target", "metadata") if k not in row]
        if missing:
            errors.append(f"{where}: missing {', '.join(missing)}")
        if row.get("id") in seen:
            errors.append(f"{where}: duplicate id {row.get('id')!r}")
        seen.add(row.get("id"))
        is_example = isinstance(row.get("metadata"), dict) and row["metadata"].get("example") is True
        if f.parent.name == "example" and not is_example:
            errors.append(f"{where}: items in example/ need metadata.example: true")
        if f.parent.name != "example" and is_example:
            errors.append(f"{where}: example items belong in example/, not in the test data")
if not (ROOT / "CHANGELOG.md").exists():
    errors.append("CHANGELOG.md is missing")
print("\n".join(errors) or "OK")
sys.exit(1 if errors else 0)
