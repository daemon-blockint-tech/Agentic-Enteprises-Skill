---
name: life-health-insurance
description: |
  Guides life and health insurance—life (term, whole, universal, variable overview), health
  (individual, group, Medicare/Medicaid overview), disability and LTC, underwriting, policy provisions,
  claims and benefits administration, reinsurance, distribution, and metrics (lapse, persistency, loss
  ratio, MLR). Regulatory overview (state DOI, NAIC, ACA, HIPAA privacy—not legal advice). Use for life
  insurance, health insurance, term life, group health, underwriting life, Medicare, Medicaid, ACA,
  medical loss ratio, MLR, disability insurance, long-term care, LTC, persistency, reinsurance
  life—not P&C (property-casualty-insurance), pensions (pension-retirement-funds), actuarial modeling
  (actuary), actuarial engagements (actuarial-consulting), legal interpretation (commercial-counsel),
  or GRC without insurance context (compliance-engineer).
---

# Life and Health Insurance

## When to Use

- Explain life, health, disability, and LTC products and how individual vs group markets differ
- Walk through underwriting: risk classification, evidence of insurability, rate classes, appeals
- Clarify policy mechanics: face amount, beneficiaries, riders, exclusions, contestability
- Describe health plan design: networks, cost sharing, essential health benefits (ACA overview)
- Frame Medicare/Medicaid program context at overview level (not enrollment legal advice)
- Outline claims and benefits administration: life death claims, health claims, appeals, EOBs
- Compare distribution models (career agent, independent, broker, MGA, worksite)
- Interpret life/health metrics (lapse, persistency, loss ratio, MLR, benefit ratio)
- Outline state DOI, NAIC, ACA, and HIPAA privacy concepts—not legal or actuarial sign-off

## When NOT to Use

- Property, casualty, GL, workers comp, or commercial auto lines → `property-casualty-insurance`
- Defined benefit pensions, 401(k), or retirement plan administration → `pension-retirement-funds`
- Loss development triangles, IBNR, mortality table construction, or appointed-actuary work → `actuary`
- Actuarial consulting SOW, due diligence engagement design, or opinion support governance → `actuarial-consulting`
- Legal interpretation of policy wording, coverage disputes, or regulatory enforcement → `commercial-counsel`
- Corporate FP&A, investor metrics, or non-insurance financial modeling → `financial-analyst` (if installed)
- SOC 2 / ISO control mapping without insurance operations context → `compliance-engineer`
- Executive strategy without insurance domain detail → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| P&C lines, FNOL, occurrence vs claims-made, cat reinsurance | `property-casualty-insurance` |
| Pricing, reserving, triangles, mortality/morbidity assumptions | `actuary` |
| Actuarial engagement scoping, SOW, due diligence, opinion support | `actuarial-consulting` |
| Pension and retirement plan design, funding, ERISA context | `pension-retirement-funds` |
| Contract review, policy disputes, regulatory interpretation | `commercial-counsel` |
| Financial statements, variance, non-insurance analytics | `financial-analyst` (if installed) |
| Technical control evidence, audit packages | `compliance-engineer` |
| IFRS 17 / insurance contract measurement (accounting) | `ifrs` |
| Anti-false-positive alert triage (fraud/claims analytics) | `anti-false-positive-decision-making` |

## Core Workflows

### 1. Engagement scoping

Before analysis:

1. **Segment** — Life vs health vs DI/LTC; individual vs group; admitted vs worksite
2. **Product** — Term, permanent, major medical, ASO, Medicare supplement, etc.
3. **Decision** — Quote, renewal, claim, benefit design, reinsurance placement, filing context
4. **Jurisdiction** — State(s), ACA market, Medicare/Medicaid program rules (overview)
5. **Materiality** — Face amount, member months, network, stop-loss, prior claims experience

**See `references/life_health_insurance_scope.md`.**

### 2. Life underwriting and products

1. Define **insurable interest** and purpose (protection, estate, business)
2. Collect application, labs, APS, financials, and MIB/inspection where applicable
3. Assign **risk class** (preferred, standard, substandard, table ratings)
4. Select product: **term**, **whole**, **universal**, **variable** (overview of tradeoffs)
5. Structure face amount, beneficiaries, and riders (Waiver, ADB, etc.)
6. Bind with contestability and suicide clause awareness; track in-force changes

**See `references/life_products_and_underwriting.md`.**

### 3. Health products and markets

1. Classify market: **individual ACA**, **small/large group**, **self-funded ASO**, **government**
2. Map **benefit design**: deductible, copay, coinsurance, OOP max, network tier
3. Note **risk adjustment**, pooling, and stop-loss for group blocks
4. Outline **Medicare** (Parts A–D, MA, Medigap) and **Medicaid** (overview only)
5. Align distribution and compensation (commission, PEPM, bonuses) to segment

**See `references/health_products_and_markets.md`.**

### 4. Disability, LTC, and riders

1. Distinguish **short-term** vs **long-term** disability definitions (own occ vs any occ overview)
2. Set **elimination period**, benefit period, and offsets (SSDI, workers comp)
3. Frame **LTC** triggers (ADLs, cognitive), benefit pool, inflation options
4. Inventory **riders**: waiver of premium, ADB, chronic illness, guaranteed insurability
5. Escalate contract interpretation to `commercial-counsel`

**See `references/disability_ltc_and_riders.md`.**

### 5. Claims and benefits administration

1. **Life** — death claim intake, proof of death, beneficiary verification, contestability check
2. **Health** — eligibility, authorization, claim adjudication, COB, appeals (internal/external overview)
3. Establish **reserves** directionally; detail with `actuary`
4. Manage **fraud/SIU** referrals and documentation standards
5. Close with file quality; feed experience to underwriting and product

**See `references/claims_benefits_and_administration.md`.**

### 6. Reinsurance, metrics, and regulation

1. Select life/health **reinsurance** structures (YRT, coinsurance, excess, stop-loss)
2. Compute **lapse**, **persistency**, **loss ratio**, **MLR** (health) with defined numerators
3. Separate **attritional** vs large claims in health narrative
4. Outline **NAIC**, state DOI, **ACA** reforms, and **HIPAA** privacy context (not legal advice)
5. Map distribution economics and MGA/program oversight

**See `references/reinsurance_metrics_and_regulatory.md`.**

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Underwriting summary | Product, risk class, face/benefit, riders, open requirements |
| Coverage/benefit memo | Plan type, cost sharing, network, key exclusions, ACA/ERISA note if relevant |
| Claims status | Intake facts, eligibility/coverage position (preliminary), next steps |
| Reinsurance brief | Structure, retention, treaty type, data requirements |
| Metrics commentary | Period ratios, lapse/persistency, MLR drivers, actions |

Always label preliminary coverage positions and regulatory comments as **not legal or actuarial advice**; escalate to qualified professionals for filings, sign-off, and disputes.

## When to load references

- **Scope and segments** → `references/life_health_insurance_scope.md`
- **Life products and underwriting** → `references/life_products_and_underwriting.md`
- **Health products and markets** → `references/health_products_and_markets.md`
- **Disability, LTC, riders** → `references/disability_ltc_and_riders.md`
- **Claims and administration** → `references/claims_benefits_and_administration.md`
- **Reinsurance, metrics, regulation** → `references/reinsurance_metrics_and_regulatory.md`
