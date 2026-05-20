---
name: sentiment-forecasting-engineer
description: |
  This skill should be used when the user asks to forecast aggregate sentiment and opinion
  dynamics over time—sentiment indices from text streams; temporal rollups; leading/lagging KPI
  links; time-series and sequence models (ARIMA, Prophet, state-space, ML); nowcasting; spikes,
  bots, and bias; walk-forward backtests; intervals and scenarios; volume/velocity/topic features;
  BI or brand dashboards. Triggers: sentiment forecasting, forecast sentiment, sentiment index,
  opinion trend forecast, social sentiment time series, brand sentiment trajectory, nowcast
  sentiment, sentiment leading indicator, aggregate polarity forecast, sentiment backtest,
  walk-forward sentiment, sentiment spike prediction. Not for per-text labeling
  (sentiment-analysis-engineer), demand forecasting without sentiment
  (predictive-logistics-developer, data-scientist), trade advice (methodology only), marketing
  copy (content-creator), macro without text sentiment (financial-analyst partial).
---

# Sentiment Forecasting Engineer

## When to Use

- Build **aggregate sentiment indices** from high-volume text streams (social, news, reviews, surveys)
- Design **temporal rollups** — hourly, daily, weekly aggregation with consistent weighting rules
- Forecast **opinion trajectories** — point forecasts, prediction intervals, and scenario bands
- Model **leading/lagging relationships** between sentiment and sales, traffic, volatility, or brand KPIs
- Select and implement **time-series and sequence models** — ARIMA, Prophet, state-space, TFT, etc.
- Run **nowcasts** and choose forecast horizons aligned to decision cadence
- Engineer features from **volume, velocity, topic mix**, and engagement quality
- **Backtest** with walk-forward validation and report calibration of uncertainty
- Handle **spikes, bot noise, sample bias**, and regime shifts in language or product mix
- Integrate outputs with **BI dashboards**, brand monitoring, or research workflows (methodology only)

## When NOT to Use

- Per-document or per-span **polarity labeling**, annotation, or classifier training → `sentiment-analysis-engineer`
- Generic demand, inventory, or logistics forecasting **without** sentiment inputs → `predictive-logistics-developer`, `data-scientist`
- **Investment advice**, trade recommendations, or actionable trading signals → provide forecasting methodology and uncertainty only
- Marketing copy, campaigns, or brand voice → `content-creator`, `brand-voice-enforcement`
- Broad macro econometrics or financial modeling **without** text-derived sentiment → `financial-analyst` (partial overlap only)
- Exploratory NLP or single-shot sentiment scores on a static corpus → `sentiment-analysis-engineer`
- LLM product features, agents, or RAG (unless sentiment forecasting is one pipeline component) → `ai-engineer`

## Related skills

| Need | Skill |
|---|---|
| Document-level polarity, ABSA, annotation, classifier eval | `sentiment-analysis-engineer` |
| General ML, experimentation, non-time-series predictive modeling | `data-scientist` |
| Warehouse metrics, dbt, analytics pipelines (if present in repo) | `analytics-engineer` |
| Demand/inventory forecasting without opinion indices | `predictive-logistics-developer` |
| Campaign ROI and channel performance (if present in repo) | `marketing-analyst` |
| Ratios, valuation, macro series without text sentiment (if present) | `financial-analyst` |
| LLM apps, feature stores for agent products | `ai-engineer` |

## Core Workflows

### 1. Scope and index design

Clarify population (brand, product, geo), text sources, aggregation grain, target horizon, and downstream KPIs.

**See `references/sentiment_forecasting_engineer_scope.md`.**

### 2. Indices, aggregation, and features

Define index formulas, rollups, topic/strata splits, and covariates (volume, velocity, mix).

**See `references/indices_aggregation_and_features.md`.**

### 3. Time-series and forecast models

Choose baselines and advanced models; align seasonality, holidays, and exogenous drivers.

**See `references/time_series_and_forecast_models.md`.**

### 4. Backtesting, validation, and metrics

Walk-forward evaluation, interval calibration, and spike-event holdouts.

**See `references/backtesting_validation_and_metrics.md`.**

### 5. Data quality, bias, and events

Bot filtering, sample bias, language drift, and shock labeling for scenario analysis.

**See `references/references_data_quality_bias_and_events.md`.**

### 6. Production monitoring and stakeholders

Serving cadence, drift monitors, dashboard contracts, and stakeholder-ready narratives.

**See `references/production_monitoring_and_stakeholders.md`.**

## Outputs

- **Index specification** — formula, universe, weights, strata, and revision policy
- **Feature catalog** — engineered signals with definitions and lag structure
- **Forecast spec** — horizon, frequency, model family, and exogenous inputs
- **Backtest report** — walk-forward metrics, interval coverage, and failure slices
- **Nowcast playbook** — latency budget, refresh rules, and stale-data handling
- **Monitoring plan** — drift, spike alerts, and human review triggers
- **Stakeholder brief** — trajectory narrative with explicit uncertainty (no trade advice)

## Principles

- Forecast **aggregates**, not individual opinions — index stability and definitional clarity come first
- Treat **index construction** as part of the model — changing weights invalidates historical comparability
- Prefer **walk-forward** evaluation over single holdout splits for time-ordered data
- Report **intervals and scenarios**, not point estimates alone; disclose coverage on backtests
- Separate **methodology from decisions** — do not present forecasts as buy/sell or guaranteed outcomes
- Document **known biases** (platform mix, bot share, demographic skew) beside every published index
