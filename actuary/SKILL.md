---
name: actuary
description: |
  Guides actuarial work for insurance and reinsurance—pricing and rate adequacy, reserving and IBNR,
  loss development and triangles, mortality/morbidity and lapse assumptions, experience studies and
  credibility, capital and risk metrics at overview level, product design tradeoffs (life, health,
  P&C, annuity), and regulatory reporting concepts (NAIC, IFRS 17, Solvency II overview—not legal advice).
  Use when the user mentions actuary, actuarial, IBNR, loss development, reserve analysis, mortality table,
  pricing insurance, experience study, IFRS 17, loss ratio, combined ratio, credibility, or asks for
  assumption documentation and model governance for insurance products—not generic FP&A (financial-analyst),
  investment banking valuation (comps-analysis, dcf-model), legal policy interpretation (commercial-counsel),
  clinical trials, software-only implementation (senior-software-engineer), or broad GRC without
  actuarial models (compliance-engineer).
---

# Actuary

## When to Use

- Price insurance or reinsurance products (indication, renewal, new business)
- Estimate reserves, IBNR, and loss development (paid/incurred triangles)
- Build or review mortality, morbidity, lapse, and expense assumptions
- Run experience studies and apply credibility weighting
- Explain loss ratio, combined ratio, and underwriting metrics
- Frame capital and risk metrics (RBC, SCR overview, economic capital concepts)
- Compare product design tradeoffs (benefits, riders, deductibles, guarantees)
- Document actuarial assumptions, methods, and model governance for sign-off
- Outline IFRS 17 / Solvency II / NAIC reporting concepts at technical overview level

## When NOT to Use

- Corporate FP&A, budgets, variance commentary, or non-insurance KPI dashboards → `financial-analyst` (if installed)
- Investment banking comps, DCF equity valuation, or M&A pitch models → `comps-analysis`, `dcf-model` (if installed)
- Contract legal interpretation, policy wording, or regulatory enforcement advice → `commercial-counsel`
- IFRS general ledger recognition without insurance contract measurement lens → `ifrs`
- Clinical trial design, biostatistics, or epidemiology outside insurance morbidity → health/clinical skills
- Building production software, ETL, or model code only without actuarial judgment → `data-scientist`, `senior-software-engineer`
- SOC 2 / ISO audit evidence and control mapping without actuarial models → `compliance-engineer`
- Executive strategy without pricing/reserving/capital math → `business-consultant`
- Treasury, fundraising, and cash runway → `cfo-advisor` (if installed)

## Related skills

| Need | Skill |
|---|---|
| IFRS 17 measurement, CSM, risk adjustment (accounting lens) | `ifrs` |
| Financial statements, close, and variance packs | `financial-statements` (if installed) |
| Ratios, investor metrics, non-insurance analytics | `financial-analyst` (if installed) |
| Executive business case and operating model | `business-consultant` |
| Regulatory control implementation and audit evidence | `compliance-engineer` |
| Enterprise risk registers (non-actuarial) | `security-risk-analyst` |
| Statistical modeling, ML pipelines, feature engineering | `data-scientist` |
| CFO reporting, unit economics, runway | `cfo-advisor` (if installed) |
| AML/financial crime typologies (not actuarial pricing) | `financial-intelligence-unit` |
| Quant research and backtesting (capital markets) | `quantitative-researcher` |

## Core Workflows

### 1. Engagement scoping

Before any calculation:

1. **Line of business** — Life, health, P&C, annuity, reinsurance; direct vs assumed
2. **Decision** — Price change, reserve opinion, assumption update, product launch, regulatory filing
3. **Data** — Policy/claim bordereaux, triangles, census, experience periods, exclusions
4. **Materiality** — Volume, tail risk, new riders, or cohort changes driving review
5. **Governance** — Sign-off chain, model version, effective date, peer review requirements

**See `references/actuary_scope_and_principles.md`.**

### 2. Pricing and product design

1. Define **coverage**, limits, deductibles, and rating variables
2. Segment risks (territory, class, age band, hazard) with sufficient volume
3. Estimate **frequency × severity** or tabular costs; load for expenses, profit, and risk margin
4. Compare **indicated vs current** rates; document constraints (competitive, regulatory caps)
5. Stress key assumptions (loss trend, inflation, catastrophe load)
6. Summarize **rate change** and expected loss ratio / combined ratio impact

**See `references/pricing_and_product_design.md`.**

### 3. Reserving and loss development

1. Aggregate **paid and incurred** losses by accident year and development lag
2. Select development factors (chain ladder, BF, Cape Cod) with diagnostics
3. Estimate **IBNR** and total ultimate; separate case vs bulk reserves if needed
4. Reconcile to prior evaluation; explain changes (development, large losses, methodology)
5. Document **tail** selection and emergence patterns for long-tail lines

**See `references/reserving_and_loss_development.md`.**

### 4. Assumptions and experience studies

1. Define **exposure** base and study period; handle data quality and outliers
2. Compare **actual vs expected** (A/E) by key dimensions
3. Propose assumption updates with **credibility** (limited fluctuation, Bühlmann, or judgment)
4. Separate **trend**, **level**, and **volatility** where material
5. Version assumptions with effective dates and rationale for audit trail

