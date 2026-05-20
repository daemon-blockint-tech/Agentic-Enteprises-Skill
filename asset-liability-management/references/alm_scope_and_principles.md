# ALM scope and principles

## Table of contents

1. [What ALM is](#what-alm-is)
2. [Objectives and tradeoffs](#objectives-and-tradeoffs)
3. [Stakeholders and governance](#stakeholders-and-governance)
4. [Measurement bases](#measurement-bases)
5. [Risk taxonomy for ALM](#risk-taxonomy-for-alm)
6. [Boundaries with adjacent disciplines](#boundaries-with-adjacent-disciplines)
7. [Engagement checklist](#engagement-checklist)

## What ALM is

**Asset-liability management (ALM)** is the practice of managing the **joint** behavior of assets and liabilities so that the institution can meet its obligations and strategic goals within **risk appetite** and **capital** constraints.

ALM is not synonymous with:

- **Portfolio management** alone (alpha, security selection) without liability context
- **Treasury operations** alone (cash positioning, payments) without balance-sheet risk framing
- **Actuarial valuation** alone without investment and hedge strategy

Core ALM questions:

1. How do **interest rates**, **credit spreads**, **equity markets**, and **inflation** move **surplus** (or economic value)?
2. Are **cash flows** from assets sufficient and appropriately timed for **liability outflows**?
3. What **hedges** and **investment policies** keep risk within **limits** through stress scenarios?

## Objectives and tradeoffs

Institutions often pursue multiple objectives simultaneously. Make tradeoffs explicit.

| Objective | Description | Typical tension |
|---|---|---|
| Solvency / surplus protection | Limit tail loss on surplus or capital | Lower return target |
| Earnings stability | Smooth reported or economic earnings | Less perfect hedge |
| Cash-flow matching | Align asset receipts with liability payments | Liquidity vs yield |
| Return generation | Earn spread over liability discount rate | Higher market risk |
| Capital efficiency | Reduce regulatory or economic capital drag | Basis and model constraints |
| De-risking readiness | Preserve option to transfer or annuitize liabilities | Glide path vs return |

**Risk appetite** translates objectives into **quantitative limits** (duration gap, SaR, hedge ratio floors, concentration limits).

## Stakeholders and governance

| Role | Typical responsibilities |
|---|---|
| **ALCO** (asset-liability committee) | Approves ALM policy, limits, hedge programs, major IPS changes |
| **CRO / risk** | Owns risk framework, limit monitoring, independent challenge |
| **CFO / treasurer** | Funding, liquidity coordination, accounting impacts |
| **Chief investment officer** | Implements SAA, overlays, manager selection within policy |
| **Actuary** | Liability cash flows, assumptions, regulatory liability measures |
| **Appointed actuary / regulator** (insurance) | Statutory opinion context—not duplicated by ALM skill |

ALM deliverables should be **decision-ready**: options, sensitivities, limit usage, and recommended actions—not data dumps.

## Measurement bases

ALM analysis must state which **basis** applies. Mixing bases without reconciliation is a common failure mode.

| Basis | Assets | Liabilities | Typical use |
|---|---|---|---|
| **Economic / market-consistent** | Fair value | Best-estimate cash flows discounted at market curves | Hedge design, internal capital |
| **Accounting** | GAAP/IFRS carrying values | PBO, insurance contract liabilities | Earnings volatility dialogue |
| **Regulatory / statutory** | Admitted assets (insurance); RBC factors | Statutory reserves | Solvency reporting (overview) |
| **Funding** (pensions) | Fair value or smoothed per policy | IRC funding liability | Contribution policy |

Document **discount curves**, **credit assumptions**, and whether **liquidity premiums** are embedded in liabilities.

## Risk taxonomy for ALM

### Interest rate and curve risk

- **Level** (parallel shifts)
- **Slope** and **curvature** (key rate risks)
- **Reinvestment** risk when asset proceeds must be reinvested at unknown rates
- **Prepayment** and **extension** risk on callable or mortgage-related assets

### Credit and spread risk

- Migration and default on corporate and structured holdings
- **Basis** between hedge instruments and liability discount curves

### Market risk beyond rates

- **Equity** beta on surplus when equities are material
- **Real estate** and **alternatives** valuation lag and liquidity
- **FX** when liabilities or hedges are in different currencies

### Insurance and pension-specific

- **Longevity** / **mortality** (pensions, annuities)
- **Lapse**, **surrender**, and **utilization** (life/health)
- **Inflation** linkage on indexed benefits or claims

### Liquidity and operational

- Ability to meet **collateral** calls on derivatives
- **Fire-sale** risk under stress
- Model and data **operational risk**

## Boundaries with adjacent disciplines

| Topic | Primary skill | ALM role |
|---|---|---|
| Pension benefit design, ERISA funding | `pension-retirement-funds` | Consume liability profile; design LDI |
| Reserve triangles, pricing, assumptions | `actuary`, `assumption-setting` | Use outputs; do not rebuild |
| Security research, issuer fundamentals | `financial-analyst` | Inputs to credit risk, not ALM core |
| Consulting SOW and engagement governance | `actuarial-consulting` | Separate from ALM committee packs |
| P&C or life product education | `property-casualty-insurance`, `life-health-insurance` | Context for liability types |

## Engagement checklist

Before producing ALM analysis, confirm:

- [ ] Institution type and **regulatory** context identified
- [ ] **Valuation date** and bases for assets and liabilities
- [ ] **Surplus** definition agreed (economic vs accounting vs funding)
- [ ] **Horizon** for risk metrics (instantaneous shock vs 1y VaR/SaR)
- [ ] **Hedgeable** risks vs retained risks documented
- [ ] **ALM policy** limits and escalation paths referenced
- [ ] Owners for **liability model** and **investment book** data named
- [ ] Outputs labeled **not** actuarial opinion, legal advice, or trade instruction
