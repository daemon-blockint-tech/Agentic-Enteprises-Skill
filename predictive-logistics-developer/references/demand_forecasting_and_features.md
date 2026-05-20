# Demand forecasting and features

## Forecast design checklist

1. **Define granularity** — SKU, location, lane, customer segment; minimum volume for stable series
2. **Set horizon and cadence** — daily vs weekly; align to replenishment and transportation planning cycles
3. **Choose target** — units, cases, weight, cube; handle pack-size changes explicitly
4. **Establish hierarchy** — reconcile SKU → family → location → region (bottom-up, top-down, or MinT)
5. **Document forecast origin** — timestamp and information cutoff to prevent leakage

## Feature families

| Family | Examples | Notes |
|---|---|---|
| Calendar | DOW, month, holidays, fiscal periods | Use location time zones |
| Logistics | Lead time to node, mode, carrier tier | Lag to forecast origin only |
| Promotion | Discount depth, display, duration, halo | Separate baseline vs lift models when needed |
| Inventory state | Stockouts, backorders (careful—leakage) | Use only known-at-origin signals |
| External | Weather, events, commodity indices | Validate causal plausibility |
| Network | Upstream node fill rate, lane volume | Spatial autocorrelation features |
| New items | Analogs, attributes, launch curves | Cold-start playbook required |

## Seasonality and promotions

- Fit **multiple seasonalities** when cadence mixes daily noise with weekly retail patterns
- Model **promotional lift** with explicit start/end; avoid training on post-promo returns as demand
- Separate **stockout-censored** periods—zero demand may be unobserved demand
- For **lane demand**, aggregate ship-to patterns and mode mix shifts

## Hierarchy reconciliation

| Method | When to use |
|---|---|
| Bottom-up | Stable SKU-store series with good history |
| Top-down | Sparse stores; allocate family forecast by historical mix |
| Middle-out | Balanced retail networks |
| MinT / optimal combination | Large hierarchies with conflicting signals |

## Model selection (logistics-aware)

| Regime | Starting point | Escalate when |
|---|---|---|
| Stable high-volume | ETS, Prophet-style, light GBM | Residual structure remains |
| Intermittent | Croston, TSB, zero-inflated models | High volume of zeros |
| Rich covariates | Gradient boosting, global models across series | Many related SKUs/lanes |
| Deep global | TFT, N-BEATS class | Large panel, stable pipelines |

Prefer **global models across series** when thousands of SKUs share calendars and promotions.

## Outputs for downstream systems

- Point forecast + **prediction interval** (P50/P90) for safety stock interfaces
- **Forecast version** and `as_of` timestamp for audit
- **Explainability slice** by driver (promo, season, stockout flag) for planner trust

## Anti-patterns

- Training on **shipped quantity** when **ordered demand** is the planning target during stockouts
- Using **future inventory transfers** known only after forecast origin
- Single MAPE target without **volume weighting**—WMAPE by lane/SKU volume
- Ignoring **pack-size or UOM changes** without restating history
