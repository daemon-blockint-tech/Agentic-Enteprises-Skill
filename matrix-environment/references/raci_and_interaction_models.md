# RACI and Interaction Models

## RACI basics

| Role | Meaning |
|---|---|
| **R** Responsible | Does the work |
| **A** Accountable | Single approver; owns outcome |
| **C** Consulted | Two-way input before decision |
| **I** Informed | One-way notification |

**Matrix rule:** Every row has exactly one **A**. Shared **A** is an anti-pattern.

## Lifecycle RACI template (customize per org)

| Capability | Product Eng | Platform/SRE | AppSec | GRC | SOC | IR | TPM |
|---|---|---|---|---|---|---|---|
| Feature design & threat model | R/A | C | R | I | I | I | I |
| Build & release | R/A | C | C | I | I | I | C |
| Prod operation & SLO | R | R/A | I | I | C | C | I |
| Vuln remediation (app) | R/A | C | R | I | I | I | C |
| Vuln remediation (infra) | C | R/A | C | I | I | I | C |
| Security monitoring & triage | I | C | C | I | R/A | C | I |
| Declared incident command | C | C | C | C | C | R/A | C |
| Audit / control attestation | C | C | C | R/A | C | C | C |
| Policy exception | C | C | C | R/A | I | I | I |

Adjust **A** when product-led vs platform-led; document overrides in operating model canvas.

## Interaction models (swimlane triggers)

### 1. Vulnerability intake → fix → verify

1. **Find** — scanner, pen test, bug bounty, SOC hunt → ticket in tool of record
2. **Triage** — AppSec or vuln mgmt sets severity, SLA, owner queue
3. **Fix** — engineering **R**; platform if infra/root cause
4. **Verify** — AppSec or automated re-scan; **A** remains service owner for closure
5. **Report** — GRC informed for audit-relevant items

**SLA example (illustrative):** Critical 7d, High 30d, Medium 90d—tie to risk appetite (`chief-information-security-officer`).

### 2. Production change / release

1. Product proposes change; platform provides paved-road checks
2. AppSec: security gate on material changes (ARB threshold)
3. SRE: error-budget or blackout policy
4. CAB or lightweight change advisory for high-risk tiers

Hand off implementation details to `deployment-strategist`, `devops`.

### 3. Security incident (declared)

1. **Detect** — SOC **R** for alert triage
2. **Declare** — IR **A** for incident command; CISO informed per severity
3. **Contain** — IR + engineering + platform; AppSec for app-specific
4. **Comms** — `communication-lead` / exec per playbook
5. **Learn** — post-incident actions into chapter backlogs

Do not conflate SOC shift manager with IR commander.

### 4. Audit / control request

1. GRC **A** for control mapping and evidence calendar
2. Engineering/platform **R** for technical evidence
3. AppSec **C** for interpretation of technical controls
4. TPM **C** when cross-team evidence collection

## Escalation paths

| Situation | First escalation | Executive escalation |
|---|---|---|
| SLA breach on critical vuln | Eng director + AppSec lead | CISO / CTO joint |
| Repeated control failure | GRC + platform | Audit committee theme |
| Major incident | IR commander | CISO crisis cell |
| Resource conflict in matrix | Chapter leads | SteerCo (infra + security + product) |

## Artifacts per interaction

- Intake form fields (minimum data for routing)
- Definition of done per queue
- Tool of record (no shadow spreadsheets for authoritative status)

## Anti-patterns in RACI

- **Consulted everyone** — paralysis; limit C to roles with veto or material expertise
- **Responsible nobody** — "the team" is not R; name a role or DRI
- **Ticket ping-pong** — missing A on closure; reopen rules undefined
- **Shadow RACI** — official matrix says product A, practice says security A
