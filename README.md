---
pretty_name: <Task> (<language>)
license: mit
language:
- <code>
tags:
- buddhism
- benchmark
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/v1/test.jsonl
---

<!-- Made from the template repo BuddhistAI/template-benchmark. Name the repo <task>-<language>-benchmark,
     replace every <task>, <language> and <code>, fill in each section, and delete these comments. -->

# <Task> (<language>) benchmark

**Version:** 0.1.0 · **Maturity:** Example · **Task:** [`<task>`](https://buddhistai.github.io/knowledge-base/tasks/<task>.html) · **Scorer:** `scorer/score.py` 0.1.0

What this benchmark measures, in two or three plain sentences.

## Maturity

1. **Example**: format check only. Never on a leaderboard.
2. **Draft**: real items, one author.
3. **Reviewed**: answers checked by a second reader of the language and tradition.
4. **Stable**: held-out set, used in practice.

## Data

- `data/v1/test.jsonl`: one item per line: `id`, `input`, `target`, `metadata` (use `metadata.subset` to split scores).
- Number of items, and how they were chosen.
- Source of the texts, with their license.
- Who made the answers, and who reviewed them.

## Worked example

One real item and the expected output, explained.

## Score it

```bash
python3 scorer/score.py --language <code> --data data/v1/test.jsonl --predictions predictions.jsonl > scores.json
```

`predictions.jsonl` has one line per item: `{"id": ..., "output": ...}`. Submit results as described in [buddhist-benchmarks SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Versions

Semver: new items = minor, fixed answers = patch, scorer or format change = major (new `data/v<major>/` folder). Every change goes in [CHANGELOG.md](CHANGELOG.md).

## License and credit

MIT for this repo. The texts keep their own license (above). Authors and reviewers: list them here.
