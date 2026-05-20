---
name: ai-adversarial-robustness-engineer
description: |
  Adversarial robustness engineering for ML/AI—evasion, poisoning, extraction, membership-inference
  threat models; robust training, sanitization, detectors; ASR/certified evals; lab model attacks;
  data-pipeline integrity; production I/O guardrails (classical ML and LLM/multimodal). Use for
  adversarial examples, robustness suites, poison audits, deploy guardrails—not LLM app red team
  (ai-redteam), governance (ai-risk-governance), safety classifier R&D (ml-research-engineer-safeguards),
  safeguard serving (ml-infrastructure-engineer-safeguards), privacy research
  (privacy-research-engineer-safeguards), AppSec pentest (penetration-tester).
---

# AI Adversarial Robustness Engineer

## When to Use

- Define **threat models** for evasion, poisoning, extraction, and inference attacks on ML/LLM systems
- Design **robustness evaluation** suites — ASR, perturbation budgets, slice metrics, regression harnesses
- Implement **engineering defenses** — adversarial training, input sanitization, detectors, ensembles
- Run **lab/staging attack campaigns** on model endpoints, APIs, or batch inference (authorized only)
- Audit **training data and pipelines** for poisoning, backdoors, and supply-chain tampering
- Specify **production guardrails** — input validation, output filtering, rate limits, anomaly monitors
- Compare **certified vs empirical** robustness claims and document limitations for stakeholders
- Investigate **robustness regressions** after model updates, fine-tunes, or data refreshes

## When NOT to Use

- Broad LLM product red-team engagements, jailbreak policy, or ROE → `ai-redteam`
- AI governance, risk tiers, model cards, or compliance mapping → `ai-risk-governance`
- Safety classifier research, harm benchmarks, and moderation model training → `ml-research-engineer-safeguards`
- Safeguard gateways, GPU serving, canary routing, and inference SLOs → `ml-infrastructure-engineer-safeguards`
- PII, memorization, and privacy leakage research → `privacy-research-engineer-safeguards`
- Building production RAG/agents or LLM features → `ai-engineer`
- General literature survey without robustness scope → `ai-researcher`
- Network/web/AppSec penetration testing (non-model) → `penetration-tester`, `web-pentester`

## Related skills

| Need | Skill |
|---|---|
| LLM jailbreak and app-surface red team | `ai-redteam` |
| Governance sign-off and risk tiers | `ai-risk-governance` |
| Safety classifier R&D and harm evals | `ml-research-engineer-safeguards` |
| Production safeguard serving path | `ml-infrastructure-engineer-safeguards` |
| Privacy and extraction research | `privacy-research-engineer-safeguards` |
| Production LLM/RAG implementation | `ai-engineer` |
| General ML research methodology | `ai-researcher` |
| Pipeline and artifact security | `devsecops` |

## Core Workflows

### 1. Scope and threat model

1. Identify assets: weights, embeddings, training data, inference API, logs
2. Classify attacker goals and capabilities (white/gray/black box, budget, offline/online)
3. Map attacks to lifecycle stage (data, train, deploy, monitor)
4. Agree evaluation environment — no prod customer data without approval

**See `references/adversarial_robustness_scope.md`.**

### 2. Attack taxonomy and scenarios

Document evasion, poisoning, extraction, and inference threats with realistic preconditions.

**See `references/threat_models_and_attack_taxonomy.md`.**

### 3. Metrics and benchmarks

Select perturbation norms, ASR definitions, slices, and baselines; pre-register pass/fail gates.

**See `references/evaluation_metrics_and_benchmarks.md`.**

### 4. Defenses and mitigations

Choose layered controls: robust training, preprocessing, detectors, ensembles, and operational limits.

**See `references/defenses_and_mitigations.md`.**

### 5. Red-team campaigns on models

Plan authorized attacks in lab/staging; capture reproduction packages and severity.

**See `references/red_team_campaigns_on_models.md`.**

### 6. Production guardrails and monitoring

Translate findings into input/output policies, drift monitors, and incident playbooks.

**See `references/production_guardrails_and_monitoring.md`.**

## Outputs

- **Threat model** — assets, adversaries, attack paths, assumptions
- **Robustness eval spec** — datasets, budgets, metrics, baselines, acceptance criteria
- **Results report** — ASR/slice tables, representative failures, confidence limits
- **Defense plan** — prioritized mitigations with residual risk
- **Campaign log** — authorized tests, payloads, reproduction steps (lab/staging)
- **Guardrail spec** — validation rules, monitors, rollback triggers

## Principles

- **Authorized testing only** — written scope; never attack production without approval
- **Empirical over claims** — measure ASR and slices; treat certified bounds as supplementary
- **Defense in depth** — no single control; combine model, input, and operational layers
- **Reproducibility** — version data, model hash, attack code, and random seeds
- **Honest limits** — document threat-model mismatch and adaptive attackers
