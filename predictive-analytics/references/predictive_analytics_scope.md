# Predictive Analytics — Scope

## Table of contents

1. [Role definition](#role-definition)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Typical use cases](#typical-use-cases)
5. [Deliverables](#deliverables)
6. [Quality bar](#quality-bar)

## Role definition

**Predictive Analytics** covers **applied supervised learning** for business decisions: defining what to predict, building tabular features, training and validating models, and communicating scores or forecasts with explicit uncertainty and limitations. The focus is **practitioner-grade** workflow—not research novelty, not platform engineering, and not actuarial statutory methods.

## In scope

| Area | Examples |
|---|---|
| Problem framing | Target, horizon, grain, label timing, leakage checks |
| Data prep | Point-in-time joins, train/val/test design, imbalance handling |
| Feature engineering | Encodings, aggregations, lags, RFM-style behavior features |
| Model families | Linear/logistic, regularized GLMs, tree ensembles, gradient boosting |
| Validation | Holdout, k-fold, grouped CV, rolling-origin for time series |
| Metrics | Classification, ranking, regression, forecast accuracy by horizon |
| Calibration & thresholds | Platt/isotonic concepts, cost-sensitive cutoffs, capacity constraints |
| Explainability (practitioner) | Global importance, partial dependence, SHAP intuition |
| Deployment concepts | Batch vs real-time scoring, drift monitors, retrain triggers |
| Communication | Model cards, limitation language, segment stability |

## Out of scope

| Area | Route to |
|---|---|
| Feature stores, model registry, K8s serving, training CI | `ml-infrastructure-engineer-safeguards`, `ml-ops-engineer` |
| Deep learning, LLM training, embedding research | `ml-research-engineer-safeguards`, `ai-engineer` |
| Reserving, ratemaking, capital, regulatory actuarial | `actuarial-analyst`, `advanced-short-term-actuarial-mathematics` |
| Chart/dashboard design without modeling | `data-visualization`, `bi-analyst` |
| dbt, warehouse modeling, pipeline orchestration | `analytics-data-engineer`, `data-warehouse-engineer` |
| A/B tests, power, randomization | `ab-testing-engineer` |
| Factor/backtest research for markets | `quantitative-researcher` |

## Typical use cases

| Use case | Target type | Common pitfalls |
|---|---|---|
| Churn / retention | Binary or time-to-event proxy | Label leakage from post-cancel activity |
| Propensity / upsell | Binary or multiclass | Treating all contacts as independent when accounts cluster |
| Demand forecast | Continuous count or revenue | Using future promotions as features |
| Fraud / abuse score | Binary, heavy imbalance | Evaluating only accuracy; ignoring investigation capacity |
| Credit-style risk (non-actuarial) | Binary or score | Fairness and policy separation from model rank |
| Lead scoring | Binary | Stale CRM features; duplicate leads across campaigns |

## Deliverables

1. **Problem brief** — decision, target, horizon, grain, exclusions
2. **Data dictionary** — features, cutoff rules, refresh cadence
3. **Validation report** — splits, metrics, baselines, segment slices
4. **Model artifact spec** — inputs, outputs, versioning, fallback behavior
5. **Threshold / policy memo** — costs, capacity, expected confusion matrix at operating point
6. **Model card** — intended use, limitations, monitoring plan, owner

## Quality bar

Work is **ready to hand off** when:

- [ ] **Baseline** beats are documented; complexity is justified
- [ ] **Leakage** and label timing are explicitly ruled out or flagged
- [ ] **Holdout** or rolling evaluation was not used for hyperparameter tuning
- [ ] **Metrics** match the business decision (not accuracy alone on rare events)
- [ ] **Segments** (time, region, product) show stability or known gaps
- [ ] **Limitations** and **retrain triggers** are stated in plain language
