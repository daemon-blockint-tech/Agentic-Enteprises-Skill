# Classifier model development

## Table of contents

1. [Model families](#model-families)
2. [Training workflow](#training-workflow)
3. [LLM-as-judge](#llm-as-judge)
4. [Ensembles](#ensembles)
5. [Constraints](#constraints)

## Model families

| Family | Trade-off |
|---|---|
| Small encoder (BERT-class) | Fast, cheap; may miss nuance |
| Multi-label heads | One backbone, per-category logits |
| Generative judge (LLM) | Flexible rubric; slower, costlier |
| Multimodal encoder | Image + text safety |

Pick based on **latency budget** from `ml-infrastructure-engineer-safeguards`.

## Training workflow

1. Split data — stratified by category; no user leakage across splits
2. Train with class weights if imbalance
3. Validate on **held-out** set + frozen golden benchmark
4. Calibrate thresholds on validation only
5. Export artifact — weights, tokenizer, config, eval report

Log experiment: data version, hyperparameters, git SHA, metrics.

## LLM-as-judge

When using LLM judges:

- Fixed rubric prompt version
- Temperature 0 for scoring
- Parse structured output (JSON schema)
- Measure **judge stability** — repeat labels on subset
- Cost and latency estimate for prod path

Not a substitute for human eval on high-severity launches.

## Ensembles

- Vote or score fusion across models
- Cascade: cheap model first, expensive on uncertain band
- Document **uncertainty band** — route to human review

Ablate ensemble vs single model on same eval (`ablation_experiment_design.md`).

## Constraints

- No training on **test-only** adversarial sets
- PII handling in training pipelines
- Model size limits for edge deployment
- Document failure modes for model card (`ai-risk-governance`)
