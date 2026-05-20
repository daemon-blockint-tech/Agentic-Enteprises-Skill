# Host and memory artifacts

## Table of contents

1. [Analysis order](#analysis-order)
2. [Memory forensics](#memory-forensics)
3. [Disk and OS artifacts](#disk-and-os-artifacts)
4. [Mobile considerations](#mobile-considerations)
5. [Documentation](#documentation)

## Analysis order

On a preserved host image or triage package:

```
validate image → timeline skeleton (MFT/USN if applicable) → execution artifacts → persistence → user activity → network artifacts → correlate to central logs
```

Document **timezone** assumptions (UTC in reports; note original OS offset).

## Memory forensics

When RAM was captured:

| Target | Why it matters |
|---|---|
| Process list | Malware, LOLBins, injection |
| Network connections | C2, lateral movement |
| Loaded modules / DLLs | Injection, hooking |
| Credentials in memory | Pass-the-hash context (handle per policy) |
| Command lines | Often richer than disk-only |

If memory was **not** collected, state the gap and rely on EDR telemetry and disk artifacts.

## Disk and OS artifacts

### Windows (common)

| Category | Examples |
|---|---|
| Execution | Prefetch, Amcache, Shimcache, UserAssist, BAM/DAM |
| Persistence | Run keys, services, scheduled tasks, WMI subscriptions |
| Logon | Security event log, RDP, VPN |
| File system | MFT, USN Journal, $Recycle.Bin, LNK, Jump Lists |
| Browser | History, downloads, extensions (profile paths) |
| Email / cloud sync | Outlook OST paths, OneDrive sync logs |

### Linux / macOS

| Category | Examples |
|---|---|
| Execution | bash history, auditd, utmp/wtmp, launchd/systemd units |
| Persistence | cron, LaunchAgents/Daemons, profile scripts |
| Logs | auth.log, secure, unified logs (macOS) |

### Cross-platform

- **EDR telemetry** exports (if preserved separately)
- **Antivirus** quarantine and scan logs
- **USB attach** history where available

Map findings to **MITRE ATT&CK** only when behavior is supported by artifacts.

## Mobile considerations

- Confirm **legal authority** for device imaging vs logical export
- Note **encryption**, MDM remote wipe risk, and airplane mode if field collection
- Parse: call/SMS metadata (if in scope), app data, location (if authorized), cloud backups linkage
- **Cloud accounts** on device often require separate SaaS acquisition

## Documentation

For each significant finding record:

- **Artifact path** or log channel
- **Parser/tool** and version
- **UTC timestamp** (original and normalized)
- **Interpretation** vs **raw fact**
- **Confidence** (confirmed / likely / speculative)

Avoid destructive parsing on originals; work on verified copies with logged hashes.
