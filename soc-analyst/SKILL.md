---
name: soc-analyst
description: |
  Guides SOC operations—alert triage, SIEM/EDR investigation, enrichment, playbook execution,
  false-positive closure, escalation decisions, and detection tuning feedback.
  Use when working SOC queues, investigating suspicious alerts, correlating events, documenting
  analyst notes, or deciding escalate vs close—not for declared incident command, timelines,
  evidence preservation, or regulatory comms (incident-responder), incident program design
  (incident-management-engineer), binary/firmware RE (reverse-engineer), red team operations
  (red-team-specialist), or enterprise security strategy (cybersecurity).
---

# SOC Analyst

## When to Use

- Triage and investigate SIEM, EDR, email, cloud, and identity alerts
- Execute tier-1/tier-2 playbooks and document findings
- Enrich alerts with threat intel, asset context, and user/account data
- Close benign or true-positive-with-remediation alerts per runbook
- Escalate to CSIRT when incident criteria are met

## When NOT to Use

- Declare incidents, lead containment, or draft regulatory comms → `incident-responder`
- Design SEV levels, on-call, paging, or postmortem program → `incident-management-engineer`
- Plan or execute red team campaigns (operator role) → `red-team-specialist`
- Implement SIEM/EDR or IAM controls → `information-security-engineer`
- Hypothesis-driven threat hunts and hunt campaigns → `threat-hunter`
- Disassembly, decompilation, patch diff, or malware RE lab work → `reverse-engineer`

## Related skills

| Need | Skill |
|---|---|
| Escalate declared security incident | `incident-responder` |
| Incident program, escalation matrix | `incident-management-engineer` |
| Security strategy and IR policy | `cybersecurity` |
| Red team / purple team exercise design | `red-team-specialist` |
| Tooling implementation (SIEM, EDR, SOAR) | `information-security-engineer` |
| Cloud audit and account forensics | `cloud-security-engineer` |
| Proactive threat hunts and hunt campaigns | `threat-hunter` |
| Detection tuning and DFIR-style investigation | `defensive-security-analyst` |
| Disk/memory forensics and chain of custody | `digital-forensics-analyst` |
| Binary/protocol RE, patch diff, YARA from samples | `reverse-engineer` |
| Vetted IOC/TTP packages and tactical intel for enrichment | `cti-analyst` |

## Handoff to threat hunting

Escalate to `threat-hunter` when alerts cluster into a plausible campaign, detections are evasive, leadership requests a proactive hunt, or post-incident pattern expansion is needed. Include UTC window, entities, IOCs, what was ruled out, and linked tickets.

## Handoff to CSIRT

Escalate to `incident-responder` when incident declaration criteria are met (see `incident-responder/references/incident_declaration_and_severity.md`). Include UTC timestamps, affected entities, IOCs, evidence links, and open questions. Confirmed compromises found during hunts also route through this path.
