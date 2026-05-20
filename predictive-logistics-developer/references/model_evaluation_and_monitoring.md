# Model evaluation and monitoring

## Backtesting discipline

1. **Rolling-origin evaluation** — refit or refit-window policy documented; no single holdout on logistics seasonality
2. **Match decision cadence** — if planners run weekly, backtest weekly origins
3. **Segment reporting** — lane, node, ABC class, promo vs non-promo, cold chain vs ambient
4. **Link statistical metrics to operational proxies** — WMAPE segments vs simulated fill rate impact where possible

## Core metrics

| Metric | Formula intent | Logistics use |
|---|---|---|
| MAPE | Mean abs % error | Intuitive; unstable at low volume |
| WMAPE | Σ\|error\| / Σ actual | Preferred for mixed-volume networks |
| Bias | Signed error rate | Stock position drift, OTIF skew |
| MASE | Scaled vs naive | Compare across intermittent series |
| Pinball loss | Quantile accuracy | Safety stock and promise dates |
| Coverage | % inside P90 interval | Service level calibration |

Report **WMAPE and bias** at minimum for executive and planning audiences.

## Operational KPI linkage

| KPI | Model linkage |
|---|---|
| Fill rate | Stockout probability from forecast + policy sim |
| OTIF | Promise date error decomposition |
| Inventory turns | Over/under forecast vs targets |
| Expedite cost | Tail error on lead-time forecasts |
| Spoilage | Perishable forecast vs actual shrink |

Build a **forecast value analysis** table—did improved WMAPE reduce stockouts or inventory dollars?

## Bias and fairness checks

- **Geographic bias** — systematically under-forecasting rural lanes
- **New product bias** — ramp under/over shoot
- **Promo decay** — post-promo negative bias
- **Carrier change** — regime shift undetected

## Production monitoring

| Signal | Threshold action |
|---|---|
| Feature drift | PSI or population stability index by column |
| Prediction drift | Score distribution vs training |
| Residual bias | Rolling bias by top lanes |
| Latency / freshness | Missed batch SLA → fallback |
| Data quality | Null rate, late arrivals |

Define **retrain triggers**: sustained WMAPE degradation, major network redesign, new SKU class rules.

## Model registry artifacts

- Training data window, feature schema version, hyperparameters
- Backtest report attachment and sign-off checklist
- Champion/challenger promotion criteria
- Rollback procedure when OTIF or fill rate regresses post-deploy

## Champion/challenger workflow

1. Shadow score in production without driving decisions
2. Compare **offline backtest** and **shadow operational KPIs**
3. Promote with canary segment (e.g., one region or carrier tier)
4. Full cutover with monitoring escalation path
