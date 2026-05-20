# Pricing and rate indication (analyst)

## Table of contents

1. [Analyst role in pricing](#analyst-role-in-pricing)
2. [Experience aggregation](#experience-aggregation)
3. [Trend and on-level](#trend-and-on-level)
4. [Credibility](#credibility)
5. [Indication summary](#indication-summary)
6. [GLM and multivariate (spec level)](#glm-and-multivariate-spec-level)
7. [Constraints and implementation](#constraints-and-implementation)
8. [Analyst exhibits](#analyst-exhibits)

## Analyst role in pricing

Analysts prepare **technical support** for rate indications and renewals. The actuary or pricing actuary owns:

- Segment definition and homogeneity
- Method selection and final indication
- Regulatory filing narrative (with compliance/counsel as needed)

Analyst deliverables: **clean experience**, **documented adjustments**, **indication math** reproducible from source data.

## Experience aggregation

| Element | Definition to document |
|---|---|
| Exposure | Car-year, payroll, sales, member months, etc. |
| Earned premium | Earned during experience period at current rate level |
| Losses | Paid, incurred, or reported—match actuary instruction |
| Claims count | For frequency-severity splits |

Steps:

1. Filter experience period per memo (e.g., 3 accident years, 12 months earned)
2. Segment per **rating variables** (class, territory, limit band)
3. Remove **outliers** only per written rules; log removed records
4. Compute **pure premium** = losses ÷ exposure (or frequency × severity)

Produce **A/E vs expected** if expected table provided in assumption memo.

## Trend and on-level

| Adjustment | Purpose |
|---|---|
| **On-level** | Restate historical premium to current rate level |
| **Loss trend** | Project experience to prospective period |
| **Benefit trend** (health) | Utilization and unit cost where split |
| **Excess trend** | Large loss or limit changes |

Document:

- Formula and indices (CPI, industry benchmark, internal index)
- **From-date / to-date** for trend factors
- Sensitivity: ±1 point trend on indicated change (if material)

Do not invent trend without **approved assumption** or actuary instruction.

## Credibility

Apply weights per memo (examples—actuary selects formula):

| Approach | Analyst output |
|---|---|
| Limited fluctuation | Z by exposure threshold table |
| Bühlmann | Support inputs if model in separate tool |
| Full credibility shortcut | Z=1 above threshold; show threshold |

Show columns:

- **Observed** pure premium or loss ratio
- **Complement** (manual, industry, or prior approved)
- **Credibility-weighted** indication

```
indicated = Z × observed + (1 - Z) × complement
```

## Indication summary

Standard summary table:

| Column | Content |
|---|---|
| Segment | Class/territory/line |
| Current rate | Or base rate per unit |
| Indicated rate | Credibility-weighted |
| Indicated change % | (Indicated / Current) - 1 |
| Expected LR | At indicated rate if earned premium projected |
| Notes | Constraints, thin data, outliers |

Separate **gross indication** from **implemented** rate if underwriting constraints provided.

## GLM and multivariate (spec level)

When actuary requests GLM support, document **specification** only unless trained to run production models:

| Spec element | Example |
|---|---|
| Response | Claim count, pure premium, loss cost |
| Distributional assumption | Poisson, Gamma, Tweedie (per actuary) |
| Offsets | Log exposure |
| Factors | Territory, class, year, limit |
| Interactions | Only if pre-approved |
| Validation | Holdout year, lift chart, double-lift |

Route **model fitting and selection** to actuary or advanced analytics (`quantitative-researcher` for non-standard ML).

## Constraints and implementation

Capture non-technical constraints in a **separate tab** (do not bury in formula):

- Competitive floor/ceiling
- Regulatory maximum increase
- Filings already submitted
- Portfolio mix targets

Analyst **does not** override technical indication without actuary approval—show both columns.

## Analyst exhibits

Minimum pricing support pack:

1. Data reconciliation (premium, exposure, losses)
2. Segment experience tables
3. Trend and on-level support
4. Credibility calculation
5. Indication summary
6. Sensitivities (if requested)
7. Open questions

Cross-check **combined ratio** impact if expense and profit loads provided in separate tab.
