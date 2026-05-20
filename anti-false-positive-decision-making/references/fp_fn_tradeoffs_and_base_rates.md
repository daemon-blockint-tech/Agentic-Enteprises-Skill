# FP/FN trade-offs and base rates

## Table of contents

1. [Definitions](#definitions)
2. [Why base rate matters](#why-base-rate-matters)
3. [Cost asymmetry](#cost-asymmetry)
4. [Operating points](#operating-points)
5. [Segmentation](#segmentation)
6. [Bayesian intuition (practical)](#bayesian-intuition-practical)
7. [Worksheet](#worksheet)
8. [Common mistakes](#common-mistakes)

## Definitions

| Term | Meaning |
|---|---|
| **True positive (TP)** | Signal fires; harmful condition truly present |
| **False positive (FP)** | Signal fires; condition absent—unnecessary action |
| **False negative (FN)** | Harmful condition present; signal silent |
| **True negative (TN)** | No signal; condition absent |
| **Precision** | TP / (TP + FP) — trust when alert fires |
| **Recall (sensitivity)** | TP / (TP + FN) — catch rate |
| **False discovery rate (FDR)** | FP / (TP + FP) — same denominator as 1 − precision |

In high-stakes workflows, **precision at disposition** (after analyst review) often matters more than raw rule precision.

## Why base rate matters

**Base rate** (prevalence): fraction of the population that truly has the condition.

When prevalence is **low**, even a highly specific rule can produce **mostly false positives** among alerts:

- Example: 0.1% fraud rate, rule with 99% specificity on random population still yields ~90% FPs among alerts if sensitivity forces volume (illustrative—always model with your data).

**Never** judge a rule only by “we get 10,000 alerts/month” without prevalence and disposition outcomes.

## Cost asymmetry

Build a **cost matrix** before moving thresholds:

| | Predicted positive | Predicted negative |
|---|---|---|
| **Actually positive** | Benefit of catch | Cost of miss (FN) |
| **Actually negative** | Cost of FP | Cost of TN (usually low) |

FP costs to enumerate:

- Customer churn, support load, wrongful freeze
- Analyst hours × fully loaded rate
- Reputation and regulatory complaints
- Opportunity cost (delayed wire, failed checkout)

FN costs to enumerate:

- Direct loss, breach impact, fine exposure
- Safety harm, sanctions exposure

**Risk appetite** states which cell the org will tolerate more of, **by segment**.

## Operating points

Threshold selection is choosing an **operating point** on a precision–recall curve (or ROC for scores):

| Move | Typical effect |
|---|---|
| **Raise bar** (stricter) | ↑ precision, ↓ recall, fewer alerts |
| **Lower bar** (looser) | ↓ precision, ↑ recall, more alerts |

Document the **intended move** in every tuning packet:

- “Reduce FP on retail wires by 30% at acceptable 5% recall drop”
- Not “reduce alerts” without FN review

## Segmentation

Global thresholds fail when subpopulations differ:

| Segment | Often lower base rate | FP cost | FN cost |
|---|---|---|---|
| New users | Unknown | Medium | High fraud |
| Established low-risk | Very low | High (trust) | Medium |
| High-value corporate | Low | Very high | Very high |
| Sanctions geography | Varies | Regulatory | Critical |

Use **segment-specific** thresholds and evidence bars where policy allows; document exceptions.

## Bayesian intuition (practical)

After an alert fires, ask:

> **Given this evidence, what is the posterior probability of true harm?**

Operational proxies:

- **Single weak feature** → low posterior → Tier 1–2 only
- **Multiple independent features** → higher posterior → Tier 3
- **Human-confirmed pattern** → may justify Tier 4 with approvals

You do not need formal Bayes in production if you enforce **independent corroboration** and **calibration sampling**.

## Worksheet

Copy for each decision class:

```
Decision class: _______________
Population size (monthly): _______________
Estimated prevalence (band): ___% to ___%
Current alerts/month: _______________
Disposition TP / FP / FN (last 90d): ___ / ___ / ___
Estimated cost per FP: $________
Estimated cost per FN: $________
Target precision at disposition: ___%
Minimum acceptable recall: ___%
Approved operating point change: _______________
Approver: _______________  Date: _______________
```

## Common mistakes

| Mistake | Fix |
|---|---|
| “99% accurate model” without prevalence | Model accuracy on imbalanced data misleads; use precision/recall at operating point |
| Optimizing recall only after an FN headline | Pair with FP impact review and tiered response |
| Using training metrics in production | Track **production** disposition labels with lag correction |
| Ignoring selection bias | Analysts only see alerts—FNs require separate sampling |
| Same threshold for batch and real-time | Real-time may need higher bar or softer tier |

## Review triggers

Revisit trade-offs when:

- Product or geography launch changes population mix
- Adversary adapts (sudden FN spike)
- Regulatory feedback on over-blocking
- Major vendor or model change
- FP cost event (public complaint, executive escalation)
