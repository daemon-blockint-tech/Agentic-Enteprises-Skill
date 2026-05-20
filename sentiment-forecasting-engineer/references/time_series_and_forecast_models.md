# Time-series and forecast models

## Table of contents

1. [Model ladder](#model-ladder)
2. [Classical time-series](#classical-time-series)
3. [State-space and Bayesian](#state-space-and-bayesian)
4. [ML sequence models](#ml-sequence-models)
5. [Exogenous and multivariate](#exogenous-and-multivariate)
6. [Horizon and nowcasting](#horizon-and-nowcasting)

## Model ladder

Always fit a **simple baseline** before complex models:

1. Seasonal naive / last-value
2. Moving average with seasonality
3. ARIMA / SARIMA or ETS
4. Prophet or structural time-series (holidays, changepoints)
5. State-space (DLM, Kalman) with exogenous regressors
6. ML sequence (gradient boosting on lags, TFT, N-BEATS, etc.)

Report **lift over baseline** on walk-forward metrics, not in-sample R² alone.

## Classical time-series

| Method | Strengths | Watchouts |
|---|---|---|
| ARIMA/SARIMA | Interpretable; good short horizons | Stationarity; regime breaks |
| ETS | Trend/season components | Sparse or zero-inflated volumes |
| Prophet | Holidays, changepoints | Can overfit changepoints on short history |

**Seasonality:** align to business cycle (weekly for social, monthly for surveys). Include **known events** (launches, earnings, crises) as regressors or dummy spikes.

## State-space and Bayesian

Use when you need **online updates** or explicit uncertainty:

- Dynamic linear models for slowly drifting level
- Kalman filters for nowcasting partial days
- Bayesian structural time-series for sparse exogenous series

Document **prior sensitivity** if stakeholders interpret credible intervals as guarantees.

## ML sequence models

| Approach | When | Risk |
|---|---|---|
| Lag features + GBM | Medium history; heterogeneous features | Leakage if features use future data |
| TFT / deep seq | Rich covariates; long history | Overfit; opaque |
| Direct multi-horizon | Fixed horizon grid | Needs retrain per horizon change |

Enforce **causal feature windows**: features at time t may only use information ≤ t.

## Exogenous and multivariate

Joint modeling patterns:

- **Sentiment → outcome** (leading indicator studies): Granger-style tests with pre-specified lags
- **Outcome → sentiment** (feedback): avoid claiming lead without out-of-sample tests
- **Vector models** (VAR): when both series forecast together; check stability

Include **control series** (ad spend, pricing, seasonality) to reduce spurious correlation.

## Horizon and nowcasting

| Mode | Definition | Implementation |
|---|---|---|
| Nowcast | Estimate current incomplete period | Intraday partial aggregates + DLM |
| Short horizon | 1–7 steps | ARIMA, GBM lags |
| Medium horizon | 2–12 weeks | Seasonal models + exogenous plans |
| Long horizon | Months+ | Scenario bands; widen intervals |

Match horizon to **decision latency**; do not report 90-day precision intervals for a daily trading desk unless backtest coverage supports it.
