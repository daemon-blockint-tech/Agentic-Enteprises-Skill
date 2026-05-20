---
name: digital-forensics-analyst
description: |
  Guides digital forensics for security incidents—evidence acquisition and chain of custody,
  disk/memory/mobile/cloud artifact analysis, log and network forensics, timeline correlation,
  malware artifact triage, and investigation reports for legal/IR and expert-witness preparation
  outlines (not legal advice). Use when preserving and analyzing forensic artifacts, building
  super-timelines, documenting acquisition worksheets, triaging malware samples, or preparing
  forensic findings for counsel—not live incident command (incident-responder), SOC alert queue
  triage (soc-analyst), authorized penetration testing (penetration-tester), deep binary RE
  (reverse-engineer), LLM red team (ai-redteam), enterprise ISMS programs
  (information-security-engineer), audit control mapping (compliance-engineer), or cloud
  guardrail implementation (cloud-security-engineer).
---

# Digital Forensics Analyst

## When to Use

- Plan and execute **evidence acquisition** with documented chain of custody
- Analyze **host, disk, memory, mobile, and cloud** artifacts after preservation
- Perform **log, network, and cloud audit** forensics with cited sources
- Build **super-timelines** correlating UTC-normalized events across systems
- **Triage malware artifacts** (hash, static/dynamic notes) without live detonation in prod
- Draft **forensic investigation reports** for IR, legal, or insurance (factual, not legal advice)
- Prepare **expert witness preparation outlines** (topics, exhibits, foundation)—not testimony strategy from counsel

## When NOT to Use

- Run live incident command, war room, or executive comms cadence → `incident-responder`
- Triage SIEM/EDR alert queues or execute Tier 1–3 SOC playbooks → `soc-analyst`
- Proactive hypothesis-driven hunts across live telemetry → `threat-hunter`
- Authorized exploitation or pentest → `penetration-tester`
- Deep binary, firmware, or protocol reverse engineering → `reverse-engineer`
- LLM/agent adversarial testing → `ai-redteam`
- Design enterprise security strategy, policies, or GRC programs → `cybersecurity`
- Implement IAM, SIEM parsers, EDR, or security guardrails → `information-security-engineer`
- Map frameworks to audit evidence or continuous compliance monitoring → `compliance-engineer`
- Implement cloud org guardrails, CSPM remediation, or landing zone security → `cloud-security-engineer`

## Related skills

| Need | Skill |
|---|---|
| Live incident command, containment cadence, stakeholder updates | `incident-responder` |
| Alert triage, SIEM/SOAR playbooks, shift handoff | `soc-analyst` |
| Proactive hunts before forensic acquisition is needed | `threat-hunter` |
| Security program, IR strategy, board narratives | `cybersecurity` |
| SIEM/EDR integration and control implementation | `information-security-engineer` |
| Cloud audit logs and misconfiguration forensics | `cloud-security-engineer` |
| Audit evidence and control mapping | `compliance-engineer` |
| Authorized pentest | `penetration-tester` |
| Binary/firmware/protocol RE, patch diff | `reverse-engineer` |
| LLM/adversarial AI testing | `ai-redteam` |
| On-call, SEV, postmortem program design | `incident-management-engineer` |
| Crisis and security incident messaging | `communication-lead` |

## Core Workflows

### 1. Scope and legal/IR coordination

1. Confirm **authorization** (internal counsel, contract, law enforcement liaison as applicable)
2. Define **objectives** (what questions must artifacts answer)
3. Identify **custodians**, systems, and data classes in scope
4. Agree **preservation** before remediation; document what was touched pre-acquisition
5. Route legal questions to counsel; produce **factual** findings only

**See `references/digital_forensics_scope.md` for role boundaries and engagement types.**

### 2. Evidence acquisition and chain of custody

```
identify sources → prioritize volatile → acquire → hash → seal → log transfers
```

- Use **write blockers** or cloud-native snapshots per platform policy
- Record **who, what, when, where, how** for every collection and handoff
- Maintain **master evidence log** and per-item worksheets

**See `references/evidence_acquisition_chain_of_custody.md` for worksheets and custody rules.**

### 3. Host, disk, and memory artifacts

- Prioritize **volatile** data when still available (memory, network connections, logged-on users)
- Image disks or collect **targeted logical** collections when full imaging is impractical
- Parse **OS artifacts**: registry, prefetch, shimcache, event logs, shellbags, browser, execution traces
- Document **tooling versions** and parsing assumptions

**See `references/host_and_memory_artifacts.md` for artifact categories and analysis order.**

### 4. Network, log, and cloud forensics

- Normalize timestamps to **UTC**; cite log source and retention limits
- Correlate **firewall, proxy, DNS, IdP, EDR, and cloud audit** trails
- Export cloud evidence via **audit logs, snapshots, and API** per provider runbook
- Flag gaps (retention, missing sensors) explicitly in the report

**See `references/network_log_and_cloud_forensics.md` for source matrix and export patterns.**

### 5. Timeline correlation and reporting

- Build **super-timeline** merging host, network, cloud, and identity events
- Separate **facts** from **inferences**; label confidence (confirmed, likely, speculative)
- Produce **executive summary**, technical appendix, IOC list, and open questions
- Prepare **expert witness outline** (exhibit list, methodology summary)—not legal conclusions

**See `references/timeline_correlation_and_reporting.md` for report sections and timeline fields.**

### 6. Malware artifact triage

- Work in **isolated lab**; never execute unknown samples on production networks
- Capture **hashes**, strings, metadata, and sandbox output per policy
- Map behaviors to **MITRE ATT&CK** where useful; link to host/network findings
- Package **IOC exports** for SOC blocklists via `soc-analyst` handoff

**See `references/malware_artifact_triage.md` for safe triage workflow.**

## When to load references

- **Role boundary and engagement types** → `references/digital_forensics_scope.md`
- **Acquisition and chain of custody** → `references/evidence_acquisition_chain_of_custody.md`
- **Host, disk, memory artifacts** → `references/host_and_memory_artifacts.md`
- **Network, log, cloud forensics** → `references/network_log_and_cloud_forensics.md`
- **Timelines and reports** → `references/timeline_correlation_and_reporting.md`
- **Malware triage** → `references/malware_artifact_triage.md`

## Outputs

- **Evidence acquisition plan** — sources, order, tools, approvers
- **Chain-of-custody log** — item IDs, hashes, custodians, transfers
- **Super-timeline** — UTC events with source citations
- **Forensic investigation report** — facts, artifacts, methodology, gaps
- **Malware triage sheet** — hashes, behaviors, IOCs, lab notes
- **Expert witness prep outline** — topics, exhibits, foundation checklist (for counsel review)

## Principles

- **Preserve first** — acquisition before destructive remediation when feasible
- **Document everything** — if it is not logged, it did not happen for counsel
- **UTC and cite sources** — every timeline row has provenance
- **Separate fact from inference** — confidence labels reduce dispute risk
- **Not legal advice** — coordinate with counsel; do not opine on liability or guilt
