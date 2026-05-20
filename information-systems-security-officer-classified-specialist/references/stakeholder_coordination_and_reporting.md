# Stakeholder coordination and reporting

## Table of contents

1. [Cadence matrix](#cadence-matrix)
2. [ISSM and program management](#issm-and-program-management)
3. [Authorizing official staff](#authorizing-official-staff)
4. [Incident and event reporting](#incident-and-event-reporting)
5. [Status reporting templates](#status-reporting-templates)

## Cadence matrix

| Forum | Frequency | ISSO inputs |
|---|---|---|
| System owner sync | Weekly or biweekly | POA&M, changes, blockers |
| Control owner standup | Monthly | Evidence gaps, scan SLAs |
| ISSM portfolio review | Monthly | Risk summary, aging POA&M |
| AO staff read-ahead | Quarterly or pre-A&A | Posture, residual risk themes |
| Change advisory (security) | Per significant change | Impact analysis summary |

## ISSM and program management

Report to ISSM:

- POA&M items past milestone or escalating risk
- Significant changes submitted or pending approval
- Assessor requests at risk of missing due dates
- Inherited control provider deficiencies affecting the system
- Incidents and near-misses per program timelines
- Resource needs for authorization maintenance (tools, FTE)

ISSM owns portfolio prioritization; ISSO owns **system package accuracy**.

## Authorizing official staff

AO staff engagements (ISSO supports, does not decide):

- Pre-decision briefs before authorization or reauthorization
- Interim authorization extensions with explicit limitations
- POA&M risk acceptance packages with milestones
- Deviation requests when continuous monitoring identifies drift

Keep briefs factual: dates, counts, control IDs, trend direction. Separate recommendations from facts.

## Incident and event reporting

| Event type | Typical ISSO action |
|---|---|
| Suspected compromise | Notify ISSM immediately; open incident record per program |
| Policy violation | Document; POA&M if systemic |
| Spillage | Follow program spillage procedure; notify ISSM and security manager |
| Failed assessment sample | POA&M or hot wash with implementer |

Hand active response to `incident-responder` when incident is declared. ISSO maintains SSP and POA&M alignment post-incident.

## Status reporting templates

**Monthly ISSM snapshot (example headings):**

```markdown
## System [identifier] — monthly security status

### Authorization
- Decision: [ATO / IATO / expired] — expiration [date]
- Inherited controls: [provider status summary]

### POA&M
- Open: [n] — High: [n] — Past due: [n]
- Closed this period: [n]

### Continuous monitoring
- Last review: [date] — Outcome: [pass/partial]
- Significant changes: [count] — [one-line list]

### Vulnerabilities
- Critical open: [n] — SLA breaches: [n]

### Incidents
- Reported: [n] — [IDs or summary]

### Asks
- [Decision or resource needed]
```

Adjust fields to program templates and classification of the reporting channel.
