# ATS pipeline and hiring manager partnership

## Table of contents

1. [Pipeline stage definitions](#pipeline-stage-definitions)
2. [Required fields and hygiene](#required-fields-and-hygiene)
3. [SLAs and aging rules](#slas-and-aging-rules)
4. [Recruiter–HM operating rhythm](#recruiterhm-operating-rhythm)
5. [Calibration and slate review](#calibration-and-slate-review)
6. [Escalation patterns](#escalation-patterns)
7. [CRM and sourcing coordination](#crm-and-sourcing-coordination)

## Pipeline stage definitions

Define stages so metrics are comparable across reqs:

| Stage | Entry criteria | Exit criteria |
|---|---|---|
| New / applied | Application received | Screen scheduled or rejected |
| Recruiter screen | Qualified on paper | Pass to HM or reject |
| HM screen | HM accepted intro | Loop scheduled or reject |
| Interviewing | At least one loop interview | Debrief complete |
| Offer | Verbal approval to extend | Signed or declined |
| Hired | Offer accepted | Start date confirmed |
| Closed | Req filled or cancelled | Reason coded |

Avoid custom per-HM stages without TA ops approval—they break reporting.

## Required fields and hygiene

Minimum ATS fields per active candidate:

- Source and sub-source
- Current stage and stage entry date
- Level assessed
- Comp expectations (if collected)
- Visa / sponsorship need
- Next action owner and date
- Rejection reason (coded)

Weekly hygiene sweep:

- Remove duplicates
- Close stale "maybe" candidates
- Fix missing rejection codes
- Align agency submissions to same fields as direct applicants

## SLAs and aging rules

Example internal SLAs (tune to org):

| Metric | Target |
|---|---|
| First screen after apply | ≤ 3 business days |
| HM feedback after screen | ≤ 2 business days |
| Schedule next loop after pass | ≤ 5 business days |
| Debrief after final interview | ≤ 2 business days |
| Offer after verbal yes | ≤ 3 business days |

**Aging req** triggers:

- Open > 60 days with < 3 qualified in pipeline
- No HM feedback > 5 days on pending candidates
- Offer stage > 14 days without resolution

## Recruiter–HM operating rhythm

**Weekly 30-minute req sync** (per active req or batched by team):

1. Pipeline snapshot: counts by stage
2. Blockers: scheduling, feedback debt, missing interviewers
3. Slate review: who advances, who rejects, who needs follow-up
4. JD/process fixes if pass-through is low
5. Agency performance if applicable

**HM commitments:**

- Feedback within SLA
- Attend debriefs
- Sell role on screens
- Avoid poaching interviewers from other reqs without notice

## Calibration and slate review

Before high-volume interviewing:

- Align on **level bar** with 2–3 exemplar profiles (hire / no-hire)
- Review diversity of slate by stage—not quotas in filters
- Calibrate agency submissions against same bar

Mid-process calibration when:

- Pass-through drops at same stage twice in a row
- HM rejects all agency candidates with same reason

## Escalation patterns

| Situation | Escalate to |
|---|---|
| HM unavailable > 1 week | HM skip + TA lead |
| Req scope change mid-loop | Reset candidates or re-level req |
| Comp band blocked | HR/comp + finance approver |
| Legal concern on interview question | HR immediately |
| Agency quality failure | Procurement + agency QBR |

Document escalations in req notes for audit trail.

## CRM and sourcing coordination

- `talent-sourcer` owns top-of-funnel search; TA owns stage movement after handoff
- Use consistent **tags** for ICP tier, campaign, and event source
- Do not duplicate outreach after handoff to interview stages
- Report **source effectiveness** monthly: applicant → hire conversion by channel

For passive pipeline building only, prefer `talent-sourcer` over expanding TA scope.
