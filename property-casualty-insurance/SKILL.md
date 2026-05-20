---
name: property-casualty-insurance
description: |
  Guides property and casualty (P&C) insurance—commercial and personal lines, major LOBs (property,
  GL, workers comp, commercial auto, umbrella, specialty), underwriting and risk selection, policy
  triggers (occurrence vs claims-made), limits and exclusions, claims (FNOL, reserving, litigation),
  reinsurance and catastrophe, distribution (agents, brokers, MGAs), metrics (loss ratio, combined
  ratio, cat load), and state DOI/rate filing overview—not legal advice. Use for P&C insurance,
  property and casualty, commercial lines, workers comp, general liability, combined ratio, loss
  ratio, underwriting, claims-made, occurrence policy, reinsurance, catastrophe, MGA, rate filing,
  or FNOL—not actuarial modeling (actuary), life/health depth, legal interpretation
  (commercial-counsel), or GRC controls without insurance context (compliance-engineer).
---

# Property and Casualty Insurance

## When to Use

- Explain P&C lines, coverages, and how commercial vs personal programs differ
- Walk through underwriting workflow: appetite, submission, quote, bind, endorsements
- Clarify policy mechanics: occurrence vs claims-made, limits, deductibles, exclusions, triggers
- Describe claims lifecycle from FNOL through investigation, reserving, settlement, litigation
- Frame reinsurance structures and catastrophe risk transfer at overview level
- Compare distribution models (agent, broker, MGA, direct) and typical economics
- Interpret underwriting and profitability metrics (loss ratio, expense ratio, combined ratio)
- Outline state insurance regulation concepts (DOI oversight, rate/form filing)—not legal advice
- Support business cases, operating reviews, or due diligence with P&C domain context

## When NOT to Use

- Life, health, annuity, or long-term care product design and pricing depth → dedicated life/health skills if available; otherwise note limitation
- Loss development triangles, IBNR methods, credibility studies, or appointed-actuary sign-off → `actuary`
- Legal interpretation of policy wording, coverage disputes, or regulatory enforcement → `commercial-counsel`
- Corporate FP&A, investor metrics, or non-insurance financial modeling → `financial-analyst` (if installed)
- SOC 2 / ISO control mapping without insurance operations context → `compliance-engineer`
- Executive strategy without insurance domain detail → `business-consultant`
- Enterprise risk registers unrelated to underwriting/claims → `security-risk-analyst` (if installed)
- AML/financial crime or sanctions programs → `aml-compliance`, `financial-intelligence-unit`

## Related skills

| Need | Skill |
|---|---|
| Pricing, reserving, triangles, IBNR, assumption governance | `actuary` |
| Contract review, policy wording disputes, regulatory interpretation | `commercial-counsel` |
| Business case, operating model, transformation | `business-consultant` |
| Technical control evidence, audit packages | `compliance-engineer` |
| GRC program charter and gap plans (non-insurance-specific) | `compliance-specialist` |
| IFRS 17 / insurance contract measurement (accounting) | `ifrs` |
| Financial statements and close packs | `financial-statements` (if installed) |
| Vendor and cyber third-party risk | `vendor-cyber-risk-analyst` |
| Anti-false-positive alert triage (fraud/claims analytics) | `anti-false-positive-decision-making` |

## Core Workflows

### 1. Engagement scoping

Before analysis:

1. **Segment** — Personal vs commercial; admitted vs surplus; program vs single policy
2. **Line of business** — Property, GL, WC, auto, umbrella, specialty, package
3. **Decision** — Quote, renewal, claims handling, reinsurance placement, regulatory filing context
4. **Jurisdiction** — State(s), filing status, experience mod (WC), territory
5. **Materiality** — Limits, deductibles, cat exposure, class codes, prior loss history

**See `references/pc_insurance_scope_and_lines.md`.**

### 2. Underwriting and risk selection

1. Define **appetite** and declination triggers (class, geography, limit profile)
2. Ingest submission: application, loss runs, SOV, financials, inspections
3. Apply **rating** variables and manual vs filed factors; document debits/credits
4. Set terms: limits, deductibles/SIR, endorsements, subjectivities
5. Price to target **loss ratio** and combined ratio; note reinsurance and cat load
6. Bind with clear conditions; track endorsements and mid-term changes

**See `references/underwriting_and_risk_selection.md`.**

### 3. Policy coverage and forms

1. Identify **coverage part** (CG, CP, CA, WC, etc.) and edition date
2. Map **insuring agreement**, exclusions, conditions, and endorsements
3. Confirm **trigger** (occurrence vs claims-made) and retro dates where applicable
4. Reconcile **limits** (per occurrence, aggregate, sublimits) and **deductibles/SIR**
5. Flag common gaps (ordinance/law, BI waiting period, employee injury exclusions)
6. Escalate wording disputes to `commercial-counsel`

**See `references/policy_coverage_and_forms.md`.**

### 4. Claims lifecycle

1. **FNOL** — capture facts, policy verification, coverage preliminary
2. Assign adjuster; establish reserves (case, IBNR directionally—detail with `actuary`)
3. Investigate liability and damages; manage vendors and counsel
4. Negotiate settlement; subrogation and salvage where applicable
5. Close with file documentation; feed experience to underwriting

**See `references/claims_lifecycle_and_handling.md`.**

### 5. Reinsurance and catastrophe

1. Classify **peril** and geographic cat accumulation
2. Select structure: quota share, surplus, per-risk XOL, cat XOL, cat bonds (overview)
3. Align retentions and reinstatements to capital and rating agency context
4. Coordinate with pricing cat load and aggregate monitoring

**See `references/reinsurance_and_catastrophe.md`.**

### 6. Metrics, regulation, and operations

1. Compute and interpret **loss**, **expense**, and **combined** ratios
2. Separate **attritional** vs **cat** and large-loss development in narrative
3. Outline **DOI** filing, market conduct, and financial examination concepts
4. Map distribution economics (commission, MGA overrides, profit sharing)

**See `references/metrics_regulatory_and_operations.md`.**

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Underwriting summary | Risk description, appetite fit, terms, pricing rationale, open items |
| Coverage memo | Form edition, triggers, limits/deductibles, key exclusions, gaps |
| Claims status | FNOL facts, coverage position (preliminary), reserves, next steps |
| Reinsurance brief | Structure, layer, retention, reinstatement, cat aggregation note |
| Metrics commentary | Period ratios, drivers, cat/large loss callouts, actions |

Always label preliminary coverage positions and regulatory comments as **not legal or actuarial advice**; escalate to qualified professionals for filings, sign-off, and disputes.

## When to load references

- **Scope and LOBs** → `references/pc_insurance_scope_and_lines.md`
- **Underwriting** → `references/underwriting_and_risk_selection.md`
- **Policy and coverage** → `references/policy_coverage_and_forms.md`
- **Claims** → `references/claims_lifecycle_and_handling.md`
- **Reinsurance and cat** → `references/reinsurance_and_catastrophe.md`
- **Metrics and regulation** → `references/metrics_regulatory_and_operations.md`
