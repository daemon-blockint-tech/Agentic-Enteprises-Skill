# Classification and Propensity

## Table of contents

1. [Propensity vs classification](#propensity-vs-classification)
2. [Scores, ranks, and probabilities](#scores-ranks-and-probabilities)
3. [Calibration](#calibration)
4. [Threshold selection](#threshold-selection)
5. [Cost-sensitive decisions](#cost-sensitive-decisions)
6. [Capacity and workflow constraints](#capacity-and-workflow-constraints)
7. [Segmentation and stability](#segmentation-and-stability)
8. [Common use-case patterns](#common-use-case-patterns)

## Propensity vs classification

| Term | Meaning |
|---|---|
| **Propensity model** | Estimates likelihood of an action (buy, upgrade, churn) |
| **Classification model** | Assigns a discrete class; may use propensity + threshold |

Propensity models often feed **ranking** (who to contact first). Classification adds an **operating point** (approve/deny, flag/review).

## Scores, ranks, and probabilities

- **Raw score** (logit, margin): Good for ranking if monotonic; not calibrated.
- **Probability**: Needed for expected value, budgeting, and some compliance reviews.
- **Decile lift**: Compares top decile event rate to population rate—easy for stakeholders.

Report which output production will consume.

## Calibration

Uncalibrated models can rank well but misstate risk.

| Method | When |
|---|---|
| Platt scaling | Smaller data; logistic on validation scores |
| Isotonic regression | Larger validation sets; flexible but can overfit small val |
| Beta calibration | Alternative for skewed scores |

Evaluate with **reliability diagrams** and **Brier score** on a calibration holdout—not the same fold used for threshold tuning if possible.

## Threshold selection

Do **not** default to 0.5. Choose thresholds by:

1. **Cost matrix** (FP vs FN costs in business units)
2. **Capacity** (max reviews, calls, or approvals per day)
3. **Target precision** (fraud: “at 95% precision, what recall?”)
4. **Top-k** policy (contact best 5% of list)

Document the **expected confusion matrix** at the chosen point and sensitivity to ±0.05 score shift.

## Cost-sensitive decisions

Example framing:

```
Expected value = P(positive) * benefit_true_positive
               - P(false positive) * cost_false_positive
               - action_cost
```

When costs are unknown, present **threshold curves**: precision/recall, lift, and workload vs cutoff.

For fraud and compliance queues, pair with `anti-false-positive-decision-making` when alert volume and evidence bars matter.

## Capacity and workflow constraints

| Constraint | Modeling implication |
|---|---|
| Fixed review team | Optimize precision@k or top-N daily |
| SLA on latency | Prefer simpler models; limit feature fan-out |
| Tiered treatment | Multiple thresholds (auto-approve / manual / deny) |
| Human-in-the-loop | Model ranks; policy applies overrides |

Separate **model evaluation** from **operating policy** in documentation.

## Segmentation and stability

Report metrics by:

- Acquisition cohort, tenure band, product, geography
- Time (train period vs recent holdout month)
- Score decile stability (do top deciles stay top?)

Investigate **simpson’s paradox** slices where global metrics hide failure modes.

## Common use-case patterns

| Use case | Target tips | Metric emphasis |
|---|---|---|
| Churn | Define inactive; handle win-back | PR-AUC, recall@k for save offers |
| Upsell / cross-sell | Eligibility filters on negatives | Lift@k, incremental lift vs control if available |
| Lead scoring | Deduplicate leads; time-decay features | Precision@k for SDR capacity |
| Fraud | Delayed labels; extreme imbalance | Precision at operational review rate |
| Risk tiering (non-actuarial) | Document fair lending / ECOA review path | Ranking + calibration + adverse action inputs (process, not legal advice) |

For experiment-based validation of treatments, route to `ab-testing-engineer`—do not confuse model lift with campaign lift.
