# Tabletop exercises and governance

## Table of contents

1. [Governance model](#governance-model)
2. [Policy and plan artifacts](#policy-and-plan-artifacts)
3. [Exercise types](#exercise-types)
4. [Designing a tabletop](#designing-a-tabletop)
5. [Scenarios and injects](#scenarios-and-injects)
6. [Facilitation and scoring](#facilitation-and-scoring)
7. [After-action and tracking](#after-action-and-tracking)
8. [Regulatory BCM (high level)](#regulatory-bcm-high-level)

## Governance model

| Body | Purpose | Cadence |
|---|---|---|
| BCM steering | Priorities, budget, risk acceptance | Quarterly |
| Plan owners | Maintain BCP/DRP sections | Ongoing |
| Exercise calendar | Schedule tabletops and restore tests | Annual publish |
| Post-incident feed | Real events → plan updates | Per major incident |

**Executive sponsor** (CISO, CIO, or COO delegate) chairs steering; BCM lead runs day-to-day.

Integrate with **risk register** (`security-risk-analyst`) and **GRC** (`compliance-specialist`)—do not duplicate.

## Policy and plan artifacts

Minimum document set:

| Artifact | Contents |
|---|---|
| BCM policy | Scope, roles, testing mandate, exception process |
| BCP | Business priorities, workarounds, comms tree, relocation if any |
| DRP | Technical recovery, systems, dependencies, activation |
| Cyber recovery annex | Ransomware, IdP, logging loss; links to IR playbooks |
| Crisis comms outline | Cadence, audiences; defers wording to `communication-lead` |
| RTO/RPO register | Authoritative objectives and owners |

Version control: **annual** review minimum; **emergency** revision after failed test or major incident.

## Exercise types

| Type | Effort | Value |
|---|---|---|
| Discussion tabletop | Low | Roles, decisions, gaps |
| Functional drill | Medium | Single system restore or failover |
| Full simulation | High | Multi-team, production-like (rare) |
| Parallel IR exercise | Medium | Joint with `incident-responder` scenario |

Rotate **cyber** and **availability** scenarios—security BCM is not only ransomware.

## Designing a tabletop

1. Define **objectives** (e.g., "validate IdP recovery order," "test exec comms cadence")
2. Select **participants** — BCM, IR, SRE, cloud ops, security eng, legal, comms, business owner
3. Choose **scenario** matched to tier-0 risks from BIA
4. Draft **timeline** and **injects** (see below)
5. Assign **facilitator** (BCM) and **observer** (records gaps, no heroics)
6. Schedule **90–120 min**; pre-read one page max
7. Publish **rules** — no blame; hypotheticals unless using real sanitized incident

## Scenarios and injects

### Example scenarios

| ID | Scenario | Stresses |
|---|---|---|
| C1 | Ransomware + backup encryption | Immutable backups, rebuild decision |
| C2 | IdP total loss | Break-glass, MFA re-enrollment |
| C3 | SIEM down 24h | Detection gap, log preservation |
| C4 | Region loss (cloud) | Failover, RTO register |
| C5 | Supply chain compromise in EDR | Trust, rebuild agents |
| C6 | Prolonged SaaS outage (email/security) | Workarounds, customer comms |

### Inject pattern

Deliver injects every **15–25 min**:

- "Backup team reports last clean copy is 72h old—impact?"
- "Legal asks whether to pause user communication—who decides?"
- "SOC cannot reach SIEM—document detection gap start time"
- "Executive demands restore production before identity fixed—response?"

Force **decision points** with named roles—not open discussion only.

## Facilitation and scoring

Facilitator prompts:

- What is **known vs assumed**?
- Who has **authority** to activate DR?
- What is **RTO clock** start (declaration vs discovery)?
- Where are **runbooks**; are they reachable if IdP down?

Optional maturity scoring (1–5) per dimension:

- Roles and authority
- Technical runbooks
- Comms and stakeholders
- Backup/restore confidence
- Lessons incorporated since last exercise

## After-action and tracking

Within **10 business days** publish:

1. **Executive summary** — objectives met?, top 3 gaps
2. **Gap register** — ID, description, owner, priority, due date
3. **Plan updates** — which BCP/DRP sections change
4. **Test calendar changes** — added restore tests?

Track gaps in same system as **audit findings** or **risk register**. Close loop in next steering meeting.

**Major gap** (no tier-0 workaround): escalate to `cybersecurity` and executive sponsor.

## Regulatory BCM (high level)

Map program to frameworks **without legal interpretation**:

| Framework / domain | BCM-relevant themes (high level) |
|---|---|
| Financial (e.g., FFIEC, DORA ICT) | BCP testing, ICT service continuity, incident communication |
| HIPAA | Contingency plan, data backup, disaster recovery modes |
| PCI DSS | IR and backup procedures for CDE |
| SOC 2 | Availability/CC series continuity |
| ISO 22301 / 27031 | BCMS, ICT readiness |
| NIST CSF **Recover** | Recovery planning, improvements |

Use `compliance-specialist` for framework scoping; `compliance-engineer` for evidence automation. This skill produces **plans, tests, and exercise records** that satisfy many control narratives—legal/compliance confirms applicability.

**Disclaimer:** Regulatory text and filing obligations require qualified legal/compliance review—not provided here.
