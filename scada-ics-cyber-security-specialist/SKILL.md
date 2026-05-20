---
name: scada-ics-cyber-security-specialist
description: |
  Guides OT/ICS and SCADA cyber security—Purdue zones, IEC 62443 and NIST SP 800-82 (practitioner),
  OT asset inventory (PLCs, RTUs, HMIs, historians), secure remote access, OT patch/vuln management,
  ICS protocol monitoring (Modbus, DNP3, OPC, BACnet high level), safety-first IR, OT threat classes
  (TRITON, Industroyer), hardening roadmaps, IT/OT convergence. Use for OT program scope, ICS
  segmentation, OT vuln/patch, detection/IR playbooks, vendor remote access, IEC 62443 or NIST 800-82
  gaps—not IT network pentest (network-pentester), web apps (web-pentester), HIL bench only
  (hardware-in-the-loop-security-tester), GRC only (compliance-specialist), SOC triage (soc-analyst),
  or IT IR without OT safety (incident-responder). Safety over aggressive testing; no unsafe live-plant
  steps.
---

# SCADA / ICS Cyber Security Specialist

## When to Use

- Define **OT/ICS security program scope**, governance, and IT/OT coordination model
- Design **Purdue/ISA-95 zones**, conduits, segmentation, and DMZ patterns for control networks
- Build **OT asset inventory** — PLCs, RTUs, HMIs, historians, engineering workstations, gateways
- Plan **secure remote access** — jump hosts, PAM, vendor sessions, MFA, session recording
- Manage **patch and vulnerability** programs under change windows, compensating controls, and vendor SLAs
- Scope **ICS-aware monitoring** — passive taps, DPI for Modbus/DNP3/OPC/BACnet (high level), baselines
- Author **safety-first OT incident response** — coordination with operations, process safety, and IT IR
- Map **IEC 62443** and **NIST SP 800-82** concepts to gaps, SL-T targets, and remediation priorities
- Produce **hardening roadmaps** and evidence packs for audits, insurers, and leadership (not legal advice)
- Assess **IT/OT convergence** risks — shared AD, cloud historians, remote ops, supply chain

## When NOT to Use

- Generic **corporate network pentest** without OT methodology → `network-pentester`
- **Web application** or API testing → `web-pentester`
- **Authorized exploitation** and red-team validation on IT paths → `penetration-tester`
- **HIL bench**, automotive ECU, or embedded fault-injection testing → `hardware-in-the-loop-security-tester` (complement for lab validation)
- **Enterprise GRC program**, audit prep, or vendor questionnaires without OT lens → `compliance-specialist`
- **SOC alert triage** and corporate detection playbooks only → `soc-analyst`
- **IT-centric incident command** without process-safety and operations coordination → `incident-responder`
- **Corporate SIEM/EDR/IdP** implementation without OT architecture → `information-security-engineer`
- **Security strategy and board metrics** without OT program delivery → `cybersecurity`
- **Control-by-control evidence automation** for IT SOC 2 → `compliance-engineer`
- **Proactive threat hunting** on corporate IT telemetry only → `threat-hunter`

## Related skills

| Need | Skill |
|---|---|
| Corporate security program, policies, board narratives | `cybersecurity` |
| SIEM/EDR/IdP/PAM for enterprise IT stack | `information-security-engineer` |
| GRC program, framework scoping, audit coordination | `compliance-specialist` |
| Technical compliance evidence and control automation | `compliance-engineer` |
| Active IT IR war room, containment, legal coordination | `incident-responder` |
| SOC queue triage and corporate playbooks | `soc-analyst` |
| Hypothesis-driven hunts on IT endpoints/logs | `threat-hunter` |
| Authorized pentest and exploit validation | `penetration-tester` |
| Network/AD/infra pentest from corp paths | `network-pentester` |
| Web/API OWASP testing | `web-pentester` |
| HIL, bus injection, automotive/industrial bench safety | `hardware-in-the-loop-security-tester` |

## Core Workflows

### 1. Scope, safety, and governance

Define OT boundaries, safety constraints, roles, and handoffs with operations and IT.

**See `references/scada_ics_scope_and_safety.md`.**

### 2. Architecture and segmentation

Apply Purdue zones, conduits, remote access, and IT/OT convergence controls.

**See `references/ot_architecture_and_segmentation.md`.**

### 3. Standards and assessment

Map IEC 62443 and NIST SP 800-82 to gaps, maturity, and security levels (practitioner level).

**See `references/standards_and_assessment.md`.**

### 4. Asset and vulnerability management

Inventory OT assets; prioritize vulns with OT change constraints and compensating controls.

**See `references/ot_asset_vulnerability_management.md`.**

### 5. Detection and incident response

ICS monitoring patterns, safety-first IR sequencing, and OT threat classes.

**See `references/ot_detection_and_incident_response.md`.**

### 6. Hardening roadmaps and evidence

Phased remediation, metrics, test plans, and audit-ready artifacts.

**See `references/hardening_roadmaps_and_evidence.md`.**

## Outputs

- **OT security charter** — scope, RACI, safety gates, escalation to operations and IT IR
- **Zone/conduit diagram** — Purdue levels, data flows, remote access paths, crown jewels
- **OT asset register** — device class, firmware, zone, owner, criticality, connectivity
- **Vulnerability and patch register** — CVE/vendor advisory, risk, compensating control, change window
- **Secure remote access design** — vendor access, session controls, logging, break-glass
- **Detection use-case list** — protocol anomalies, engineering changes, remote sessions (high level)
- **OT IR playbook outline** — safety hold points, isolation options, evidence preservation
- **Standards gap matrix** — IEC 62443 / NIST 800-82 mapping with prioritized remediation
- **Hardening roadmap** — phases, dependencies, metrics, validation criteria
- **Executive OT security brief** — posture, top risks, test results (not legal or safety certification)

## Principles

- **Safety and availability first** — never recommend actions that could trip plant, endanger people, or violate site safety rules without operations approval
- **No unsafe live-plant testing** — prefer passive assessment, documentation review, lab replicas, and vendor-supported validation
- **Assume brittle systems** — patches, scans, and aggressive active tests can fault controllers; plan compensating controls
- **Separate IT and OT evidence** — corporate SOC findings do not equal OT coverage; document zone boundaries
- **Coordinate with operations** — process engineers and electricians own physical consequences; security owns risk framing
- **Document accepted risk** — deferred patches and legacy protocols need explicit sign-off and monitoring
