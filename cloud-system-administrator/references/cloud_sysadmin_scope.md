# Cloud sysadmin scope

## Table of contents

1. [Responsibility boundary](#responsibility-boundary)
2. [Change control](#change-control)
3. [Escalation](#escalation)
4. [Environments](#environments)

## Responsibility boundary

| In scope | Out of scope |
|---|---|
| IAM access operations | IAM architecture and org SCP design |
| VM patch and reboot | Application code deploy |
| Snapshot restore | Database schema migration |
| Alert triage for infra | SEV program design |
| Quota tickets | EA negotiation |
| Cert renewal ops | WAF rule design |

**cloud-engineer** builds; **cloud-system-administrator** runs.

## Change control

Standard change types:

| Type | Approval | Example |
|---|---|---|
| Standard | Pre-approved runbook | Snapshot cleanup |
| Normal | Manager + peer review | IAM role attach |
| Emergency | Post-approval within 24h | Restore prod DB |

Record: **what**, **when**, **who**, **rollback**, **verification**.

## Escalation

| Situation | Escalate to |
|---|---|
| Repeated auth failures org-wide | Security / IdP |
| Data breach suspicion | Security IR |
| Architectural fix needed | `cloud-engineer` |
| Customer-visible outage comms | `incident-management-engineer` process + `communication-lead` |
| Vendor platform bug | Cloud support case + leadership |

## Environments

- **Prod** — change window, dual control for sensitive actions
- **Non-prod** — faster path; still no shared admin passwords
- **Sandbox** — auto-cleanup policies; no prod data

Follow enterprise standards from `enterprise-cloud-architect` when applicable.
