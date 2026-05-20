# Budgeting and forecasting

## Table of contents

1. [Budgets](#budgets)
2. [Forecast methods](#forecast-methods)
3. [Variance analysis](#variance-analysis)
4. [Anomaly detection](#anomaly-detection)

## Budgets

Per account, BU, or tag value:

- Set **monthly budget** with 80% and 100% alert thresholds
- Separate **prod vs non-prod** budgets
- Include **expected credits** and EA drawdown if applicable
- Review budget vs actual in **monthly FinOps meeting**

Budget is a planning tool; GL forecast may differ (`compute-accounting-manager`).

## Forecast methods

| Method | Use when |
|---|---|
| Run-rate | Stable workloads; last 30d × seasonality |
| Driver-based | Cost ∝ users, API calls, TB stored |
| Bottom-up | New launches with architecture estimate |
| Commitment-adjusted | Subtract on-demand covered by RI/SP |

Present **range** (low/base/high) for leadership; document assumptions.

## Variance analysis

Monthly narrative:

- **Volume** — usage growth (instances, requests, GB)
- **Rate** — price list, new services, cross-region egress
- **One-time** — data transfer spike, misconfiguration, pentest environment left on
- **Commitment** — amortization true-up, unused RI

Compare to **forecast** and prior month; flag >10% movers for investigation.

## Anomaly detection

Enable native anomaly alerts (AWS, GCP, Azure) plus custom rules:

- Daily spend >2σ from 14d baseline per account
- New service first appearance in top 10
- Tag value sudden 3× increase

Triage within 48h: real growth, leak, or attack/abuse (loop security if suspicious).
