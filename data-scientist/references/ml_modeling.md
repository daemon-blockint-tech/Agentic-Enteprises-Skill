# Machine Learning Modeling

## Algorithm Selection Guide

| Problem Type | Start With | Upgrade To | Avoid |
|---|---|---|---|
| Tabular regression | Ridge/Lasso, Random Forest | XGBoost/LightGBM, TabNet | Deep learning (usually overkill) |
| Tabular classification | Logistic Regression, Random Forest | XGBoost/LightGBM, CatBoost | Deep learning (usually overkill) |
| Time series | ARIMA, Prophet | XGBoost with lags, Temporal Fusion Transformer | Standard cross-validation |
| NLP (text) | TF-IDF + Linear | BERT, LLMs | Bag-of-words for semantic tasks |
| Computer vision | ResNet, EfficientNet | Vision Transformer | Custom architectures unless research |
| Recommendation | Matrix factorization | Two-tower neural, transformers | Cold start without content features |
| Anomaly detection | Isolation Forest, LOF | Autoencoders, VAE | Supervised methods (rarely have labels) |

## Feature Engineering Patterns

### Numeric Features
```python
# Log transform for skewed distributions
import numpy as np
df['log_revenue'] = np.log1p(df['revenue'])

# Binning for non-linear relationships
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 65, 100])

# Interaction terms
df['price_per_unit'] = df['price'] / df['quantity']
```

### Categorical Features
```python
# High cardinality: target encoding (with regularization)
from category_encoders import TargetEncoder
encoder = TargetEncoder(cols=['city'])

# Ordinal: maintain order if exists
df['size_encoded'] = df['size'].map({'S': 1, 'M': 2, 'L': 3})

# One-hot for low cardinality (<10)
pd.get_dummies(df['color'], prefix='color')
```

### Temporal Features
```python
# Cyclical encoding for time
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)

# Time since event
df['days_since_signup'] = (df['event_date'] - df['signup_date']).dt.days
```

### Text Features
```python
# TF-IDF for classical ML
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))

# Embeddings for deep learning
# Use sentence-transformers or LLM APIs
```

## Cross-Validation Strategies

| Data Type | CV Strategy | Why |
|---|---|---|
| Standard i.i.d. | Stratified K-Fold | Maintains class distribution |
| Time series | Time Series Split | Prevents future leakage |
| Groups/clusters | Group K-Fold | Same group not in train and test |
| Spatial | Spatial cross-validation | Nearby locations correlated |
| Imbalanced | Stratified + SMOTE/undersampling | Balance without leakage |

**Time series split example:**
```python
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in tscv.split(X):
    # train is always before test in time
    X_train, X_test = X[train_idx], X[test_idx]
```

## Evaluation Metrics

### Classification

| Metric | When to Use | Formula |
|---|---|---|
| Accuracy | Balanced classes | `(TP + TN) / Total` |
| Precision | Cost of false positive is high | `TP / (TP + FP)` |
| Recall | Cost of false negative is high | `TP / (TP + FN)` |
| F1 | Balance precision and recall | `2 × (P × R) / (P + R)` |
| AUC-ROC | Ranking quality, threshold-independent | Area under ROC curve |
| AUC-PR | Imbalanced classes | Area under precision-recall curve |
| Log loss | Probabilistic evaluation | `-Σ(y log(p))` |

### Regression

| Metric | When to Use | Formula |
|---|---|---|
| MAE | Robust to outliers | `mean(\|y - ŷ\|)` |
| RMSE | Penalize large errors | `sqrt(mean((y - ŷ)²))` |
| MAPE | Interpretable % error | `mean(\|y - ŷ\| / y)` |
| R² | Explained variance | `1 - SSR/SST` |
| RMSLE | Log-scale targets | `sqrt(mean((log(y+1) - log(ŷ+1))²))` |

## Hyperparameter Tuning

### Search Strategies

| Strategy | When | Cost |
|---|---|---|
| Grid Search | Few parameters, known good ranges | High (exponential) |
| Random Search | Many parameters, wide ranges | Medium |
| Bayesian (Optuna) | Expensive training, need efficiency | Low (smart exploration) |
| Population Based (Ray) | Deep learning, long training | Low (early stopping) |

**Optuna example:**
```python
import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    n_estimators = trial.suggest_int('n_estimators', 50, 500)
    max_depth = trial.suggest_int('max_depth', 3, 20)
    min_samples_split = trial.suggest_float('min_samples_split', 0.01, 0.3)

    clf = RandomForestClassifier(n_estimators=n_estimators,
                                  max_depth=max_depth,
                                  min_samples_split=min_samples_split)
    score = cross_val_score(clf, X, y, cv=5, scoring='f1').mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

## Model Interpretability

### Global Interpretation
- **Feature importance**: Built-in (tree-based) or permutation importance
- **SHAP summary plot**: Feature impact distribution
- **Partial dependence plots**: Feature effect on prediction

### Local Interpretation
- **SHAP force plot**: Why this specific prediction?
- **LIME**: Local surrogate model explanation
- **Counterfactuals**: What would change the prediction?

```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

## Common Pitfalls

| Pitfall | Detection | Fix |
|---|---|---|
| Data leakage | Feature importance too good to be true | Time-based splits, pipeline all preprocessing |
| Target leakage | Feature correlated with target by construction | Remove post-event features |
| Overfitting | Train >> test performance | Regularization, more data, simpler model |
| Sampling bias | Test distribution ≠ production | Stratify, reweight, or collect better data |
| Temporal leakage | Using future information | Cutoff dates, time-aware validation |
| Group leakage | Same entity in train/test | Group K-Fold |
