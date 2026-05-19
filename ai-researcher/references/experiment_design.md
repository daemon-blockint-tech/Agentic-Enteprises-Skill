# Experiment design

## Table of contents

1. [Reproducibility checklist](#reproducibility-checklist)
2. [Leakage checks](#leakage-checks)

## Reproducibility checklist

- [ ] Random seeds recorded
- [ ] Data version / hash
- [ ] Code commit SHA
- [ ] Hyperparameters logged
- [ ] Hardware noted for timing claims

## Leakage checks

- No test labels in feature engineering
- Temporal splits for time-series
- Deduplicate near-duplicate train/test examples
