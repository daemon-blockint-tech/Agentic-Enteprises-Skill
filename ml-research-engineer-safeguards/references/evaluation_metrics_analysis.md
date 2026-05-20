# Evaluation and metrics analysis

## Table of contents

1. [Confusion matrix by category](#confusion-matrix-by-category)
2. [Slice analysis](#slice-analysis)
3. [Calibration](#calibration)
4. [Error analysis](#error-analysis)
5. [Statistical caution](#statistical-caution)

## Confusion matrix by category

Report per category:

| | Pred + | Pred - |
|---|---|---|
| Actual + | TP | FN |
| Actual - | FP | TN |

Highlight **FN** on critical categories first in executive summary.

## Slice analysis

Mandatory slices where data allows:

- Language / locale
- Attack type (direct, encoded, indirect injection)
- Prompt vs response classification
- Tenant tier (consumer vs enterprise)
- Content length buckets

Flag **regressions on any slice** even if global metric improves.

## Calibration

- Reliability diagram or ECE on validation
- Choose threshold per category to hit target FP or FN rate
- Document sensitivity — small τ change → large block rate swing

Provide **recommended τ table** for infra config.

## Error analysis

Sample 20–50 each:

- False positives — benign blocked; cluster themes
- False negatives — harmful missed; attack pattern

Qualitative tags feed next data collection and `ai-redteam` focus areas.

## Statistical caution

- Report confidence intervals on small sets
- Multiple comparisons — avoid cherry-picked slices
- Do not claim significance without adequate N
- Compare models on **same** eval version

For classical tests on proportions → coordinate with `data-scientist` if needed.
