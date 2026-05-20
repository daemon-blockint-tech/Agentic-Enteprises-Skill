---
name: pension-retirement-funds
description: |
  Guides pension and retirement fund work—DB vs DC structures, funding policy, liability measurement
  (PV of benefits, discount rates, mortality), ALM overview, plan design, public and multi-employer
  pensions, risk transfer (buyouts, annuities, de-risking), US regulatory overview (ERISA, PBGC,
  DOL, IRS qualified plans), institutional investor role, and fiduciary governance—not legal or tax advice.
  Use when the user mentions pension fund, retirement plan, defined benefit, defined contribution,
  401(k), pension funding, PBGC, ERISA, pension liability, discount rate pension, pension buyout,
  de-risking pension, or ALM pension—not P&C insurance (property-casualty-insurance), actuarial
  modeling only (actuary), actuarial engagements (actuarial-consulting), personal IRA advice
  (financial-analyst), or legal interpretation (commercial-counsel).
---

# Pension and Retirement Funds

## When to Use

- Explain **DB vs DC** plan types, hybrids, and cash balance at overview level
- Frame **funding policy**, contribution strategy, and funded status metrics (corporate DB)
- Discuss **liability measurement** concepts: PV of benefits, discount rate, mortality, COLA
- Outline **asset-liability management** (duration, hedging, glide paths, liability-driven investing)
- Support **plan design** questions: benefit formulas, vesting, early retirement, optional forms
- Compare **corporate**, **public sector**, and **multi-employer** pension contexts (high level)
- Describe **pension risk transfer**: lift-outs, buyouts, annuities, longevity reinsurance
- Summarize **US regulatory** topics (ERISA, PBGC, DOL, IRS qualified plans)—not legal advice
- Explain **fiduciary governance**, investment policy, and institutional investor role of pension funds
- Support due diligence, board briefings, or transformation with pension domain context

## When NOT to Use

- P&C insurance lines, underwriting, or claims → `property-casualty-insurance`
- Loss triangles, IBNR, insurance pricing/reserving methods, or appointed-actuary sign-off → `actuary`
- Actuarial consulting SOW, engagement governance, or M&A actuarial program management → `actuarial-consulting`
- Individual retirement planning, IRA rollovers, or personal wealth advice → `financial-analyst` (if installed)
- Contract interpretation, plan document legal disputes, or regulatory enforcement → `commercial-counsel`
- SOC 2 / ISO control mapping without pension operations context → `compliance-engineer`
- Executive strategy without pension/benefits domain detail → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| Insurance pricing, reserving, triangles, assumption governance | `actuary` |
| Actuarial engagement scoping, SOW, due diligence programs | `actuarial-consulting` |
| P&C coverages, underwriting, claims lifecycle | `property-casualty-insurance` |
| Corporate FP&A, investor metrics, non-pension analytics | `financial-analyst` (if installed) |
| Business case, operating model, transformation | `business-consultant` |
| Technical control evidence, audit packages | `compliance-engineer` |
| Contract, plan document, regulatory interpretation | `commercial-counsel` |

## Core Workflows

### 1. Engagement scoping

Before analysis:

1. **Plan type** — DB, DC, hybrid, governmental, multi-employer
2. **Sponsor** — Corporate, public, union, Taft-Hartley, church plan (note limitations)
3. **Decision** — Funding, design change, de-risking, accounting disclosure, governance review
4. **Measurement basis** — Funding (IRC/ERISA), GAAP (ASC 715), economic, solvency (public)
5. **Jurisdiction** — US federal/state; flag non-US for local counsel and standards
6. **Materiality** — Participant count, funded status, benefit richness, tail longevity risk

**See `references/pension_retirement_scope.md`.**

### 2. Plan structures (DB vs DC)

1. Map **benefit promise** (defined vs account balance) and sponsor risk allocation
2. Identify **participant populations** (active, deferred, retired) and data needs
3. Note **hybrid** features (cash balance, floor-offset, PEP/MPP DB/DC combos)
4. Separate **401(k)/403(b)/457** DC mechanics from DB accrual formulas
5. Escalate legal classification and document wording to `commercial-counsel`

**See `references/db_vs_dc_plan_structures.md`.**

