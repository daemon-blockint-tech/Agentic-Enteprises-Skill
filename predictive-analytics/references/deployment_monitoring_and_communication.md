# Deployment, Monitoring, and Communication

## Table of contents

1. [Deployment modes (conceptual)](#deployment-modes-conceptual)
2. [Scoring contract](#scoring-contract)
3. [Monitoring signals](#monitoring-signals)
4. [Drift types](#drift-types)
5. [Retrain triggers](#retrain-triggers)
6. [Explainability for stakeholders](#explainability-for-stakeholders)
7. [Model card outline](#model-card-outline)
8. [Uncertainty and limitations language](#uncertainty-and-limitations-language)
9. [Governance handoffs](#governance-handoffs)

## Deployment modes (conceptual)

| Mode | When | Trade-offs |
|---|---|---|
| Batch scoring | Nightly/weekly lists; churn campaigns | Stale between runs; simple ops |
| Near-real-time | Fraud, routing within minutes | Feature pipeline latency critical |
| On-demand API | Interactive eligibility | Needs SLAs, fallbacks, versioning |

Platform implementation (containers, feature store, autoscaling) → `ml-infrastructure-engineer-safeguards`. This skill stops at **requirements** and **acceptance criteria**.

## Scoring contract

Document for engineering partners:

- **Input schema**: feature names, types, max null rates
- **Output**: score, probability, decile, optional reason codes
- **Version**: model ID, training data snapshot date
- **Fallback**: default score or rules when features missing
- **Latency budget** and **throughput**
- **Idempotency** for batch replays

## Monitoring signals

Track at minimum:

| Signal | Question answered |
|---|---|
| Score distribution | Did the model’s output shape shift? |
| Feature distributions | Did inputs change (new product, pricing)? |
| Volume & null rates | Pipeline breaks? |
| Label delay & outcome rate | Is realized churn/fraud rate drifting? |
| Business KPI | Did campaign ROI or loss rate change post deploy? |
| Latency & error rate | Serving health |

Set review cadence (daily for fraud, weekly for churn, etc.).

## Drift types

| Type | Symptom | Response (conceptual) |
|---|---|---|
| **Data drift** | Feature means/quantiles shift | Investigate upstream; retrain or recalibrate |
| **Concept drift** | Same features, weaker label relationship | Retrain; revisit features |
| **Prior shift** | Base rate changes | Recalibrate thresholds; adjust capacity |
| **Schema drift** | Missing columns, type changes | Block scoring; alert owners |

Population Stability Index (PSI) is a common **heuristic**—document thresholds and false alarm tolerance.

## Retrain triggers

Define triggers in advance:

- **Calendar** (quarterly retrain) for stable domains
- **Performance decay** (PR-AUC drop vs benchmark on recent labeled window)
- **Drift breach** (PSI or KS on key features/scores)
- **Material business change** (new product line, pricing overhaul)
- **Regulatory / policy** change requiring review

Include **rollback** plan: keep prior model version until new model passes shadow or champion/challenger checks (conceptual).

## Explainability for stakeholders

Practitioner toolkit (not full XAI research):

| Tool | Audience value |
|---|---|
| Global feature importance | What drives the model overall |
| Partial dependence / ICE | Direction of effect for top features |
| SHAP (summary, beeswarm) | Local explanations for cases; watch correlated features |
| Reason codes (top 3–5) | Ops teams for fraud/support |

Caveats to state:

- Importance ≠ causation
- Correlated features split importance arbitrarily
- Explanations trained on historical bias reflect historical decisions

Fairness and adverse action processes are **organizational**—flag review with legal/compliance; do not provide legal conclusions.

## Model card outline

1. **Intended use** and **non-goals**
2. **Training data** (dates, population, exclusions)
3. **Target definition** and horizon
4. **Features** (categories, PII, refresh)
5. **Metrics** on holdout and key slices
6. **Calibration** and **threshold** policy
7. **Limitations** and known failure segments
8. **Monitoring** plan and owners
9. **Version history** and approval sign-off

## Uncertainty and limitations language

Prefer:

- “On holdout data from Q1–Q3, top decile had 3.2× lift vs random.”
- “Precision at our review capacity (2k/day) was 42%; expect ±5% if base rate shifts.”
- “Forecasts are median scenarios; intervals covered 80% of holdout weeks.”

Avoid:

- “The model proves causation.”
- “Accuracy is 99%” without prevalence context.
- Point forecasts without horizon or segment caveats.

## Governance handoffs

| Topic | Skill |
|---|---|
| Experiment validation of interventions | `ab-testing-engineer` |
| BI reporting of scores | `bi-analyst`, `data-visualization` |
| Feature pipeline ownership | `analytics-data-engineer` |
| Model platform & serving | `ml-infrastructure-engineer-safeguards` |
| AI system risk tiering | `ai-risk-governance` |
| Alert disposition policy | `anti-false-positive-decision-making` |
