---
name: threat-hunter
description: |
  Guides proactive threat hunting for advanced SOC—hypothesis-driven hunt campaigns, advanced SIEM/query
  workflows, baseline and anomaly analysis, MITRE ATT&CK–aligned techniques, threat intel fusion,
  detection engineering feedback, and hunt reporting with IR handoff. Use for threat hunting, proactive
  hunt, hypothesis-driven detection, advanced SOC, hunt campaign, detection engineering, MITRE ATT&CK
  hunt, anomaly hunting—not routine SOC alert triage (soc-analyst), declared incident command
  (incident-responder), adversary simulation campaigns (red-team-specialist), disk forensics
  acquisition (digital-forensics-analyst), authorized pentest (penetration-tester), or binary RE
  lab work (reverse-engineer).
---

# Threat Hunter (Advanced SOC)

## When to Use

- Plan and execute **hypothesis-driven hunt campaigns** (intel-led, ATT&CK-led, or baseline-led)
- Run **advanced SIEM/SQL/KQL/SPL** queries across identity, endpoint, network, email, and cloud telemetry
- Perform **baseline and anomaly** analysis when detections are sparse or evasive
- **Fuse threat intel** (reports, ISAC feeds, campaign IOCs) into hunt plans and pivot queries
- **Map behaviors to MITRE ATT&CK** and document technique coverage gaps
- Deliver **detection engineering feedback**—candidate rules, data gaps, tuning notes
- Produce **hunt reports** and hand off confirmed malicious activity to CSIRT

## When NOT to Use

- Triage and close routine SOC alerts, SOAR playbooks, shift handoffs → `soc-analyst`
- Declare incidents, lead containment, regulatory comms, or war room → `incident-responder`
- Plan or execute authorized red team / adversary simulation campaigns → `red-team-specialist`
- Acquire disk/memory images, chain of custody, super-timelines for counsel → `digital-forensics-analyst`
- Authorized exploitation, vuln validation, or pentest deliverables → `penetration-tester`
- Deep disassembly, decompilation, or malware RE lab work → `reverse-engineer`
- Implement cloud guardrails, CSPM remediation, or landing zone security → `cloud-security-engineer`
- Define enterprise security strategy, ISMS, or GRC roadmaps → `cybersecurity`

## Related skills

| Need | Skill |
|---|---|
| SOC alert triage, playbooks, false-positive closure | `soc-analyst` |
| Declared incident command, containment, stakeholder IR | `incident-responder` |
| Security program, hunt program governance, board narrative | `cybersecurity` |
| Cloud audit log hunts, org-wide cloud telemetry gaps | `cloud-security-engineer` |
| Purple team / adversary simulation and detection validation | `red-team-specialist` |
| Authorized pentest findings as hunt hypotheses | `penetration-tester` |
| Forensic acquisition after hunt confirms major incident | `digital-forensics-analyst` |
| Sample-driven static/dynamic analysis from hunt artifacts | `reverse-engineer` |
| CTI briefs, IOC/TTP packages, actor/campaign analysis | `cti-analyst` |

## Escalation chain

1. **`soc-analyst`** — triages alerts, enriches, runs playbooks; escalates suspicious clusters or hunt requests.
2. **`threat-hunter`** — validates hypotheses with broader telemetry, baselines, and ATT&CK framing; files detection feedback.
3. **`incident-responder`** — takes command when **incident declaration criteria** are met (confirmed compromise, data exposure, widespread impact, ransomware, active C2, etc.).

Hunters do **not** replace SOC queues or IR command. Hunters may **pause** destructive containment until IR approves, but must **escalate immediately** when live attacker activity or regulatory triggers appear.

## Core Workflows

### 1. Intake and hypothesis

1. Capture trigger: SOC escalation, intel report, purple-team gap, post-incident pattern, leadership ask
2. State **hypothesis** in falsifiable form (“If actor X, we will see Y in Z data”)
3. Define success criteria, time range, data sources, and out-of-scope systems
4. Estimate effort; open hunt record with ID and owner

**See `references/hypothesis_and_hunt_planning.md`.**

### 2. Hunt execution

1. Inventory available telemetry; log **gaps** that block the hypothesis
2. Run staged queries (broad → narrow); save queries and result counts
3. Baseline “normal” for key entities; flag statistically or behaviorally rare events
4. Pivot on entities (user, host, IP, app, cloud principal, session)
5. Correlate across domains; attach UTC timestamps and source systems

**See `references/siem_query_and_telemetry.md`.**

### 3. Intel and ATT&CK mapping

1. Map observed behaviors to **technique IDs**; note procedure-level detail when known
2. Compare to relevant intel (sector campaign, actor profile, recent CVE/exploit chain)
3. Document **coverage**: detected vs hunted-only vs no visibility

**See `references/threat_intel_and_attck_mapping.md`.**

### 4. Detection feedback

1. For sustained true positives, draft **candidate detection** (logic, data source, expected FP rate)
2. Specify **logging gaps** (missing fields, retention, parser errors)
3. Hand tuning notes to detection owners; link hunt ID in ticket

**See `references/detection_engineering_feedback.md`.**

### 5. Report and handoff

1. Summarize hypothesis, methods, findings, and confidence
2. List IOCs, entities, and recommended actions (monitor, block, isolate, declare incident)
3. Route **confirmed incidents** to `incident-responder` with evidence package
4. Route **benign closure** back to `soc-analyst` with context for alert tuning

**See `references/hunt_reporting_and_handoff.md`.**

## When to load references

- **Role boundaries and handoffs** → `references/threat_hunter_scope.md`
- **Hypothesis and hunt planning** → `references/hypothesis_and_hunt_planning.md`
- **SIEM queries and telemetry** → `references/siem_query_and_telemetry.md`
- **Threat intel and ATT&CK** → `references/threat_intel_and_attck_mapping.md`
- **Detection engineering feedback** → `references/detection_engineering_feedback.md`
- **Hunt reporting and handoff** → `references/hunt_reporting_and_handoff.md`

## Outputs

- **Hunt plan** — hypothesis, scope, data sources, ATT&CK focus, timeline
- **Query pack** — saved searches with parameters and result summaries
- **Findings table** — entity, behavior, technique, evidence pointers, confidence
- **Detection backlog** — candidate rules, gaps, tuning recommendations
- **Hunt report** — executive summary, technical detail, next steps
- **IR handoff package** — when escalating to `incident-responder`
