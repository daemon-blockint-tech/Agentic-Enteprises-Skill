# Forecasting and Time Series

## Table of contents

1. [When this applies](#when-this-applies)
2. [Problem setup](#problem-setup)
3. [Baselines](#baselines)
4. [Feature patterns](#feature-patterns)
5. [Model choices (tabular focus)](#model-choices-tabular-focus)
6. [Validation for time order](#validation-for-time-order)
7. [Intervals and scenarios](#intervals-and-scenarios)
8. [Demand forecasting pitfalls](#demand-forecasting-pitfalls)
9. [Handoff to stakeholders](#handoff-to-stakeholders)

## When this applies

Use this reference when the target is **future values over time** (demand, volume, revenue, tickets) rather than a one-time entity label. For cross-sectional tabular classification, use `classification_and_propensity.md`.

Markets-style factor research and backtests → `quantitative-researcher`.

## Problem setup

Define explicitly:

| Choice | Example decisions |
|---|---|
| Granularity | Daily vs weekly vs monthly |
| Horizon | h=1 step vs multi-step (1–13 weeks) |
| Geography / SKU scope | Hierarchy for reconciliation |
| Target | Units, revenue, orders; handle returns and cancellations |
| Exogenous inputs | Promotions, price, holidays—**available at forecast origin** |

Align granularity with **planning cadence** (ops buys weekly; finance plans monthly).

## Baselines

Required before ML:

| Baseline | Description |
|---|---|
| Naive | Last observed value |
| Seasonal naive | Same period last year/week |
| Moving average | Simple smooth; transparent |
| Linear trend | Quick sanity on drift |

Report **MASE** (vs seasonal naive) when seasonality is strong—scale-free comparison.

## Feature patterns

Lag and window features (all computed with cutoff at origin time):

- Lags: `y_{t-1}`, `y_{t-7}`, `y_{t-52}`
- Rolling means / std / min / max over windows
- Calendar: day-of-week, month, holiday flags
- Promotions: lead/lag flags only if known in advance
- Price and stock: use planned price; document stockout censoring

Avoid **global** normalization that uses future series statistics.

## Model choices (tabular focus)

| Approach | Fit |
|---|---|
| Regularized linear on lags | Strong baseline; interpretable coefficients |
| Gradient boosting on lag features | Common production choice for heterogeneous series |
| Global model across series | Shared model with series ID feature; needs enough history per series |
| Classical ARIMA/ETS (workflow level) | Univariate benchmarks; seasonality explicit |
| Prophet-style decomp (if used) | Document holidays and changepoints; validate on rolling origin |

Deep sequence models are out of default scope unless paired with `data-scientist` / research skills.

## Validation for time order

**Never** shuffle time randomly for final evaluation.

| Method | Purpose |
|---|---|
| Holdout tail | Last N periods as test |
| Rolling-origin CV | Retrain on expanding window; score next h steps |
| Blocked CV | Multiple contiguous test blocks for regime coverage |

Report error **by horizon step** (h=1 often easier than h=4).

## Intervals and scenarios

Stakeholders often need **ranges**, not only point forecasts:

- Quantile regression or conformal-style intervals (workflow level)
- Scenario overlays: promo on/off, supply shock assumptions
- Clearly label **intervals are not guarantees**—coverage on holdout only

## Demand forecasting pitfalls

| Pitfall | Mitigation |
|---|---|
| Stockouts suppress demand | Model censored demand or flag stockout periods |
| Promotions in future unknown | Separate promo-driven vs base forecast |
| New SKU cold start | Hierarchical pooling; analog series |
| One-off spikes (COVID) | Exclude or tag regime; document |
| Reconciliation mismatch | Top-down vs bottom-up reconciliation rules with finance |

## Handoff to stakeholders

Deliver:

1. **Forecast table** with horizon, grain, point, optional intervals
2. **Accuracy history** on holdout by horizon and key segments
3. **Assumptions** (promo calendar, price list, capacity)
4. **Known failure modes** (new markets, sparse history)

Visualization of forecasts → `data-visualization`; warehouse pipelines for history → `analytics-data-engineer`.
