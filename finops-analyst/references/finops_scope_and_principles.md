# FinOps scope and principles

## Table of contents

1. [FinOps phases](#finops-phases)
2. [Role boundary](#role-boundary)
3. [Shared metrics](#shared-metrics)
4. [Anti-patterns](#anti-patterns)

## FinOps phases

| Phase | Activities |
|---|---|
| Inform | Visibility, allocation, showback, anomaly alerts |
| Optimize | Rightsizing, waste, commitments, architecture cost review |
| Operate | Budgets, forecasts, governance cadence, accountability |

Run all three; do not skip **Inform** and jump to commitment purchases.

## Role boundary

| finops-analyst | Partner |
|---|---|
| Usage analytics and optimization recommendations | `compute-accounting-manager` — GL, amortization, audit |
| CUR analysis and dashboards | `cloud-engineer` — implements tags and infra |
| EA/commit strategy at enterprise scale | `enterprise-cloud-architect` |
| Delete idle resources in prod | `cloud-system-administrator` with owner approval |
| Design-time cost architecture | `cloud-architect` |

FinOps does **not** post journal entries or capitalize hardware.

## Shared metrics

Align with finance where possible:

- Same **tag keys** (`cost-center`, `environment`, `service`)
- Same **billing account** hierarchy in reports
- Document **lag** (CUR 24h+, invoice monthly)

Reconciliation meeting: FinOps dashboard vs GL flux (`compute-accounting-manager`).

## Anti-patterns

- Buying 3-year RIs before workload is stable
- Optimizing only at month-end after invoice shock
- Chargeback without tagging discipline (arbitrary splits)
- Savings that harm SLOs without SRE sign-off (`site-reliability-engineer`)
- Blaming finance for untagged sprawl — fix process with engineering leads
