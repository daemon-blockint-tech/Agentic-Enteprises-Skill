# Month-end reconciliation

## Table of contents

1. [Close calendar](#close-calendar)
2. [Standard reconciliations](#standard-reconciliations)
3. [Accruals](#accruals)
4. [Flux analysis](#flux-analysis)

## Close calendar

Typical compute accounting tasks (align to company close day):

| Day | Task |
|---|---|
| T+1 | Pull final cloud invoice / CUR close |
| T+2 | Run allocation; post cloud JEs |
| T+3 | Depreciation run; prepaid amortization |
| T+4 | Reconcile subledgers to GL |
| T+5 | Flux and variance notes for controller |

## Standard reconciliations

| Reconciliation | Tie |
|---|---|
| Cloud AP / invoice | Vendor statement ↔ GL AP ↔ cash |
| Prepaid cloud | Schedule ↔ console commitment balance |
| Hosting / COGS expense | CUR subtotal ↔ GL (by account) |
| Fixed assets | Register ↔ GL asset and accum depr |
| Accrued colo / hardware | Estimate ↔ subsequent invoice |
| Intercompany chargeback | Subledger ↔ elimination (if applicable) |

Each reconciliation: preparer, reviewer, **threshold** for investigation.

## Accruals

Accrue when **goods/services received** but invoice not yet booked:

- Cloud usage after last invoice cut (usage accrual from CUR)
- Colo MRC for current month
- Hardware received not invoiced (GRNI)
- Estimated vendor credits not yet applied

Reverse **automatically** next period when invoice hits.

## Flux analysis

Explain material MoM changes:

| Driver | Example narrative |
|---|---|
| Volume | GPU training hours +18% |
| Rate | On-demand mix vs reserved |
| New product launch | New account/subscription |
| One-time | Migration project capitalized |
| FX | USD invoice for non-US entity |
| Classification | Reclass from R&D to COGS |

Link flux to **business metrics** (nodes deployed, customers) when possible.
