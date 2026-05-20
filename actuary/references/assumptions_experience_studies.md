# Assumptions and experience studies

## Table of contents

1. [Study design](#study-design)
2. [Actual vs expected](#actual-vs-expected)
3. [Mortality and longevity](#mortality-and-longevity)
4. [Morbidity and health trend](#morbidity-and-health-trend)
5. [Lapse and persistency](#lapse-and-persistency)
6. [Credibility](#credibility)
7. [Assumption governance](#assumption-governance)

## Study design

1. **Objective** — Update pricing, valuation, or both
2. **Population** — In-force, new business, closed block; include/exclude rules
3. **Period** — Enough exposure for stability; exclude distortion years or footnote
4. **Basis** — Exposure measure (earned premium, member months, life years)
5. **Dimensions** — Age, gender, class, duration, geography, product

Data prep checklist:

- Match **policy admin** to **claims** keys
- Handle **reinstatements**, **riders**, and **terminations**
- Define **claim types** consistently (medical vs RX vs dental)

## Actual vs expected

```
A/E ratio = actual experience / expected experience (on same exposure basis)
```

| A/E | Typical interpretation |
|---|---|
| < 1 | Favorable vs assumption (mortality: lower deaths than expected) |
| > 1 | Adverse; consider assumption increase |
| Volatile | Credibility-weight or extend study period |

Present A/E by **dimension** and in aggregate; investigate interaction effects before changing factors.

## Mortality and longevity

| Context | Key assumptions |
|---|---|
| Life insurance | Mortality table, underwriting class, improvement scale |
| Annuity | Mortality improvement, anti-selection at issue |
| Group life | Age/sex schedule, industry adjustment |

Compare to **standard tables** (e.g., industry tables) with scaling factors. Document **selection** period and **ultimate** period separately for some products.

## Morbidity and health trend

- **Utilization** — Visits, admits, RX fills per member
- **Unit cost** — Allowed amount per service; fee schedule inflation
- **Mix** — Shift to high-cost sites of care
- **Trend** — Separate frequency and unit cost trend where possible

Health experience often needs **seasonality** and **network** changes called out explicitly.

## Lapse and persistency

| Product | Drivers |
|---|---|
| Term life | Rate shock, replacement, economic cycle |
| UL/VUL | COI increase, account performance |
| Health | Premium increase, alternative coverage |

Model **dynamic lapse** (overview) when interest rates or guarantees dominate.

## Credibility

Blend **observed** experience with **prior** (manual, industry, or last approved assumption):

| Approach | Formula (conceptual) |
|---|---|
| Limited fluctuation | Z = f(exposure, k) |
| Bühlmann | Empirical Bayes credibility |
| Judgment | Document when data insufficient |

Report **full credibility exposure** threshold and Z used per segment.

## Assumption governance

Assumption change package:

| Field | Content |
|---|---|
| Assumption ID | Name, version, effective date |
| Prior vs proposed | Table with % change |
| Supporting study | Period, A/E, credibility |
| Impact | Reserve, income, pricing indication (ranges) |
| Approvals | Actuarial, risk, finance per policy |

Maintain **assumption library** linked to models; no ad hoc hardcoding without version bump.
