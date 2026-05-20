# Executive and escalation summaries

## Table of contents

1. [Executive summary rules](#executive-summary-rules)
2. [Escalation summary template](#escalation-summary-template)
3. [Audience-specific asks](#audience-specific-asks)
4. [Status cadence](#status-cadence)
5. [Coordination with comms and TPM](#coordination-with-comms-and-tpm)

## Executive summary rules

Executives need **decisions and consequences**, not activity logs.

| Do | Don't |
|---|---|
| Lead with recommendation or status (RAG) | Open with background history |
| Quantify impact (revenue, customers, risk, time) | List meeting attendees |
| State explicit **ask** and deadline | Bury ask in paragraph 4 |
| Offer 2–3 options with trade-offs | Present one path without alternatives |
| Flag what is **unknown** | Speculate on root cause |

Target length: **150–250 words** for email; **one slide** for deck inserts.

## Escalation summary template

```markdown
# Escalation: [short title]

**Severity:** [P0–P3 or company scale]
**Status:** [Investigating / Mitigating / Monitoring / Resolved]
**Incident commander / DRI:** [name/role]
**Last updated:** [timestamp UTC]

## Situation (facts only)
What is happening; scope (customers, regions, systems); start time.

## Impact
- Customer: [experience, count if known]
- Financial: [revenue, credits, penalties if known]
- Regulatory / contractual: [if applicable]

## Current actions
Bulleted; owner per line.

## Options (if decision needed)
| Option | Pros | Cons | Owner |
|---|---|---|---|
| A | | | |
| B | | | |

## Recommendation
One clear path if appropriate.

## Asks by audience
- **Executive:** [decision / resource / comms approval]
- **Engineering:** [priority / staffing]
- **Finance:** [accrual / forecast / credit]
- **Legal / compliance:** [notice / filing / control]
- **Sales / support:** [talk track / customer comms timing]

## What not to do yet
Actions that would worsen state or violate policy.

## Links
Status page, war room, ticket, runbook.
```

Separate **message packs** for customers from this internal summary—route external wording to `communication-lead`.

## Audience-specific asks

| Function | Useful ask format |
|---|---|
| Executive | Approve $X / accept risk Y / delay launch Z |
| Engineering | Staff N engineers; freeze deploys; priority queue |
| Finance | Approve credit budget; restate guidance range |
| Legal | Approve customer notice language by [time] |
| Compliance | Confirm reporting obligation and timeline |
| Sales | Pause outbound to segment; exec bridge for top accounts |

Each ask must be **actionable in one meeting** or declined with reason.

## Status cadence

| Severity | Update frequency | Channels |
|---|---|---|
| P0 | Every 30–60 min until stable | War room + exec brief |
| P1 | Every 2–4 hours | Program channel + exec email |
| P2 | Daily | Status doc |
| P3 | Weekly or at milestone | RAID / program review |

Each update: **delta since last** (not full rehash).

## Coordination with comms and TPM

| Need | Skill |
|---|---|
| Customer/partner **wording**, holding lines | `communication-lead` |
| Multi-team **timeline**, RAID, dependencies | `technical-program-manager` |
| Incident **process**, severity, paging | `incident-management-engineer` |
| Security incident facts | `cybersecurity` + incident commander |

This skill owns **internal cross-functional clarity**; partner skills own program machinery and external narrative.
