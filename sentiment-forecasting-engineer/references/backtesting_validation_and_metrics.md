# Backtesting, validation, and metrics

## Table of contents

1. [Walk-forward protocol](#walk-forward-protocol)
2. [Point forecast metrics](#point-forecast-metrics)
3. [Interval and scenario metrics](#interval-and-scenario-metrics)
4. [Event and spike holdouts](#event-and-spike-holdouts)
5. [Reporting template](#reporting-template)

## Walk-forward protocol

```
Timeline:  |---- train ----|-- test --|-- train' --|-- test' --| ...
           origin expands or rolls forward each step
```

| Parameter | Guidance |
|---|---|
| Origin | First date with stable index definition |
| Step | Match production retrain cadence (e.g., weekly) |
| Test window | ≥ one full season for seasonal series |
| Embargo | Gap between train end and test start if labels lag |
| Retrain | Freeze hyperparameters per protocol; document tuning set |

**Forbidden:** random train/test splits on time series; tuning on the full history; peeking at future spikes when engineering features.

## Point forecast metrics

| Metric | Use | Caveat |
|---|---|---|
| MAE / RMSE | Level accuracy | Scale-dependent across indices |
| MAPE | Stakeholder-friendly | Undefined near zero; biased low volumes |
| sMAPE | Symmetric % errors | Still unstable at zero |
| MASE | Compare to naive | Good for model selection |
| Directional hit rate | Trend sign | Ignores magnitude |

Report metrics **per horizon** and **per stratum** (channel, region). Aggregate with volume weights when combining strata.

## Interval and scenario metrics

| Metric | Definition | Target |
|---|---|---|
| Coverage | % actuals inside PI | Near nominal (e.g., 80% for 80% PI) |
| Width | Mean interval width | Minimize subject to coverage |
| CRPS | Probabilistic score | Lower is better |
| Calibration plot | Nominal vs empirical | Diagnose under/over-confidence |

**Scenarios:** stress bands (optimistic/base/pessimistic) must map to documented shocks (volume −50%, bot spike, classifier drift), not arbitrary ±2σ.

## Event and spike holdouts

Reserve **labeled crisis windows** (product recall, viral backlash, outage) for out-of-sample spike tests:

- Did intervals widen before the peak?
- Did nowcast lag exceed SLA?
- Did bot-filter failure inflate the false spike?

Do not **remove** spikes from training without documenting that production forecasts must handle spikes too.

## Reporting template

1. Data window and index version
2. Walk-forward diagram and fold count
3. Baseline vs challenger metrics table (by horizon)
4. Interval coverage and calibration figure
5. Worst misses — dates, drivers, data gaps
6. Sensitivity — weighting, neutral policy, bot filter on/off
7. Production readiness — latency, refresh, monitoring hooks
