# SLI, SLO, and error budgets

## Table of contents

1. [Choosing SLIs](#choosing-slis)
2. [Setting SLOs](#setting-slos)
3. [Error budget math](#error-budget-math)
4. [Policy actions](#policy-actions)
5. [Multi-window burn alerts](#multi-window-burn-alerts)

## Choosing SLIs

Good SLIs are **measurable**, **user-aligned**, and **actionable**.

| Journey | Example SLI |
|---|---|
| API availability | % successful requests (exclude client 4xx if policy says so) |
| API latency | % requests < 300ms at p99 |
| Async pipeline | % jobs completed within SLA window |
| Data freshness | % partitions landed within N hours |

Avoid infra-only SLIs (CPU < 80%) as primary customer SLO unless no better proxy exists.

Document **exclusions**: maintenance windows, vendor outages, abuse traffic (policy decision).

## Setting SLOs

Start from historical performance + business need:

1. Plot SLI for 30–90 days
2. Set target slightly below sustained good period (leave headroom)
3. Define **measurement window** (rolling 30d common for product SLOs)
4. Assign **owners** (service team + SRE partner)

Example: **99.9%** availability → ~43.8 min downtime budget per 30 days.

## Error budget math

```
error_budget = 1 - SLO_target   (as proportion of events or time)
budget_remaining = budget - consumed_in_window
```

Track **budget consumed %** weekly. Report alongside deploy count and incident count.

## Policy actions

When budget burn exceeds thresholds (example—tune to org):

| Burn (30d window) | Action |
|---|---|
| <50% | Normal feature velocity |
| 50–80% | Freeze risky launches; reliability sprint items |
| >80% | Release freeze except fixes; exec visibility |
| Exhausted | Incident review; mandatory reliability work before new features |

Product and eng leads agree policy in advance — not invented during outage.

## Multi-window burn alerts

Google SRE pattern — alert on **fast burn** (page) and **slow burn** (ticket):

| Window | Burn rate (example for 99.9% SLO) | Severity |
|---|---|---|
| 1h | 14.4× budget | Page |
| 6h | 6× budget | Page |
| 3d | 1× budget | Ticket |
| 30d | 1× budget | Review in ops meeting |

Tune multipliers to alert noise; pair every page with runbook link.
