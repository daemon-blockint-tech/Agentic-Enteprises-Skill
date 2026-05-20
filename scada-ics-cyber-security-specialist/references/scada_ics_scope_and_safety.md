# SCADA/ICS scope and safety

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Safety and operational constraints](#safety-and-operational-constraints)
6. [Roles and RACI](#roles-and-raci)
7. [Handoffs](#handoffs)

## Purpose

Establish **OT/ICS cyber security** program boundaries so assessments, designs, and roadmaps respect **process safety**, **availability**, and site-specific operating procedures.

This skill covers **program design, architecture, assessment, and playbook authoring**—not live plant manipulation or unsupervised testing.

## Terminology

| Term | Meaning |
|---|---|
| OT | Operational technology — hardware/software that monitors or controls physical processes |
| ICS | Industrial control system — SCADA, DCS, PLC-centric systems |
| SCADA | Supervisory control and data acquisition — HMIs, historians, wide-area telemetry |
| DCS | Distributed control system — integrated control in continuous processes |
| Purdue / ISA-95 | Reference model for levels L0–L5 and zone segmentation |
| Engineering workstation | Config tools for PLCs/RTUs; high-value target |
| SIS | Safety instrumented system — often separate from BPCS; highest caution |

## In scope

| Area | Examples |
|---|---|
| Program | OT security policy, standards alignment, metrics, vendor management |
| Architecture | Zones, conduits, DMZ, data diodes (conceptual), remote access |
| Assets | PLCs, RTUs, I/O, HMIs, historians, OPC servers, protocol gateways |
| Vulnerability | OT CVE triage, vendor advisories, compensating controls, patch windows |
| Monitoring | Passive ICS traffic, asset behavior baselines, remote session alerts |
| IR planning | Safety-first playbooks, coordination with IT IR and operations |
| Threat intel | OT-centric campaigns (TRITON, Industroyer classes) at awareness level |
| Convergence | Shared AD, cloud historians, VPN into OT, supply chain for OT vendors |

## Out of scope

| Topic | Route to |
|---|---|
| Live CSIRT command on IT corporate estate | `incident-responder` |
| SOC alert triage without OT context | `soc-analyst` |
| IT network pentest methodology | `network-pentester` |
| Web/API testing | `web-pentester` |
| Red-team exploitation on IT | `penetration-tester` |
| HIL fault injection and bus-level bench tests | `hardware-in-the-loop-security-tester` |
| Enterprise GRC and audit program | `compliance-specialist` |
| Corporate SIEM/EDR deployment | `information-security-engineer` |
| Process safety engineering (SIL, LOPA) | Site process safety / engineering |
| Legal or regulatory determinations | Legal/compliance counsel |

## Safety and operational constraints

**Never instruct** the agent or operator to:

- Change setpoints, logic, or I/O on live equipment without written operations authorization
- Run vulnerability scanners, port scans, or fuzzing against production PLCs/RTUs
- Disable interlocks, safety systems, or antivirus on OT without documented change control
- Bridge OT and IT networks without an approved conduit design

**Prefer instead:**

- Document review, passive monitoring, vendor maintenance windows, lab replicas, and tabletop exercises
- Engage **operations**, **maintenance**, and **vendor OEM** before any change that touches control logic
- Use **maintenance mode** and **backup/restore** procedures per site runbooks

## Roles and RACI

| Activity | OT security | Operations | IT security | Engineering | Vendor |
|---|---|---|---|---|---|
| Zone architecture approval | C | A | C | C | I |
| Asset inventory accuracy | A | C | I | C | C |
| Patch decision (defer/apply) | C | A | I | C | C |
| Remote access policy | A | C | C | I | C |
| OT IR playbook | A | C | C | I | I |
| Passive monitoring deployment | C | C | C | A | C |

(A = accountable, R = responsible, C = consulted, I = informed — adapt to site RACI.)

## Handoffs

- **To `incident-responder`** — when an event crosses into corporate IT, identity, or widespread ransomware; OT lead retains safety sequencing
- **To `digital-forensics-analyst`** — when disk images, malware analysis, or legal hold on OT hosts is required (with operations approval)
- **To `compliance-specialist`** — when audit scope spans IT and OT frameworks and evidence binders
- **To `hardware-in-the-loop-security-tester`** — when validation requires bench HIL, not production
