# Reverse engineer scope

## Table of contents

1. [Engagement types](#engagement-types)
2. [Role boundary](#role-boundary)
3. [In-scope activities](#in-scope-activities)
4. [Out-of-scope activities](#out-of-scope-activities)
5. [Handoff patterns](#handoff-patterns)

## Engagement types

| Type | Typical trigger | RE focus |
|---|---|---|
| Vulnerability research | CVE, bug bounty, internal audit | Root cause, patch diff, variants |
| Malware defense | SOC/IR sample, threat intel | Behavior, IOCs, YARA ideas |
| Protocol/format RE | Interop, legacy system, security review | Wire format, parsers, crypto usage |
| Firmware assessment | IoT, appliance, embedded (authorized) | Image layout, update path, keys |
| Incident support | IR team needs binary understanding | Targeted function/protocol analysis |
| Patch analysis | Vendor advisory, emergency fix | Diff, regression surfaces |

Match depth to **authorization** and **objectives**—do not expand scope without written approval.

## Role boundary

| reverse-engineer | Partner skill |
|---|---|
| Binary/firmware/protocol RE, patch diff, vuln research docs | `digital-forensics-analyst` — disk/memory acquisition, custody, super-timelines |
| Static/dynamic malware understanding for defense | `incident-responder` — live command, containment cadence, stakeholder updates |
| IOCs and detection ideas from RE | `soc-analyst` — alert triage, playbook execution, queue SLAs |
| Authorized exploitation and pentest PoCs | `penetration-tester` — ROE, attack paths, remediation retest |
| Enterprise vuln program and research policy | `cybersecurity` |
| LLM jailbreaks and agent abuse | `ai-redteam` |
| SAST, SBOM, CI gates on source | `devsecops` |

## In-scope activities

- Disassembly, decompilation, and control-flow/data-flow analysis
- Debugger-driven dynamic analysis in isolated environments
- Protocol and file-format reconstruction from samples
- Defensive malware triage (no distribution of weaponized payloads)
- Patch and binary diffing for security impact
- Documenting vulnerabilities with remediation guidance
- Ghidra/IDA/Binary Ninja/radare2-style workflows and automation notes

## Out-of-scope activities

- Full forensic imaging, chain-of-custody worksheets, expert witness prep → forensics skill
- Running live incident war rooms or executive comms → IR skill
- SIEM alert closure and Tier 1–3 SOC playbooks → SOC skill
- In-scope exploitation chains for pentest deliverables → pentest skill
- Bypassing license/DRM on software you do not own or lack rights to analyze
- Advising on export-controlled technique transfer without legal review

## Handoff patterns

1. **SOC → RE:** SOC (`soc-analyst`) collects sample/hash and context → RE analyzes in lab → returns IOCs/YARA ideas → SOC validates blocks and detections.
2. **IR → RE:** IR (`incident-responder`) preserves scope and priorities → RE explains binary/protocol facet → IR coordinates containment with engineering.
3. **RE → Forensics:** RE identifies need for host/disk/legal-grade timeline → `digital-forensics-analyst` owns acquisition and custody.
4. **RE → Pentest:** RE finds architectural weakness → pentest (`penetration-tester`) validates exploitability only under separate ROE if required.
