# Sentiment forecasting engineer scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [In-scope deliverables](#in-scope-deliverables)
3. [Out of scope](#out-of-scope)
4. [Engagement checklist](#engagement-checklist)
5. [Handoff map](#handoff-map)

## Role boundary

Own **aggregate opinion dynamics over time**—how sentiment indices move, correlate with outcomes, and forecast under uncertainty.

| Own | Partner skill |
|---|---|
| Index design, rollups, and revision policy | `sentiment-analysis-engineer` — per-text labeling and classifiers |
| Time-series and sequence forecasting | `data-scientist` — general predictive modeling without opinion indices |
| Demand/inventory forecasts without sentiment | `predictive-logistics-developer` |
| LLM product surfaces beyond forecasting pipelines | `ai-engineer` |
| Marketing copy and campaign creative | `content-creator` |
| Trade recommendations or investment advice | Methodology only; no actionable signals |

**Unit of analysis:** time-indexed **population aggregates** (brand, product line, geo, channel), not individual posts unless explicitly modeling distributions.

## In-scope deliverables

| Artifact | Contents |
|---|---|
| Index specification | Universe, sampling, polarity→score mapping, weights, strata |
| Aggregation playbook | Grain (H/D/W), missing-data rules, revision and restatement policy |
| Feature catalog | Volume, velocity, topic mix, engagement quality, exogenous KPIs |
| Forecast design | Horizon, frequency, model ladder, exogenous structure |
| Backtest report | Walk-forward metrics, interval coverage, spike holdouts |
| Nowcast SOP | Latency budget, partial-period handling, stale-source fallbacks |
| Monitoring spec | Drift, bot share, coverage, alert thresholds |
| Stakeholder brief | Trajectory + uncertainty; explicit limitations |

## Out of scope

- Training or evaluating **document-level** sentiment classifiers (see `sentiment-analysis-engineer`)
- **Buy/sell**, position sizing, or guaranteed alpha claims from sentiment forecasts
- **Marketing messaging** or creative based on forecast direction
- **Legal/compliance** determinations from sentiment alone
- Pure **macro econometric** models with no text-derived sentiment component

## Engagement checklist

- [ ] Business decision named (brand health, product launch, risk desk research, ops staffing)
- [ ] Target population and text sources listed with access and retention constraints
- [ ] Index formula frozen (or versioned) before backtest claims
- [ ] Forecast horizon and decision cadence aligned (e.g., daily index → 7/14/28-day horizons)
- [ ] Outcome variables for lead/lag study defined (sales, NPS proxy, volatility, search)
- [ ] Bot/spam and sample-bias mitigation documented
- [ ] Walk-forward protocol pre-registered (origin, step, embargo if needed)
- [ ] Interval/scenario reporting required for all external forecasts
- [ ] Dashboard or API consumer identified; SLA for refresh documented

## Handoff map

```
Text streams → Score/label (partner: sentiment-analysis-engineer)
            → Aggregate index (this skill)
            → Features + forecast (this skill)
            → BI / research dashboard (consumer)
            → Monitor drift + restate (this skill)
```

When upstream classifiers change, **rebuild or re-link** historical indices with a version bump; do not silently splice incompatible scores.
