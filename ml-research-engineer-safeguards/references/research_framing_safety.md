# Research framing (safety)

## Table of contents

1. [Harm taxonomy](#harm-taxonomy)
2. [Hypothesis templates](#hypothesis-templates)
3. [Metrics selection](#metrics-selection)
4. [Baselines](#baselines)

## Harm taxonomy

Align categories with **policy** (`ai-risk-governance`) but own the ML mapping:

| Layer | Examples |
|---|---|
| Severity | Critical / high / medium / low |
| Category | Hate, violence, sexual, self-harm, illegal, PII, injection |
| Modality | Text, image, tool output, multi-turn |
| Context | User prompt vs model response vs retrieved chunk |

Document **overlap rules** — when multiple labels apply, primary label for metrics.

## Hypothesis templates

- "Fine-tuning on **dataset X** improves recall on category Y at fixed FP rate vs baseline B"
- "Ensemble of **small classifier + LLM judge** reduces FNs on jailbreak slice Z vs classifier alone"
- "Threshold **τ** calibrated on validation minimizes cost function C(FP, FN) for tier T"

Each hypothesis must be **falsifiable** with a pre-registered eval set.

## Metrics selection

| Metric | When |
|---|---|
| Recall @ fixed FP | Safety-critical categories |
| Precision @ fixed recall | UX-sensitive categories |
| AUROC / PR-AUC | Model selection, not policy sign-off alone |
| Calibration (ECE) | Threshold setting in production |
| Latency / cost per classification | Feasibility for infra path |

Define **primary** and **guardrail** metrics before running experiments.

## Baselines

Always compare against:

1. **Current production** classifier (same eval set)
2. **Simple baseline** — keyword, regex, or vendor API
3. **Previous research champion** — last promoted model

Note **data leakage** if baseline was trained on overlapping data.
