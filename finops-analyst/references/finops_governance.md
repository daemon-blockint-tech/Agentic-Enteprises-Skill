# FinOps governance

## Table of contents

1. [RACI](#raci)
2. [Cadence](#cadence)
3. [Policies](#policies)
4. [Engineering partnership](#engineering-partnership)

## RACI

| Activity | FinOps | Engineering | Finance | Leadership |
|---|---|---|---|---|
| Tag compliance | A/R | R | I | I |
| Rightsizing prod | C | R/A | I | I |
| Budget setting | R | C | A | I |
| Commit purchases | R | C | A | I |
| GL close mapping | C | I | R/A | I |

A = accountable, R = responsible, C = consulted, I = informed.

## Cadence

| Meeting | Frequency | Outcome |
|---|---|---|
| Cost standup | Weekly | Anomalies, blockers |
| Service owner review | Monthly | Per-team backlog |
| FinOps council | Monthly | Policy, commits, budget |
| QBR with leadership | Quarterly | Strategy, targets |

## Policies

Document and enforce:

- **Sandbox** auto-shutdown or budget cap
- **Prod** requires tags before deploy (policy-as-code)
- **Commit** approval threshold (e.g., >$50k annual)
- **New region/service** FinOps review for cost estimate
- **Anomaly** response SLA

Exceptions with expiry in register.

## Engineering partnership

- Embed FinOps review in **PRR** (`site-reliability-engineer`) for cost estimate
- Celebrate **verified savings** in team metrics
- No punitive chargeback without visibility first
- Provide **self-service** dashboards before demanding cuts

Escalate chronic untagged spend to engineering director with data, not anecdotes.
