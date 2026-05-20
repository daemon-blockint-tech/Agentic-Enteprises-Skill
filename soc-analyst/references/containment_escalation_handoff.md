# Containment, escalation, and handoff

## Table of contents

1. [Containment recommendations](#containment-recommendations)
2. [Approval matrix](#approval-matrix)
3. [Escalation paths](#escalation-paths)
4. [Shift handoff template](#shift-handoff-template)
5. [Evidence preservation](#evidence-preservation)

## Containment recommendations

SOC **recommends**; IR or designated approver **authorizes** unless runbook grants auto-approve.

| Action | Typical when | Risk |
|---|---|---|
| Disable user / revoke sessions | Confirmed credential compromise | Business disruption |
| Force password reset | Account takeover suspected | User lockout |
| EDR isolate host | Active malware or C2 | Production outage |
| Block IOC (IP/domain/hash) | Confirmed malicious comms | Collateral if shared infra |
| Revoke OAuth / app tokens | Token theft | App downtime |
| Snapshot / image capture | Before wipe or rebuild | Storage/time |

List **order of operations** in recommendation (e.g., snapshot → isolate → block IOC).

## Approval matrix

| Scope | Approver |
|---|---|
| Single workstation | SOC T2+ or runbook auto |
| Server / production | Service owner + IR |
| Identity (standard user) | SOC T2+ per runbook |
| Identity (privileged / exec) | IR lead + IT leadership |
| Network block (wide) | IR + network team |
| Cloud resource change | Cloud security + IR |

If approver unavailable, escalate to IR lead—do not delay SEV1 containment waiting on business hours unless policy requires.

## Escalation paths

| To | When | Deliverable |
|---|---|---|
| **IR / defensive analyst** | SEV1–2, complex scope, hunt needed | Timeline, IOCs, containment status |
| **Information security engineering** | Tooling gap, integration failure | Tickets with logs and error detail |
| **Cloud security** | Cloud-specific compromise | Resource IDs, API trail exports |
| **IT / identity** | Account recovery, rebuild | Clear action list |
| **IM engineer** | Customer-facing outage tied to security | Link security case to incident record |
| **Legal / compliance** | Regulated data, external disclosure | Through IR commander only |

## Shift handoff template

Post in handoff channel at shift end:

```markdown
## SOC handoff — [DATE] [SHIFT]

### Open P1/P2
- [CASE-ID] — severity — one-line status — owner — next action — blocker

### Watch list (monitoring)
- [CASE-ID] — why watching — expire time

### Tuning in flight
- [TICKET-ID] — rule ID — FP pattern

### Queue health
- Backlog count — oldest unassigned age

### Notes for next shift
- Maintenance windows, known noisy rules, staffing gaps
```

Require verbal read-back for any **SEV1** or **active containment** case.

## Evidence preservation

Before destructive containment when policy allows:

1. Export relevant SIEM searches (time-bounded)
2. EDR investigation package or snapshot
3. Identity sign-in export for affected users
4. Hash of exported bundles stored in case

Document **who** exported, **when UTC**, and **storage location** (case folder ID).
