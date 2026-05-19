---
name: d3fend-evict
description: |
  Guides cybersecurity eviction and incident response using MITRE D3FEND—credential revocation,
  account locking, process termination, file removal, and system recovery. Covers containment
  actions during incidents: killing malicious processes, revoking compromised credentials,
  removing persistent files, and restoring systems. Use during active incident response,
  containment, eradication—not for detection (d3fend-detect), hardening (d3fend-harden),
  or forensic investigation (incident-management-engineer).
---

# D3FEND — Evict

## When to Use

- Responding to active security incidents requiring containment
- Revoking compromised credentials and locking accounts
- Terminating malicious processes and sessions
- Removing malicious files, registry keys, and email
- Evicting adversary presence (shutdown, reboot, disk operations)
- Coordinating takedowns (domain registration, DNS cache)

## When NOT to Use

- Building detection or monitoring → `d3fend-detect`
- System hardening or prevention → `d3fend-harden`
- Network segmentation → `d3fend-isolate`
- Forensic investigation and evidence preservation → `incident-management-engineer`
- Post-incident recovery and restoration → `d3fend-restore`

## Core Workflows

### 1. Credential Eviction

| Action | When | Considerations |
|---|---|---|
| Account locking | Immediate containment | May disrupt business; have unlock procedure |
| Authentication cache invalidation | Session hijacking confirmed | Force re-auth across all systems |
| Credential revocation | Stolen cert/token | Update CRL, rotate secrets |

**See `references/credential_eviction.md`**

### 2. Object & File Eviction

- File eviction (quarantine, delete, restore from clean backup)
- Email removal (phishing, malware delivery)
- Registry key deletion (persistence removal)
- DNS cache eviction (poisoning response)
- Domain registration takedown (phishing sites)

**See `references/object_eviction.md`**

### 3. Process & System Eviction

- Process suspension (pause for analysis)
- Process termination (kill malicious process)
- Session termination (disconnect attacker)
- Host shutdown/reboot (emergency containment)
- Disk operations (format, erase, partition for sanitization)

**See `references/process_system_eviction.md`**

## When to load references

- **Credential eviction** → `references/credential_eviction.md`
- **Object & file eviction** → `references/object_eviction.md`
- **Process & system eviction** → `references/process_system_eviction.md`
