# Stakeholders and assurance interfaces

## Table of contents

1. [Stakeholder map](#stakeholder-map)
2. [RACI for lifecycle governance](#raci-for-lifecycle-governance)
3. [Assurance and security interfaces](#assurance-and-security-interfaces)
4. [DevSecOps interface](#devsecops-interface)
5. [ISSO and ATO interface (generic)](#isso-and-ato-interface-generic)
6. [Operations and reliability peers](#operations-and-reliability-peers)
7. [Executive and program interfaces](#executive-and-program-interfaces)
8. [Communication patterns](#communication-patterns)

## Stakeholder map

| Stakeholder | Lifecycle interest |
|---|---|
| **Lifecycle sponsor** | Charter authority, gate escalation, retire decisions |
| **System owner** | Baseline truth, sustainment, risk acceptance |
| **Engineering lead** | Build/verify execution, traceability quality |
| **Architecture** | Design baseline, integration standards |
| **Operations / SRE** | Runbooks, drift, incidents, capacity |
| **Assurance / security** | Assessments, control mapping, findings |
| **ISSO / authorization (program)** | ATO boundary, continuous monitoring hooks |
| **DevSecOps** | Pipeline gates, SBOM, deployment controls |
| **Compliance engineering** | Evidence automation (`compliance-engineer`) |
| **Program management** | Schedule, funding (`technical-program-manager`) |
| **Legal / privacy** | Disposition, contracts (escalation) |

## RACI for lifecycle governance

| Activity | Sponsor | System owner | Engineering | Ops | Assurance | ISSO |
|---|---|---|---|---|---|---|
| Lifecycle charter | A | R | C | C | C | I |
| Gate criteria | A | R | C | C | C | I |
| Gate decision | A | R | C | C | C | I |
| Baseline manifest | I | A | R | C | I | I |
| Traceability matrix | I | A | R | I | C | I |
| Sustainment review | C | A | R | R | C | I |
| Decommission plan | A | R | C | R | C | C |
| Data disposition | I | R | C | C | C | I |

**Legend:** R = responsible, A = accountable, C = consulted, I = informed.

Adjust for org size; **single-person teams** must document **independence compensations**.

## Assurance and security interfaces

Lifecycle **provides**; assurance **consumes and assesses**:

| Provided artifact | Assurance use |
|---|---|
| Gate records | Control operating effectiveness samples |
| Threat model pointer | Risk treatment verification |
| Test and scan summaries | Vulnerability management evidence |
| Baseline manifest | Configuration management audits |

| Assurance provides | Lifecycle use |
|---|---|
| Assessment findings | Verify-phase remediation inputs |
| Security requirements | Design and traceability seeds |
| Pen test scope/results | Gate 4 evidence (interface) |

Do **not** close assurance findings in lifecycle records without assurance acknowledgment.

## DevSecOps interface

| DevSecOps delivers | Lifecycle binds to |
|---|---|
| Pipeline policy (branch protection, scans) | Build/verify gates |
| SBOM and provenance | Build baseline manifest |
| Deployment automation logs | Deploy gate evidence |
| Secret scanning / IaC policy | Drift and change detection |

**Handoff:** each production baseline promotion references **pipeline run IDs** and **artifact digests**.

Pair `classified-software-devsecops-engineer` when **cleared pipeline** rules apply; lifecycle still owns **phase gates and baselines**.

## ISSO and ATO interface (generic)

**NDA-safe framing only:**

- Map lifecycle gates to **authorization boundary** milestones (e.g., assessment before production)
- Supply **continuous monitoring** hooks: baseline change notifications, inventory updates
- Do **not** author System Security Plans or control implementations as ISSO
- Track **ATO conditions** as inputs to gate criteria and sustainment reviews

When program is **classified**, use generic program labels; detailed accreditation → cleared cyber peers.

## Operations and reliability peers

| Peer | Interface |
|---|---|
| `site-reliability-engineer` | SLOs, error budgets—within operational baseline |
| `incident-management-engineer` | SEV process during operate phase |
| `cyber-resilience-engineer` | Recovery evidence supports sustainment |
| `bcm-disaster-recovery-specialist` | Enterprise DR vs system lifecycle retire |

Lifecycle defines **which baseline** was live during incidents and drills.

## Executive and program interfaces

| Need | Peer |
|---|---|
| Cross-team delivery schedule | `technical-program-manager` |
| Infra portfolio and capex | `vp-of-infrastructure` |
| Criticality and tier governance | `mission-critical` |
| Prevention culture | `zero-tolerance-for-failure` |

**Executive brief** (quarterly for high assurance): phase status, gate waivers, obsolescence risks, retire candidates.

## Communication patterns

| Audience | Message | Cadence |
|---|---|---|
| Steering / exec | Phase, gates, top risks, EOL | Quarterly |
| Engineering | Baseline promotions, trace gaps | Per sprint / per release |
| Ops | Manifest updates, runbook changes | Per promotion |
| Assurance | Gate packets, open findings | Per gate |
| Dependents | Interface changes, retire notice | As needed |

Keep communications **factual and artifact-linked**—avoid status without baseline IDs.
