# Production guardrails and monitoring

## Table of contents

1. [Input guardrails](#input-guardrails)
2. [Output guardrails](#output-guardrails)
3. [Monitoring signals](#monitoring-signals)
4. [Incident and rollback](#incident-and-rollback)

## Input guardrails

| Control | Purpose |
|---|---|
| Schema validation | Reject malformed feature vectors or prompt structures |
| Norm clipping | Bound L∞/L2-style magnitudes on numeric inputs |
| Token/byte limits | Mitigate sponge and extraction query volume |
| Denylist / homoglyph normalize | Reduce obfuscation evasion |
| File type and dimension caps | Multimodal abuse containment |
| Authentication and per-tenant quotas | Slow model stealing |

Implement at **edge/gateway** (`ml-infrastructure-engineer-safeguards`) before GPU batching.

## Output guardrails

| Control | Purpose |
|---|---|
| Confidence thresholds | Abstain or escalate low-margin predictions |
| Consistency checks | Ensemble disagreement flags |
| Stability probes | Light perturbation — large flip → quarantine |
| Watermarking (if used) | Trace extraction misuse |
| Logging minimization | Avoid storing raw adversarial payloads in prod logs |

Separate **robustness monitors** from **harm classifiers** (`ml-research-engineer-safeguards`).

## Monitoring signals

Track continuously (dashboards + alerts):

| Signal | Interpretation |
|---|---|
| ASR on **canary attack set** (online shadow) | Robustness regression post-deploy |
| Input norm distribution shift | Possible evasion campaign |
| Query rate per key / entropy of inputs | Extraction or probing |
| Detector trigger rate | Tune FP vs FN; slice by tenant |
| Clean accuracy drift | Poisoning or data pipeline issue |
| Defense bypass count | Sanitizer/detector failures |

Set **rollback triggers** when canary ASR exceeds champion + δ for N hours.

## Incident and rollback

1. **Triage** — evasion spike vs poison vs extraction vs infra
2. **Contain** — tighten rate limits, enable stricter sanitization, route to fallback model
3. **Preserve** — sample payloads (redacted), model version, config for offline replay
4. **Remediate** — hotfix guardrails vs emergency retrain (coordinate `ai-engineer`, `ai-lead-ops`)
5. **Post-incident** — update golden attack set; rerun full robustness eval before re-promote

Link governance notifications to `ai-risk-governance` for material robustness failures.
