# Sentiment analysis engineer scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [In-scope deliverables](#in-scope-deliverables)
3. [Lifecycle coverage](#lifecycle-coverage)
4. [Engagement checklist](#engagement-checklist)

## Role boundary

Own **engineering and evaluation** of sentiment and opinion-mining systems:

| Own | Partner skill |
|---|---|
| Label schema, annotation, and gold data | `data-scientist` — general ML when sentiment is not the focus |
| Model selection, training, and eval harnesses | `ai-engineer` — LLM product features beyond classification |
| Production serving, drift, and audit loops | `ml-ops-engineer` — platform MLOps without NLP design |
| Research memos and SOTA surveys | `ai-researcher` — papers without build/eval scope |
| Marketing copy and brand tone | `content-creator`, `brand-voice-enforcement` |
| Social campaigns and channel strategy | `social-content`, `marketing-analyst` |
| Legal or compliance determinations | `compliance-engineer`, `legal-risk-assessment` |

## In-scope deliverables

| Artifact | Contents |
|---|---|
| Problem spec | Unit of analysis, label set, languages, domains, SLA |
| Annotation guide | Definitions, borderline examples, adjudication rules |
| Baseline ladder | Lexicon → classical ML → fine-tuned encoder → LLM prompt |
| Eval harness | Held-out splits, slice definitions, significance checks |
| Model card | Data lineage, metrics, limitations, bias notes |
| Serving contract | Input schema, score outputs, versioning, fallback behavior |
| Monitoring spec | Drift metrics, human audit rate, alert thresholds |

Out of scope: using sentiment scores as sole evidence for employment, credit, or legal outcomes without human review and policy.

## Lifecycle coverage

```
Define labels → Annotate → Train/eval → Deploy → Monitor
      │            │          │          │         │
   schema/IAA   gold set   metrics    batch/stream  drift/audit
```

Document which stages are in scope per engagement (e.g., eval-only refresh vs greenfield build).

## Engagement checklist

- [ ] Business question stated (routing, analytics, research, moderation support)
- [ ] Label definitions signed off with product/legal where scores affect users
- [ ] Language and domain list frozen (reviews, social, tickets, news, finance)
- [ ] Baseline and acceptance metrics pre-registered (macro-F1 floor, calibration target)
- [ ] PII and retention policy for text samples in logs and error analysis
- [ ] Production path chosen (batch nightly vs real-time API) with latency budget
- [ ] Handoff owners for dashboards (`analytics-engineer`) and infra (`ml-ops-engineer`) identified
