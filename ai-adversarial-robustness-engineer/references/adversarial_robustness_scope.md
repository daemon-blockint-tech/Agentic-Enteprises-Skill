# Adversarial robustness scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [In-scope systems](#in-scope-systems)
3. [Lifecycle coverage](#lifecycle-coverage)
4. [Engagement checklist](#engagement-checklist)

## Role boundary

Own **engineering robustness** against adversarial ML threats:

| Own | Partner skill |
|---|---|
| Threat models for ML attacks | `ai-redteam` — LLM app policy, jailbreak ROE |
| Robust training and eval harnesses | `ml-research-engineer-safeguards` — classifier R&D |
| Dataset/pipeline integrity checks | `devsecops` — CI/CD and artifact signing |
| Deployment input/output guardrails | `ml-infrastructure-engineer-safeguards` — serving path |
| Governance artifacts | `ai-risk-governance` — risk tiers, model cards |

## In-scope systems

| System type | Typical robustness work |
|---|---|
| Classical ML | Image/tabular/audio evasion, poisoning, model extraction |
| Deep learning APIs | Gradient-based or query-based attacks on endpoints |
| LLM / multimodal | Perturbation of prompts/images, tool-output manipulation, indirect triggers |
| Retrieval-augmented | Poisoned documents, embedding attacks, ranking manipulation |
| Fine-tuned adapters | LoRA/backdoor checks, adapter swap integrity |

Out of scope: pure application OWASP testing without model surface (`web-pentester`).

## Lifecycle coverage

```
Data ingest → Train/fine-tune → Eval → Deploy → Monitor
     │              │            │        │         │
  poisoning      backdoors    ASR/slices  I/O     drift/ASR
  supply chain   robust train  benchmarks  guards  alerts
```

Document **which stages** are in scope for each engagement.

## Engagement checklist

- [ ] Written authorization and environment (lab/staging/prod exception documented)
- [ ] Model version, weights hash, and config frozen for eval
- [ ] Attack budget defined (L∞/L2 norm, query count, token budget)
- [ ] Success metrics pre-registered (ASR threshold, slice floors)
- [ ] Out-of-scope: customer PII, destructive load, social engineering (unless `ai-redteam`)
- [ ] Handoff owners for infra guardrails and governance sign-off identified
