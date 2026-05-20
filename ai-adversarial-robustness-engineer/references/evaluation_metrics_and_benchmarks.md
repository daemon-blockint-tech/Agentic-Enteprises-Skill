# Evaluation metrics and benchmarks

## Table of contents

1. [Core metrics](#core-metrics)
2. [Perturbation budgets](#perturbation-budgets)
3. [Benchmark selection](#benchmark-selection)
4. [Reporting standards](#reporting-standards)

## Core metrics

| Metric | Definition | Use |
|---|---|---|
| **Clean accuracy** | Performance on unperturbed holdout | Guardrail — defenses must not collapse utility |
| **ASR** | Attack success rate under defined budget | Primary robustness comparison |
| **Robust accuracy** | Accuracy on adversarially perturbed inputs | Single-number summary when attacks are diverse |
| **Query count** | Queries to reach success (black-box) | API abuse and extraction risk |
| **Certified radius** | Provable bound (e.g., randomized smoothing) | Supplementary — state assumptions and tightness |

Always report **confidence intervals** or multiple seeds for stochastic attacks.

## Perturbation budgets

Fix budgets **before** running campaigns:

| Modality | Common budgets |
|---|---|
| Images | L∞ ε ∈ {2/255, 4/255, 8/255}; L2 ball radius |
| Tabular | Feature-wise ε as fraction of scale |
| Text/LLM | Edit distance, synonym swaps, char insertions, token budget |
| Audio | SNR floor, max L∞ on spectrogram |

Document **threat model mismatch** if production inputs differ from benchmark norms.

## Benchmark selection

| Domain | Examples (illustrative) |
|---|---|
| Vision | CIFAR-10/100 robust sets, ImageNet-C, AutoAttack suite |
| Tabular | Custom slices with domain-valid perturbations |
| LLM | Adversarial prompt suites, jailbreak-adjacent **robustness** sets (not policy harm alone) |
| Retrieval | Poisoned-doc corpora, ranking manipulation sets |

Build **internal golden sets** from production failure clusters; version with dataset cards.

Regression harness: every model release runs **fixed attack seed + budget** against champion.

## Reporting standards

Include in every robustness report:

1. Model ID, data version, attack library version
2. Budget table and attack list (FGSM/PGD/AutoAttack/…)
3. ASR and clean accuracy — overall and **slices** (class, locale, modality)
4. Representative **failure examples** (inputs, perturbations, outputs)
5. Comparison to **baseline** and previous release
6. Known gaps — adaptive attacks not run, transferability untested

Coordinate harm-category metrics with `ml-research-engineer-safeguards` when eval overlaps moderation.
