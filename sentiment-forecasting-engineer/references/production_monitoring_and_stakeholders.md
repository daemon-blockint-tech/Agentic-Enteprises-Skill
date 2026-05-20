# Production monitoring and stakeholders

## Table of contents

1. [Serving architecture](#serving-architecture)
2. [SLAs and refresh cadence](#slas-and-refresh-cadence)
3. [Drift and quality monitors](#drift-and-quality-monitors)
4. [Dashboard and API contracts](#dashboard-and-api-contracts)
5. [Stakeholder communications](#stakeholder-communications)
6. [Governance](#governance)

## Serving architecture

Typical pipeline:

```
Ingest → score (batch/stream) → aggregate index → feature store → forecast job → publish
```

| Mode | Latency | Notes |
|---|---|---|
| Batch daily | Hours acceptable | Reconcile partial days next run |
| Intraday nowcast | Minutes–hours | Strong staleness alerts |
| On-demand API | Seconds | Cache latest forecast + metadata |

Version every publish with **index_version**, **model_id**, and **data_through** timestamp.

## SLAs and refresh cadence

Document:

- **Data through** time shown on every chart
- Maximum acceptable ingest lag
- Retrain schedule vs forecast-only refresh
- Fallback when upstream classifier unavailable (last good scores vs halt)

## Drift and quality monitors

| Monitor | Threshold idea | Response |
|---|---|---|
| Volume Z-score | \|z\| > 4 | Page on-call; verify ingest |
| Score distribution PSI | > 0.2 | Audit classifier; consider retrain |
| Bot rate | Week-over-week +10pp | Tighten filters |
| Coverage | Authors or posts −20% | Widen intervals; flag |
| Forecast error | Rolling MAE +30% | Model review |
| Interval coverage live | Below nominal −10pp | Recalibrate uncertainty |

Run **human audit samples** weekly on high-visibility brands.

## Dashboard and API contracts

Minimum fields for consumers:

```json
{
  "index_id": "brand_x_daily_net",
  "as_of": "2026-05-20T14:00:00Z",
  "data_through": "2026-05-20T12:00:00Z",
  "point": 0.12,
  "pi80": [0.05, 0.19],
  "horizon_days": 7,
  "provisional": false,
  "index_version": "v3",
  "model_id": "prophet_v2_20260501"
}
```

Charts should show **history**, **forecast**, **intervals**, and **annotated events**. Provide strata drill-down when headline moves are mix-driven.

## Stakeholder communications

| Audience | Emphasize | Avoid |
|---|---|---|
| Brand / CX | Trajectory, drivers, uncertainty | False precision |
| Product | Topic strata, launch windows | Single-number hype |
| Research / markets | Methodology, lags, backtest | Trade instructions |
| Executives | Scenarios, risks, data limits | Causal claims without evidence |

Use plain language: “directionally positive with wide uncertainty” when coverage is poor.

## Governance

- **No automated trading** from this skill’s outputs without separate compliance review
- Log **who approved** index formula changes
- Retain reproducibility artifacts (configs, hashes) per retention policy
- Escalate when forecasts could affect **public communications** or **regulated disclosures**

Partner with `sentiment-analysis-engineer` for classifier changes; with `data-scientist` for generic experiment design when A/B testing forecast-informed decisions.
