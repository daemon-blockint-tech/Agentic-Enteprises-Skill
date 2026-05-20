# Extreme lifecycle scope

## Table of contents

1. [Purpose and boundaries](#purpose-and-boundaries)
2. [What “extreme lifecycle” means](#what-extreme-lifecycle-means)
3. [System boundary and assurance level](#system-boundary-and-assurance-level)
4. [In scope vs out of scope](#in-scope-vs-out-of-scope)
5. [Lifecycle charter elements](#lifecycle-charter-elements)
6. [Regulated and classified contexts (generic)](#regulated-and-classified-contexts-generic)
7. [Deliverables and review cadence](#deliverables-and-review-cadence)

## Purpose and boundaries

**Extreme lifecycle governance** is the discipline of managing a system from **concept through retirement** when failure, corruption, or unauthorized change has severe impact—mission-critical operations, high assurance, or zero-failure-tolerance environments.

This skill owns **phase structure, gates, baselines, traceability, sustainment, and retirement**—not:

| Peer | Focus |
|---|---|
| `mission-critical` | Tiering, objectives, architecture patterns by criticality |
| `zero-tolerance-for-failure` | Prevention culture, HRO, verification mindset |
| `technical-program-manager` | Cross-team milestones and RAID without lifecycle baselines |
| `classified-software-devsecops-engineer` | Cleared build/release pipeline mechanics |
| `compliance-engineer` | Control automation and audit evidence pipelines |

## What “extreme lifecycle” means

**Extreme** signals that lifecycle decisions are **gated, evidenced, and traced**—not that every project uses heavyweight waterfall.

Characteristics:

- **Phase exit criteria** are explicit; skipping phases requires documented waiver
- **Configuration baselines** are authoritative for what runs in each environment
- **Sustainment** includes obsolescence, vendor support, and tech refresh—not only uptime
- **Retirement** includes data disposition and verification of shutdown

Contrast with generic agile: backlogs and sprints **implement** work inside phases; they do not replace gates or baselines.

## System boundary and assurance level

Document in the lifecycle charter:

| Element | Content |
|---|---|
| **System name and ID** | Unique identifier in CMDB or architecture repository |
| **Boundary** | In-scope components, interfaces, data stores, environments |
| **Exclusions** | Adjacent systems owned elsewhere; shared platforms with separate baselines |
| **Assurance level** | High / moderate / low—or org-specific labels tied to impact |
| **Data classes** | Generic sensitivity (public, internal, regulated, classified tier label without spillage) |
| **Dependencies** | Upstream/downstream with baseline coupling notes |

Pair with `mission-critical` when **tiering** and **RTO/RPO** must align to lifecycle gates.

## In scope vs out of scope

| In scope | Out of scope (delegate) |
|---|---|
| Lifecycle phase map and gate criteria | Day-to-day sprint facilitation |
| Traceability matrix structure and gap remediation | Formal proof obligations → `software-assurance-formal-methods-specialist` |
| Baseline identification and change authorization | ISSO/ATO package authorship |
| Obsolescence and tech-refresh planning | Enterprise infra capex portfolio → `vp-of-infrastructure` |
| Decommissioning and data disposition sequencing | Legal hold and litigation strategy → counsel |
| Assurance interface definitions | Penetration test execution → `penetration-tester` |

## Lifecycle charter elements

Minimum charter sections:

1. **Executive summary** — mission, assurance drivers, lifecycle sponsor
2. **Authority** — who may approve phase transitions, baselines, and waivers
3. **Phase model** — see `lifecycle_phases_and_gates.md`
4. **Evidence standards** — types, retention, independence → `traceability_and_evidence.md`
5. **Baseline policy** — naming, promotion, emergency change → `change_baseline_and_retirement.md`
6. **Sustainment cadence** — reviews, EOL triggers → `operate_sustain_and_obsolescence.md`
7. **Retirement triggers** — when dispose phase starts
8. **RACI** — see `stakeholders_and_assurance_interfaces.md`

## Regulated and classified contexts (generic)

Operate **NDA-safe**:

- Describe **control families** and **authorization interfaces** without customer-specific control text
- Use **generic clearance / program labels** only when the user confirms they may be referenced
- Do not paste **export-controlled** technical data, schematics, or operational identifiers
- Map lifecycle gates to **common patterns** (e.g., security assessment before production baseline) without inventing legal obligations

When cleared pipeline mechanics dominate, **pair** `classified-software-devsecops-engineer` and keep this skill on **lifecycle evidence and baselines**.

## Deliverables and review cadence

| Deliverable | Typical cadence |
|---|---|
| Lifecycle charter | At program start; annual refresh |
| Gate readiness packets | Per phase transition |
| Traceability matrix | Continuous; gate freeze snapshot |
| Baseline manifest | Each approved release to production |
| Obsolescence register | Quarterly sustainment review |
| Decommissioning plan | Triggered at EOL decision |

**Exit:** charter approved by lifecycle sponsor and system owner; peer skills engaged where boundaries apply.
