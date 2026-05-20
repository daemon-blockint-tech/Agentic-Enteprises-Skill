# Labeling schemas and annotation

## Table of contents

1. [Labeling schemes](#labeling-schemes)
2. [Guideline design](#guideline-design)
3. [Annotation workflow](#annotation-workflow)
4. [Quality metrics](#quality-metrics)

## Labeling schemes

| Scheme | Granularity | Typical use |
|---|---|---|
| Document polarity | One label per review/post | Dashboard aggregates, routing |
| Sentence / span | Sub-document units | Long documents, mixed sentiment |
| Aspect-based (ABSA) | (aspect, opinion, polarity) triples | Product features, NPS drivers |
| Emotion | Multi-class or multi-label (joy, anger, …) | CX analytics, moderation signals |
| Intensity | Ordinal or continuous score | Fine-grained trends |
| Target-aware | Sentiment toward entity X | News, finance tickers |

Choose the **smallest schema** that answers the business question; extra labels increase cost and disagreement.

## Guideline design

- Define **in-scope text** (title + body, quoted replies, emojis, hashtags)
- Provide **positive, negative, neutral, and borderline** examples per class
- Document **neutral rules** (factual statements, questions, mixed without dominant polarity)
- Specify handling for **emoji-only**, **URLs**, **@mentions**, and **deleted/edited** content
- For ABSA: list **aspect inventory** (closed vs open vocabulary) and opinion span rules
- For finance/news: separate **market sentiment** from **author opinion** when required

Run a **pilot batch** (50–200 items) before full annotation; revise guidelines when adjudication rate exceeds ~15%.

## Annotation workflow

1. **Dual annotation** on training/eval gold; single pass only for low-stakes exploratory sets
2. **Adjudication** by senior annotator or SME on disagreements
3. **Active learning** queue for uncertain model predictions in production (optional)
4. **Version guidelines** (v1, v2) and remap or re-label when definitions shift

Store: `text_id`, `annotator_id`, `label`, `timestamp`, `guideline_version`, `adjudicated` flag.

## Quality metrics

| Metric | Interpretation |
|---|---|
| Cohen's κ / Fleiss' κ | Pairwise or multi-rater agreement on nominal labels |
| Krippendorff's α | Nominal/ordinal, handles missing raters |
| % adjudicated | Volume of unresolved disagreements |
| Guideline violation rate | QA spot-checks on random samples |

**Targets (rule of thumb):** κ ≥ 0.6 acceptable for noisy social text; κ ≥ 0.75 for reviews with clear guidelines. Below 0.5 → fix guidelines before training.

Do not treat **majority vote** on ambiguous social text as ground truth without SME review on error slices.
