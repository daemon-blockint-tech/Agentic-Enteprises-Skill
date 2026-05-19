# MLOps & Production

## Model Deployment Patterns

### Batch Scoring
```python
# Scheduled job (Airflow, cron, cloud scheduler)
def batch_predict(model, input_path, output_path):
    df = pd.read_parquet(input_path)
    df['prediction'] = model.predict(df[features])
    df[['id', 'prediction']].to_parquet(output_path, partition_cols=['date'])
```

### Real-Time API
```python
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load('model.pkl')

@app.post("/predict")
def predict(input_data: dict):
    features = preprocess(input_data)
    prediction = model.predict([features])[0]
    return {"prediction": prediction, "model_version": "1.0.0"}
```

### Embedded (Database Native)
```sql
-- BigQuery ML example
CREATE OR REPLACE MODEL `project.dataset.model`
OPTIONS(model_type='LOGISTIC_REG')
AS SELECT * FROM `project.dataset.training_data`;

-- Predict in SQL
SELECT * FROM ML.PREDICT(MODEL `project.dataset.model`,
  (SELECT * FROM `project.dataset.new_data`));
```

## Model Monitoring

### What to Monitor

| Layer | Metric | Alert When |
|---|---|---|
| Data drift | PSI (Population Stability Index) > 0.2 | Between training and production features |
| Feature drift | KS test p < 0.01 | Individual feature distribution changes |
| Prediction drift | KL divergence > threshold | Output distribution changes |
| Concept drift | Rolling accuracy decline | >5% drop from baseline |
| Latency | P99 response time | >500ms for real-time APIs |
| Error rate | Failed requests % | >1% |
| Null predictions | % None/NaN outputs | >0.1% |

### Drift Detection Example

```python
from scipy.stats import ks_2samp
import numpy as np

def detect_drift(reference, production, threshold=0.01):
    """Returns True if distributions are significantly different"""
    statistic, p_value = ks_2samp(reference, production)
    return p_value < threshold

# For each feature
for col in features:
    if detect_drift(train[col], production[col]):
        alert(f"Drift detected in {col}")
```

### Shadow Deployment
Run new model alongside production without serving its predictions:
- Log predictions from both models
- Compare offline metrics
- Switch traffic when new model is validated

## Feature Stores

### When to Use
- Same features needed by multiple models
- Complex feature engineering (streaming aggregations)
- Need point-in-time correctness (prevent leakage)

### Architecture
```
Raw Data → Feature Pipelines → Feature Store → Models
                               (online + offline)
```

| Store | Online Latency | Offline | Examples |
|---|---|---|---|
| Feast | Redis/DynamoDB | BigQuery/Snowflake | Open source |
| Tecton | Low latency | Spark | Enterprise |
| SageMaker Feature Store | <10ms | S3 | AWS native |

### Point-in-Time Correctness
```python
# Critical: feature values as they were at prediction time
# NOT as they are now
features_at_time = feature_store.get_features(
    entity_ids=['user_123'],
    timestamp='2024-01-15T10:00:00Z'  # NOT now()
)
```

## Model Versioning & Registry

### MLflow Tracking
```python
import mlflow

mlflow.set_experiment("churn_prediction")

with mlflow.start_run():
    mlflow.log_params({"n_estimators": 100, "max_depth": 6})
    mlflow.log_metrics({"f1": 0.85, "auc": 0.92})
    mlflow.sklearn.log_model(model, "model")
    mlflow.set_tag("version", "v1.2.0")
```

### Model Registry Stages
1. **Staging**: Candidate model under evaluation
2. **Production**: Currently serving traffic
3. **Archived**: Retired, kept for audit

## CI/CD for ML

### Pipeline Stages

```
Code commit → Unit tests → Integration tests → Train model → Evaluate → Register → Deploy
```

**Key differences from software CI/CD:**
- Model training is non-deterministic (set seeds, log everything)
- Evaluation needs hold-out data (not just unit tests)
- Deployment may require data validation, not just code validation
- Rollback means reverting to previous model artifact

### Testing Strategy

| Test Type | What | When |
|---|---|---|
| Unit tests | Feature transforms, preprocessing | Every commit |
| Data tests | Schema, nulls, distributions | Before training |
| Model tests | Performance > baseline on hold-out | After training |
| Integration tests | End-to-end inference pipeline | Before deploy |
| Canary tests | A/B production validation | After deploy |

### Git-Based Workflows

**Git-flow for ML:**
- `main`: Production model + code
- `develop`: Integration branch
- `experiment/<name>`: Model experiments (may not merge)
- `feature/<name>`: Code features (merge to develop)

**Model promotion via PR:**
- Training run triggered on PR
- Evaluation metrics posted as PR comment
- Human review + automated gates → merge → deploy

## Retraining Strategy

| Trigger | When | Implementation |
|---|---|---|
| Scheduled | Weekly/monthly | Cron job retrains on latest data |
| Performance-based | Accuracy < threshold | Monitor metric, trigger retrain |
| Data volume | N new labeled samples | Count new labels, threshold trigger |
| Manual | Ad-hoc needs | One-off training job |

**Retraining checklist:**
- [ ] New data passes quality checks
- [ ] Feature pipeline unchanged (or updated and tested)
- [ ] New model beats current production on hold-out
- [ ] A/B test or shadow mode before full cutover
- [ ] Update model metadata and documentation

## Cost Optimization

| Technique | Savings |
|---|---|
| Spot/preemptible instances for training | 60-90% |
| Auto-scaling inference | Pay for actual load |
| Model distillation | Smaller model, faster inference |
| Feature caching | Reduce repeated computation |
| Early stopping in HPO | Don't train poor configurations to completion |
