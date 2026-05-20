# Severity and frequency models

## Table of contents

1. [Severity modeling](#severity-modeling)
2. [Frequency modeling](#frequency-modeling)
3. [Mixtures and heterogeneity](#mixtures-and-heterogeneity)
4. [Censoring and truncation](#censoring-and-truncation)
5. [Model selection](#model-selection)
6. [Common pitfalls](#common-pitfalls)

## Severity modeling

**Goal:** Model payment \(X\) per claim (or per loss event) with emphasis on **body** and **tail** behavior.

| Family | Support | Tail | Typical use |
|---|---|---|---|
| Exponential | \((0,\infty)\) | Light | Baseline; often inadequate alone for P&C |
| Gamma | \((0,\infty)\) | Light/medium | Positive, flexible shape |
| Lognormal | \((0,\infty)\) | Medium | Positive skew; multiplicative effects |
| Pareto / generalized Pareto | Tail region | Heavy | Large losses; tail extrapolation |
| Weibull | \((0,\infty)\) | Tunable | Failure-time analogies |

**Moments** drive aggregate approximations: \(\mathrm{E}[X]\), \(\mathrm{Var}(X)\), and skewness affect normal approximation quality.

**Tail behavior:**

- Compare **empirical** tail (mean excess plot, Hill estimator conceptually) to parametric tail
- Document **threshold** where tail model starts if using GPD-style reasoning
- Sensitivity: shift in high percentiles when tail parameter changes

## Frequency modeling

**Goal:** Model claim count \(N\) in a fixed exposure period.

| Model | Mean–variance | When to use |
|---|---|---|
| Poisson | \(\mathrm{Var}(N)=\mathrm{E}[N]\) | Equidispersed counts |
| Negative binomial | \(\mathrm{Var}(N) > \mathrm{E}[N]\) | Overdispersion |
| Binomial | Bounded counts | Fixed exposure with cap |
| Zero-modified / zero-inflated | Extra mass at 0 | Excess zeros vs Poisson |

**Poisson** with exposure \(e\): often \(N \sim \mathrm{Pois}(\lambda e)\) or rate per unit exposure.

**Negative binomial** parametrizations differ by software—always state \(\mathrm{E}[N]\) and \(\mathrm{Var}(N)\) in output.

## Mixtures and heterogeneity

**Mixture models** capture unobserved heterogeneity:

- Discrete mixture: e.g., “good” vs “bad” risk subpopulations
- Continuous mixture: gamma–Poisson yields negative binomial frequency

Document **identifiability** limits: mixtures can fit similarly with different interpretations.

## Censoring and truncation

| Mechanism | Effect on observed data |
|---|---|
| **Truncation** (deductible \(d\)) | Observe \(X\) only if \(X > d\); severity model on \(X \mid X>d\) |
| **Censoring** (policy limit \(u\)) | Observe \(\min(X,u)\) |

Misapplying uncensored fits to **limited** data biases severity downward and distorts frequency–severity splits.

## Model selection

Use multiple lenses:

1. **Graphical** — Histogram, density, QQ plot (log scale for severity)
2. **Goodness-of-fit** — Chi-square (binned), Anderson–Darling, Kolmogorov–Smirnov (note sensitivity to tail)
3. **Information criteria** — AIC/BIC for nested models; not sufficient alone for tail choice
4. **Business** — Stability across accident years; interpretability for pricing

Prefer **parsimony** when tail differences are immaterial to the estimand (e.g., median severity vs 99th percentile of \(S\)).

## Common pitfalls

- Fitting severity on **incurred** including IBNR noise as if claim-level payments
- Ignoring **large loss** caps or reinsurance recoveries in the severity sample
- Using **Poisson** when variance clearly exceeds mean
- Extrapolating **Pareto** tail without sufficient large-loss data
- Mixing **accident year** and **calendar year** counts in frequency
