# Classified operations and incident escalation

## Table of contents

1. [Operations interfaces](#operations-interfaces)
2. [Change and maintenance governance](#change-and-maintenance-governance)
3. [Cross-domain and data flow themes](#cross-domain-and-data-flow-themes)
4. [Incident classification and escalation](#incident-classification-and-escalation)
5. [Government stakeholder communication](#government-stakeholder-communication)
6. [Handoff to incident-responder](#handoff-to-incident-responder)

## Operations interfaces

| Interface | Senior manager role |
|---|---|
| Classified NOC / ops center | Define escalation tiers; approve maintenance windows affecting security controls |
| Mission owners | Align outage vs security control downtime |
| Engineering / platform | Change advisory for security-relevant releases |
| Help desk | Route classified incidents to CSIRT path; no ad-hoc admin passwords |

Maintain an **operations calendar** overlay: patches, cert renewals, DR tests, assessor visits.

## Change and maintenance governance

**Change categories (example):**

| Category | Approval theme |
|---|---|
| Routine patch | Pre-approved window; rollback plan |
| Control-affecting | ISSO review; may trigger significant change |
| Emergency | Document after-action; government notify if contract requires |

Require: maintenance notice, backout, security control validation checklist (summary), and comms to mission.

## Cross-domain and data flow themes

At manager depth—do not design technical guards here:

- Approved transfer mechanisms only (organization policy names only)
- No ad-hoc removable media without policy exception
- Remote administration paths documented in authorization package
- Wireless and mobile excluded unless explicitly authorized

Escalate **policy exceptions** with risk memo and authorizing official awareness.

## Incident classification and escalation

| Stage | Manager action |
|---|---|
| Suspected event | Confirm classified handling; activate program incident cell |
| Declaration | Align severity with mission and data impact; assign executive sponsor |
| Containment direction | Authorize account isolation themes; delegate execution to IR |
| Evidence | Legal hold and log preservation themes; chain of custody to IR/forensics |
| Recovery | Prioritize mission restoration vs forensic needs—document trade-off |

**Clocks:** contract notification windows, government reporting interfaces, internal exec cadence—coordinate with legal and contracts; do not invent deadlines.

## Government stakeholder communication

Prepare **fact packs** (minimum necessary):

- What happened (unclassified summary if allowed; otherwise per classification guide)
- Systems and data in scope (boundary reference)
- Current status: contained / investigating / recovered
- Preliminary root cause themes (not final until validated)
- Actions taken and next 24–72 hours
- Decisions needed from government (access, inspection deferral, additional resources)

Route **wording** through legal and contracts before external send.

## Handoff to incident-responder

| classified-cyber-security-senior-manager | incident-responder |
|---|---|
| Stakeholder map, government interfaces | Timeline, containment playbooks |
| Resource and priority decisions | Technical investigation |
| Briefings to leadership and AO | Evidence preservation execution |
| POA&M linkage for systemic fixes | Post-incident review facilitation support |

After stabilization, manager owns **inspection and authorization impact** (new POA&M, significant change, reauth timing).
