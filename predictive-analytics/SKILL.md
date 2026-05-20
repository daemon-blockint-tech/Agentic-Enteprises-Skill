---
name: predictive-analytics
description: |
  Guides applied predictive analytics for business—target and leakage framing, tabular feature
  engineering, regression and classification models (baselines, boosting, regularized linear),
  validation splits and metrics, calibration and cost-sensitive thresholds, practitioner
  explainability (importance, SHAP), drift monitoring concepts, and uncertainty comms. Covers
  churn, demand, fraud, propensity, risk scores—not actuarial reserving. Use for "predictive
  analytics", "build a predictive model", "propensity model", "churn prediction", "demand
  forecast model", "classification model", "feature engineering", "model validation",
  "predict customer behavior", "risk score model", or "predictive modeling workflow". Not for
  MLOps (ml-infrastructure-engineer-safeguards), DL research (ml-research-engineer-safeguards),
  actuarial reserving (actuarial-analyst), BI only (data-visualization), warehouse/dbt only
  (data-warehouse-engineer, analytics-data-engineer), or A/B tests (ab-testing-engineer).
---

# Predictive Analytics

## When to Use

- Define the **prediction target**, **unit of analysis**, **horizon**, and success criteria before modeling
- Audit **leakage**, label timing, and train/validation design for tabular or time-ordered data
- Engineer and **select features** for churn, propensity, fraud, demand, or risk scoring use cases
- Choose **model families** and baselines (linear, tree ensembles, gradient boosting) matched to data size and interpretability needs
- Run **validation**: holdout, cross-validation, or time-based splits with metrics aligned to the decision
- Tune **calibration**, **thresholds**, and **cost-sensitive** operating points for classification and scores
- Explain models at **practitioner level** (importance, partial dependence, SHAP-style intuition—not full XAI research)
- Plan **conceptual** post-deployment monitoring: drift signals, retrain triggers, and limitation language for stakeholders

## When NOT to Use

- **MLOps platform** build—feature stores, model registry, K8s serving, CI for training pipelines → `ml-infrastructure-engineer-safeguards`, `ml-ops-engineer` (if installed)
- **Deep learning** research, LLM fine-tuning, or novel architecture search → `ml-research-engineer-safeguards`, `ai-engineer`
- **Actuarial** reserving, loss development, rate indication, or regulatory pricing math → `actuarial-analyst`, `advanced-short-term-actuarial-mathematics`, `actuary`
- **Dashboard-only** KPI layout, chart design, or viz specs without modeling → `data-visualization`, `bi-analyst`
- **Warehouse/dbt** dimensional modeling, mart SQL, or pipeline idempotency only → `data-warehouse-engineer`, `analytics-data-engineer`
- **A/B test** design, power, randomization, and experiment readouts → `ab-testing-engineer`
- **Markets/finance** factor research, backtests, and alpha hygiene → `quantitative-researcher`
- **Cloud cost** forecasting and FinOps allocation → `finops-analyst`

## Related skills

| Need | Skill |
|---|---|
| Broader ML lifecycle, causal inference, heavy MLOps detail | `data-scientist` |
| Factor research, backtests, market time series | `quantitative-researcher` |
| dbt marts, metric layers, analytics pipelines | `analytics-data-engineer` |
| Warehouse modeling, ELT, data quality frameworks | `data-warehouse-engineer` |
| Chart type, dashboard layout, honest viz | `data-visualization` |
| Experiment design, power, SRM, readouts | `ab-testing-engineer` |
| Cloud spend models and allocation | `finops-analyst` |
| Insurance reserving, pricing, regulatory actuarial work | `actuarial-analyst` |
| GenAI products, agents, LLM application patterns | `ai-engineer` |
| Training/serving infrastructure and platform guardrails | `ml-infrastructure-engineer-safeguards` |

## Core Workflows

### 1. Frame the problem and label

1. State the **business decision** the score or forecast will drive
2. Define **target** (binary, multiclass, continuous), **horizon**, and **grain** (user, account, SKU, region)
3. Document **label window** and **feature cutoff** (what is knowable at scoring time)
4. Check **base rate**, class imbalance, and whether rules/heuristics already suffice
5. List **constraints**: latency, interpretability, fairness review, regulatory context

**See `references/problem_framing_and_data_prep.md`.**

### 2. Prepare data and features

1. Profile missingness, cardinality, outliers, and temporal coverage
2. Build **point-in-time** feature tables; never join future outcomes into training rows
3. Encode categoricals, scale numerics, and handle high-cardinality keys deliberately
4. Document feature definitions, refresh cadence, and upstream dependencies
5. Split data with the right strategy (random, grouped, or time-based)

**See `references/problem_framing_and_data_prep.md`.**

### 3. Model, validate, and compare

1. Fit **baselines** first (majority class, linear/logistic, naive forecast)
2. Iterate tree ensembles or regularized models; avoid unnecessary complexity
3. Select **metrics** tied to the decision (PR-AUC for rare events, MAPE vs WAPE for demand, etc.)
4. Use **cross-validation** or rolling-origin evaluation for time-ordered problems
5. Compare models on holdout data never used for tuning

**See `references/modeling_and_validation.md`.**

### 4. Classification, propensity, and scores

1. Calibrate probabilities when ranks are not enough for thresholds or expected value
2. Set **thresholds** using cost matrices, capacity, or top-decile lift—not default 0.5
3. Report **lift**, **capture**, and **stability** by segment and time
4. Separate **model quality** from **policy** (who gets contacted, approved, or reviewed)

**See `references/classification_and_propensity.md`.**

### 5. Forecasting and time series (when applicable)

1. Choose granularity (daily/weekly) and horizon aligned to planning cycles
2. Use naive and seasonal baselines; add exogenous features only when available at forecast time
3. Validate with **rolling** or blocked time splits; report interval or quantile forecasts when decisions need range
4. Document seasonality, promotions, and structural breaks that limit extrapolation

**See `references/forecasting_and_time_series.md`.**

### 6. Deploy, monitor, and communicate

1. Specify **scoring cadence**, input schema, and fallback when features are missing
2. Define **monitoring**: label delay, score distribution drift, feature drift, and business outcome tracking
3. Set **retrain triggers** (calendar, performance decay, population shift)—conceptual triggers only here
4. Deliver a **model card** or memo: intended use, limitations, metrics, and what would falsify trust

**See `references/deployment_monitoring_and_communication.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and deliverables | `references/predictive_analytics_scope.md` |
| Target, leakage, unit of analysis, data prep | `references/problem_framing_and_data_prep.md` |
| Model families, splits, metrics, validation | `references/modeling_and_validation.md` |
| Propensity, calibration, thresholds, costs | `references/classification_and_propensity.md` |
| Demand forecast and time-series workflow | `references/forecasting_and_time_series.md` |
| Monitoring, retrain, stakeholder comms | `references/deployment_monitoring_and_communication.md` |
