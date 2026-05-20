---
name: reverse-engineer
description: |
  Guides authorized reverse engineering—static and dynamic binary analysis, disassembly and
  decompilation workflows, protocol and file-format reversing, defensive malware analysis
  (behavior, IOCs, YARA ideas), firmware RE, patch diffing, and vulnerability research
  documentation. Emphasizes written authorization, export-control awareness, and no assistance
  bypassing protections on unowned or unlicensed software. Use for reverse engineering, disassemble,
  decompile, Ghidra/IDA-style workflows, binary analysis, malware analysis for defense, firmware RE,
  patch analysis—not disk imaging forensics (digital-forensics-analyst), live incident command
  (incident-responder), SOC alert triage (soc-analyst), authorized pentest exploitation
  (penetration-tester), LLM red team (ai-redteam), or CI pipeline gates (devsecops).
---

# Reverse Engineer

## When to Use

- Perform **authorized** static or dynamic analysis of binaries, libraries, or firmware
- Run **disassembly/decompilation** workflows (Ghidra, IDA, Binary Ninja, radare2, objdump)
- Reverse **protocols, file formats, or wire formats** for interoperability or security research
- Conduct **defensive malware analysis**—behavior, IOCs, YARA rule ideas, ATT&CK mapping
- **Patch diff** vendor updates or CVE fixes to find root cause and variant surfaces
- Document **vulnerability research** with reproducible steps, impact, and remediation guidance
- Analyze **firmware/images** when you own or are contracted to assess the target

## When NOT to Use

- Acquire disk/memory images, chain of custody, super-timelines for legal/IR → `digital-forensics-analyst`
- Lead live incident command, war room, or stakeholder comms → `incident-responder`
- Triage SIEM/EDR alert queues or SOC playbooks → `soc-analyst`
- Proactive enterprise telemetry hunts → `threat-hunter`
- Execute authorized exploitation, pentest PoCs, or attack playbooks → `penetration-tester`
- Jailbreak LLMs, prompt injection, or agent tool abuse → `ai-redteam`
- Define enterprise security strategy or GRC programs → `cybersecurity`
- Add SAST, SBOM, or CI/CD security gates → `devsecops`

## Related skills

| Need | Skill |
|---|---|
| Forensic acquisition, custody, host/disk/memory artifacts | `digital-forensics-analyst` |
| Live IR coordination, containment cadence, breach comms | `incident-responder` |
| Alert triage, SIEM/SOAR playbooks, IOC blocking handoff | `soc-analyst` |
| Hunt-surfaced samples needing deep RE | `threat-hunter` (handoff from) |
| Authorized offensive testing and exploitation within ROE | `penetration-tester` |
| Security program, vuln management, research governance | `cybersecurity` |
| LLM/agent adversarial testing | `ai-redteam` |
| Pipeline scanning, SBOM, supply-chain gates | `devsecops` |
| Headless binary RE (Ghidra) | `ghidra-headless` (if installed) |

## Core Workflows

### 1. Authorization and scope

**Do not analyze targets without clear legal authority.**

1. Confirm **written authorization** (employer asset, customer SOW, bug bounty, coordinated disclosure)
2. Verify **ownership or license** to analyze the binary/firmware
3. Check **export control** and jurisdictional restrictions before sharing artifacts or techniques
4. Define **in-scope** artifacts, environments (isolated lab), and deliverables
5. Refuse requests to bypass DRM, license checks, or protections on **unowned** software

**See `references/legal_authorization_and_ethics.md` and `references/reverse_engineer_scope.md`.**

### 2. Static analysis

```
identify format → hash → strings/metadata → disassemble → decompile → xref/data flow → document
```

- Record **tool versions**, hashes (SHA-256), and file provenance
- Map **entry points**, imports, exports, and interesting strings
- Label **assumptions** vs confirmed facts in notes

**See `references/static_analysis_workflows.md`.**

### 3. Dynamic analysis and debugging

- Use **isolated VMs** or dedicated lab networks; snapshot before execution
- Capture **API/file/registry/network** behavior per platform
- Correlate runtime observations with static hypotheses
- Never detonate unknown malware on production networks

**See `references/dynamic_analysis_and_debugging.md`.**

### 4. Malware and firmware

- Triage samples in **malware lab**; document behaviors and IOCs for SOC handoff
- Extract **configs, C2 indicators, and persistence** for defensive use
- For firmware: identify **image layout**, boot chain, and update mechanisms
- Coordinate with `digital-forensics-analyst` when legal-grade preservation is required

**See `references/malware_and_firmware_reversing.md`.**

### 5. Reporting, IOCs, and patch diffing

- Produce **reproducible** steps, affected versions, and remediation recommendations
- Export **IOCs** and YARA **ideas** (test in lab before production deployment)
- Diff patches with clear **before/after** semantics and variant hunting notes
- Separate **facts** from speculation; cite offsets, functions, or commits

**See `references/reporting_iocs_and_patch_diffing.md`.**

## When to load references

- **Role boundary and engagement types** → `references/reverse_engineer_scope.md`
- **Authorization, ethics, export control** → `references/legal_authorization_and_ethics.md`
- **Static RE workflow** → `references/static_analysis_workflows.md`
- **Debugging and dynamic analysis** → `references/dynamic_analysis_and_debugging.md`
- **Malware and firmware** → `references/malware_and_firmware_reversing.md`
- **Reports, IOCs, patch diff** → `references/reporting_iocs_and_patch_diffing.md`

## Outputs

- **RE analysis notes** — hashes, toolchain, key functions, data structures
- **Behavior summary** — API/network/file actions with confidence labels
- **IOC list** — hashes, domains, IPs, mutexes, paths (for SOC ingestion)
- **YARA rule draft** — tested strings/byte patterns with false-positive notes
- **Patch diff report** — changed functions, security relevance, variant ideas
- **Vulnerability research memo** — impact, preconditions, affected versions, fix guidance

## Principles

- **Authorize first** — no RE on unowned or unlicensed targets
- **Lab isolation** — especially for malware and exploit-adjacent work
- **Document provenance** — hashes, versions, and tool chain on every deliverable
- **Defensive bias** — IOCs, detections, and fixes over offensive reuse
- **Refuse bypass assistance** — do not help circumvent protections without lawful authority
