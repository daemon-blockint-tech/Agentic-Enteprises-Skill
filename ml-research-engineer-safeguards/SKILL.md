---
name: ml-research-engineer-safeguards
description: |
  Guides ML/research engineering for safeguards—safety classifier development, harm benchmarks and
  eval suites, labeled dataset design, fine-tuning and ablations, calibration and slice analysis,
  attack-surface research memos, and promotion criteria for new moderation models.
  Use when building or evaluating guardrail models, designing safety benchmarks, measuring
  precision/recall on policy categories, comparing mitigation techniques, or writing research
  reports on classifier improvements—not for production inference gateways (ml-infrastructure-engineer-safeguards),
  PII/leakage privacy research (privacy-research-engineer-safeguards), red-team attack campaigns (ai-redteam),
  AI governance policy (ai-risk-governance), general non-safety research (ai-researcher), or token-efficiency
  studies (research-engineer-scientist-tokens).
---

# ML / Research Engineer, Safeguards

## When to Use

- Define **research questions** on harm detection, jailbreak resistance, or policy categories
- Curate or audit **safety datasets** — labeling guidelines, bias checks, version control
- **Train or fine-tune** classifiers, rankers, or small LLM judges for moderation
- Design **benchmarks and eval suites** — golden sets, adversarial slices, regression harnesses
- Run **ablations** — architecture, threshold, data mix, ensemble vs single model
- Analyze **metrics** — precision/recall, calibration, false positive/negative slices
- Write **research memos** — methods, results, limitations, production recommendation
- Specify **promotion bar** for a new safeguard model version

## When NOT to Use

- Deploy gateways, GPU serving, canary routing → `ml-infrastructure-engineer-safeguards`
- Execute structured red-team engagements on prod → `ai-redteam`
- Draft acceptable-use policy or risk tiers → `ai-risk-governance`
- Build customer-facing RAG/agents → `ai-engineer`
- General literature survey unrelated to safety → `ai-researcher`
- Token/context compression research → `research-engineer-scientist-tokens`
- Product A/B and business metrics → `data-scientist`
- PII detection benchmarks, memorization, logging minimization → `privacy-research-engineer-safeguards`

## Related skills

| Need | Skill |
|---|---|
| Privacy research for safeguards | `privacy-research-engineer-safeguards` |
| Production safeguard path and rollout | `ml-infrastructure-engineer-safeguards` |
| Adversarial attack campaigns | `ai-redteam` |
| Governance sign-off and model cards | `ai-risk-governance` |
| Production eval harness in app | `ai-engineer` |
| General research methodology | `ai-researcher` |
| Classical ML and statistics | `data-scientist` |
| Token efficiency ablations | `research-engineer-scientist-tokens` |
| Release gates and ops cadence | `ai-lead-ops` |

## Core Workflows

### 1. Research framing (safety)

Hypotheses, harm taxonomy, success metrics.

**See `references/research_framing_safety.md`.**

### 2. Benchmarks and datasets

Golden sets, labeling, versioning.

**See `references/safety_benchmarks_datasets.md`.**

### 3. Model development

Training, fine-tuning, ensembles.

**See `references/classifier_model_development.md`.**

### 4. Evaluation and metrics

Slices, calibration, error analysis.

**See `references/evaluation_metrics_analysis.md`.**

### 5. Ablations and experiments

Controls, reproducibility.

**See `references/ablation_experiment_design.md`.**

### 6. Handoff to production

Promotion criteria, monitoring hooks.

**See `references/research_to_production_handoff.md`.**

## Outputs

- **Research brief** — question, baseline, hypothesis, metrics
- **Dataset card** — sources, label schema, known limitations
- **Benchmark spec** — cases, categories, pass/fail rubric
- **Results table** — metrics by slice with confidence intervals where possible
- **Error analysis** — representative FP/FN clusters
- **Promotion recommendation** — go/no-go vs current production classifier

## Principles

- **Measure what policy cares about** — category-level recall on high-severity harms
- **Report failures honestly** — FPs hurt UX; FNs hurt safety
- **Hold out adversarial refresh** — do not train on the only test set
- **Reproducible** — seeds, data version, model hash, eval script
- **Separate research from ops** — research proves lift; infra ships it
