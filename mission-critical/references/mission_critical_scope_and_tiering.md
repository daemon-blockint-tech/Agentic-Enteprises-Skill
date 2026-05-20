# Mission-critical scope and tiering

## Table of contents

1. [Purpose and boundaries](#purpose-and-boundaries)
2. [Criticality tiers](#criticality-tiers)
3. [Classification criteria](#classification-criteria)
4. [Sector and contractual drivers](#sector-and-contractual-drivers)
5. [Stakeholders and RACI](#stakeholders-and-raci)
6. [Deliverables and review cadence](#deliverables-and-review-cadence)

## Purpose and boundaries

**Mission-critical systems engineering** frames how services are **classified, designed, operated, and governed** when outage or corruption causes severe harm—safety, legal/regulatory breach, large financial loss, or loss of essential public function.

This skill is a **design and governance lens**. It complements:

| Peer | Focus |
|---|---|
| `site-reliability-engineer` | Steady-state SLOs, error budgets, toil |
| `zero-tolerance-for-failure` | Prevention culture, HRO, verification gates |
| `cyber-resilience-engineer` | Recovery architecture and restore evidence |
| `senior-system-architecture` | General NFRs and integration patterns |
| `enterprise-security-architect` | Enterprise security reference architecture |

You own **tiering, objectives, and proportional controls**—not incident command, BCM policy ownership, or SRE math alone.

## Criticality tiers

Use a **small, enforced taxonomy** (example—adapt names to org glossary):

| Tier | Label | Typical impact if failed |
|---|---|---|
| **0** | Mission-critical | Loss of life, major safety event, systemic market/public-service failure, or severe regulatory sanction |
| **1** | Business-critical | Material revenue/regulatory breach; widespread customer incapacity; multi-hour executive crisis |
| **2** | Important | Degraded experience for many users; recoverable within business day with workarounds |
| **3** | Standard | Limited blast radius; standard IT change and monitoring |

**Rules:**

- **One tier per service** in the register; subcomponents may differ only with documented decomposition
- **Tier 0/1** require named **service owner**, **deputy**, and **executive sponsor**
- **Down-tiering** needs written rationale and risk acceptance—not budget convenience

## Classification criteria

Score each dimension; highest sustained score drives tier (document overrides):

| Dimension | Questions |
|---|---|
| **Safety** | Could failure cause injury, loss of life, or unsafe physical state? |
| **Legal / regulatory** | Mandatory reporting, license to operate, or sector rules (finance, health, utilities)? |
| **Financial** | Revenue, settlement, or liability beyond delegated authority? |
| **Operational continuity** | Essential function for customers, citizens, or warfighter mission (generic)? |
| **Data integrity** | Corruption worse than outage (ledger, dosing, control commands, evidence)? |
| **Dependency centrality** | Many Tier 0/1 services depend on this component? |
| **Recoverability** | Is rebuild/restore unproven or longer than MTPD without workaround? |

**Anti-patterns:** labeling everything Tier 0; tiering by team prestige; ignoring **integrity** and **covert change** scenarios.

## Sector and contractual drivers

Frame drivers **generically**—do not invent customer-specific obligations:

| Sector (generic) | Common drivers |
|---|---|
| **Finance** | Market integrity, settlement windows, record accuracy, operational resilience expectations |
| **Healthcare** | Patient safety, PHI integrity, care continuity, device/software safety classes |
| **Public safety / utilities** | Service continuity, SCADA/OT safety interlocks, emergency communications |
| **Defense industrial base** | Mission assurance, supply chain integrity, export/control interfaces (pair `classified-cyber-security-senior-manager` when cleared) |

Extract **contractual SLAs**, **audit clauses**, and **notification timelines** into the criticality register as **constraints**, not legal advice.

## Stakeholders and RACI

| Role | Responsibility |
|---|---|
| **Service owner** | Tier proposal, objectives, dependency truth, runbook currency |
| **Architecture / platform** | Pattern standards, shared fate reviews, control-plane tiering |
| **SRE / operations** | Measurement, alerting hooks, drill participation |
| **Security / GRC** | Integrity class, regulatory mapping inputs |
| **BCM** | MTPD alignment, exercise calendar (`bcm-disaster-recovery-specialist`) |
| **Executive sponsor** | Tier 0/1 risk acceptance, investment prioritization |

## Deliverables and review cadence

| Artifact | Minimum content | Review |
|---|---|---|
| **Criticality register** | Tier, owner, drivers, objectives link, dependencies | Quarterly; after major architecture change |
| **Tier decision record** | Criteria scores, dissent, approver | Per promotion to Tier 0/1 |
| **Exception log** | Temporary down-tier or control gap with expiry | Monthly until closed |

Escalate unresolved tier disputes to architecture review with explicit **residual risk** statement.
