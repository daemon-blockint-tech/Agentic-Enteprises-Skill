# Safety benchmarks and datasets

## Table of contents

1. [Benchmark types](#benchmark-types)
2. [Dataset curation](#dataset-curation)
3. [Labeling](#labeling)
4. [Versioning](#versioning)

## Benchmark types

| Type | Purpose |
|---|---|
| Golden set | Stable regression; small, high-quality |
| Broad eval | Coverage across categories |
| Adversarial slice | Jailbreaks, encodings, multi-turn from `ai-redteam` |
| Long-tail / edge | Rare harms, multilingual |
| Benign hard negatives | Reduce false positives |

Keep **golden set frozen** between model iterations; refresh on schedule with governance review.

## Dataset curation

Sources (document provenance and license):

- Internal production samples (redacted, sampled, consent)
- Synthetic generation with human review
- Public safety datasets (check license and bias)
- Red-team harvests (separate train/holdout splits)

**De-duplication** and near-duplicate detection before train/test split.

## Labeling

- **Guideline doc** — definitions, examples, borderline cases
- Double-label subset; compute inter-annotator agreement (Cohen's κ)
- Escalation queue for disagreements
- Avoid single annotator on severity-critical labels

Track demographic and language **representation** — report slice gaps.

## Versioning

Dataset card fields:

- `dataset_id`, version, date
- Size per category and language
- Label schema hash
- Known limitations and toxic content warnings for handlers
- Train/val/test split policy

Never bump version without changelog — downstream benchmarks depend on it.
