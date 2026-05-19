# Experiment design and ablations

## Table of contents

1. [Baseline ladder](#baseline-ladder)
2. [Ablation matrix](#ablation-matrix)
3. [Sweeps and power](#sweeps-and-power)
4. [Stopping and preregistration](#stopping-and-preregistration)

## Baseline ladder

Always include:

1. **Current production** — realistic stack
2. **Simple strong** — full context, best model (upper bound quality)
3. **Naive cheap** — smallest model / truncate tail (lower bound)
4. **Proposed** — method under test

Avoid comparing only to a weak baseline.

## Ablation matrix

Example for context compression study:

| Arm | System | History | Retrieval | Tools |
|---|---|---|---|---|
| A0 | Full | Full | Full | Full |
| A1 | +compress history | Compressed | Full | Full |
| A2 | +compress retrieval | Full | Top-k halved | Full |
| A3 | +both | Compressed | Reduced | Full |

Change **one family** per ablation wave; combine only after singles validated.

## Sweeps and power

- Grid: context cap {4k, 8k, 16k, 32k}
- Grid: compression ratio {0.25, 0.5, 0.75}
- Use **paired** comparisons on same queries when possible
- Estimate CI via bootstrap over eval items
- Minimum n: justify from pilot variance (e.g., 200+ tasks for 2% pass rate shifts)

## Stopping and preregistration

Pre-register:

- Primary metric and direction
- Minimum effect size of interest (δ)
- Max spend (GPU hours or $)
- Early stop rule (only if planned; adjust for multiple testing)

Do not stop at best-looking interim slice without correction.

Record **negative results** — methods that saved tokens but broke quality.
