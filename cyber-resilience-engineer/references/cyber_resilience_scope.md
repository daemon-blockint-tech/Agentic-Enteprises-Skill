# Cyber resilience scope

## Table of contents

1. [Purpose and boundaries](#purpose-and-boundaries)
2. [In scope vs out of scope](#in-scope-vs-out-of-scope)
3. [Stakeholders and interfaces](#stakeholders-and-interfaces)
4. [NIST CSF Recover alignment](#nist-csf-recover-alignment)
5. [Deliverables and lifecycle](#deliverables-and-lifecycle)
6. [Maturity model](#maturity-model)

## Purpose and boundaries

**Cyber resilience engineering** designs how the organization **withstands, adapts to, and recovers** from cyber disruptions while preserving critical security and business functions. It sits between:

- **BCM/DR program** (`bcm-disaster-recovery-specialist`) — policy, BIA, regulatory BCM, crisis comms cadence
- **Incident response** (`incident-responder`) — live containment, investigation, evidence
- **Reliability engineering** (`site-reliability-engineer`) — steady-state SLOs, capacity, toil reduction

You own **how systems are built and tested to recover**, not who declares incidents or signs BCM policy.

## In scope vs out of scope

| In scope | Out of scope (route to peer skill) |
|---|---|
| RTO/RPO architecture, tiering, recovery strategy selection | Enterprise BCM charter and regulatory interpretation → `bcm-disaster-recovery-specialist` |
| Backup topology, immutability, restore validation design | Ticket-level restore execution → `cloud-system-administrator` |
| Dependency maps, blast radius, failure-domain design | War-room command and containment → `incident-responder` |
| Attack-scenario **engineering** playbooks (sequences, gates) | SEV/on-call program design → `incident-management-engineer` |
| Chaos/game days, restore drills, evidence packs | Control mapping and audit workpapers → `compliance-specialist` |
| Resilience KPIs and engineering briefs | Board strategy and risk appetite → `chief-information-security-officer` |
| Cloud DR patterns (regions, replication) with recovery fit | Full landing-zone build without recovery lens → `cloud-engineer` |

## Stakeholders and interfaces

| Function | Your ask | Their ask |
|---|---|---|
| BCM | Tier inputs, MTPD, exercise calendar | Approved RTO/RPO, test evidence, gap remediation |
| IR / CSIRT | Playbook handoffs, isolation constraints | Forensic go/no-go on restore-in-place |
| SRE / Platform | Failure injection windows, dependency truth | SLO impact during tests; automation hooks |
| Security engineering | IdP/SIEM/EDR recovery order | Control implementation priorities |
| App owners | Service criticality, data classes | Runbook steps, validation criteria |
| Legal / Compliance | Retention and notification constraints | Not legal advice—escalate interpretations |

Document **RACI** in the resilience charter: who approves tier changes, who authorizes chaos in production, who signs test exceptions.

## NIST CSF Recover alignment

Map engineering work to **Recover** categories (CSF 2.0):

| Category | Engineering focus |
|---|---|
| **RC.RP** Recovery planning | Playbooks, runbooks, dependency maps, activation criteria |
| **RC.IM** Improvements | Post-test and post-incident remediation backlog |
| **RC.CO** Communications | Technical status inputs to comms (`bcm-disaster-recovery-specialist` owns cadence) |
| **RC.MA** Recovery activities | Restore sequences, rebuild-from-gold, validation scripts |
| **RC.SC** Supply chain | Third-party SaaS RTO/RPO, exit paths, API dependencies |

Pair with **Identify** (asset inventory) and **Protect** (immutable backups) implementations from `information-security-engineer` where controls are missing.

## Deliverables and lifecycle

1. **Charter** — scope, owners, interfaces, escalation
2. **Architecture** — tiers, backup design, regions, isolation
3. **Registers** — RTO/RPO, dependencies, SaaS recovery contacts
4. **Playbooks** — per attack scenario with decision trees
5. **Test calendar** — restore, tabletop, chaos; linked evidence store
6. **Metrics** — RTA, test pass rate, coverage by tier
7. **Annual refresh** — after major architecture, M&A, or material incident

Store evidence (reports, screenshots, RTA logs) in a **durable, access-controlled** repository—not only in chat.

## Maturity model

| Level | Characteristics |
|---|---|
| **1 Ad hoc** | Backups exist; no tiering; restores untested |
| **2 Defined** | RTO/RPO documented; annual restore test for subset |
| **3 Managed** | Tier coverage >80%; game days; immutable backups for crown jewels |
| **4 Measured** | RTA tracked vs RTO; chaos in non-prod; SaaS register complete |
| **5 Optimized** | Continuous validation; automated restore checks; lessons drive architecture |

Target **level 3+** for tier-0/1 security services (IdP, logging, KMS) before claiming "cyber resilient."
