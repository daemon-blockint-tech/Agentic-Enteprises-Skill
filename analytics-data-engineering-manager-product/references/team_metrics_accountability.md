# Team Metrics and Accountability

## Team scorecard (examples)

| Metric | Target | Notes |
|---|---|---|
| **Mart test pass rate** | >99% weekly | dbt / CI |
| **Critical source freshness** | Per SLA | Tier-1 sources |
| **Launch analytics on-time** | >90% | GA checklist complete |
| **Time-to-metric (new feature)** | Trend down | Discover → prod mart |
| **Incident count (P1/P2)** | Trend down | Analytics-owned |
| **Tech debt allocation** | ≥20% capacity | Manager enforces |

## Product analytics SLA tiers

| Tier | Example | Freshness | Response |
|---|---|---|---|
| **1** | Revenue, active users exec | <4h | Page on-call |
| **2** | Squad KPIs | <24h | Next business day |
| **3** | Exploratory | Best effort | Backlog |

Align tiers with `data-manager` org SLAs where they exist.

## Quality escalation

| Signal | Action |
|---|---|
| Test fail in prod | Block deploy; owner fixes <4h if Tier-1 |
| Metric mismatch reported | Triage with `bi-analyst`; root cause in 48h |
| Repeated freshness breach | CAPA: pipeline vs model vs capacity |

## Incident roles

| Role | Responsibility |
|---|---|
| **Incident commander** | Analytics eng lead or on-call |
| **Comms** | Manager → PM + leadership |
| **Fix** | Domain owner engineer |
| **Post-mortem** | Required P1/P2; actions tracked |

## Performance accountability

Managers own **predictable delivery** and **standards**, not single-handedly fixing SQL.

Review quarterly: scorecard trends, debt burned, hiring plan vs roadmap.
