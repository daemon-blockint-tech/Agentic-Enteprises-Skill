# Sample Size, Power, and Duration

## Table of contents

1. [Core parameters](#core-parameters)
2. [MDE and business alignment](#mde-and-business-alignment)
3. [Sample size (proportions)](#sample-size-proportions)
4. [Sample size (continuous)](#sample-size-continuous)
5. [Multiple variants](#multiple-variants)
6. [Duration and seasonality](#duration-and-seasonality)
7. [Allocation and traffic](#allocation-and-traffic)
8. [Worked example checklist](#worked-example-checklist)

## Core parameters

| Symbol | Typical default | Notes |
|---|---|---|
| α (alpha) | 0.05 | False positive rate; one- or two-sided pre-specified |
| Power (1−β) | 0.80 (0.90 for high-stakes) | Probability of detecting true effect ≥ MDE |
| MDE | Business-driven | Smallest effect worth detecting |
| Baseline rate / mean | Historical data | Use recent, stable window |
| Variants | k | Inflates total traffic need |

**Document all assumptions** in the experiment brief; revisit if baseline shifts during run.

## MDE and business alignment

MDE should answer: *"If we only detect a change this large, is the experiment still worth it?"*

```
Expected annual impact ≈ (detectable lift) × (eligible users/year) × (value per user)
```

If required N exceeds available traffic within acceptable calendar time:

- Increase MDE (accept smaller detectable effect only if business agrees)
- Lengthen runtime (seasonality permitting)
- Narrow population
- Use variance reduction (CUPED, stratification)—coordinate with `data-scientist`

Do **not** silently lower power below 0.8 without stakeholder sign-off.

## Sample size (proportions)

For conversion-style metrics (Bernoulli):

- Inputs: baseline rate `p`, absolute or relative MDE, α, power
- Per-group N increases as `p` approaches 0.5 and as MDE shrinks

**Relative vs absolute MDE:**

- Relative: 5% lift on 10% baseline → 10.5% absolute
- State which definition was used in the memo

Use a standard calculator or library (`statsmodels`, Evan Miller calculator) and **paste inputs** into registry.

## Sample size (continuous)

For means (revenue per user, session length):

- Need baseline mean and **standard deviation** (or variance of user-level metric)
- Heavy-tailed metrics (revenue): consider winsorization policy in analysis plan
- Log transform or bootstrap analysis—pre-specify

Ratio metrics (clicks/views): treat carefully; consult statistician or `data-scientist` for delta-method/bootstrap plan.

## Multiple variants

For **k** treatment arms + control:

- Total sample often scales with number of comparisons of interest
- Pre-specify: test each vs control (k tests) vs best vs control (different multiplicity)
- Apply **multiplicity adjustment** in analysis plan (Bonferroni, Holm, FDR)

Power **all** comparisons you will report as wins.

## Duration and seasonality

Minimum runtime should cover:

| Factor | Guidance |
|---|---|
| Full weekly cycle | At least 7 days for consumer products with weekday/weekend effects |
| Pay cycle / billing | B2B or subscription: include monthly cycle if metric is payment-sensitive |
| Holidays / promos | Do not start during known anomalies without annotation |
| Learning / novelty | Short UX tests may need 2+ weeks for retention metrics |

**Runtime formula (approximate):**

```
days ≈ (required sample per variant × number of variants) / (daily eligible assignments × allocation fraction)
```

Add buffer (10–20%) for data loss, SRM exclusions, and incident pauses.

## Allocation and traffic

| Allocation | When |
|---|---|
| 50/50 | Default A/B; maximizes power per user |
| Unequal (e.g., 90/10) | Low-risk rollout; **reduces power** for treatment—recalculate N |
| Ramp | Gradual exposure increase; not a substitute for randomization QA |

Document **mutual exclusion** with other experiments consuming same population.

## Worked example checklist

- [ ] Baseline estimated from last 14–28 days (stable)
- [ ] MDE signed by PM/finance for primary metric
- [ ] α, power, one/two-sided documented
- [ ] Per-variant N and total N calculated
- [ ] Calendar days estimated with allocation %
- [ ] Seasonality and conflicting launches checked
- [ ] Max runtime and extension criteria pre-defined
- [ ] Results pasted into experiment registry
