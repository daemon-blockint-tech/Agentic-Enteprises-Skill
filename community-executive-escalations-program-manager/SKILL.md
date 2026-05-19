---
name: community-executive-escalations-program-manager
description: |
  Guides program management for community and executive customer escalations—intake and triage
  frameworks, severity matrices, cross-functional war rooms, executive briefings, SLA design,
  playbooks for VIP and public-facing issues, decision logs, and program metrics. Use when
  standing up or running an exec escalation path, community incident response, champion/VIP
  programs, steering forums for strategic accounts, or unblocking high-visibility customer
  issues across CS, support, product, legal, and comms—not for single-ticket debugging
  (support-engineer), product SEV/on-call design (incident-management-engineer), general TPM
  milestones (technical-program-manager), marketing campaigns, or legal contract terms
  (commercial-counsel). Customer ops playbooks: customer-ops-specialist. Message packs:
  communication-lead.
---

# Community & Executive Escalations Program Manager

## When to Use

- Design or improve **exec escalation** intake, severity, and SLA
- Run **community escalation** response (forums, social, GitHub, Discord, public posts)
- Stand up **program charter**, RACI, and escalation ladder to leadership
- Facilitate **war rooms** for strategic accounts or reputational issues
- Produce **executive briefings** (facts, impact, options, recommendation, ask)
- Define **metrics**: time to acknowledge, owner assignment, resolution, recurrence
- Coordinate **cross-functional** owners (CS, support, eng, product, legal, comms)
- Run **post-escalation retros** and playbook updates

## When NOT to Use

- Reproduce bugs and engineering handoff artifacts → `support-engineer`
- Paging, SEV definitions, postmortem process for outages → `incident-management-engineer`
- Multi-team delivery milestones without customer/exec visibility → `technical-program-manager`
- Company-wide narrative and holding lines → `communication-lead`
- Renewal health scoring and CS operations → `customer-ops-specialist`
- Contract negotiation or liability language → `commercial-counsel`

## Related skills

| Need | Skill |
|---|---|
| Ticket repro and eng escalation package | `support-engineer` |
| Outage/incident program and status page | `incident-management-engineer` |
| Cross-team technical program RAID | `technical-program-manager` |
| External/customer message approval | `communication-lead` |
| CS onboarding, health, renewals | `customer-ops-specialist` |
| Legal review of public response | `commercial-counsel` |
| Exec storyline and business framing | `business-consultant` |

## Core Workflows

### 1. Program charter and governance

Scope, forums, RACI, escalation ladder.

**See `references/program_charter_governance.md`.**

### 2. Intake and triage

Community vs executive paths; severity; routing.

**See `references/intake_triage_matrix.md`.**

### 3. Executive escalation playbook

VIP handling, briefing template, leadership cadence.

**See `references/executive_escalation_playbook.md`.**

### 4. Community escalation playbook

Public issues, moderation, coordinated response.

**See `references/community_escalation_playbook.md`.**

### 5. War room operations

Cadence, roles, decision log, exit criteria.

**See `references/war_room_operations.md`.**

### 6. Metrics and reporting

KPIs, exec dashboard, retrospective.

**See `references/metrics_reporting_retro.md`.**

## Output standards

- Every active escalation has **single DRI**, severity, and next update time
- Executive briefs are **one page**: situation, impact, options, recommendation, ask
- Public responses **approved** via comms/legal when reputational or legal risk
- Decisions logged with **date, owner, rationale**
- Close with **customer outcome** and **program learnings** (playbook delta)

## When to load references

- **Charter** → `references/program_charter_governance.md`
- **Triage** → `references/intake_triage_matrix.md`
- **Exec path** → `references/executive_escalation_playbook.md`
- **Community path** → `references/community_escalation_playbook.md`
- **War room** → `references/war_room_operations.md`
- **Metrics** → `references/metrics_reporting_retro.md`
