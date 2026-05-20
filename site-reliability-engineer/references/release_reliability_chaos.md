# Release reliability and chaos

## Table of contents

1. [Release gates](#release-gates)
2. [Canary and rollback](#canary-and-rollback)
3. [Failure mode analysis](#failure-mode-analysis)
4. [Chaos and game days](#chaos-and-game-days)

## Release gates

Align with `deployment-strategist` for ceremony; SRE owns **SLO gates**:

| Gate | Criteria |
|---|---|
| Pre-deploy | Error budget not in freeze zone; PRR complete |
| Canary | SLI within margin vs baseline (e.g., 5 min window) |
| Full rollout | Canary SLI stable; no burn-rate page |
| Post-deploy | 24h watch window; anomaly detection armed |

Block promotion when fast burn alert fires during canary.

## Canary and rollback

- Canary **traffic %** and duration defined per risk tier
- Compare **golden signals** canary vs control (errors, latency, saturation)
- **Rollback** = one command or revert PR; test quarterly
- Feature flags for **kill switch** without full redeploy when possible

Coordinate artifact rollback with `devops` pipeline owners.

## Failure mode analysis

Lightweight FMEA per critical service:

| Component | Failure | Effect | Detection | Mitigation |
|---|---|---|---|---|
| Cache | Down | DB load spike | Error rate, latency | TTL stale-while-revalidate |
| Region | Unavailable | Partial outage | Health checks | Route traffic; DR runbook |

Update after each SEV incident.

## Chaos and game days

Prerequisites: observability, runbooks, error budget culture, IM process.

| Type | Scope | Safety |
|---|---|---|
| Tabletop | Process only | Low risk |
| Staging chaos | Kill dependency | No customer impact |
| Prod game day | Controlled fault injection | Small blast radius, abort criteria |

Hypothesis format: *If X fails, we detect in T minutes and mitigate via Y.*

Never run prod chaos during budget freeze or major launch without exec approval.

Record results; convert gaps to reliability backlog items.
