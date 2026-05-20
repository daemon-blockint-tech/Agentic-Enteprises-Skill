# Pipeline handoff and sourcing metrics

## Table of contents

1. [Pipeline stages](#pipeline-stages)
2. [CRM hygiene](#crm-hygiene)
3. [Handoff criteria](#handoff-criteria)
4. [Handoff package](#handoff-package)
5. [Sourcing metrics](#sourcing-metrics)
6. [Reporting cadence](#reporting-cadence)
7. [Escalation triggers](#escalation-triggers)

## Pipeline stages

Standard sourcer-owned stages:

| Stage | Definition | Owner action |
|---|---|---|
| Identified | Profile matches ICP | Log source + link |
| Qualified | Meets handoff bar | Tier A/B/C |
| Contacted | First outreach sent | Log date + template id |
| Replied | Any response | Classify sentiment |
| Interested | Wants conversation | Hand to recruiter |
| Handed off | Recruiter accepted | Close sourcer tasks |
| Nurture | Timing not right | Set revisit date |
| Closed | Declined / unresponsive | Reason code |

Align stage names with ATS/CRM (`recruiting-pipeline` may define global req stages).

## CRM hygiene

**Required fields** per candidate:

- Source (boolean v2, referral, GitHub, etc.)
- Fit tier (A/B/C)
- Req ID
- Last activity date
- Next action

**Dedup rules:**

- Match on LinkedIn URL, email, or ATS candidate ID
- Merge duplicates; preserve full activity history
- Never delete audit trail—mark inactive

**Note standard** (one paragraph):

```
Fit: A — staff-level backend, 8y Go/K8s, ex-{company}.
Evidence: {link}; led {project} per profile.
Outreach: 2026-05-01 LI; replied interested 2026-05-03.
Risks: needs visa; comp may be above band.
Next: recruiter screen — suggest HM intro on platform scale.
```

## Handoff criteria

| Tier | Criteria |
|---|---|
| A | All must-haves; strong evidence; replied or warm intro |
| B | Most must-haves; minor gap documented; cold OK if scarce role |
| C | Possible fit; needs sourcer or recruiter validation—do not mass-outreach |

**Handoff to recruiter when:**

- Candidate is A-tier and interested, OR
- B-tier with HM pre-approval for scarce skill, OR
- Referral with intro made

**Handoff to HM** only when process allows sourcer→HM skip-level; default through recruiter.

## Handoff package

Send recruiter:

1. Profile links (LinkedIn, GitHub, portfolio)
2. Fit summary (3 bullets)
3. Outreach history (dates, channels, responses)
4. Suggested pitch angle for screen
5. Open questions (visa, comp, level)

Attach **candidate list** export if batch handoff.

## Sourcing metrics

| Metric | Formula / definition |
|---|---|
| Qualified adds | Count entering Qualified stage/week |
| Contact rate | Contacted / Qualified |
| Reply rate | Replied / Contacted |
| Interest rate | Interested / Replied |
| Handoff rate | Handed off / Interested |
| Time to handoff | Days from Identified → Handed off |
| Slate diversity | Per TA-defined reporting (aggregated) |
| Source mix | % by channel |

Set targets with recruiter based on role difficulty.

## Reporting cadence

**Weekly sourcer report** (5-minute read):

- Qualified adds vs target
- Reply and interest rates by sequence
- A-tier backlog awaiting handoff
- Blockers: JD clarity, comp, visa, channel fatigue
- Plan next week: booleans to test, companies to map

## Escalation triggers

Escalate to recruiter/HM/TA when:

- <2× pool size after 1 week of search
- Reply rate <8% after 100+ sends with tested variants
- HM rejects >80% of A-tier handoffs (ICP drift)
- Legal flags on target company list
- Diversity slate gap vs plan with no path forward

Document escalation with data, not anecdotes.
