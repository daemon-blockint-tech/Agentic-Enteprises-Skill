# Latency, throughput, and SLOs

## Table of contents

1. [Metric selection](#metric-selection)
2. [SLO structure](#slo-structure)
3. [Latency budgets](#latency-budgets)
4. [Error budget](#error-budget)
5. [Alerting](#alerting)

## Metric selection

| Metric | Use |
|---|---|
| p50 | Typical experience |
| p95 / p99 | Tail; user frustration, SLO |
| Max | Rarely SLO; good for debugging |
| Throughput (RPS) | Capacity planning |
| Apdex / satisfaction | Product-aligned threshold |

Prefer **histograms** over averages. Align window with traffic (1m, 5m rollups).

## SLO structure

Example API SLO:

- **Availability:** 99.9% successful (non-5xx) over 30d
- **Latency:** 99% of requests < 300ms at gateway
- **Freshness** (if applicable): 95% of reads < 60s stale

Document:

- **SLI** — what is measured (synthetic vs real user)
- **Scope** — which routes, regions, tenants
- **Exclusions** — maintenance, client errors (4xx policy)

Coordinate with `devops` for implementation in observability backend.

## Latency budgets

Decompose end-to-end budget across hops:

```
client → CDN → gateway → service A → service B → DB
  50ms     20ms    30ms      80ms       60ms    40ms  (example)
```

Rules:

- Sum of sub-budgets ≤ user-facing target with margin
- **Parallel calls** use max(sub-budgets), not sum
- Reserve **slack** for retries and jitter

Publish budget table in RFC or runbook; flag violations in traces.

## Error budget

```
error_budget = (1 - SLO_target) × eligible_requests
```

When budget burns:

1. Freeze risky releases
2. Prioritize reliability over features
3. Post-incident review if exhaustion from single cause

Performance work that **improves tail** often restores budget faster than mean fixes.

## Alerting

- Page on **SLO burn rate** (multi-window), not raw CPU
- Separate **symptom** (latency) from **cause** (DB connections)
- Load test failures should block release if SLO regression > threshold

Avoid alert fatigue — pair with `devops` and `incident-management-engineer` process.
