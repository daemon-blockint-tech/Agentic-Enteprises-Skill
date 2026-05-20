# Privacy research framing

## Table of contents

1. [Threat model](#threat-model)
2. [Research questions](#research-questions)
3. [Metrics](#metrics)
4. [Baselines](#baselines)

## Threat model

| Asset | Risk |
|---|---|
| User prompts/responses | Exposure via logs, training, support tools |
| Safety reviewer queues | Over-retention of harmful + PII content |
| Classifier training sets | Memorization, re-identification from outputs |
| Embeddings / caches | Nearest-neighbor leaks across tenants |
| Eval artifacts | Researchers copying prod samples to laptops |

Adversaries: insider, compromised log store, cross-tenant bug, model inversion (research threat).

Coordinate **legal/processing basis** with `ai-risk-governance` before using production data.

## Research questions

Examples:

- Does redaction **before** logging reduce FN on downstream harm detection?
- What **false negative rate** on phone/email across top 10 locales at FP budget X?
- After fine-tune on safety data, does the model **regurgitate** rare strings from training?
- Can aggregated safety metrics be published without **re-identifying** users?

Pre-register primary metric and holdout set.

## Metrics

| Metric | Use |
|---|---|
| PII precision/recall | Per entity type (email, phone, name, ID) |
| Redaction completeness | % sensitive spans removed |
| Utility preservation | Task success after redaction (downstream harm F1) |
| Re-identification risk | k-anonymity-style or attacker simulation (document method) |
| Log field coverage | % requests with unnecessary raw text stored |

## Baselines

Compare:

1. Production detector/redaction stack
2. Regex/heuristic baseline
3. Vendor API (document data handling terms)
4. Previous research champion

Report **privacy–utility Pareto** — not accuracy alone.
