# Ablation and experiment design

## Table of contents

1. [Controls](#controls)
2. [Ablation matrix](#ablation-matrix)
3. [Reproducibility](#reproducibility)
4. [Stopping rules](#stopping-rules)

## Controls

One change at a time unless factorial design is intentional:

| Knob | Examples |
|---|---|
| Data | +adversarial slice, -synthetic, relabel v2 |
| Model | backbone size, multi-task heads |
| Training | LR, epochs, class weights |
| Inference | threshold, ensemble, cascade depth |
| Prompt (judge) | rubric v1 vs v2 |

Fixed across ablations: eval sets, random seed policy, hardware class.

## Ablation matrix

Example table for memo:

| Run | Change | Recall@FP=1% | FP rate @τ | Latency ms |
|---|---|---|---|---|
| A0 | Production | | | |
| A1 | +data X | | | |
| A2 | A1 + larger model | | | |

Mark **Pareto improvements** — better safety metric without latency regression.

## Reproducibility

Checklist:

- [ ] Data version pinned
- [ ] Code commit hash
- [ ] Training config YAML archived
- [ ] Eval script version
- [ ] Model artifact checksum
- [ ] Results JSON in artifact store

Enable another researcher to re-run eval without retraining.

## Stopping rules

Pre-register:

- Minimum lift on primary metric to pursue promotion
- Maximum acceptable FP regression on benign hard set
- Maximum latency increase for infra

Stop early if **critical FN** appears on golden set in mid-training checkpoint.
