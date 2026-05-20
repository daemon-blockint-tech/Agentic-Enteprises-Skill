---
name: red-team-specialist
description: |
  Guides authorized enterprise adversary simulation and red team operations—campaign planning,
  threat-informed objectives, MITRE ATT&CK–framed TTP selection, OPSEC and scope, purple-team
  coordination, detection validation narratives, executive reporting, and blue-team lessons learned.
  Emphasizes rules of engagement, written authorization, and no unauthorized targeting. Use for
  red team, adversary simulation, purple team, assumed breach exercise, MITRE ATT&CK campaign,
  detection gap assessment, or threat-informed emulation—not LLM/agent adversarial testing
  (ai-redteam), single-vector pentest deliverables only (web-pentester, network-pentester,
  penetration-tester as execution specialists), SOC alert triage (soc-analyst), or incident command
  (incident-responder).
---

# Red Team Specialist

## When to Use

- Plan or lead **authorized** enterprise adversary simulation (assumed breach, full-scope red team, purple team)
- Define **threat-informed objectives** aligned to business risk and threat intelligence
- Select and sequence **TTPs** using MITRE ATT&CK framing (technique IDs, detection expectations)
- Draft **rules of engagement**, scope, OPSEC constraints, and emergency stop procedures
- Coordinate **purple team** exercises and **detection validation** with blue team / SOC
- Produce **executive narratives**, attack-path stories, and remediation handoff for defenders
- Capture **lessons learned** for detection engineering, tabletop, and control improvement

## When NOT to Use

- Jailbreak LLMs, prompt injection, RAG/tool abuse, or AI safety harnesses → `ai-redteam`
- Execute hands-on web/API OWASP testing as primary deliverable → `web-pentester`
- Execute network/AD/infra pentest as primary deliverable → `network-pentester`
- Run a standard pentest engagement (recon → vuln → PoC → report) without campaign emulation → `penetration-tester`
- Triage SIEM/EDR alerts or SOC shift work → `soc-analyst`
- Proactive blue-team hunt campaigns (non-simulation) → `threat-hunter`
- Declare incidents, lead containment, or regulatory comms → `incident-responder`
- Define enterprise security strategy or GRC roadmaps → `cybersecurity`
- Implement SIEM rules, IAM, or guardrails from findings → `information-security-engineer`

## Related skills

| Need | Skill |
|---|---|
| LLM/agent adversarial testing and safety eval | `ai-redteam` |
| Multi-domain pentest under one ROE (execution) | `penetration-tester` |
| Web/API OWASP and proxy methodology | `web-pentester` |
| Network, AD, lateral movement, segmentation | `network-pentester` |
| Security program, pentest/red team governance | `cybersecurity` |
| SOC triage, alert enrichment, playbook execution | `soc-analyst` |
| Follow-on threat hunts from purple-team gaps | `threat-hunter` |
| Live incident command and stakeholder IR comms | `incident-responder` |
| Implement detections, IAM, SIEM content from gaps | `information-security-engineer` |
| Risk register updates from campaign findings | `security-risk-analyst` |
| Threat actor profiles, sector campaigns, IOC/TTP intel products | `cti-analyst` |

## Core Workflows

### 1. Scope, authorization, and OPSEC

**Do not operate without written authorization and defined scope.**

1. Confirm signed SOW/ROE: assets, methods, windows, contacts, legal constraints
2. Define objectives (crown jewels, scenarios, kill-chain depth) and success criteria
3. Agree out-of-scope (third parties, prod PII, physical access, ransomware simulation unless approved)
4. Establish OPSEC: infrastructure, attribution, comms, artifact handling
5. Document emergency stop, escalation, and purple-team visibility rules

**See `references/red_team_scope.md` and `references/scoping_roe_and_opsec.md`.**

### 2. Campaign planning and objectives

1. Map threat actors or **threat intelligence** to relevant TTPs
2. Build **campaign timeline** (phases, injects, decision points)
3. Align objectives to **detection validation** or business narrative needs
4. Reserve execution slots for specialist testers where needed

**See `references/campaign_planning_and_objectives.md`.**

### 3. TTP selection and execution coordination

```
objectives → ATT&CK mapping → playbooks → specialist execution → evidence + timeline
```

- Delegate in-scope technical work to `penetration-tester`, `web-pentester`, or `network-pentester` as appropriate
- Maintain **operator log**: UTC timestamps, technique ID, host/account, outcome, detection observed (Y/N/unknown)
- Stop at agreed impact; remove persistence and test artifacts per ROE

**See `references/ttp_selection_and_execution_coordination.md`.**

### 4. Purple team and detection validation

1. Pre-brief blue team on **expected telemetry** and safe observation windows
2. Run **inject schedule** with optional blind vs collaborative modes
3. Document **detection gaps** (missed stage, delayed alert, wrong severity)
4. Hand off **detection engineering** recommendations to `information-security-engineer` / SOC

**See `references/purple_team_and_detection_validation.md`.**

### 5. Reporting and remediation handoff

Deliver: executive summary (risk story), technical timeline, ATT&CK heatmap, detection matrix, prioritized remediations, and blue-team actions. Schedule retest or purple **re-run** for critical gaps.

**See `references/reporting_and_remediation_handoff.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries | `references/red_team_scope.md` |
| Authorization, ROE, OPSEC | `references/scoping_roe_and_opsec.md` |
| Campaign planning | `references/campaign_planning_and_objectives.md` |
| TTP selection and coordination | `references/ttp_selection_and_execution_coordination.md` |
| Purple team and detections | `references/purple_team_and_detection_validation.md` |
| Reporting and handoff | `references/reporting_and_remediation_handoff.md` |
