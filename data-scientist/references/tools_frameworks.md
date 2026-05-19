# Tools & Frameworks

## Environment Setup

### Python Environment
```bash
# Recommended: uv or conda
uv venv .venv
source .venv/bin/activate

# Core stack
uv pip install pandas polars numpy scikit-learn xgboost

# Optional by use case
uv pip install torch transformers  # deep learning
uv pip install statsmodels scipy  # statistics
uv pip install mlflow optuna     # experiment tracking + HPO
uv pip install fastapi uvicorn    # API serving
uv pip install shap lime          # interpretability
```

### R Environment
```r
install.packages(c("tidyverse", "caret", "randomForest", "xgboost"))
install.packages(c("broom", "infer", "rsample"))  # tidy stats
```

## Library Comparison

### Data Manipulation

| Library | Strengths | Weaknesses | When to Use |
|---|---|---|---|
| pandas | Ubiquitous, rich ecosystem | Slow on large data | <10M rows, exploration |
| Polars | Fast, lazy evaluation, memory efficient | Newer, smaller ecosystem | Large data, production |
| DuckDB | SQL engine, in-process | Not a dataframe library | SQL-heavy workflows |
| PySpark | Distributed, big data | Heavy overhead | >100M rows, cluster |
| data.table (R) | Fast, concise syntax | R-only | R users, large data |

### Machine Learning

| Library | Algorithms | Best For |
|---|---|---|
| scikit-learn | Comprehensive classical ML | Baselines, preprocessing, pipelines |
| XGBoost | Gradient boosted trees | Tabular data, competitions |
| LightGBM | Faster XGBoost alternative | Large tabular datasets |
| CatBoost | Categorical handling | Datasets with many categoricals |
| PyTorch | Deep learning, flexible | Research, custom architectures |
| TensorFlow/Keras | Deep learning, production | Google Cloud, TF Serving |
| Statsmodels | Statistical models | Inference, regression diagnostics |

### Experiment Tracking

| Tool | Open Source | Best Feature | Limitation |
|---|---|---|---|
| MLflow | Yes | Model registry + tracking | Self-hosted complexity |
| Weights & Biases | No | Visualization, collaboration | Cost at scale |
| Neptune | No | Fast UI, model comparison | Cost |
| DVC | Yes | Data versioning, git-like | CLI-heavy |
| TensorBoard | Yes | Free with TensorFlow | TF-centric |

## Code Patterns

### Reproducible Experiment
```python
import random
import numpy as np
from sklearn.model_selection import cross_val_score

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    # Add framework-specific seeds
    # torch.manual_seed(seed)
    # tf.random.set_seed(seed)

set_seed(42)

# Log everything
config = {
    "model": "XGBClassifier",
    "n_estimators": 100,
    "max_depth": 6,
    "seed": 42
}
# mlflow.log_params(config)

model = XGBClassifier(**config)
scores = cross_val_score(model, X, y, cv=5)
# mlflow.log_metric("cv_f1", scores.mean())
```

### Pipeline Pattern
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('model', XGBClassifier())
])

# Prevents leakage: preprocessing fit only on training fold
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)
```

### Time Series Split
```python
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error

tscv = TimeSeriesSplit(n_splits=5)
scores = []

for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    scores.append(mean_squared_error(y_test, preds))
```

## Cloud ML Services

| Service | Provider | Best For |
|---|---|---|
| SageMaker | AWS | Full ML lifecycle, notebook instances |
| Vertex AI | GCP | AutoML, model registry, pipelines |
| Azure ML | Azure | Enterprise, MLOps integration |
| Databricks | Multi-cloud | Spark + ML + collaborative notebooks |

## Performance Tips

**Pandas:**
- Use `category` dtype for low-cardinality strings
- Vectorize with `.apply()` only as last resort
- Use `.loc[]` for assignment to avoid SettingWithCopy
- Chunk large files: `pd.read_csv(file, chunksize=100000)`

**scikit-learn:**
- Use `n_jobs=-1` for parallelizable operations
- Prefer `joblib` over `pickle` for model serialization
- Use `Pipeline` to prevent data leakage

**XGBoost/LightGBM:**
- Use `early_stopping_rounds` to prevent overfitting
- Set `tree_method='hist'` for large datasets
- Use `feature_name` and `feature_types` for interpretability

## Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| `ValueError: Input contains NaN` | Missing values in features | Impute or drop before fitting |
| `DataConversionWarning` | Wrong dtype (e.g., object instead of numeric) | Convert types explicitly |
| `ConvergenceWarning` | Model didn't converge | Increase `max_iter`, scale features |
| MemoryError with large data | Loading everything into RAM | Use generators, sample, or distributed |
| Different train/test encodings | Fit transform on train, only transform on test | Use Pipeline |
