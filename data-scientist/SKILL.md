---
name: data-scientist
description: |
  Execute data science workflows from exploration to production.
  Apply machine learning modeling, statistical analysis, A/B testing, causal inference,
  feature engineering, model evaluation, and MLOps patterns.
  Triggers on "build predictive model", "design A/B test", "feature engineering",
  "model evaluation", "causal inference", "productionize ML", "choose ML algorithm",
  "statistical analysis", "model monitoring", or "data science workflow".
---

# Data Scientist

## Overview

Execute data science workflows from exploration to production. This skill covers machine learning
modeling, statistical analysis, A/B testing, causal inference, feature engineering, model evaluation,
and MLOps patterns.

## Features

- ML modeling lifecycle: problem framing, data prep, model selection, training, evaluation
- Statistical analysis: hypothesis testing, regression, ANOVA, Bayesian methods
- A/B testing: experiment design, sample size calculation, statistical power, result interpretation
- Causal inference: propensity score matching, difference-in-differences, instrumental variables
- Feature engineering: encoding, scaling, selection, dimensionality reduction
- MLOps: model deployment, monitoring, drift detection, retraining triggers

## Usage

1. Identify the user's data science need (modeling, analysis, experimentation, or MLOps)
2. Follow the corresponding workflow below
3. Produce structured outputs: model cards, experiment reports, feature engineering pipelines, or MLOps runbooks

## Examples

- **User**: "Build a churn prediction model"
  **Agent**: Runs ML Modeling workflow, frames problem, selects features, trains classifier, evaluates with precision/recall, produces model card

- **User**: "Design an A/B test"
  **Agent**: Runs Experiment Design workflow, calculates sample size, defines success metrics, sets up randomization, produces experiment plan

- **User**: "Monitor model drift"
  **Agent**: Runs MLOps workflow, defines drift metrics, sets up monitoring dashboard, configures retraining triggers

## When to Use

- Scoping ML problems, baselines, feature engineering, and model evaluation
- Designing A/B tests, power analysis, or causal inference when experiments are infeasible
- Productionizing models (batch, real-time, monitoring, retraining triggers)
- Selecting ML, stats, or MLOps tools for a given problem and data regime

## When NOT to Use

- Executive dashboards, KPI definitions, or BI storytelling → use `bi-analyst`
- Warehouse dimensional modeling or ETL idempotency patterns → use `data-warehouse-engineer`
- Prompt design, LLM agents, or guardrailed GenAI features → use `prompt-engineer`
- Revenue metrics (ARR, NRR) or ASC 606 accounting → use `senior-revenue-accountant`

## Core Workflows

### 1. End-to-End ML Project Workflow

**Phase checklist:**

1. **Problem definition**
   - Define the business metric to optimize
   - Determine if ML is needed (rule-based may suffice)
   - Set success criteria and failure modes

2. **Data exploration & validation**
   - Profile distributions, missing values, duplicates
   - Check for leakage (future information in training data)
   - Validate data freshness and coverage

3. **Feature engineering**
   - Create domain-relevant features
   - Encode categoricals, scale numerics
   - Document feature definitions and dependencies

4. **Modeling**
   - Baseline: simple model first (linear regression, logistic)
   - Iterate: tree-based, then ensembles, then deep learning if needed
   - Cross-validate properly (time-based for temporal data)

5. **Evaluation**
   - Hold-out test set, never used for hyperparameter tuning
   - Check calibration, fairness, robustness
   - Compare against baseline and business threshold

6. **Production**
   - Serialize model, build inference API
   - Add monitoring (prediction drift, latency)
   - Document retraining triggers

### 2. Statistical Analysis & Experimentation

**A/B testing workflow:**

1. Define hypothesis, primary metric, and minimal detectable effect (MDE)
2. Calculate sample size (power analysis)
3. Randomize and run experiment
4. Check invariant metrics (randomization sanity)
5. Analyze primary metric with proper statistical test
6. Correct for multiple comparisons if needed
7. Document and socialize results

**Causal inference when A/B test is impossible:**
- Difference-in-differences
- Propensity score matching
- Instrumental variables
- Regression discontinuity

### 3. Productionizing Models (MLOps)

**Deployment patterns:**

| Pattern | When | Trade-off |
|---|---|---|
| Batch scoring | Periodic predictions, no latency requirement | Simple, stale predictions between runs |
| Real-time API | User-facing, latency-sensitive | Complex, requires monitoring |
| Edge / on-device | Mobile/IoT, offline needed | Model size constraints, hard to update |
| Embedded | Database/warehouse native (BigQuery ML, Snowpark) | Limited to supported algorithms |

**Monitoring checklist:**
- [ ] Prediction distribution drift vs training
- [ ] Feature drift (incoming data changes)
- [ ] Latency and throughput
- [ ] Error rate and fallback behavior
- [ ] Business metric tracking

### 4. Tool Selection

| Task | Recommended Tools |
|---|---|
| Data manipulation | pandas, Polars, SQL |
| Feature engineering | scikit-learn, Feature-engine, Tsfresh |
| Modeling | scikit-learn, XGBoost, LightGBM, PyTorch, TensorFlow |
| Experiment tracking | MLflow, Weights & Biases, Neptune |
| Hyperparameter tuning | Optuna, Ray Tune, Hyperopt |
| Causal inference | CausalML, DoWhy, EconML |
| Interpretability | SHAP, LIME, ELI5 |
| Deployment | FastAPI, BentoML, Seldon, SageMaker |
