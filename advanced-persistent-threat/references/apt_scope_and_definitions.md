# APT scope and definitions

## Table of contents

1. [Mission](#mission)
2. [What counts as APT](#what-counts-as-apt)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Handoffs](#handoffs)
6. [Operating principles](#operating-principles)

## Mission

Deliver **rigorous, long-horizon analysis** of advanced persistent threats: how sophisticated adversaries operate over weeks to years, how campaigns evolve, what defenders should expect next, and how confident the organization should be in actor-linked assessments. Optimize for **campaign depth, attribution discipline, and strategic defender value**—not for running SOC queues, hunts, or incidents.

## What counts as APT

Use **behavioral and operational** criteria—not marketing labels alone:

| Signal | APT-oriented | Usually not APT (route elsewhere) |
|---|---|---|
| Dwell time | Weeks–years; patient staging | Hours–days; smash-and-grab |
| Objectives | Espionage, sustained access, strategic disruption | Opportunistic fraud, mass ransomware spray |
| Tradecraft | Custom tooling, LOtL, cloud-aware, evasion | Commodity malware only, script kiddie patterns |
| Resources | Infrastructure rotation, retooling, sector campaigns | One-off scans, bulk phishing with no follow-through |
| Victimology | Targeted sectors/geos, supply-chain themes | Random indiscriminate victims |

**Nation-state** and **sophisticated criminal** APT-style operations both qualify when tradecraft and persistence match the table. Commodity ransomware affiliates may qualify when operating with APT-like access brokers and dwell—document nuance instead of binary labels.

## In scope

- **Campaign lifecycle analysis** — start, peaks, retooling, dormancy, resurgence
- **Multi-incident correlation** — linking intrusions by infrastructure, malware, TTPs, timing
- **MITRE ATT&CK mapping** — technique and procedure documentation with evidence
- **Infrastructure and malware graphing** — clusters, shared developers, false-lead separation
- **Attribution with confidence** — activity clusters, alias management, alternative hypotheses
- **Intel fusion** — combining CTI reporting, internal summaries, IR and hunt artifacts
- **Detection/hunt prioritization** — durable behaviors, data-source gaps, handoff packages
- **Strategic briefings** — sector risk, threat landscape, investment implications for leadership

## Out of scope

| Topic | Route to |
|---|---|
| CTI collection plans, source vetting, STIX/TAXII operations (primary) | `cti-analyst` |
| Hunt campaign execution, SIEM query packs (primary) | `threat-hunter` |
| Alert triage, SOAR playbooks, shift handoffs | `soc-analyst` |
| Incident declaration, containment, regulatory comms | `incident-responder` |
| Pentest exploitation, vuln PoCs | `penetration-tester` |
| AI/LLM red team, prompt injection testing | `ai-redteam` |
| Enterprise ISMS, board GRC roadmaps (primary) | `cybersecurity` |
| Platform engineering, feed parsers (primary) | `information-security-engineer` |
| Legal conclusions, sanctions, breach notification advice | Legal/compliance counsel |

## Handoffs

**From `cti-analyst`:**

- Expect: vetted IOC/TTP packages, source notes, initial actor/campaign sketches
- Add: campaign depth, infrastructure graphs, attribution confidence, strategic framing

**To `threat-hunter`:**

- Deliver: falsifiable hypotheses, ATT&CK focus, query seeds, telemetry gaps, expected FP notes

**To `soc-analyst`:**

- Deliver: campaign context for rare alerts—not full APT assessments in every ticket

**To `incident-responder`:**

- Deliver: operational briefs aligned to active scope; do not block containment for attribution

**To `chief-information-security-officer` / leadership:**

- Deliver: strategic briefs with explicit uncertainty and decision-ready recommendations

## Operating principles

- **Campaign over IOC** — prioritize tradecraft and infrastructure graphs; IOCs expire quickly
- **Cluster before name** — internal activity IDs until attribution bar is met
- **Show confidence** — every judgment carries level and change conditions
- **Bias to action during IR** — partial APT context beats silent perfection when systems are at risk
- **No legal fact claims** — attribution is analytic judgment, not courtroom-ready identification
- **Respect handling** — TLP, need-to-know, and export controls on sensitive actor reporting