**See `references/assumptions_experience_studies.md`.**

### 5. Capital and regulatory overview

1. Identify **regime** (NAIC RBC, Solvency II SCR, internal economic capital)
2. Map main **risk drivers**: underwriting, market, credit, operational (high level)
3. Relate reserves and pricing to **solvency** metrics—not a substitute for appointed actuary sign-off
4. Flag **disclosure** topics (IFRS 17 CSM, risk adjustment, LIC) for coordination with `ifrs`
5. Escalate legal or filing interpretation to counsel and appointed actuary

**See `references/capital_risk_and_regulatory_overview.md`.**

### 6. Model governance and deliverables

1. Inventory **models** (pricing, reserving, ALM); owner and validation status
2. Document **inputs**, **methods**, **outputs**, and **limitations**
3. Run **sensitivity** and reasonability checks; retain reproducible workpapers
4. Produce **actuarial memo** or exhibit: executive summary, exhibits, assumptions appendix
5. Archive versioned data cuts and sign-offs per model risk policy

**See `references/model_governance_and_deliverables.md`.**

## Key metrics (insurance)

| Metric | Typical formula / note |
|---|---|
| Earned premium | Written premium adjusted for unearned; match loss basis |
| Loss ratio (LR) | Incurred losses ÷ earned premium |
| Expense ratio | Underwriting expense ÷ earned (or written, per policy) |
| Combined ratio | Loss ratio + expense ratio; < 100% underwriting profit before investment income |
| Frequency | Claims ÷ exposure (policies, car-years, member months) |
| Severity | Average loss per claim |
| Pure premium | Expected loss cost per unit exposure |
| IBNR | Ultimate losses − reported incurred (definition varies by basis) |
| Prior-year development | Change in estimate of past accident years’ ultimates |
| Credibility Z | Weight on observed experience in assumption update |

Clarify **numerator/denominator** conventions in every exhibit footnote.

## Line-of-business notes

### P&C

- Ratemaking on **exposure** (payroll, sales, vehicles) with class plans and territory
- **Long-tail** lines need tail factors and paid/incurred reconciliation
- **Catastrophe** loads separate from attritional; event years flagged in triangles

### Life

- **Mortality**, **lapse**, and **expense** drive profit testing and reserves
- **Cash-value** products need interest and crediting assumptions coordinated with ALM
- **Select vs ultimate** periods for recently underwritten cohorts

### Health

- **Morbidity trend** split utilization vs unit cost when data allows
- **Seasonality** and benefit design changes (deductible, network) dominate A/E
- **Risk adjustment** and pooling (ACA, large group) affect segment homogeneity

### Annuity

- **Longevity** and **withdrawal** drive guarantee costs; scenario sets for sensitivities
- Hedge effectiveness is investment-led; actuary supplies liability cash-flow shapes

## Data requests (starter checklist)

When the user has not supplied data, ask for:

1. **Valuation date** and reporting basis (statutory, GAAP, IFRS 17)
2. **Triangle or bordereaux** with field definitions (accident date, paid, case, count)
3. **Exposure** definition and earning pattern
4. **Reinsurance** structure (quota share, excess, aggregates) and netting rules
5. **Large loss** and catastrophe treatment in prior studies
6. **Prior** actuarial memo, approved assumptions, and model version

## Reasonability and peer review

Before sign-off, complete:

- [ ] Triangle diagnostics (stability, tail, calendar-year check)
- [ ] Implied ultimate LR vs pricing and plan
- [ ] Bridge of reserve change to prior quarter (volume, PYD, method)
- [ ] Assumption changes tied to experience study with credibility
- [ ] Sensitivities on top 3 drivers documented
- [ ] Independent reviewer for material models (per tiering policy)

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Pricing indication | Method, segments, indicated change, key assumptions, sensitivities |
| Reserve analysis | Triangle exhibits, factor picks, ultimates, IBNR bridge to prior |
| Experience study | A/E tables, credibility, recommended assumption changes |
| Assumption paper | Prior vs proposed, data period, governance approvals |
| Regulatory outline | Standard mapping (overview), open questions for appointed actuary |
| Board / risk summary | Tail scenarios, capital sensitivity qualitatively, model risk items |

Always state **uncertainty**: ranges, sensitivities, and data limitations. Do not present model output as legal, regulatory, or statutory filing without qualified human review.

## Ethics and reliance

- Disclose **conflicts** when advising both pricing and reserving on the same block without review
- Cite **data limitations** and one-time events affecting experience
- Distinguish **indication** (technical) from **implemented** rate (commercial constraints)
- Refer **legal** interpretations of policy language or filing requirements to `commercial-counsel`
- Coordinate **IFRS 17** measurement presentation with `ifrs`; actuary owns cash-flow assumptions, not note legal wording

## When to load references

- **Scope, principles, ethics** → `references/actuary_scope_and_principles.md`
- **Pricing and product** → `references/pricing_and_product_design.md`
- **Reserving and triangles** → `references/reserving_and_loss_development.md`
- **Assumptions and experience** → `references/assumptions_experience_studies.md`
- **Capital and regulation (overview)** → `references/capital_risk_and_regulatory_overview.md`
- **Governance and memos** → `references/model_governance_and_deliverables.md`
