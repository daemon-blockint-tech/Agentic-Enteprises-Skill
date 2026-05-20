# Evaluation metrics and error analysis

## Table of contents

1. [Splits and leakage](#splits-and-leakage)
2. [Classification metrics](#classification-metrics)
3. [Calibration and thresholds](#calibration-and-thresholds)
4. [Error analysis](#error-analysis)
5. [Regression testing](#regression-testing)

## Splits and leakage

- **Temporal split** for reviews and social streams (train past, test future)
- **Group split** by author, product, or ticket ID to detect memorization
- **Stratify** rare classes in dev/test
- Remove **duplicates** and near-duplicates (MinHash) before metrics
- Hold out **adjudicated gold** never used for hyperparameter tuning

## Classification metrics

| Metric | When to use |
|---|---|
| Accuracy | Balanced classes only |
| Macro-F1 | Default for imbalanced polarity/emotion |
| Weighted-F1 | When class frequency reflects production |
| Per-class precision/recall | Cost-sensitive routing (e.g., miss negative) |
| ROC-AUC / PR-AUC | Score ranking; not a business KPI alone |
| Cohen's κ vs human | Model–human agreement on eval set |

For **ABSA**: micro-F1 over (aspect, polarity) pairs; separate aspect extraction F1 if two-stage.

Report **confidence intervals** (bootstrap) when test set < 2k examples.

## Calibration and thresholds

- Plot **reliability diagrams**; apply temperature scaling or Platt scaling if scores drive automation
- Tune thresholds on **cost matrix** (false positive vs false negative), not default 0.5
- Report **expected calibration error (ECE)** when scores feed dashboards or alerts

## Error analysis

Build a **failure taxonomy** with 20–50 quoted examples per bucket:

| Bucket | Examples |
|---|---|
| Sarcasm / irony | Positive words, negative intent |
| Negation | "not bad", "hardly recommend" |
| Mixed sentiment | Pros and cons in one document |
| Domain shift | Training reviews, test support chat |
| Entity-specific | Sentiment toward brand vs competitor |
| Neutral vs weak polarity | "OK", "it arrived" |
| Language / script | Code-switching, transliteration |
| OCR / ASR noise | Garbled text in pipelines |

Link each bucket to **mitigation** (more labels, rules, model swap, human review).

## Regression testing

- Freeze **golden eval set** (500–5k adjudicated items) per schema version
- CI gate: macro-F1 drop > 1–2 pts or per-class recall breach
- Compare **lexicon, encoder, and LLM** baselines on every release
- Log **confusion matrix** and top regression examples in model card

For production monitoring metrics, see `production_serving_monitoring_governance.md`.
