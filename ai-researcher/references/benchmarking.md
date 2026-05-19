# Benchmarking

## Table of contents

1. [Leaderboard caveats](#leaderboard-caveats)
2. [Custom eval sets](#custom-eval-sets)

## Leaderboard caveats

- Test set contamination in pretraining
- Tuning budget unfairness
- Metric gaming (format tricks)

## Custom eval sets

Build domain-specific eval from:

- Production failure samples (redacted)
- SME-authored gold Q&A
- Adversarial cases from `ai-redteam` (sanitized)

Report mean, variance, and worst decile.
