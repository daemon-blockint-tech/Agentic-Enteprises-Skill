# Capex forecast and executive reporting

## Table of contents

1. [Forecast structure](#forecast-structure)
2. [Plan vs actual bridge](#plan-vs-actual-bridge)
3. [Run-rate and depreciation](#run-rate-and-depreciation)
4. [Board narrative](#board-narrative)

## Forecast structure

Align categories with engineering and portfolio:

| Layer | Owner input | Accounting view |
|---|---|---|
| Strategic | `data-center-portfolio-planning-execution-lead` | Multi-year capex envelope |
| Program | Capacity delivery | MW / rack waves by quarter |
| Tactical | Platform / DC ops | SKU counts, cloud commits |
| OpEx overlap | FinOps | RI amortization vs new prepay |

Forecast in **cash**, **commitment**, and **P&L** views:

- Cash — payments
- Capex — WIP additions and direct asset buys
- Depreciation — forward run-rate from approved builds

## Plan vs actual bridge

Monthly or quarterly bridge:

```
Budget capex
± Scope changes (new racks, deferred hall)
± Price (SKU cost, FX)
± Timing (slip to next quarter)
± Reclass (OpEx vs capex correction)
= Actual capex
```

Explain **timing slips** separately from **true savings** (deferral vs efficiency).

Tie to `data-center-compute-supply-efficiency` **capex avoidance** metrics when engineering claims consolidation savings.

## Run-rate and depreciation

After major in-service events, update:

- Quarterly **depreciation expense** forecast
- **Prepaid cloud** amortization schedule
- **Free cash flow** impact narrative for FP&A

Show **capex-to-depreciation conversion** for board: when spend drops, depreciation may still rise.

## Board narrative

Keep slides factual:

- Spend vs approved budget and prior guidance
- Major projects: status, in-service date, WIP balance
- Efficiency: utilization or deferred capex (with engineering source)
- Risks: supply chain, slip, impairment watchlist
- Audit / control headline if material

Avoid engineering jargon without accounting translation (MW → $ and asset class).
