---
name: privacy-research-engineer-safeguards
description: |
  Guides privacy research engineering for safeguards—PII and sensitive-data detection research,
  redaction and de-identification evals, memorization and extraction risk studies, privacy
  benchmarks and labeled corpora, logging/retention minimization for safety pipelines, and
  research memos on privacy–utility trade-offs for guardrail systems.
  Use when measuring PII detector quality, designing privacy eval suites for moderation stacks,
  studying training-data leakage or prompt logging risk, or recommending privacy mitigations for
  safeguard models—not for SOC 2/GDPR evidence automation (compliance-engineer), legal DPIA or AI
  policy (ai-risk-governance), harm/toxicity classifier R&D (ml-research-engineer-safeguards),
  production inference gateways (ml-infrastructure-engineer-safeguards), or general non-privacy
  research (ai-researcher).
---

# Privacy Research Engineer, Safeguards

## When to Use

- Frame **privacy research questions** for safeguard and moderation stacks
- Design **PII detection/redaction benchmarks** — precision/recall, re-identification risk
- Evaluate **de-identification** techniques (mask, tokenize, synthetic replace) on realistic prompts
- Study **memorization and extraction** — can models or logs leak user content?
- Curate **privacy-sensitive datasets** — synthetic data, consent boundaries, labeling rules
- Run **ablations** on detector architecture, threshold, or post-processing
- Define **logging minimization** — what safety systems may store vs must discard
- Write **research memos** with privacy–utility trade-offs and production recommendations
- Specify **promotion criteria** for privacy mitigations before prod rollout

## When NOT to Use

- Audit evidence pipelines for GDPR/SOC 2 attestations → `compliance-engineer`
- Legal DPIA, acceptable-use policy, regulatory mapping → `ai-risk-governance`
- Harm categories, jailbreak benchmarks, toxic classifiers → `ml-research-engineer-safeguards`
- Deploy gateways, canaries, safety-path SLOs → `ml-infrastructure-engineer-safeguards`
- Red-team attack campaigns → `ai-redteam`
- Enterprise data governance architecture → `data-architect`
- Human-data platform product ethics (contributor labor) → `product-management-human-data-platform`
- General literature review unrelated to privacy in ML → `ai-researcher`

## Related skills

| Need | Skill |
|---|---|
| Safety classifier research | `ml-research-engineer-safeguards` |
| Safeguard production infra | `ml-infrastructure-engineer-safeguards` |
| AI governance and DPIA framing | `ai-risk-governance` |
| Compliance controls and evidence | `compliance-engineer` |
| Data classification and lineage | `data-architect` |
| Adversarial extraction testing | `ai-redteam` |
| General research methods | `ai-researcher` |
| Human-data platform privacy | `product-management-human-data-platform` |
| Release and incident ops | `ai-lead-ops` |

## Core Workflows

### 1. Privacy research framing

Threat model, metrics, baselines.

**See `references/privacy_research_framing.md`.**

### 2. PII detection and redaction research

Detectors, redaction quality, evals.

**See `references/pii_detection_redaction_research.md`.**

### 3. Memorization and extraction

Leakage studies, attack surfaces.

**See `references/memorization_and_extraction.md`.**

### 4. Privacy benchmarks and datasets

Corpora, labeling, versioning.

**See `references/privacy_benchmarks_datasets.md`.**

### 5. Logging and retention minimization

Safety observability without over-collection.

**See `references/logging_retention_minimization.md`.**

### 6. Handoff to production

Promotion bar, monitoring hooks.

**See `references/privacy_to_production_handoff.md`.**

## Outputs

- **Threat model** — assets, adversaries, failure modes for privacy in safeguards
- **Benchmark spec** — PII types, locales, adversarial variants
- **Results table** — detection/redaction metrics by slice (language, format)
- **Leakage study report** — methodology, findings, confidence
- **Logging policy draft** — fields allowed, TTL, access controls (engineering input to legal)
- **Promotion recommendation** — go/no-go with privacy–utility summary

## Principles

- **Minimize data** — collect and retain only what eval and ops truly need
- **Separate privacy from safety metrics** — low PII leak rate is not interchangeable with low toxicity FN
- **Locale and format matter** — email in one language ≠ global PII detector
- **Synthetic ≠ risk-free** — synthetic PII can still encode patterns; document limits
- **Legal review for human data** — research plans involving real user content need governance sign-off
