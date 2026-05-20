# Observability for reliability

## Table of contents

1. [Golden signals](#golden-signals)
2. [Dashboard hierarchy](#dashboard-hierarchy)
3. [Alert hygiene](#alert-hygiene)
4. [Tracing and logs](#tracing-and-logs)

## Golden signals

Per service (Google SRE):

| Signal | Question |
|---|---|
| Latency | How slow? (distinguish success vs error latency) |
| Traffic | How much demand? |
| Errors | What rate fails? |
| Saturation | How full (CPU, queue depth, connections)? |

Add **USE** for resources and **RED** for request-driven services in dashboards.

## Dashboard hierarchy

1. **Executive / product** — SLO status, budget remaining, incident count
2. **Service** — SLI charts, deploy markers, dependency health
3. **Debugging** — per-instance, per-region, per-endpoint drill-down

Mark **deployments** and **feature flags** on SLI graphs to correlate regressions.

## Alert hygiene

Rules:

- Page humans only on **SLO burn** or **imminent customer impact**
- Ticket for **degradation** with time to fix before breach
- No pages on **non-actionable** thresholds (disk 70% with autoscale)
- Every page links **runbook** with first three mitigation steps

Review alert-to-incident ratio monthly; silence or fix noisy alerts.

Stack implementation often shared with `devops` — SRE owns **what** to alert on, not only **how** to wire Prometheus/Datadog.

## Tracing and logs

- **Correlation ID** across services for incident timelines
- Structured logs; no PII/secrets in info level
- Trace sampling: higher rate during incidents or canaries
- Log-based metrics only when no better native metric exists (cost and cardinality)

For deep APM tuning of hot paths → `performance-engineer`.
