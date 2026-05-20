# Digital forensics scope

## Table of contents

1. [Engagement types](#engagement-types)
2. [Role boundary](#role-boundary)
3. [Authorization and coordination](#authorization-and-coordination)
4. [Deliverables](#deliverables)

## Engagement types

| Type | Typical trigger | Forensics focus |
|---|---|---|
| Insider / HR | Policy violation, data theft allegation | Host, email, cloud audit, DLP |
| External intrusion | EDR/SIEM confirmed compromise | Disk, memory, logs, lateral movement |
| Ransomware | Encryption event | Initial access, staging, exfil indicators |
| Fraud / BEC | Financial loss | Email, IdP, mailbox rules, MFA events |
| Litigation support | Counsel request | Preserved collections per legal hold |
| Insurance / regulator | Post-incident inquiry | Factual timeline and artifact inventory |

Match depth to **objectives** and **retention**—do not over-collect without scope.

## Role boundary

| digital-forensics-analyst | Partner skill |
|---|---|
| Acquisition, analysis, timelines, forensic reports | `incident-responder` — live command, containment cadence, war room |
| Deep artifact work after preservation | `soc-analyst` — alert triage, playbook execution, queue SLAs |
| Security strategy, enterprise IR policy | `cybersecurity` |
| Build SIEM/EDR, IAM, guardrails | `information-security-engineer` |
| Cloud guardrails and CSPM remediation | `cloud-security-engineer` |
| Audit control mapping and evidence binders | `compliance-engineer` |
| Authorized offensive testing | `ai-redteam`, `offensive-security-analyst` |

**Handoff pattern:** SOC (`soc-analyst`) validates and contains → IR (`incident-responder`) coordinates response → forensics preserves and analyzes → counsel reviews outputs.

## Authorization and coordination

Before acquisition:

1. Confirm **written authority** (internal policy, legal, LE request, or contract)
2. Identify **data classes** (PII, PHI, PCI, attorney-client)
3. Notify **privacy/legal** when employee or customer data is in scope
4. Document **systems already remediated** (triage actions affect artifact state)

Produce **factual** findings. Do not provide legal advice, guilt/innocence opinions, or regulatory filing decisions.

## Deliverables

Minimum set for most engagements:

- Evidence inventory and chain-of-custody log
- Super-timeline (UTC) with source per event
- Forensic investigation report (executive + technical appendix)
- IOC export for SOC consumption when applicable
- Expert witness **preparation outline** only when counsel requests—not testimony scripts
