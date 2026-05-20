# Threat models and attack taxonomy

## Table of contents

1. [Adversary capabilities](#adversary-capabilities)
2. [Attack classes](#attack-classes)
3. [LLM-specific notes](#llm-specific-notes)
4. [Threat-model template](#threat-model-template)

## Adversary capabilities

| Dimension | Options |
|---|---|
| Knowledge | White-box (gradients), gray-box (surrogate), black-box (queries only) |
| Access | Offline data, training API, inference API, batch export, physical sensor |
| Goal | Misclassification, availability, steal model, infer membership, insert backdoor |
| Budget | Perturbation norm, query count, compute time, social cost |

State assumptions explicitly — robustness claims are **conditional** on them.

## Attack classes

| Class | Objective | Examples |
|---|---|---|
| **Evasion** | Wrong prediction at inference | FGSM, PGD, C&W, patch attacks, universal perturbations |
| **Poisoning** | Degrade or backdoor via training data | label flip, clean-label, trigger patches, trojan weights |
| **Model stealing** | Replicate decision boundary | query synthesis, knockoff training, API extraction |
| **Membership inference** | Infer record was in training set | shadow models, loss thresholds |
| **Privacy extraction** | Recover training snippets | memorization probes (coordinate with `privacy-research-engineer-safeguards`) |
| **Availability** | Deny service or burn cost | sponge examples, adversarial queries, token exhaustion |

Map each class to **detection** and **mitigation** owners in the defense plan.

## LLM-specific notes

| Vector | Robustness angle |
|---|---|
| Prompt perturbation | Typos, homoglyphs, tokenization splits — measure ASR on intent |
| Multimodal | Adversarial patches on images paired with benign text |
| Indirect injection | Poisoned RAG chunks — data pipeline integrity, not prompt policy alone |
| Tool misuse | Parameter fuzzing on tool schemas — overlaps `ai-redteam` for app ROE |
| Fine-tune surface | Poisoned SFT rows, adapter backdoors — dataset audits |

Distinguish **model robustness** from **product safety policy** (`ai-redteam`, `ml-research-engineer-safeguards`).

## Threat-model template

```markdown
## Assets
- Model weights / API / training set / embeddings

## Adversaries
- Capability matrix (knowledge, access, budget)

## Attack paths
1. [Stage] → [Attack] → [Impact]

## Assumptions
- What defender controls (preprocessing, monitoring, retrain cadence)

## Out of scope
- ...

## Metrics
- Primary: ASR @ ε, clean accuracy floor
- Slices: ...
```
