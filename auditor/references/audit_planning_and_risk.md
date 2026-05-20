# Audit planning and risk assessment

## Table of contents

1. [Purpose](#purpose)
2. [Inputs](#inputs)
3. [Audit universe](#audit-universe)
4. [Risk assessment model](#risk-assessment-model-practical)
5. [Annual audit plan structure](#annual-audit-plan-structure)
6. [Engagement scope memo](#engagement-scope-memo-per-audit)
7. [Coordination hooks](#coordination-hooks)
8. [Ad-hoc and continuous auditing](#ad-hoc-and-continuous-auditing)
9. [Common planning pitfalls](#common-planning-pitfalls)
10. [Work products](#work-products-from-planning-phase)

## Purpose

Build a **risk-based annual audit plan** and engagement scope that allocates effort to highest-risk areas and satisfies audit committee expectations.

## Inputs

| Source | Use in planning |
|---|---|
| Enterprise risk register | Inherent risk themes |
| Prior audit reports | Repeat findings, open MAP items |
| External audit / SOC gaps | Coordination, avoid duplication |
| Incident and loss data | Emerging IT and fraud risk |
| Regulatory and customer obligations | Mandatory coverage |
| Organizational change | M&A, new systems, reorgs |
| Key risk indicators (KRIs) | Trend triggers for ad-hoc reviews |

## Audit universe

Maintain a living **audit universe** listing auditable entities:

- Legal entities and business units
- Significant processes (order-to-cash, procure-to-pay, record-to-report)
- Applications (tier by criticality, data sensitivity, custom code)
- Infrastructure (cloud accounts, identity provider, network segments)
- Third parties (critical vendors, subprocessors)
- Governance forums (board, AC, risk committee)

Tag each entity: **criticality**, **last audit date**, **inherent risk**, **residual risk**, **planned period**.

## Risk assessment model (practical)

Score **inherent risk** (1–5) using factors:

| Factor | Examples raising score |
|---|---|
| Financial magnitude | Revenue, payroll, treasury |
| Complexity | Custom dev, multi-entity, estimates |
| Volume | High transaction counts |
| Regulation | PCI, HIPAA, SOX, sector rules |
| Change | New ERP, migration, reorg |
| History | Prior deficiencies, incidents |
| Dependency | Single vendor, fragile manual controls |

Adjust for **mitigation** (control maturity, automation, monitoring) to estimate **residual risk**.

**Plan priority:** residual risk high OR last test > N years OR mandatory cycle.

## Annual audit plan structure

```text
Section 1 — Executive summary (themes, hours, co-source needs)
Section 2 — Risk assessment methodology
Section 3 — Planned engagements (table)
Section 4 — Resource and skill gaps
Section 5 — Dependencies (external audit, SOC window)
Section 6 — Budget and co-source / guest auditor
Appendix — Full universe with ratings
```

### Planned engagement table (columns)

| Field | Description |
|---|---|
| Engagement ID | Tracker key |
| Name | e.g., "ITGC — Logical Access" |
| Risk rating | H/M/L |
| Objectives | 2–4 bullets |
| Scope systems | Apps, IdP, cloud |
| Period | Calendar / fiscal |
| Hours | Estimate |
| Skills | IT, data analytics |
| AC approval | Y/N date |

## Engagement scope memo (per audit)

Minimum elements:

1. **Background** and drivers
2. **Objectives** (what assurance is sought)
3. **Scope** — in/out, systems, locations, period
4. **Approach** — walkthrough, test types, analytics
5. **Criteria** — policies, SOC TSC, SOX ITGC library
6. **Timeline** and milestones
7. **Team** and client contacts
8. **Deliverables** — report date, draft review
9. **Limitations** — access, timing, reliance on management reps

## Coordination hooks

- **External auditors:** agree reliance on internal IT audit work; document scope split
- **SOC observation:** align ITGC tests with Type II period boundaries
- **Compliance-engineer:** note where automated evidence may reduce sample size (document reliance, not blind trust)

## Ad-hoc and continuous auditing

Trigger **unplanned** work when:

- Critical incident (breach, fraud allegation, outage)
- Major change without pre-implementation review
- Whistleblower or regulator inquiry support (factual inventory only)
- KRI threshold breach

Document **why** the plan changed and obtain CAE / AC notification per charter.

## Common planning pitfalls

| Pitfall | Mitigation |
|---|---|
| Checkbox rotation without risk refresh | Re-score universe annually |
| Scope creep mid-engagement | Change memo + hour reforecast |
| Duplicating SOC external work | Map criteria once; retest gaps only |
| Understaffing ITGC | Bundle access + change + ops by platform |
| No follow-up capacity | Reserve % hours for retest |

## Work products from planning phase

- Risk-assessed **audit universe** (spreadsheet or GRC tool export)
- **Annual audit plan** (AC-approved)
- **Engagement scope memo** (signed by CAE or lead)
- **Audit program outline** (control list draft before fieldwork)
