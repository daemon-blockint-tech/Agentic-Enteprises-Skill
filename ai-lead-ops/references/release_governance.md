# Release governance

## Table of contents

1. [Risk tiers](#risk-tiers)
2. [Canary metrics](#canary-metrics)

## Risk tiers

| Tier | Gates |
|---|---|
| Low | Eval smoke + automated safety |
| Medium | + human review + 24h canary |
| High | + red-team + exec sign-off |

## Canary metrics

Watch for 2h minimum:

- Error rate vs baseline
- p95 latency
- Cost per request
- Thumbs-down / report rate
- Safety classifier triggers

Auto-rollback if any breach SLO burn threshold.
