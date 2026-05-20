# Capex and OpEx governance

## Table of contents

1. [Budget components](#budget-components)
2. [Cadence](#cadence)
3. [Trade-off frames](#trade-off-frames)
4. [Metrics](#metrics)
5. [Finance partners](#finance-partners)

## Budget components

| Bucket | Typical owners | VP focus |
|--------|----------------|----------|
| **Cloud run-rate** | FinOps + platform | Growth vs efficiency target |
| **Commits / EA** | Economist + procurement | Coverage, flexibility, true-up risk |
| **DC capex** | Portfolio + finance | Envelope by region/program |
| **Hardware / GPU** | Supply + DC efficiency | Utilization before new build |
| **People** | VP + HR | Ratio of platform to embedded |
| **SaaS / observability** | Platform | Consolidation and enterprise deals |

## Cadence

| Cycle | Activity |
|-------|----------|
| **Annual planning** | Top-down envelope, bottom-up initiatives, base/downside scenarios |
| **Quarterly forecast** | Reforecast cloud and capex; explain variance to CFO |
| **Monthly** | FinOps review, incident cost of downtime, commit utilization |
| **Ad hoc** | Major launch, M&A, outage-driven investment |

## Trade-off frames

Present leadership choices explicitly:

- **Reliability vs cost** — higher SLO tier vs smaller footprint
- **Speed vs standardization** — exception process cost
- **Build vs buy vs cloud** — delegate modeling to `cloud-economist`
- **Central vs federated** — tooling cost vs policy risk
- **Capex now vs opex flexibility** — partner with `director-infrastructure-capex-accounting` on capitalization

## Metrics

Portfolio-level (not service-level):

- Cloud spend vs plan; commit utilization %
- DC **MW/rack** deployed vs forecast
- **P0/P1** incident trend and MTTR (by tier)
- **Toil / automation** investment as % of platform capacity
- **Security** critical vuln aging on infra estate

## Finance partners

| Topic | Skill |
|---|---|
| Monthly actuals, CUR, allocation | `finops-analyst` |
| Capex policy, WIP/CIP, audit | `director-infrastructure-capex-accounting` |
| GL, amortization, close | `compute-accounting-manager` |
| EA/commit economics | `cloud-economist` |

Do not invent figures — cite FinOps, FP&A, and DC portfolio sources; use placeholders if data is missing.
