# Modeling and Validation

## Table of contents

1. [Modeling philosophy](#modeling-philosophy)
2. [Baseline ladder](#baseline-ladder)
3. [Model families](#model-families)
4. [Feature selection](#feature-selection)
5. [Hyperparameters and tuning](#hyperparameters-and-tuning)
6. [Validation design](#validation-design)
7. [Metrics by problem type](#metrics-by-problem-type)
8. [Diagnostics and sanity checks](#diagnostics-and-sanity-checks)

## Modeling philosophy

- **Simple first**: If baselines are strong, complexity needs a measured lift.
- **Match interpretability** to stakeholder needs and regulatory review.
- **Separate** offline model selection from policy (thresholds, queues, budgets).
- **Document** random seeds, data snapshots, and library versions for reproducibility.

## Baseline ladder

Always report at least one baseline before advanced models:

| Problem | Baselines |
|---|---|
| Binary classification | Majority class; prevalence; simple rules (e.g., tenure > X) |
| Multiclass | Stratified majority; one-vs-rest logistic on few features |
| Regression | Mean/median; last value (for series); seasonal naive |
| Ranking / propensity | Random score; single-feature sort (recency, spend) |

If uplift over baseline is small, question whether ML is worth operational cost.

## Model families

| Family | When to use | Caveats |
|---|---|---|
| Regularized linear / logistic | Linear-ish effects, high interpretability, wide sparse data | Needs careful encoding; interactions manual |
| Tree ensembles (RF, GBDT) | Tabular default for medium/large data | Watch overfit on small data; document monotonic constraints if used |
| Gradient boosting (XGBoost, LightGBM, CatBoost) | Strong tabular performance | Tune carefully; handle categoricals per library |
| GLM / GAM (optional) | Smooth terms, insurance-style transparency | Not a substitute for actuarial sign-off |

Avoid deep learning for typical business tabular problems unless `data-scientist` or research skills justify it.

## Feature selection

Principles:

1. **Domain-first**: Keep features with causal or operational story when possible.
2. **Remove redundant** highly correlated columns after documenting which to keep.
3. Use **embedded** selection (L1, tree importance) on training folds only—not holdout.
4. Prefer **stability** across CV folds over single-run importance rankings.
5. Cap **dimensionality** when rows are limited (rules of thumb: tens of features per thousand positives for rare events).

Do not iterate feature sets using holdout performance.

## Hyperparameters and tuning

- Tune on **inner CV** or a dedicated validation fold.
- Track **search budget**; avoid exhaustive grids on large data without need.
- Record **best params** and **variance across folds**—a lucky fold is not production-ready.
- For boosting: watch **early stopping** on validation; document `n_estimators` effective count.

## Validation design

| Method | Use when |
|---|---|
| Single holdout | Large IID data; final gate only |
| k-fold CV | Medium data; hyperparameter selection |
| Group k-fold | Repeated measures per customer/account |
| Rolling-origin | Time-ordered rows; forecasts and drift-prone populations |
| Nested CV | Unbiased estimate when heavy tuning (report outer fold metrics) |

**Final holdout** is touched once for the delivery report unless deploying iterative research under governance.

## Metrics by problem type

### Binary classification (imbalanced)

| Metric | Role |
|---|---|
| PR-AUC | Primary for rare positives |
| ROC-AUC | Supplementary; can look optimistic when negatives dominate |
| Precision@k / lift@k | Aligns to top-decile campaigns |
| Brier score | Calibration quality |
| Confusion at operating point | Tie to capacity and costs |

Avoid accuracy as the sole metric when prevalence < 10%.

### Multiclass

Macro vs weighted F1 depending on whether rare classes matter equally; report **per-class** recall for operational classes.

### Regression

| Metric | Notes |
|---|---|
| MAE | Robust, same units as target |
| RMSE | Penalizes large errors |
| MAPE / WAPE | Scale-free; beware zeros (use WAPE or sMAPE) |
| Quantile loss | When reporting P10/P50/P90 forecasts |

### Forecasting

Report accuracy **by horizon bucket** (1-step vs 4-step ahead). See `forecasting_and_time_series.md`.

## Diagnostics and sanity checks

- **Calibration plot** (reliability curve) for classifiers used with thresholds
- **Residual plots** for regression; heteroscedasticity and tail errors
- **Learning curves** (train vs val) for over/underfit
- **Slice analysis**: time cohorts, regions, product lines, acquisition channel
- **Score stability**: rank correlation month-over-month on holdout cohorts

Flag any slice where the model is **worse than baseline** before release.
