# Stress scenarios and governance

## Table of contents

1. [Scenario design principles](#scenario-design-principles)
2. [Scenario types](#scenario-types)
3. [Risk factor shocks](#risk-factor-shocks)
4. [Reverse stress and escalation](#reverse-stress-and-escalation)
5. [ALM policy and limits](#alm-policy-and-limits)
6. [ALCO process](#alco-process)
7. [Model risk and validation](#model-risk-and-validation)
8. [Documentation standards](#documentation-standards)

## Scenario design principles

Effective ALM stress testing is:

- **Coherent** — joint shocks respect economic plausibility (e.g., rates down + equity up vs crisis correlation)
- **Transparent** — assumptions documented and versioned
- **Actionable** — tied to limits, capital, and management decisions
- **Comparable** — repeatable quarter-over-quarter with bridges

Define:

1. **Valuation approach** (full revaluation vs sensitivity approximation)
2. **Rebalancing** behavior (static vs dynamic hedges)
3. **Time horizon** (instantaneous vs 1-year path)

## Scenario types

| Type | Purpose | Examples |
|---|---|---|
| **Sensitivity** | Marginal impact of one factor | +100bp parallel rates |
| **Historical** | Replay past regimes | 2008, 2020, 2022 rate shock |
| **Hypothetical** | Forward-looking narratives | Stagflation, credit crunch |
| **Regulatory** | Compliance with prescribed sets | IRRBB, ORSA, ICAAP templates (overview) |
| **Reverse stress** | Find scenarios that break limits | Max equity drop before SaR breach |

Combine **level** shocks with **shape** shocks (steepener, flattener, butterfly).

## Risk factor shocks

### Interest rates

- Parallel ±50/100/200bp
- Key-rate bumps by tenor
- Negative rate floor handling

### Credit spreads

- Widening by rating bucket
- Migration overlays for structured books

### Equity and alternatives

- Equity -20% / -35% with correlation to rates per scenario narrative
- Private asset **valuation lag** and **haircuts**

### Inflation

- CPI/RPI paths for indexed liabilities and ILBs
- Wage inflation for active pension participants

### Insurance / pension-specific

- **Longevity** improvement shock (+X years)
- **Lapse** mass lapse or surrender spike
- **Morbidity** utilization spike (health)

Report impacts on:

- **Surplus** or **economic value**
- **Funded ratio**
- **Earnings** (if requested, accounting basis)
- **Capital ratios** (overview)

## Reverse stress and escalation

**Reverse stress** identifies combinations of factors that drive surplus to **policy floor** or **regulatory minimum**.

Steps:

1. Start from limit breach definition (e.g., SaR > appetite)
2. Search or narrative-build scenario combinations
3. Identify **mitigations**: additional hedges, contribution, benefit changes (pension), capital raise

**Escalation**:

| Severity | Typical action |
|---|---|
| Green | Monitor; within appetite |
| Amber | Hedge adjustment proposal; management review |
| Red | ALCO emergency session; regulator notification (per policy) |

## ALM policy and limits

ALM policy should define:

- **Objectives** and **risk appetite**
- **Permitted instruments** and **counterparty** criteria
- **Quantitative limits** (examples below)
- **Roles** and **approval** authorities
- **Review cadence** and **exception** process

Example limit categories (institution-specific):

| Limit | Example metric |
|---|---|
| Duration gap | \|D_A - D_L\| < X years |
| Surplus-at-risk | 99% 1y SaR < $Y |
| Hedge ratio | HR between 80%–120% |
| Concentration | Single issuer < Z% |
| Derivatives | Notional / VAR caps |

Limits must align with **measurement basis** used in risk systems.

## ALCO process

**Asset-Liability Committee (ALCO)** agenda (template):

1. **Market update** — rates, spreads, inflation, liquidity
2. **Surplus / funded status** — bridges since prior meeting
3. **Risk metrics** — duration gap, KRD, SaR, limit utilization
4. **Hedge program** — performance, roll, proposed changes
5. **Stress results** — new scenarios, breaches, mitigations
6. **Policy exceptions** — status and remediation
7. **Decisions and actions** — owners and dates

Minutes should capture **dissent**, **assumptions**, and **follow-ups** for audit trail.

## Model risk and validation

ALM relies on:

- **Liability models** (actuarial)
- **ALM / risk** aggregation engines
- **Vendor** analytics for derivatives and KRD

Governance elements:

- Model inventory with **tiering**
- Independent **validation** and periodic revalidation
- **Change control** for assumptions and code
- **Back-testing** of sensitivities vs full revaluation where possible

Escalate model materiality to enterprise **model risk management** policy.

## Documentation standards

Each stress cycle should archive:

1. Scenario definitions (shocks, correlations, dates)
2. Input data cut (positions, curves, FX)
3. Model version IDs
4. Output exhibits and **limit breach** log
5. Management responses and hedge tickets (reference only)

Label outputs as **internal management** information—not regulatory filing or actuarial opinion unless reviewed by qualified roles.
