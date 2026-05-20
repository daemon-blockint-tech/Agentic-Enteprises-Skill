# Observability, SLO, and Operational Health

## Golden signals per service

For each tier-0/1 service, verify coverage of:

| Signal | Minimum expectation |
|---|---|
| Latency | p50/p95/p99 by dependency edge |
| Traffic | RPS or queue depth |
| Errors | HTTP/gRPC codes, business error rate |
| Saturation | CPU, memory, pool exhaustion, lag |

Mark **gaps** explicitly (e.g., "no traces on checkout→payment edge").

## SLO coverage assessment

| Question | Pass criteria |
|---|---|
| SLO defined? | Documented SLI + target + window |
| Error budget policy? | Burn alerts and response playbook |
| Tier alignment? | Tier-0 has stricter targets than tier-3 |
| Dependency SLOs? | Upstream contracts referenced or ignored knowingly |
| Customer-facing mapping? | SLO ties to user journey, not pod name only |

Produce a **coverage matrix**: service × {SLI defined, dashboard, alert, runbook, owner}.

## Alert quality heuristics

| Smell | Action |
|---|---|
| >30% pages non-actionable | Tune or delete; route to `site-reliability-engineer` |
| Same alert fires daily | Threshold or architecture fix |
| No alert on tier-0 without SLO | Define SLI or downgrade tier (with approval) |
| Alerts without service label | Fix observability taxonomy |

## Deployment and change health

Proxy metrics when formal DORA data exists:

| Metric | Source ideas |
|---|---|
| Deploy frequency | CI/CD per service |
| Lead time | Commit → prod duration |
| Change failure rate | Failed deploys / rollbacks |
| MTTR | Incident duration by service |

Highlight **version skew**: multiple prod versions, stale sidecars, config drift between regions.

## Operational toil indicators

Qualitative and quantitative themes:

- Manual steps in runbooks (scale, failover, data fix)
- Recurring ticket categories (quota, cert, cache flush)
- "Hero" on-call knowledge not in docs
- Frequent hotfix deploys outside pipeline

Summarize as **toil themes** with estimated engineer-hours/month if data exists.

## Incident correlation

Map last 90 days (or available window):

- Incidents touching multiple services (shared fate)
- Repeat root causes (timeouts, DB locks, contract mismatch)
- Services with no incidents but no SLOs (unknown risk)

## Operational health scorecard (example)

| Service | Tier | SLO | Traces | Deploy/wk | Incidents | Grade |
|---|---|---|---|---|---|---|
| checkout-api | 0 | Y | partial | 12 | 2 | C |
| legacy-pricing | 1 | N | N | 0.5 | 4 | F |

Grades drive narrative; define rubric in appendix for transparency.

## Handoffs

- SLO program design, error budgets → `site-reliability-engineer`
- Load/latency deep dives → `performance-engineer`
- Platform observability standards → `platform-engineer`
