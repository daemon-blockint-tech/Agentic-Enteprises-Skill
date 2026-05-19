# Crisis and incident communications

## Table of contents

1. [Roles](#roles)
2. [Message ladder](#message-ladder)
3. [Holding lines](#holding-lines)
4. [Customer statement template](#customer-statement-template)

## Roles

| Role | Owns |
|---|---|
| Incident commander | Facts, timeline, mitigation status |
| Comms lead | Wording, channels, approvals |
| Legal | Regulatory, customer contract, public statements |
| Security (if applicable) | Breach classification, law enforcement |

Comms does not invent technical root cause. Process design → `incident-management-engineer`.

## Message ladder

1. **Internal holding** (Slack/email) — acknowledge, investigating, next update time
2. **Customer status** — impact scope, workaround, ETA if known
3. **Resolution** — what fixed, residual risk, prevention steps (high level)
4. **Postmortem summary** — blameless, customer-safe version when appropriate

Set **update cadence** upfront (e.g., every 30 min for SEV1 until stable).

## Holding lines

Until facts confirmed:

- "We are aware of [symptom] affecting [scope]. Engineering is investigating."
- "We will update by [time] at [channel]."
- Avoid: root cause guesses, blame, competitor mentions.

## Customer statement template

```
Subject: [Service] — [status: investigating | mitigated | resolved]

We are [investigating / have mitigated] an issue affecting [who/what].

Impact: [plain language]
Workaround: [if any]
Next update: [time and channel]

We apologize for the disruption and will share more when [condition].
```

Version each draft; timestamp in filename. Archive approved text for audit.
