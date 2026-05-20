# SLO targeting and error budgets

## Table of contents

1. [Setting targets](#setting-targets)
2. [Measurement windows](#measurement-windows)
3. [Error budget math](#error-budget-math)
4. [Budget consumption tracking](#budget-consumption-tracking)
5. [Policy actions](#policy-actions)
6. [Multi-SLO budgets](#multi-slo-budgets)
7. [Capacity implications](#capacity-implications)

## Setting targets

Process:

1. Plot each SLI for **30–90 days** (exclude known anomalies)
2. Identify **sustained good** performance (p50 of monthly aggregates)
3. Set target **slightly below** sustained good to leave headroom (or match product minimum)
4. Compare to **tier defaults** and **customer SLA** (must be stricter than SLA metric)
5. Record **rationale** in review pack when deviating from tier default

| Availability target | Approx. allowed bad per 30d (request-based) |
|---|---|
| 99% | ~7.2 hours equivalent |
| 99.9% | ~43.8 minutes |
| 99.95% | ~21.9 minutes |
| 99.99% | ~4.4 minutes |

Latency targets: derive from percentile history; avoid targets no month has ever met.

**Target change rules:**

- Increase strictness: requires capacity or reliability investment plan
- Relax target: requires product sign-off + customer comms if SLA-bound
- Never change target retroactively without versioning spec

## Measurement windows

| Window | Use case | Pros | Cons |
|---|---|---|---|
| Rolling 30d | Product SLOs, executive reporting | Smooth, familiar | Slow to reflect fixes |
| Rolling 7d | Tactical teams | Faster feedback | Noisier |
| Calendar month | SLA billing alignment | Matches contracts | Cliff effects at month boundary |
| Rolling 90d | Seasonal services | Stable | Slow policy response |

**Recommendation:** internal SLO on **rolling 30d**; SLA may use calendar month—document conversion if dashboards differ.

## Error budget math

### Proportion-based (availability, latency good %)

```
error_budget = 1 - objective          # e.g., 0.001 for 99.9%
budget_consumed = 1 - current_sli   # over same window
budget_remaining = error_budget - budget_consumed
```

### Time-based

```
allowed_downtime = (1 - objective) * window_minutes
consumed_downtime = sum(incident_bad_minutes)
```

### Budget consumed %

```
burn_pct = budget_consumed / error_budget * 100
```

Report **burn_pct** weekly in SLO review; tie to deploy count and incident count for context.

## Budget consumption tracking

Dashboard minimum:

| Panel | Purpose |
|---|---|
| SLI vs objective | Current position |
| Budget remaining % | Policy decisions |
| Burn rate (1h, 6h, 30d) | Alert alignment |
| Top contributing routes/errors | Actionability |
| Incidents overlay | Narrative for review |

Attribute consumption to:

- **Deploy correlation** — release introduced regression?
- **Dependency** — upstream SLO burn?
- **Traffic shape** — new cohort or abuse?

Hand off deep incident analysis to `site-reliability-engineer`; this skill tracks **accounting** of budget.

## Policy actions

Agree **in advance** with product and engineering leadership:

| Budget consumed (30d) | Typical action |
|---|---|
| < 50% | Normal feature velocity |
| 50–80% | Freeze risky launches; prioritize reliability backlog |
| 80–100% | Release freeze except fixes; exec visibility |
| Exhausted | Mandatory reliability sprint; no new features until recovery |

**Recovery:** define what restores budget (rolling window roll-off vs explicit reset)—usually time-based roll-off only.

Link to `ci-cd-engineer` / `deployment-strategist` when pipelines enforce gates on burn thresholds.

## Multi-SLO budgets

When a service has availability **and** latency SLOs:

| Strategy | When |
|---|---|
| **Independent budgets** | Either can block release per policy |
| **Weighted composite** | Single score for exec summary only—not for paging |
| **Primary + secondary** | Page on primary; ticket on secondary |

Do not multiply independent probabilities without explaining to stakeholders.

## Capacity implications

Latency SLOs imply **headroom**:

| Signal | Implication |
|---|---|
| SLI near objective with flat traffic | No headroom; target too aggressive or under-provisioned |
| p99 rising while p50 flat | Tail issue—thread pools, GC, slow deps |
| Seasonal peak within 2× traffic | Load test at `performance-engineer`; scale plan |

Document **minimum capacity** to meet SLO in spec appendix when T0/T1:

- RPS at objective latency
- Dependency timeouts aligned with latency threshold
- Autoscaling bounds

Escalate capacity funding when sustained burn >50% without incidents (chronic tail latency).
