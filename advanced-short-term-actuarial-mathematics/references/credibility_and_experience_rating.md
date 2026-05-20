# Credibility and experience rating

## Table of contents

1. [Experience rating overview](#experience-rating-overview)
2. [Limited fluctuation credibility](#limited-fluctuation-credibility)
3. [Bühlmann model](#bühlmann-model)
4. [Bühlmann-Straub](#bühlmann-straub)
5. [Credibility-weighted estimators](#credibility-weighted-estimators)
6. [Diagnostics and governance](#diagnostics-and-governance)

## Experience rating overview

**Experience rating** updates a **manual** or **prior** indication with **observed** loss experience for a class, employer, or policy group.

Standard linear blend:

\[
\hat{\theta}_Z = Z \cdot \bar{X} + (1-Z) \cdot \mu
\]

where:

- \(\bar{X}\) — observed experience statistic (pure premium, loss ratio, etc.)
- \(\mu\) — complement (manual rate, industry benchmark, prior approved)
- \(Z \in [0,1]\) — credibility weight

Distinguish **gross** observed from **credibility-weighted** final—underwriters implement constraints separately (`actuarial-analyst`).

## Limited fluctuation credibility

**Full credibility** rules (conceptual): find minimum exposure \(n_0\) such that \(P(|\bar{X}-\mu| \le k\mu) \ge p\) under stated distributional assumptions.

Examples (Poisson frequency, normal severity approximations—verify formulas against company standard):

- Frequency full credibility thresholds on claim counts
- Severity full credibility on claim counts above a minimum

**Partial credibility:**

\[
Z = \min\left(1, \sqrt{\frac{n}{n_0}}\right)
\]

(variants exist—document company formula).

**Pros:** Simple, transparent  
**Cons:** Ignores structural heterogeneity across years/classes

## Bühlmann model

**Structural model** for contract \(i\):

\[
X_{ij} = \theta_i + \varepsilon_{ij}
\]

\(\theta_i\) — random risk parameter; \(\varepsilon_{ij}\) — noise.

**Homogeneous Bühlmann** credibility factor:

\[
Z = \frac{k}{k + n}
\]

where \(k\) is a **structural parameter** estimated from data (ratio of process variance to parameter variance) and \(n\) is exposure measure (e.g., claim counts or earned exposure).

**Credibility premium** for risk \(i\):

\[
\hat{\theta}_i = Z_i \bar{X}_i + (1-Z_i) \hat{\mu}
\]

with \(\hat{\mu}\) the collective estimate.

Report estimated **\(k\)**, within- and between-group variances, and sensitivity of \(Z\) to \(k\).

## Bühlmann-Straub

Extends Bühlmann when **exposure varies** across observations (different payroll, car-years):

- Weights \(w_{ij}\) on observations
- Credibility formulas incorporate **weighted** means and effective exposures

Use when experience periods have **unequal** exposure bases—common in commercial lines.

## Credibility-weighted estimators

| Estimand | Observed \(\bar{X}\) | Complement \(\mu\) |
|---|---|---|
| Pure premium | Losses / exposure | Manual pure premium |
| Loss ratio | Incurred / earned premium | Target or manual LR |
| Frequency | Claims / exposure | Manual frequency |

**Loss ratio** form often pairs with **on-level** premium and **trend** (see `ratemaking_and_trend.md`).

Show **before/after** credibility table:

| Segment | Observed | Z | Complement | Weighted |
|---|---|---|---|---|

## Diagnostics and governance

- **Credibility too high** with thin data → unstable rates; check \(Z\) caps
- **Complement stale** → biased toward outdated manual
- **Outliers** in experience → document removal rules before credibility
- **Correlation** across segments → Bühlmann may understate uncertainty

Assumption changes to complement or \(k\) belong in `assumption-setting` with actuary approval.

Execution of rating worksheets → `actuarial-analyst`.
