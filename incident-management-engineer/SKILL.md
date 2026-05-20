---
name: incident-management-engineer
description: |
  Guides incident management engineering—severity models, escalation policies, on-call design,
  paging and comms tooling (PagerDuty/Opsgenie/Slack), incident lifecycle workflows, status pages,
  blameless postmortems, and reliability metrics (MTTD, MTTR, incident rate).
  Use when designing or improving incident response programs, on-call rotations, escalation paths,
  incident tooling integrations, postmortem templates, or SEV definitions—not for hands-on outage
  debugging (devops), security investigations (defensive-security-analyst), security IR policy
  (cybersecurity), multi-team program tracking (technical-program-manager), or individual
  customer technical tickets (support-engineer), or exec/VIP and community customer escalation
  programs (community-executive-escalations-program-manager). For incident **message** drafting
  and approval workflows, use communication-lead.
---

# Incident Management Engineer

## When to Use

- Define or revise severity levels and escalation policies
- Design on-call rotations, schedules, and handoffs
- Integrate alerting → paging → incident channel → ticket timeline
- Run blameless postmortem process and action-item tracking
- Report incident metrics and improve MTTR/MTTD
- Configure status page and customer comms workflows for outages

## When NOT to Use

- Fix pipelines, deploys, or service code during outage → `devops`, `fullstack-software-engineer`
- Investigate malware, phishing, or SOC alerts → `soc-analyst` (deep hunts → `defensive-security-analyst`)
- Enterprise security IR and legal/compliance program → `cybersecurity`
- Cross-team launch programs and RAID → `technical-program-manager`
- Data platform-specific ops → `data-system-ops-lead`
- Write customer-facing runbooks only → `tech-writer-researcher`
- Single-account repro and support escalations → `support-engineer`

## Related skills

| Need | Skill |
|---|---|
| SLOs, error budgets, reliability metrics | `site-reliability-engineer` |
| Pipelines, alerts stack implementation | `devops` |
| Rollback and cutover during outage | `deployment-strategist` |
| Security incident playbooks | `cybersecurity` |
| SOC alert triage and playbooks | `soc-analyst` |
| Active CSIRT response, timelines, evidence | `incident-responder` |
| BCP/DRP, cyber recovery playbooks, restore tests, tabletops | `bcm-disaster-recovery-specialist` |
| Deep investigation, hunts, detections | `defensive-security-analyst` |
| Major cross-team incident coordination | `technical-program-manager` |
| Runbook documentation | `tech-writer-researcher` |
| Customer ticket repro and engineering escalation | `support-engineer` |
| Incident and crisis message packs | `communication-lead` |
| Exec/community customer escalation program | `community-executive-escalations-program-manager` |

## Core Workflows

### 1. Severity and escalation

1. Align severity to **customer impact**, not alert noise
2. Map each level: response time, who pages, comms required
3. Document escalation ladder (primary → secondary → manager → exec)
4. Review quarterly with recent incident data

**See `references/severity_escalation.md` for matrix template.**

### 2. On-call program

- Primary + secondary coverage; no single point of failure
- Rotation length: prefer weekly over daily for sustainability
- Fairness: track pages per person; cap repeat pages
- Handoff ritual with open incidents and deploy context

**See `references/on_call_design.md` for rotation and handoff patterns.**

### 3. Incident lifecycle tooling

Standard flow:

```
Alert → page → incident declared → comms channel → roles assigned → mitigate → resolve → postmortem
```

- Auto-create incident record with timeline (who/when)
- Integrate chat, tickets, and paging in one timeline
- Reserve manual steps for role assignment and customer comms approval

**See `references/incident_tooling.md` for integration checklist.**

### 4. Active incident (commander-lite)

During SEV1–2:

| Role | Responsibility |
|---|---|
| Incident commander | Coordinates; does not debug alone |
| Communications | Internal + external updates on cadence |
| Technical lead(s) | Mitigation per service |

- Time-box updates (e.g., every 30 min until stable)
- Log decisions in incident timeline
- Defer root-cause deep dive until mitigated

**See `references/incident_lifecycle.md` for phases.**

### 5. Postmortem program

- Blameless; focus on systems and process
- Within 48h for SEV1–2; required before closing incident
- Action items: owner, due date, tracked to completion
- Share learnings broadly; link detection gaps to monitoring (`devops`)

**See `references/postmortem_process.md` for template and metrics.**

### 6. Metrics and improvement

Track monthly:

- Incident count by severity
- MTTD, MTTR (mitigation and full resolution)
- Repeat incidents (same root cause class)
- Postmortem action item closure rate
- On-call load (pages per engineer)

## When to load references

- **SEV matrix and escalation** → `references/severity_escalation.md`
- **Rotations and handoffs** → `references/on_call_design.md`
- **Lifecycle phases** → `references/incident_lifecycle.md`
- **PagerDuty/Slack/ticket wiring** → `references/incident_tooling.md`
- **Postmortems and metrics** → `references/postmortem_process.md`
