# Logging and retention minimization

## Table of contents

1. [Data minimization principles](#data-minimization-principles)
2. [Safety pipeline fields](#safety-pipeline-fields)
3. [Retention tiers](#retention-tiers)
4. [Research observability](#research-observability)

## Data minimization principles

- Log **decision codes** and scores, not raw user text, when policy allows
- Hash or tokenize stable identifiers for correlation
- Separate **security incident** retention from product analytics
- Default TTL; no infinite raw prompt stores for safety tuning

Engineering draft ≠ legal retention schedule — align with `compliance-engineer` and counsel.

## Safety pipeline fields

| Field | Typical need |
|---|---|
| `trace_id`, timestamp | Yes |
| Category scores, block reason | Yes |
| Full prompt/response | Only if required; prefer redacted copy |
| Embeddings | High risk; justify |
| Reviewer notes | Encrypt; short TTL |

Review each new log field in **privacy review checklist** before prod.

## Retention tiers

| Tier | Content | TTL example |
|---|---|---|
| Hot ops | Redacted metadata | Days |
| Incident | Sealed bundle | Case-based |
| Research sample | Approved subset | Project end + delete |
| Aggregates | Metrics only | Months |

Automate deletion jobs; verify with sampling audit.

## Research observability

Researchers need signal without prod dumps:

- Stratified samples via **privacy-preserving export** pipeline
- Differential privacy on aggregate block rates (if used, document epsilon)
- Synthetic replay environments mirroring format but not content

Document what researchers may **not** do (paste prod logs in external tools).
