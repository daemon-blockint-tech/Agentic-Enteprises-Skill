# Safety observability

## Table of contents

1. [Metrics](#metrics)
2. [Logging](#logging)
3. [Sampling and review](#sampling-and-review)
4. [Alerts](#alerts)

## Metrics

| Metric | Use |
|---|---|
| `safety_blocks_total` by stage, category, tenant | Policy drift, attacks |
| `safety_latency_ms` by stage | Regression detection |
| `safety_errors_total` | Reliability |
| `model_calls_avoided` | Pre-filter effectiveness |
| `false_positive_reports` | Tuning (human labeled) |
| `override_count` | Human review outcomes |

Dashboards: exec summary + engineer drill-down by model/policy version.

## Logging

- Log **decision code**, scores (bucketed), stage, latency — not full harmful text by default
- Hash or encrypt sensitive payloads in debug streams
- Retention aligned with privacy policy; separate **security incident** retention
- Correlate with `trace_id` across gateway → classifiers → model

Red-team repro artifacts → restricted access store, not general logs.

## Sampling and review

- Random sample of **allowed** traffic for quality audit
- 100% capture of **blocked** metadata (not necessarily content)
- Feed samples to `ai-redteam` and policy owners on schedule
- Feedback loop: label → retrain threshold or model version

## Alerts

Page when:

- Safety error rate > SLO
- Block rate spike/drop vs baseline (attack or broken classifier)
- Safety p99 regression breaking user SLO
- Fail-open path activated (if ever allowed)

Avoid alerting on raw block rate alone without baseline — seasonal traffic shifts.

Coordinate paging with `devops` and `ai-lead-ops` runbooks.
