"""Scorer for the <task> (<language>) benchmark.

python3 scorer/score.py --data data/v1/test.jsonl --predictions predictions.jsonl [--language <code>] > scores.json

This template scores exact match after trimming whitespace. Replace `score_item` with the task's real metric,
put language-specific normalization in `normalize` (keyed by language code), and bump SCORER_VERSION.
"""
import argparse, json, sys

SCORER_VERSION = "0.1.0"


def normalize(text, language):
    return " ".join(str(text).split())


def score_item(output, target, language):
    return 1.0 if normalize(output, language) == normalize(target, language) else 0.0


def load(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--predictions", required=True)
    ap.add_argument("--language", default="")
    a = ap.parse_args()
    items = load(a.data)
    preds = {p["id"]: p.get("output", "") for p in load(a.predictions)}
    by_subset = {}
    for it in items:
        s = score_item(preds.get(it["id"], ""), it["target"], a.language)
        sub = it.get("metadata", {}).get("subset", "all")
        by_subset.setdefault("all", []).append(s)
        if sub != "all":
            by_subset.setdefault(sub, []).append(s)
    scores = {k: {"accuracy": sum(v) / len(v)} for k, v in by_subset.items()}
    json.dump({"scorer_version": SCORER_VERSION, "items": len(items), "missing": sum(1 for it in items if it["id"] not in preds), "scores": scores}, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
