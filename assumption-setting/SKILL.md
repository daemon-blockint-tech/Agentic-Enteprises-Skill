---
name: assumption-setting
description: |
  Guides defining, documenting, and governing actuarial and risk assumptions for insurance and
  related models—mortality, morbidity, lapse, discount rates, inflation, loss development, expense,
  cat, credit; categories and sources; selection methodology and judgment; sensitivity and scenarios;
  governance and change control; pricing vs reserving vs capital packs; audit trail—not legal or
  accounting sign-off. Use for assumption setting, set assumptions, mortality/lapse/discount rate/
  loss development assumption, assumption governance, assumption documentation, assumption review,
  change assumptions—not full model build (actuary), consulting SOW (actuarial-consulting), LOB education
  (property-casualty-insurance, life-health-insurance), pensions (pension-retirement-funds), or FP&A
  without actuarial context (financial-analyst).
---

# Assumption Setting

## When to Use

- Define or update **assumption sets** for pricing, reserving, capital, or ALM models
- Document **assumption rationale**, sources, and effective dates for governance or audit
- Classify assumptions by **category** (economic, demographic, behavioral, operational)
- Apply **selection methodology** (experience, industry tables, judgment, blending)
- Design **sensitivity** and **scenario** grids tied to material drivers
- Establish **governance**: owners, approval tiers, change control, version history
- Build **assumption packs** differentiated by use case (rate indication vs valuation vs ORSA)
- Reconcile **emerging experience** vs last-approved assumptions before model runs
- Benchmark assumptions against **industry** or regulatory reference points (overview)

## When NOT to Use

- Execute full pricing indications, IBNR triangles, or reserve ultimates as primary deliverable → `actuary`
- Scope actuarial consulting engagements, SOW, due diligence, or opinion support governance → `actuarial-consulting`
- Teach P&C coverages, FNOL, or underwriting without assumption governance lens → `property-casualty-insurance`
- Teach life/health products, benefits, or distribution without assumption pack focus → `life-health-insurance`
- Pension funding, ERISA, or retirement plan design → `pension-retirement-funds`
- Corporate budgets, investor metrics, or non-insurance FP&A → `financial-analyst` (if installed)
- Executive strategy without actuarial/risk assumption workstream → `business-consultant`
- Legal interpretation of policy wording, filings, or statutory sign-off → `commercial-counsel`
- IFRS note legal wording or general ledger recognition → `ifrs`
- SOC 2 / ISO control evidence without actuarial models → `compliance-engineer`

## Related skills

| Need | Skill |
|---|---|
| Pricing, reserving, triangles, A/E studies, capital overview | `actuary` |
| Engagement scoping, SOW, due diligence, opinion support | `actuarial-consulting` |
| P&C lines, claims, cat, reinsurance product context | `property-casualty-insurance` |
| Life, health, annuity product and benefit context | `life-health-insurance` |
| DB/DC pensions, funding, demographic tables for plans | `pension-retirement-funds` |
| Financial statements, variance, non-insurance analytics | `financial-analyst` (if installed) |
| Executive strategy without assumption governance | `business-consultant` |
| IFRS 17 measurement presentation (coordinate assumptions) | `ifrs` |
| Regulatory control implementation and audit evidence | `compliance-engineer` |

## Core Workflows

### 1. Scope the assumption exercise

1. **Purpose** — Pricing, valuation, capital, ALM, planning, or stress testing
2. **Model** — Name, version, owner; which outputs consume each assumption
3. **Materiality** — Drivers ranked by impact on key metrics (LR, reserves, SCR, surplus)
4. **Population** — In-force, new business, closed block; segment dimensions
5. **Effective date** — Align with valuation date, rate filing, or budget cycle

**See `references/assumption_setting_scope_and_principles.md`.**

### 2. Inventory categories and sources

1. List assumptions by **category** (economic, demographic, behavioral, operational)
2. Map each to **source** (company experience, industry table, vendor, judgment)
3. Flag **prescribed** vs **company-specific** and jurisdictional constraints
4. Note **dependencies** (e.g., lapse tied to crediting rate; trend tied to inflation)
5. Record **data period** and quality caveats per assumption

**See `references/assumption_categories_and_sources.md`.**

### 3. Select and justify assumptions

1. Run or reference **experience studies** (A/E); coordinate with `actuary` for technical fitting
2. Apply **credibility** blending where data is thin
3. Document **expert judgment** when overriding data
4. Set **level**, **trend**, and **volatility** components separately when material
5. Compare to **benchmarks** and prior approved set; explain deltas

**See `references/selection_methodology_and_judgment.md`.**

### 4. Govern, document, and control changes

1. Assign **owner** and **approver** per assumption or pack tier
2. Version the **assumption pack** (ID, date, model compatibility)
3. Maintain **change log**: prior → proposed → approved, with rationale
4. Attach **exhibits**: A/E tables, sensitivity summary, peer review sign-off
5. Archive reproducible **data cuts** per model risk policy

**See `references/governance_documentation_and_change_control.md`.**

### 5. Sensitivities, scenarios, and stress

1. Identify **top drivers** from materiality or prior sensitivity work
2. Define **base**, **adverse**, **favorable**, and **regulatory/stress** scenarios
3. Keep grids **parsimonious**—avoid combinatorial explosion
4. Align scenarios with **risk appetite** and ORSA/capital narrative (overview)
5. Document **correlations** or explicit independence assumptions

**See `references/sensitivity_scenarios_and_stress.md`.**

### 6. Line-of-business assumption packs

1. Select pack template: **P&C**, **life/health**, **pension**, or **multi-line**
2. Pull LOB-specific drivers (e.g., development factors vs mortality improvement)
3. Cross-check pack against **product** and **regulatory** context skills
4. Separate packs for **pricing** vs **reserving** vs **capital** when conventions differ
5. Hand off model execution to `actuary` after pack is approved

**See `references/line_of_business_assumption_packs.md`.**

## Assumption pack checklist

Before models run, confirm:

- [ ] Every material driver has owner, source, and effective date
- [ ] Pricing vs valuation vs capital **basis** differences documented
- [ ] Changes from prior pack bridged with quantified impact where possible
- [ ] Sensitivities on top 3–5 drivers completed or scheduled
- [ ] Judgment overrides explicitly approved and time-bounded if interim
- [ ] No legal, statutory, or accounting **sign-off** claimed by the agent

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Assumption register | ID, name, category, value, unit, source, owner, effective date |
| Assumption paper | Executive summary, changes vs prior, studies cited, approvals |
| Governance memo | Roles, change control, model mapping, retention |
| Sensitivity exhibit | Drivers, shocks, metric impacts, scenario definitions |
| Pack manifest | Files/worksheets, model version, LOB, use case (price/reserve/capital) |

State **uncertainty** and data limitations. Do not present outputs as appointed-actuary, legal, or audit opinions.

## When to load references

- **Scope and principles** → `references/assumption_setting_scope_and_principles.md`
- **Categories and sources** → `references/assumption_categories_and_sources.md`
- **Selection and judgment** → `references/selection_methodology_and_judgment.md`
- **Governance and change control** → `references/governance_documentation_and_change_control.md`
- **Sensitivity and stress** → `references/sensitivity_scenarios_and_stress.md`
- **LOB packs** → `references/line_of_business_assumption_packs.md`
