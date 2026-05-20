# Framework scoping and mapping

## Table of contents

1. [Framework selection](#framework-selection)
2. [Scoping decisions](#scoping-decisions)
3. [Control matrix structure](#control-matrix-structure)
4. [Common mappings](#common-mappings)

## Framework selection

| Driver | Typical frameworks | Notes |
|---|---|---|
| B2B SaaS sales | SOC 2 Type II | Trust Service Criteria selection drives effort |
| Global enterprise customers | ISO 27001 | Annex A control subset; statement of applicability |
| US healthcare data | HIPAA Security Rule | BAA chain with cloud and subprocessors |
| Payment card data | PCI DSS | Scope reduction via segmentation and SAQ path |
| EU/UK personal data | GDPR-style program | Pair with `commercial-counsel` for lawful basis; technical measures to engineering |
| US federal customers | FedRAMP (moderate/high) | Often routes to `cloud-compliance-specialist` |

Select **one primary** framework for the first certification cycle; map others as overlays to avoid duplicate work.

## Scoping decisions

Document explicitly:

- **Legal entities** and brands covered by report
- **Products and services** in scope (version, region)
- **Environments** — production only vs include staging with customer data
- **Subprocessors** — list with function, data types, region
- **Exclusions** — legacy systems, acquired units, dev laptops without prod access
- **Trust criteria / control families** out of scope with approver sign-off

Refresh scope when launching new regions, AI features processing personal data, or material vendor changes.

## Control matrix structure

Use one row per control requirement with columns:

| Column | Content |
|---|---|
| Framework ID | e.g., CC6.1, A.8.2, 164.312(a)(1) |
| Requirement summary | Plain language |
| Policy ref | Linked approved policy |
| Procedure ref | Runbook or SOP |
| Technical control | What must be true (not how to code) |
| Owner | Name + backup |
| Evidence type | Export, ticket, attestation, config report |
| Frequency | Continuous, monthly, quarterly, annual |
| Status | Implemented / partial / gap / N/A |
| Notes | Dependencies, inherited controls |

Keep **implementation detail** in engineering runbooks; matrix stays assessor-readable.

## Common mappings

### SOC 2 ↔ ISO 27001 (illustrative)

Many organizations map:

- CC6 (logical access) ↔ A.5, A.8 identity and access
- CC7 (system operations) ↔ A.8 operations security
- CC8 (change management) ↔ A.8 change control
- C1 (confidentiality) ↔ A.5 information classification

Maintain a **crosswalk tab** only where dual reporting is required; do not maintain two conflicting definitions of the same control.

### HIPAA ↔ SOC 2

Map administrative, physical, and technical safeguards to TSC where customers ask for both. Flag gaps where HIPAA requires elements not in selected TSC (document compensating narrative).

### PCI scoping

Confirm CDE boundaries, connected systems, and segmentation evidence requirements early. Engage `cloud-compliance-specialist` when CDE is in cloud.

**Escalate** novel regulatory questions to `commercial-counsel`; do not interpret statute.
