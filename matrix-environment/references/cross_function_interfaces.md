# Cross-Functional Interfaces

## Interface catalog template

For each interface document:

| Field | Content |
|---|---|
| **Name** | e.g., SOC → AppSec escalation |
| **Trigger** | Event that starts the flow |
| **Sender / Receiver** | Teams and roles |
| **Artifacts in** | Alerts, tickets, logs, RFC links |
| **Artifacts out** | Findings, fixes, attestations |
| **SLA** | Time to acknowledge / resolve tier |
| **Tool of record** | Jira, ServiceNow, PagerDuty, etc. |
| **Metrics** | Volume, age, reopen rate |

## SOC ↔ Engineering / SRE

| Direction | Typical work | Owner |
|---|---|---|
| SOC → Eng | Suspicious activity on service, containment ask | SOC R triage; Eng R fix; IR A if declared |
| Eng → SOC | Logging gaps, detection requests | Eng R request; SOC R backlog; SRE C for pipeline |
| SOC → SRE | Reliability-impacting security control | Joint prioritization; SRE A for SLO impact |

**Peer skills:** `defensive-security-analyst`, `soc-analyst`, `site-reliability-engineer`.

## SOC ↔ IR (CSIRT)

| Trigger | SOC role | IR role |
|---|---|---|
| Alert exceeds severity threshold | Detect, enrich, initial ticket | Declare, command, comms clock |
| Active intrusion indicators | Contain support | **A** incident commander |
| Post-incident | Feed detection gaps | **A** PIR actions, track to closure |

**Peer skills:** `incident-responder`, `incident-management-engineer` (program, not command).

## AppSec ↔ Product Engineering

| Interface | Purpose |
|---|---|
| Design review / threat model | Shift-left; ARB gate for high risk |
| Secure SDLC gates | CI checks, dependency policy, secrets |
| Pen test / bounty intake | Findings routed with single A per service |
| Exception process | Compensating controls; GRC C |

**Peer skills:** `information-security-engineer` (tooling), `enterprise-security-architect` (patterns).

## GRC ↔ Engineering / Platform

| Interface | Purpose |
|---|---|
| Control calendar | Evidence due dates, owners |
| Policy publication | Standards chapter consumes |
| Risk acceptance | Exception with expiry; CISO A for material |
| Audit requests | Read-only access, single coordinator |

**Peer skills:** `compliance-specialist`, `compliance-engineer`.

## Platform ↔ Product

| Interface | Purpose |
|---|---|
| Golden path onboarding | New service checklist (observability, IAM, logging) |
| Environment request | Account/project vending; **not** full org design |
| Shared services | CI, registry, secrets, mesh—SLA and versioning |
| Cost / quota | FinOps visibility; product A for usage |

**Peer skills:** `platform-engineer`, `cloud-engineer`, `devops`.

## TPM ↔ Matrix functions

TPM **coordinates** cross-team work; does not own technical **A** for security or reliability outcomes.

| TPM adds value | TPM does not replace |
|---|---|
| Dependency maps, RAID, status | AppSec sign-off |
| Launch readiness checklist | IR command |
| Steering prep | GRC control design |

**Peer skill:** `technical-program-manager`.

## Environment tier handoffs (org view)

| Tier transition | Typical R | Typical A |
|---|---|---|
| Dev → stage | Product eng | Eng lead or platform delegate |
| Stage → prod | Product + platform checks | Eng director or CAB |
| Prod data / prod keys | Security + GRC C | Service owner A |
| Break-glass access | IR or on-call | Security + audit trail |

Technical implementation of tiers → `cloud-engineer`, `deployment-strategist`.

## Metrics that expose broken interfaces

- Mean time in queue between teams (handoff wait)
- Reopen rate after "closed" by wrong party
- Repeat escalations to SteerCo for same conflict
- % work done outside tool of record
- Audit findings citing missing evidence owner
