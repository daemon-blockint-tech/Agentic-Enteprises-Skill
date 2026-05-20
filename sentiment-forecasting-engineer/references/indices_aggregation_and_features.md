# Indices, aggregation, and features

## Table of contents

1. [Index families](#index-families)
2. [Aggregation grains](#aggregation-grains)
3. [Weighting and stratification](#weighting-and-strification)
4. [Feature engineering](#feature-engineering)
5. [Revision and comparability](#revision-and-comparability)

## Index families

| Index type | Definition | Typical use |
|---|---|---|
| Net polarity | (positive − negative) / volume or weighted mean of signed scores | Headline brand trajectory |
| Positive share | positive / (positive + negative + neutral policy) | Simple stakeholder dashboards |
| Intensity-weighted mean | mean score × engagement weight | Social where likes/shares matter |
| Aspect/strata indices | Same formulas per topic, product, geo | Diagnostic decomposition |
| Dispersion | variance or entropy of scores within window | Polarization early warning |

Document **neutral handling** explicitly (exclude, separate series, or map to 0). Changing neutral policy breaks historical continuity.

## Aggregation grains

| Grain | Pros | Cons |
|---|---|---|
| Hourly | Fast nowcasts, event detection | Noisy; needs stronger smoothing |
| Daily | Standard for brand and markets | Misses intraday shocks |
| Weekly | Stable for executive reporting | Lags fast-moving crises |

**Rollup rules:**

- Use **consistent timezone** (UTC vs market local) and document market-hours filters for finance use cases
- For partial periods (today), emit **provisional** flags until window closes
- Apply **minimum volume thresholds**; suppress or widen intervals when N is low

## Weighting and stratification

| Scheme | When to use | Pitfall |
|---|---|---|
| Equal post | Democratic voice | Dominated by spam/bots |
| Engagement-weighted | Influence-aware | Celebrities swamp signal |
| Author-deduped | Reduce bot farms | Needs stable author IDs |
| Sample-weighted | Correct platform mix | Requires population estimates |

Stratify by **language, channel, product, and region** when mix shifts drive headline moves more than opinion shifts.

## Feature engineering

Build **forecast-ready** covariates alongside the target index:

| Feature | Construction | Notes |
|---|---|---|
| Volume | post count, unique authors | Log-transform; watch outages |
| Velocity | Δvolume, acceleration | Spike precursor |
| Topic mix | share of top-K topics | Drift when product launches |
| Engagement rate | interactions per post | Separates “loud” from “many” |
| New-author share | first-time posters / total | Bot/inorganic indicator |
| Score dispersion | std dev within window | Polarization |
| Exogenous KPIs | sales, search, prices | Align lags in modeling stage |

**Lag structure:** pre-specify max lag (e.g., 0–14 days) for outcome linkage studies; avoid fishing every lag without multiple-testing control.

## Revision and comparability

- Version indices when **classifier**, **lexicon**, or **weighting** changes
- Publish **overlap period** where v1 and v2 run in parallel
- Never restate backtests using formulas not available at historical decision times
- Store raw inputs (hashed IDs, counts) to reproduce aggregates without re-scraping
