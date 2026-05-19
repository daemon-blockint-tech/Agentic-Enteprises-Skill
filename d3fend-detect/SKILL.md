---
name: d3fend-detect
description: |
  Guides cybersecurity detection engineering using MITRE D3FEND—file analysis, identifier
  reputation, network traffic analysis, physical access monitoring, and platform monitoring.
  Covers dynamic/emulated analysis, traffic signature detection, behavior analytics, and
  integrity monitoring. Use when building detection rules, analyzing malware, monitoring
  networks, or designing SOC workflows—not for hardening (d3fend-harden), isolation
  (d3fend-isolate), or deception (d3fend-deceive).
---

# D3FEND — Detect

## When to Use

- Building file analysis pipelines (static, dynamic, emulated)
- Implementing identifier reputation checks (IP, domain, file hash, URL)
- Designing network traffic analysis and anomaly detection
- Monitoring platform health (OS, firmware, applications)
- Setting up physical access controls and surveillance
- Creating file integrity and behavioral monitoring

## When NOT to Use

- System hardening or secure configuration → `d3fend-harden`
- Network segmentation or access mediation → `d3fend-isolate`
- Honeypots or decoy operations → `d3fend-deceive`
- Threat hunting playbooks → `defensive-security-analyst`
- SIEM/SOAR engineering → `cybersecurity`

## Core Workflows

### 1. File Analysis

| Method | What It Finds | Tools |
|---|---|---|
| Static analysis | File structure, hashes, strings, imports | YARA, ssdeep, ExifTool |
| Dynamic analysis | Runtime behavior, API calls, network | Cuckoo, ANY.RUN |
| Emulated analysis | Sandboxed execution, evasion detection | Speakeasy, Unicorn |
| Content rules | Signature matching, entropy analysis | ClamAV, custom YARA |

**See `references/file_analysis.md`**

### 2. Identifier & Reputation Analysis

- IP reputation (blocklists, geo, ASN)
- Domain reputation (age, DGA, homoglyphs)
- File hash reputation (VT, local DB)
- URL analysis (phishing, redirect chains)
- Sender/MTP reputation (SPF, DKIM, DMARC)

**See `references/identifier_reputation.md`**

### 3. Network Traffic Analysis

- Protocol command analysis (DNS, HTTP, RPC, IPC)
- Payload profiling and byte sequence emulation
- Certificate analysis (active/passive)
- Connection attempt and session volume analysis
- Community deviation and signature matching

**See `references/network_traffic.md`**

### 4. Platform & Physical Monitoring

- File integrity monitoring (FIM)
- Firmware behavior analysis and verification
- OS and application performance/exception monitoring
- Scheduled job and system daemon monitoring
- Physical: electronic locks, motion, video, proximity

**See `references/platform_monitoring.md`**

## When to load references

- **File analysis** → `references/file_analysis.md`
- **Identifier reputation** → `references/identifier_reputation.md`
- **Network traffic** → `references/network_traffic.md`
- **Platform monitoring** → `references/platform_monitoring.md`
