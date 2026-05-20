# Capital, risk, and regulatory overview

## Table of contents

1. [Purpose and limits](#purpose-and-limits)
2. [NAIC and US statutory (overview)](#naic-and-us-statutory-overview)
3. [IFRS 17 (overview)](#ifrs-17-overview)
4. [Solvency II (overview)](#solvency-ii-overview)
5. [Economic capital concepts](#economic-capital-concepts)
6. [Risk metrics map](#risk-metrics-map)
7. [Coordination with finance and counsel](#coordination-with-finance-and-counsel)

## Purpose and limits

This reference provides **orientation** for actuaries coordinating with finance, risk, and legal teams. It is **not**:

- Legal advice on filing requirements
- A substitute for **appointed actuary** sign-off
- Detailed IFRS journal entries (see `ifrs` skill)
- Investment or ALM strategy execution

Escalate binding regulatory positions to qualified professionals in the relevant jurisdiction.

## NAIC and US statutory (overview)

| Topic | Actuarial touchpoint |
|---|---|
| RBC | Company action level vs TAC; underwriting/investment risk categories |
| Statutory reserves | Line-specific formulas or principle-based reserves |
| Actuarial opinion | Statement of actuarial opinion on reserves (appointed actuary) |
| PBR | Principle-based reserving for life (VM-20/21 overview) |

Actuaries supply **reserve adequacy** analysis supporting opinion; coordinate asset adequacy testing with investments.

## IFRS 17 (overview)

Insurance contracts standard (high level):

| Element | Actuarial role |
|---|---|
| Fulfillment cash flows | Best estimate liability cash flows |
| Risk adjustment | Compensation for non-financial risk |
| CSM | Unearned profit for profitable groups; amortization pattern |
| Discounting | Current rates vs locked-in (general model) |
| Onerous groups | Loss component recognition |

Coordinate measurement outputs with **`ifrs`** skill for presentation, disclosure, and reconciliation to GL.

## Solvency II (overview)

| Pillar | Focus |
|---|---|
| Pillar 1 | SCR, MCR, technical provisions |
| Pillar 2 | ORSA, internal risk management |
| Pillar 3 | Public QRT disclosures |

**Technical provisions** split best estimate and risk margin; actuaries often own BE assumptions. **SCR** uses standard formula or internal model (overview)—not full internal model build here.

## Economic capital concepts

Internal frameworks often estimate capital as **VaR** or **TVaR** of surplus over a horizon:

```
economic capital ≈ quantile(loss distribution) − expected loss
```

Link to:

- **Underwriting** — catastrophe, reserve error, premium risk
- **Market** — rates, equity, spread (ALM)
- **Credit** — reinsurance default, bond downgrades

Document **diversification** assumptions and correlation matrices at high level; refer to enterprise risk for governance.

## Risk metrics map

| Metric | Typical use |
|---|---|
| Loss ratio / combined ratio | Underwriting performance |
| Reserve adequacy ratio | Actual vs carried |
| RBC ratio | US solvency buffer |
| SCR coverage | EU solvency |
| Surplus at risk | Life/annuity guarantee exposure |

Present **sensitivities** (interest ±100 bps, mortality ±%, cat event) as scenarios, not single points, when advising committees.

## Coordination with finance and counsel

| Question | Route to |
|---|---|
| IFRS 17 note disclosure wording | `ifrs` + external reporting |
| Filing deadline and form | Counsel + regulatory affairs |
| Control environment for models | `compliance-engineer` |
| DCF / M&A valuation | `dcf-model`, `comps-analysis` (if installed) |
| Enterprise strategy narrative | `business-consultant` |

Document **open issues** list for appointed actuary or auditor review before external distribution.
