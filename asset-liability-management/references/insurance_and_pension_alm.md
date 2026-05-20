# Insurance and pension ALM

## Table of contents

1. [Institution comparison](#institution-comparison)
2. [Life and annuity ALM](#life-and-annuity-alm)
3. [P&C and health ALM (overview)](#pc-and-health-alm-overview)
4. [Pension and retirement fund ALM](#pension-and-retirement-fund-alm)
5. [Bank ALM (IRRBB overview)](#bank-alm-irrbb-overview)
6. [Capital and regulatory touchpoints](#capital-and-regulatory-touchpoints)
7. [Coordination with actuarial owners](#coordination-with-actuarial-owners)

## Institution comparison

| Dimension | Life / annuity insurer | Pension fund / trust | Bank (ALM desk) |
|---|---|---|---|
| Primary liability | Policyholder obligations, reserves | Benefit payments to participants | Deposits, borrowings, structural products |
| Typical horizon | Long; mortality/longevity | Very long; demographic | Short to medium for NII; long for EVE |
| Key ALM metric | Surplus, PVFP, capital | Funded ratio, surplus volatility | NII sensitivity, EVE, IRRBB limits |
| Hedge tools | Bonds, swaps, derivatives, reinsurance | LDI, glide paths, risk transfer | Swaps, bonds, deposits pricing |
| Regime examples | RBC, Solvency II (overview) | ERISA funding, GAAP (overview) | Basel IRRBB, local banking rules |

Use institution-appropriate vocabulary in ALCO materials.

## Life and annuity ALM

### Liability features driving ALM

- **Guaranteed** minimum rates and **crediting** strategies
- **Surrender** and **lapse** options
- **Annuitization** and **GMxB**-style guarantees (overview)
- **Longevity** on payout annuities

### Asset strategies

- **Liability-sensitive** segments: long bonds, swaps, ILBs
- **Spread** assets: corporate credit with capital and liquidity limits
- **Separate accounts** vs **general account** ring-fencing

### ALM metrics (overview)

| Metric | Purpose |
|---|---|
| Surplus (economic) | Assets − best-estimate liabilities |
| Duration of surplus | Rate risk after hedges |
| PVFP / embedded value components | Management view of franchise value |
| Capital coverage | Regulatory ratio sensitivity |

Detailed reserving, pricing, and assumption work → `actuary`, `life-health-insurance`.

## P&C and health ALM (overview)

P&C liabilities are often **shorter** and **inflation-linked** (claims trends) compared to life.

ALM focus areas:

- **Loss reserve** discounting (where permitted) and **investment income** matching
- **Inflation** sensitivity on long-tail lines
- **Liquidity** for large cat events
- **Asset adequacy** testing concepts (high level)

Do not replace **reserve adequacy** analysis with duration metrics alone → `actuary`, `property-casualty-insurance`.

## Pension and retirement fund ALM

### Liability profile

- **DB** plans: long duration, sensitive to **discount rate**, **mortality**, **salary inflation**
- **De-risking** path: equity-heavy → LDI → **buyout** readiness

### Funding vs economic ALM

| Lens | ALM implication |
|---|---|
| **Funding (IRC)** | Smoothed rates may diverge from hedge curves—basis risk |
| **GAAP (ASC 715)** | PBO duration drives accounting volatility |
| **Economic** | Market-consistent LDI design |

### Pension-specific metrics

- **Funded ratio** (specify numerator/denominator)
- **Surplus volatility** under rate scenarios
- **Contribution** risk and **policy** corridor

Plan design, ERISA, and risk transfer structures → `pension-retirement-funds`; ALM consumes **cash-flow** and **duration** outputs.

## Bank ALM (IRRBB overview)

Banks separate:

- **Interest rate risk in the banking book (IRRBB)** — EVE and NII metrics
- **Liquidity risk** — LCR/NSFR (not ALM core unless user asks liquidity crisis ops)

### Typical metrics

| Metric | Measures |
|---|---|
| **EVE sensitivity** | Economic value of equity under rate shocks |
| **NII sensitivity** | Earnings over 12–24 months under rate paths |
| **Gap reports** | Repricing mismatches by bucket |

ALM skill covers **IRRBB framing** for balance-sheet dialogue—not payment operations or crisis liquidity runbooks.

## Capital and regulatory touchpoints

High-level links only—qualified roles sign filings.

| Context | ALM question for capital |
|---|---|
| Life insurer | How do rate/spread shocks affect **RBC** or **SCR**? |
| Pension | Does LDI reduce **volatility** relevant to sponsor balance sheet? |
| Bank | Do shocks breach **IRRBB** internal limits? |

Coordinate **assumption sets** with `assumption-setting` and **liability measurement** with `actuary`.

## Coordination with actuarial owners

| Deliverable from actuary / pension team | ALM use |
|---|---|
| Liability cash-flow projection | Cash-flow and duration matching |
| Discount curve specification | Hedge curve selection, basis analysis |
| Sensitivity exhibits (rates, longevity) | Hedge sizing, stress design |
| Funding valuation | Contribution policy—not duplicate |

ALM skill **interprets and structures** investment/hedge responses; it does not replace **appointed actuary** or **actuarial certification**.