### 3. Funding, liabilities, and ALM

1. State **valuation date** and purpose (funding, accounting, transaction)
2. Outline **liability cash flows**: benefits, timing, indexing, optional forms
3. Explain **discount rate** role (segment rates, full yield curve, market vs smoothed)
4. Summarize **mortality** and **improvement** assumptions at concept level
5. Connect **assets** to liabilities: funded ratio, duration, hedge ratio, glide path
6. Hand off detailed actuarial calculations to `actuary` when models are required

**See `references/funding_liabilities_and_alm.md`.**

### 4. Plan design and benefits

1. Document **benefit formula** (final average, career average, flat dollar)
2. Capture **eligibility**, **vesting**, **service crediting**, and **breaks in service**
3. Address **early retirement** subsidies, **disability**, and **survivor** forms
4. Flag **COLA**, **lump sum**, and **cash balance** conversion issues (overview)
5. Coordinate **communications** and **amendment** process with counsel and recordkeeper

**See `references/plan_design_and_benefits.md`.**

### 5. Risk transfer and de-risking

1. Clarify objective: balance sheet, volatility reduction, participant security, admin simplification
2. Compare **LDTI/LDI**, **buy-in**, **buy-out**, **annuity placement**, **longevity reinsurance**
3. List **data**, **insurer/market**, and **fiduciary** prerequisites
4. Outline **transaction timeline** and **accounting/funding** impacts at high level
5. Refer pricing, mortality, and liability sizing to `actuary`; legal docs to `commercial-counsel`

**See `references/risk_transfer_and_de-risking.md`.**

### 6. Regulatory, governance, and operations

1. Map **ERISA** fiduciary duties, **IPS**, and committee governance
2. Summarize **PBGC** premiums and termination concepts (corporate DB)
3. Note **DOL** reporting (Form 5500) and **IRS** qualification/testing at overview
4. Describe **recordkeeper/custodian**, **payroll**, and **administration** operating model
5. Label all regulatory comments as **not legal or tax advice**

**See `references/regulatory_governance_and_operations.md`.**

## Key metrics (pension)

| Metric | Typical use |
|---|---|
| Funded ratio (assets ÷ liabilities) | Funding and risk monitoring; basis matters |
| Projected benefit obligation (PBO) | GAAP liability snapshot |
| Accumulated benefit obligation (ABO) | Benefits earned to date |
| Normal cost | Cost of benefits accruing in period |
| Required / minimum contribution | IRC minimum funding (overview) |
| Discount rate | Sets liability present value; method-specific |
| Duration / interest rate sensitivity | ALM and hedge design |
| Service cost / interest cost | Expense components (GAAP) |

Always state **measurement basis** and **assumption set** in footnotes.

## Data requests (starter checklist)

When the user has not supplied data, ask for:

1. **Plan document** summary or SPD highlights (not legal interpretation)
2. **Census** or participant counts by status (active, term, retiree)
3. **Asset statement** and allocation policy
4. **Latest actuarial valuation** (funding and/or accounting) with assumptions
5. **Contribution history** and funding policy
6. **Prior** board materials, de-risking studies, or RFPs

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Plan overview | DB/DC type, populations, key benefits, sponsor context |
| Funded status memo | Basis, funded ratio, main assumptions, trend |
| ALM summary | Liability profile, asset mix, hedge/glide path, risks |
| Design options | Formula/vesting changes, cost direction, participant impact |
| De-risking brief | Objectives, structures considered, fiduciaries, next steps |
| Governance note | Committees, IPS, regulatory touchpoints (overview) |

Always state **uncertainty** and **limitations**. Do not present outputs as legal, tax, actuarial opinion, or regulatory filing without qualified human review.

## When to load references

- **Scope and boundaries** → `references/pension_retirement_scope.md`
- **DB vs DC structures** → `references/db_vs_dc_plan_structures.md`
- **Funding, liabilities, ALM** → `references/funding_liabilities_and_alm.md`
- **Plan design and benefits** → `references/plan_design_and_benefits.md`
- **Risk transfer and de-risking** → `references/risk_transfer_and_de-risking.md`
- **Regulation and governance** → `references/regulatory_governance_and_operations.md`
