# Research to production handoff

## Table of contents

1. [Promotion criteria](#promotion-criteria)
2. [Deliverables package](#deliverables-package)
3. [Shadow and canary](#shadow-and-canary)
4. [Post-launch monitoring](#post-launch-monitoring)

## Promotion criteria

Minimum bar (tune with `ai-risk-governance` and `ai-lead-ops`):

| Gate | Example |
|---|---|
| Golden set | No critical FN regression; recall lift ≥ X% |
| Benign set | FP rate ≤ Y% or ≤ production |
| Adversarial holdout | Pass mandatory cases from `ai-redteam` |
| Latency | p99 ≤ budget on reference hardware |
| Calibration | Threshold table signed |
| Docs | Model card, dataset card, rollback plan |

No promotion on val-set overfit alone.

## Deliverables package

Hand to `ml-infrastructure-engineer-safeguards`:

- Model artifact URI and format (ONNX, Torch, API-only)
- Config: thresholds, category mapping, model ID
- Container/resource requirements
- Eval report JSON and summary memo
- Known limitations and **do-not-deploy** contexts

## Shadow and canary

Research supports but does not operate prod:

1. **Shadow mode** — log scores, no user impact; compare distributions
2. **Canary** — infra owns traffic %; research monitors slice metrics
3. **Rollback trigger** — pre-agreed block-rate and error bounds

Attend launch war room; on-call for model behavior questions first 48h.

## Post-launch monitoring

Define research-owned **weekly checks** first month:

- Slice metrics vs shadow baseline
- New FN/FP samples from production sampling
- Drift signals — score distribution shift
- Retrain trigger when attack surface shifts

Feed findings into next benchmark version and red-team backlog.
