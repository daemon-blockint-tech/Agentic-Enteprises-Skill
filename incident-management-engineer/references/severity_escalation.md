# Severity and escalation

## Table of contents

1. [Severity matrix](#severity-matrix)
2. [Escalation triggers](#escalation-triggers)

## Severity matrix

| Level | Customer impact | Response target | Comms |
|---|---|---|---|
| SEV1 | Outage or data at risk | Page immediately | Exec + status page |
| SEV2 | Major degradation | Page within 15 min | Status page optional |
| SEV3 | Limited impact | Business hours | Internal only |
| SEV4 | Low / internal | Backlog | None |

Define **mitigation** vs **resolution** separately in runbooks.

## Escalation triggers

Escalate when:

- SEV not reduced within target window
- Cross-team dependency blocks mitigation
- Customer or legal/comms involvement needed
- Unclear ownership after 15 min on SEV1

Document named approvers for customer-facing messages.
