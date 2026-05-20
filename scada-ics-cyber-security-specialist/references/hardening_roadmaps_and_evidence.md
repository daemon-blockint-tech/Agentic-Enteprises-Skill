# Hardening roadmaps and evidence

## Table of contents

1. [Roadmap structure](#roadmap-structure)
2. [Phasing and dependencies](#phasing-and-dependencies)
3. [Control families](#control-families)
4. [Validation and retest](#validation-and-retest)
5. [Evidence pack](#evidence-pack)
6. [Executive reporting](#executive-reporting)
7. [Peer skill alignment](#peer-skill-alignment)

## Roadmap structure

Build a **12–36 month OT security roadmap** aligned to business outages and capital cycles.

| Column | Description |
|---|---|
| Initiative | Short name (e.g., OT DMZ, PAM for vendors) |
| Control objective | Tie to IEC 62443-3-3 or NIST 800-82 family |
| Current state | As-is risk |
| Target state | Measurable outcome |
| Dependencies | Network refresh, vendor firmware, ops training |
| Phase | 0–quick wins, 1–foundation, 2–optimize |
| Cost band | OPEX/CAPEX rough order |
| Owner | OT security + operations sponsor |
| KPI | Metric to prove done |

## Phasing and dependencies

**Phase 0 — Quick wins (0–90 days)**

- Inventory critical assets and remote access paths
- Disable unused conduits; document exceptions
- MFA on jump servers; vendor session recording
- Emergency contacts and OT IR outline

**Phase 1 — Foundation (3–12 months)**

- Zone/conduit remediation per architecture doc
- Passive monitoring on control VLANs
- OT vulnerability triage process live
- Gold images for EWS/HMI

**Phase 2 — Optimize (12–36 months)**

- SL-T uplift per zone
- Replace EOL gear; qualified firmware program
- Integrated IT/OT SOC workflows
- Annual tabletops and restore tests for OT servers

Sequence **identity and remote access** before deep protocol analytics if budget is constrained.

## Control families

| Family | Example initiatives |
|---|---|
| Identify | Asset inventory, zone diagrams, data classification |
| Protect | Segmentation, PAM, application whitelisting on HMIs |
| Detect | SPAN monitoring, Modbus/DNP3 baselines, session alerts |
| Respond | OT IR playbook, ops liaison roster |
| Recover | Backups of logic/projects; historian restore tests |
| Govern | Policies, risk acceptance, vendor security clauses |

Crosswalk to `compliance-specialist` when audits require SOC 2, ISO 27001, or sector frameworks.

## Validation and retest

For each initiative define:

- **Test method** — config review, passive replay, tabletop, maintenance-window functional test
- **Success criteria** — measurable (e.g., 100% vendor sessions via PAM)
- **Rollback** — operations-approved backout
- **Evidence artifact** — screenshot, export, signed checklist

**Never** use production active exploitation as validation.

## Evidence pack

Assemble for auditors, insurers, or leadership:

| Artifact | Source |
|---|---|
| OT network diagram with zones | Architecture workflow |
| Asset register export | Asset management |
| Remote access policy + sample logs | IAM/PAM |
| Patch/vuln register with risk acceptances | Vuln management |
| Monitoring use-case list + sample alert | Detection |
| OT IR playbook + tabletop AAR | IR workflow |
| Gap matrix vs IEC 62443 / NIST 800-82 | Standards workflow |
| Roadmap with phase status | This reference |

Redact **safety-critical** details that should not leave the site.

## Executive reporting

One-page brief structure:

- **Posture summary** — maturity level, top 3 risks
- **Progress** — initiatives completed vs plan
- **Incidents/near misses** — OT-relevant only
- **Investments needed** — CAPEX for EOL, monitoring, staffing
- **Decisions requested** — risk acceptances, outage windows

Not a substitute for **legal compliance** or **process safety certification**.

## Peer skill alignment

| Need | Skill |
|---|---|
| Corporate security strategy | `cybersecurity` |
| Implement corp SIEM/EDR/PAM | `information-security-engineer` |
| Audit and framework mapping | `compliance-specialist`, `compliance-engineer` |
| Active IT incident | `incident-responder` |
| Hunt on IT endpoints | `threat-hunter` |
| Pentest in lab | `penetration-tester`, `hardware-in-the-loop-security-tester` |
| BCM/ransomware recovery | `bcm-disaster-recovery-specialist` |
