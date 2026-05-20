# BCM and disaster recovery scope

## Table of contents

1. [Program purpose](#program-purpose)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Roles and RACI](#roles-and-raci)
5. [Lifecycle and cadence](#lifecycle-and-cadence)
6. [Handoffs](#handoffs)

## Program purpose

Establish **security-focused** continuity and recovery so the organization can:

- Restore **identity, detection, and logging** within agreed RTO/RPO after cyber or infrastructure events
- Execute **documented recovery** for ransomware, wipers, and prolonged identity or SaaS outages
- Prove **restore capability** through tested backups and exercised playbooks
- Coordinate **prolonged recovery comms** with incident response without owning the war room

This skill addresses **program design, analysis, playbooks, and exercises**—not live operations.

## In scope

| Area | Examples |
|---|---|
| BIA | Security services, IdP, SIEM/SOAR, EDR, KMS, CASB, PKI, vault, audit log pipelines |
| Objectives | RTO, RPO, MTPD, recovery tiers, workarounds |
| Plans | BCP, DRP, cyber recovery annex, crisis comms outline tied to IR |
| Cyber recovery | Ransomware/wiper paths, clean rebuild, segmented recovery |
| Backups | Immutability, air-gap, retention vs legal/regulatory hold |
| Testing | Restore tests, tabletop exercises, after-action tracking |
| Governance | Policy hooks, metrics, regulatory BCM mapping (high level) |

## Out of scope

| Topic | Route to |
|---|---|
| Live CSIRT command, containment, forensics | `incident-responder`, `digital-forensics-analyst` |
| SOC queue triage | `soc-analyst` |
| SEV/on-call/paging design | `incident-management-engineer` |
| SLO/error budget operations | `site-reliability-engineer` |
| Ticket-level snapshot restore | `cloud-system-administrator` |
| Greenfield cloud/K8s build | `cloud-engineer`, `infrastructure-engineer` |
| Control implementation (EDR rules, IAM) | `information-security-engineer` |
| Legal notification decisions | Legal/compliance; fact packs via `incident-responder` |
| VP portfolio and multi-year capex | `vp-of-infrastructure` |

## Roles and RACI

| Activity | BCM/DR lead | IR commander | SRE/platform | Security eng | Legal/comms |
|---|---|---|---|---|---|
| BIA and tiering | **A/R** | C | C | C | I |
| RTO/RPO approval | **R** | C | C | C | I |
| BCP/DRP maintenance | **A/R** | C | C | C | I |
| Activate BCP during incident | C | **A** (SEV/security) | R | C | C |
| Ransomware recovery playbook | **R** | **A** during event | C | C | C |
| Restore test execution | **A** | I | **R** | C | I |
| Tabletop facilitation | **R** | C | C | C | C |
| Customer/regulatory messaging | I | C | I | I | **A** |

**A** = accountable, **R** = responsible, **C** = consulted, **I** = informed.

## Lifecycle and cadence

1. **Annual** — refresh BIA, RTO/RPO register, executive brief
2. **Semi-annual** — restore tests for tier-0/1 security and identity systems
3. **Quarterly** — tabletop (rotate cyber, regional, IdP, logging-loss scenarios)
4. **Per major change** — update dependencies when IdP, logging, or SOC stack changes
5. **Post-incident** — feed real RTO/RPO and gaps into plan updates within 30 days

## Handoffs

**From IR (`incident-responder`):** After containment, provide recovery sequencing, rebuild criteria, and comms templates for prolonged outage.

**To IR:** During BCP activation for security incidents, IR owns timeline and evidence; BCM owns recovery milestones and service restoration order.

**To SRE (`site-reliability-engineer`):** Customer-facing SLO impact and mitigation; BCM owns security-service recovery order and backup validation.

**To cloud ops (`cloud-system-administrator`):** Execute restores per runbook; BCM defines scope, success criteria, and test schedule.
