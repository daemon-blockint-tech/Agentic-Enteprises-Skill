---
name: Sentiment Analysis Engineer
description: |
  This skill should be used when the user asks to build or evaluate sentiment and opinion-mining
  systems—label schemas, lexicon/ML/transformer/LLM classifiers, annotation and IAA, F1/calibration,
  domain adaptation, multilingual/code-switching, sarcasm/negation/bias, and production inference with
  drift monitoring. Triggers: sentiment analysis, sentiment engineer, opinion mining, text
  classification, aspect-based sentiment, ABSA, fine-tune sentiment, sentiment model, polarity
  detection, emotion detection, review sentiment, social media sentiment, sentiment labeling, sentiment
  evaluation, sarcasm detection, multilingual sentiment. Not for marketing copy (content-creator),
  MLOps without NLP (ml-ops-engineer), general data science (data-scientist), social campaigns
  (social-content), safety-classifier R&D (ml-research-engineer-safeguards), or legal outcomes from
  scores alone.
---

# Sentiment Analysis Engineer

## When to Use

- Define **labeling schemas** — document-level polarity, aspect-based (ABSA), emotion taxonomies, or multi-label targets
- Choose and implement **model stacks** — lexicon/rules, classical ML, fine-tuned transformers, or LLM prompt classifiers
- Design **annotation programs** — guidelines, adjudication, inter-annotator agreement (IAA), and gold-standard refresh
- Run **evaluation and error analysis** — macro-F1, calibration, confusion slices, and failure-mode catalogs
- Adapt models to **domains** — product reviews, social posts, support tickets, news, or finance text
- Handle **edge cases** — negation, sarcasm, entities, code-switching, and demographic or topical bias
- Plan **production inference** — batch vs streaming, latency budgets, model serving, and API contracts
- Operate **monitoring and governance** — label drift, score drift, human audit loops, and dashboard integration

## When NOT to Use

- Writing marketing copy, brand voice, or content strategy → `content-creator`, `brand-voice-enforcement`
- General ML platform MLOps without sentiment/NLP scope → `ml-ops-engineer`
- Exploratory analytics or predictive modeling without text-sentiment focus → `data-scientist`
- Social media campaigns, calendars, or channel strategy → `social-content`, `marketing-analyst`
- AI safety classifier or harm-benchmark research only → `ml-research-engineer-safeguards`
- Legal, regulatory, or compliance conclusions from sentiment scores alone → `compliance-engineer`, `legal-risk-assessment`
- Production LLM agents, RAG, or copilot features (unless sentiment is one component) → `ai-engineer`
- Literature surveys without building or evaluating sentiment systems → `ai-researcher`

## Related skills

| Need | Skill |
|---|---|
| Classical ML, A/B tests, general model evaluation | `data-scientist` |
| LLM apps, RAG, agents, prompt eval harnesses | `ai-engineer` |
| Papers, benchmarks, research methodology | `ai-researcher` |
| Warehouse metrics, dbt, analytics pipelines | `analytics-engineer` |
| Campaign performance and channel ROI | `marketing-analyst` |
| De-AI-ing prose or editorial voice | `content-humanizer` |
| MLOps deploy, drift, retraining platform | `ml-ops-engineer` |

## Core Workflows

### 1. Scope and problem framing

Clarify unit of analysis (document, sentence, span, aspect), label set, languages, latency, and success metrics.

**See `references/sentiment_analysis_engineer_scope.md`.**

### 2. Labeling and annotation

Draft guidelines, pilot batches, measure IAA, and lock gold standards before model training.

**See `references/labeling_schemas_and_annotation.md`.**

### 3. Model selection and training

Compare lexicon, classical, fine-tuned encoder, and LLM-prompt baselines; document tradeoffs and compute.

**See `references/models_lexicon_transformers_llm.md`.**

### 4. Evaluation and error analysis

Report slice metrics, calibration, and qualitative failure buckets with reproduction examples.

**See `references/evaluation_metrics_and_error_analysis.md`.**

### 5. Domain, multilingual, and edge cases

Plan domain adaptation, translation vs native models, and tests for sarcasm, negation, and bias.

**See `references/domain_multilingual_and_edge_cases.md`.**

### 6. Production, monitoring, and governance

Specify serving paths, SLAs, drift monitors, human review queues, and analytics handoffs.

**See `references/production_serving_monitoring_governance.md`.**

## Outputs

- **Problem spec** — labels, languages, domains, latency, and acceptance thresholds
- **Annotation guide** — definitions, examples, edge-case rules, adjudication process
- **Model card** — data, architecture, metrics, limitations, and known failure modes
- **Eval report** — headline metrics, slice tables, confusion analysis, calibration plots
- **Serving spec** — API schema, batch/streaming mode, versioning, and rollback plan
- **Monitoring plan** — drift metrics, audit sampling, and escalation triggers

## Principles

- Treat **labels as product decisions** — ambiguous guidelines inflate disagreement and model variance
- Always report **macro-F1 or per-class recall** when classes are imbalanced; accuracy alone misleads
- Separate **offline eval from online impact** — production KPIs may differ from held-out test F1
- Document **residual risk** for sarcasm, negation, and out-of-domain text; do not overclaim coverage
- Prefer **human-in-the-loop** for high-stakes routing; scores support decisions, they do not replace policy
