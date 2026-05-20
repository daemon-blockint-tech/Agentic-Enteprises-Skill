# Longevity improvement, estimation, and discounting

## Table of contents

1. [Mortality improvement frameworks](#mortality-improvement-frameworks)
2. [Longevity risk](#longevity-risk)
3. [Estimation from experience](#estimation-from-experience)
4. [Graduation and smoothing](#graduation-and-smoothing)
5. [Yield curves and long cash flows](#yield-curves-and-long-cash-flows)
6. [Profit testing overview](#profit-testing-overview)

## Mortality improvement frameworks

**Mortality improvement** — systematic decline in mortality rates over calendar time.

Common approaches (conceptual):

| Approach | Idea | Document |
|---|---|---|
| **Improvement scale** | Multiply base \(q_x\) by factor by calendar year | Scale name, version, cap |
| **Age-period-cohort** | Separate age, period, cohort effects | Identifiability limits |
| **Expert judgment** | Overlay on experience | Governance via `assumption-setting` |

Distinguish:

- **Base table** (cross-section at valuation date)
- **Projection** (future calendar years)
- **Long-term rate** vs **short-term** improvement

## Longevity risk

**Longevity risk** — risk that realized mortality is **lower** than assumed (payments last longer).

Sources:

- **Process risk** — random fluctuation in small portfolios
- **Level risk** — wrong average mortality level
- **Trend risk** — improvement faster than assumed
- **Basis risk** — mismatch between hedge and liability cohort

Mitigation (overview only): **reinsurance**, **longevity swaps**, **pension risk transfer** → `pension-retirement-funds`; **ALM** for interest-longevity interaction → `asset-liability-management`.

## Estimation from experience

Workflow for **experience analysis** (math framing; execution in `actuarial-analyst`):

1. **Define** exposure (policy years, central exposed to risk)
2. **Stratify** age, gender, duration, product, underwriting class
3. **Compute** \( \hat{q}_x = \text{deaths} / \text{exposure} \) with credibility checks
4. **Compare** to industry or regulatory standard table (A/E ratios)
5. **Propose** standard table or blend; submit to `assumption-setting`

Address **censoring** (lapses, end of study) and **large claims** separately for health riders.

## Graduation and smoothing

**Graduation** — smooth raw \(\hat{q}_x\) to produce publishable rates.

| Method | Use when |
|---|---|
| **Moving average** | Quick smooth; watch endpoints |
| **Whittaker-Henderson** | Balance fit vs smoothness |
| **Parametric (Heligman-Pollard, etc.)** | Extrapolate old ages |
| **Spline** | Flexible shape with constraints |

Checks after graduation:

- **Smoothness** — no jagged runs in \(q_x\)
- **Adherence** — weighted fit to raw experience
- **Tail** — plausible at high ages; avoid zero denominators

## Yield curves and long cash flows

Long-dated liabilities require **discounting** aligned with cash-flow timing:

1. Map liability **cash flows** by duration bucket
2. Select **spot** or **par** curve; document **liquidity premium** if any
3. Compute **duration** and **convexity** for ALM dialogue → `asset-liability-management`
4. For pensions, note **segment rates** (IRC) vs **market** curves (economic)

**Nominal vs real** — link benefit indexation (COLA) to inflation assumptions in `assumption-setting`.

## Profit testing overview

**Profit testing** for life products (conceptual steps):

1. **Projection** — premiums, claims, expenses, reserves, investment income by duration
2. **Scenario grid** — mortality, lapse, interest, expense shocks
3. **Metrics** — PV profit, profit margin, IRR, break-even year
4. **Regulatory capital** — cite need for actuary; do not fabricate RBC formulas without source

Emerging cost ties **actual** experience to **pricing** assumptions over time—pair with `premiums_and_reserves.md`.

Hand **model implementation** and **sensitivity exhibits** to `actuarial-analyst`; **pricing sign-off** to `actuary`.
