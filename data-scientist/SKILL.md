---
name: data-scientist
description: |
  Guides data science workflows from exploration to production.
  Covers machine learning modeling, statistical analysis, A/B testing, causal inference,
  feature engineering, model evaluation, and MLOps patterns.
  Use when building predictive models, designing experiments, analyzing data statistically,
  productionizing ML, debugging model performance, or choosing algorithms and tools.
---

# Data Scientist

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

**See `references/ml_modeling.md` for algorithm selection, feature engineering patterns, and evaluation metrics.**

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

**See `references/analytics_statistics.md` for test selection, power analysis, and causal methods.**

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

**See `references/mlops_production.md` for deployment patterns, monitoring, feature stores, and CI/CD.**

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

**See `references/tools_frameworks.md` for environment setup, library comparisons, and code patterns.**

## When to Load References

- **ML modeling** → `references/ml_modeling.md`
- **Statistics & experiments** → `references/analytics_statistics.md`
- **MLOps & production** → `references/mlops_production.md`
- **Tools & frameworks** → `references/tools_frameworks.md`
