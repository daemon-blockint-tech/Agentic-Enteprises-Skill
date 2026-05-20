# Defenses and mitigations

## Table of contents

1. [Defense layers](#defense-layers)
2. [Training-time](#training-time)
3. [Inference-time](#inference-time)
4. [Data and pipeline](#data-and-pipeline)
5. [Residual risk](#residual-risk)

## Defense layers

Prefer **defense in depth** — document which layer catches which attack class:

```
Input sanitize → Detector → Robust model → Output policy → Monitor
```

No layer is sufficient alone against adaptive attackers.

## Training-time

| Technique | Targets | Engineering notes |
|---|---|---|
| **Adversarial training** | Evasion | PGD/FGSM inner loop; monitor clean-acc tradeoff |
| **TRADES / MART** | Robustness-accuracy tradeoff | Tune β; validate on holdout attacks |
| **Certified methods** | Provable L2/L∞ bounds | Often costly; document radius vs deploy norm |
| **Poisoning defenses** | Data poisoning | Outlier removal, robust losses, provenance checks |
| **Differential privacy** | Membership inference | Privacy-utility tradeoff — pair with `privacy-research-engineer-safeguards` |

Track **robust overfitting** — robust val gap vs clean val gap.

## Inference-time

| Technique | Targets | Engineering notes |
|---|---|---|
| **Input sanitization** | Perturbations, typos | JPEG, bit-depth, clipping, spell-normalize |
| **Randomized smoothing** | Certified inference | Multiple noise samples — latency cost |
| **Detector networks** | Adversarial inputs | Train on neg+adv; watch false positives on OOD |
| **Ensembles** | Evasion, extraction | Diversity (architecture, data); aggregation rules |
| **Temperature / rejection** | Low-confidence attacks | Abstain path for human review |
| **Rate limits & auth** | Query extraction | Per-key quotas; watermark outputs if applicable |

Align runtime policies with `ml-infrastructure-engineer-safeguards` for gateway placement.

## Data and pipeline

- **Provenance**: signed datasets, immutable version IDs, anomaly scans on new shards
- **Label audit**: spot-check high-loss points; trigger-based review for poison patterns
- **Supply chain**: verify pretrained weights checksums; scan for suspicious layers
- **Retrain gates**: block promotion if ASR regresses beyond threshold on golden attacks

## Residual risk

Document explicitly:

- Adaptive attacks not evaluated
- Transfer from surrogate models untested
- Distribution shift between benchmark and production
- Cost/latency of defenses under peak load

Recommend **monitoring** hooks in `production_guardrails_and_monitoring.md`.
