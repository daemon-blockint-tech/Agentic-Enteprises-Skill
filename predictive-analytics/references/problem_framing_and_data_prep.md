# Problem Framing and Data Prep

## Table of contents

1. [Decision-first framing](#decision-first-framing)
2. [Target and horizon](#target-and-horizon)
3. [Unit of analysis and grain](#unit-of-analysis-and-grain)
4. [Leakage checklist](#leakage-checklist)
5. [Label construction](#label-construction)
6. [Feature cutoff rules](#feature-cutoff-rules)
7. [Data quality gates](#data-quality-gates)
8. [Split strategies](#split-strategies)

## Decision-first framing

Start from the **action**, not the algorithm:

- Who receives the prediction, and what do they do differently?
- What is the **cost** of false positives vs false negatives (or forecast error direction)?
- Is a **score rank** enough, or are calibrated probabilities / dollar forecasts required?
- Can a **simple rule** or segmentation deliver 80% of value?

Document answers before selecting features or models.

## Target and horizon

| Element | Questions to answer |
|---|---|
| Target | What exact field or derived label? Binary, multiclass, continuous? |
| Horizon | Predict 30-day churn vs 90-day; next-week demand vs next-quarter |
| Observation window | How much history is required before a row is scorable? |
| Delay | How long until labels are observable (fraud chargebacks, churn confirmation)? |

Align horizon with **when the business can act** and when features are frozen.

## Unit of analysis and grain

Pick one primary grain and stick to it:

- **User** — consumer apps, subscriptions
- **Account / customer** — B2B, householding rules documented
- **SKU-location-day** — retail demand
- **Transaction** — fraud (often with user/account aggregates as features)

If labels exist at a different grain (e.g., account churn from user events), define **aggregation rules** explicitly and avoid duplicate rows that inflate confidence.

## Leakage checklist

Leakage makes offline metrics lie. Audit for:

- [ ] Features computed **after** the prediction moment (including “current status” fields)
- [ ] Target information embedded in features (e.g., `cancellation_reason` before cancel)
- [ ] **Random** train/test split on time-series or repeated measures per entity
- [ ] **Future** aggregates (30-day spend including days after scoring date)
- [ ] **Test set** used for feature selection, imputation stats, or target encoding fit globally
- [ ] **Duplicate** entities across train and test without grouped splits
- [ ] **Survivorship** (only customers who stayed long enough to get a label)

When in doubt, rebuild features with a strict **as-of timestamp** per row.

## Label construction

| Pattern | Guidance |
|---|---|
| Binary churn | Define active vs churned with inactivity threshold; handle reactivations |
| Propensity | Label positive only if action occurred within window; negative = eligible but no action |
| Fraud | Use confirmed fraud labels; document delay and partial labels |
| Demand | Align to fulfillment calendar; handle stockouts and censored demand |

Document **class balance** and whether negatives are “true negatives” or “not yet positive.”

## Feature cutoff rules

For each feature, record:

1. **Source table** and refresh lag
2. **As-of rule** (e.g., events with `event_time < score_time`)
3. **Aggregation window** (7d, 30d, lifetime-with-decay)
4. **Default** when missing (and whether missingness is informative)

Prefer **interpretable** aggregates over opaque embeddings unless `ml-research-engineer-safeguards` scope applies.

## Data quality gates

Before modeling:

- Coverage by time, segment, and key dimensions
- Cardinality and rare level handling plan
- Outlier policy (cap, winsorize, flag)—document, do not silently drop
- Consistency between training snapshot and production schema
- Join fan-out checks (one-to-many explosions)

## Split strategies

| Data regime | Split approach |
|---|---|
| IID tabular | Stratified random holdout; k-fold CV for tuning |
| Many rows per entity | **Group** CV by entity ID |
| Time-ordered | **Time-based** holdout; rolling-origin CV |
| Deployment geography | Hold out regions or cohorts for robustness |

Never tune on the final holdout. For time series, see `forecasting_and_time_series.md`.
