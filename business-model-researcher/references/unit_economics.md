# Unit economics

## Table of contents

1. [Core metrics](#core-metrics)
2. [SaaS template](#saas-template)
3. [Marketplace template](#marketplace-template)
4. [Sensitivity](#sensitivity)
5. [Red flags](#red-flags)

## Core metrics

| Metric | Formula | Notes |
|---|---|---|
| **ARPU / ARPA** | Revenue / paying accounts / period | Specify gross vs net |
| **Gross margin** | (Revenue - COGS) / Revenue | Include support at scale if material |
| **CAC** | Sales+marketing spend / new customers | Blended vs channel |
| **Payback** | CAC / (ARPU × gross margin) | Months to recover CAC |
| **LTV** | ARPU × gross margin / churn (simple) | Or cohort-based |
| **LTV:CAC** | LTV / CAC | Rule-of-thumb >3 for SaaS; context matters |

State whether metrics are **monthly** or **annual**; never mix.

## SaaS template

```
MRR = customers × ARPU
Gross profit = MRR × gross_margin%
CAC_payback_months = CAC / (ARPU × gross_margin)
LTV = ARPU × gross_margin / monthly_churn
```

For annual contracts, use **logo churn** and **NDR** when public data exists.

## Marketplace template

```
GMV = transactions × AOV
Net revenue = GMV × take_rate
Contribution = net_revenue - variable_cost_per_order
```

Unit may be **order** or **active buyer**—pick one and stay consistent.

## Sensitivity

Vary one lever at a time (base / low / high):

| Lever | Low | Base | High |
|---|---|---|---|
| Monthly churn | 1% | 2% | 4% |
| CAC | $800 | $1,200 | $2,000 |
| ARPU | $90 | $120 | $150 |

Show impact on LTV:CAC and payback—not only LTV alone.

## Red flags

- LTV computed with revenue instead of gross profit
- Ignoring expansion revenue (NDR >100%) in enterprise
- CAC excludes salaries or credits paid to customers
- Payback >24 months without enterprise contract justification
- Churn assumed without segment split (SMB vs enterprise)

For audited financial statements and ASC 606, use `senior-revenue-accountant`.
