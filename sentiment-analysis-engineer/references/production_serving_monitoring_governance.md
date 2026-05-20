# Production serving, monitoring, and governance

## Table of contents

1. [Inference modes](#inference-modes)
2. [Serving architecture](#serving-architecture)
3. [API and versioning](#api-and-versioning)
4. [Monitoring and drift](#monitoring-and-drift)
5. [Human review and governance](#human-review-and-governance)
6. [Analytics integration](#analytics-integration)

## Inference modes

| Mode | When | Notes |
|---|---|---|
| Batch | Nightly dashboards, backfill | Higher throughput; stale up to SLA |
| Micro-batch | Near-line aggregations | Kafka + windowed scoring |
| Real-time API | Routing, alerts | p99 latency budget drives model size |
| Edge / on-device | Mobile, privacy | Quantized models; limited labels |

Size models to **p99 latency**; keep LLM tier for low-volume or audit queues unless budget allows.

## Serving architecture

- **Model server**: TorchServe, Triton, HF TEI, or managed endpoints
- **Preprocessor**: normalize unicode, strip PII, language ID, max length truncation
- **Postprocessor**: threshold, abstain class, aspect aggregation
- **Feature store** (optional): cache embeddings for repeat texts
- **Shadow deploy**: new model scores logged without affecting routing

Document **cold start**, **batch size**, and **GPU vs CPU** footprint in runbook.

## API and versioning

Expose stable contract:

```json
{
  "text_id": "…",
  "polarity": "negative",
  "confidence": 0.91,
  "aspects": [{"name": "battery", "polarity": "negative", "span": [12, 24]}],
  "model_version": "sentiment-encoder-v3.2",
  "schema_version": "polarity-v1"
}
```

- Semantic **model_version** per trained artifact; **schema_version** per label definition
- **Rollback** to prior version without redeploying consumers
- **Abstain** when confidence below τ or language unsupported

## Monitoring and drift

| Signal | Detection | Action |
|---|---|---|
| Label drift | Score distribution vs baseline | Investigate product/event change |
| Prior drift | Class prevalence shift | Retrain or recalibrate thresholds |
| Concept drift | Macro-F1 drop on audit sample | Guideline refresh, new labels |
| Language drift | Language ID mix change | Route or retrain per locale |
| Latency / errors | p99, 5xx rate | Scale, rollback model |

- Sample **human audit** (e.g., 0.1–1% daily) on live traffic
- Store **input hash + score + model_version**; avoid raw PII in logs when policy requires redaction

## Human review and governance

- Route **low-confidence** or **high-impact** items to review queues
- Never present sentiment as **legal or compliance verdict**
- Align with **retention and deletion** policies for stored text
- Incident playbook: schema change → re-eval golden set → staged rollout

## Analytics integration

- Emit scores to **warehouse** (`analytics-engineer`) with `scored_at`, `model_version`, dimensions
- Dashboards: volume-weighted sentiment, aspect trends, slice by product/region
- Separate **model metrics** from **business KPIs** (CSAT, churn) in reporting

Partner `ml-ops-engineer` for CI/CD, canaries, and infra; own **NLP-specific eval gates** in this skill.
