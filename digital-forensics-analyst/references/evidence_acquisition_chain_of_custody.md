# Evidence acquisition and chain of custody

## Table of contents

1. [Acquisition order](#acquisition-order)
2. [Collection methods](#collection-methods)
3. [Chain of custody](#chain-of-custody)
4. [Evidence worksheet fields](#evidence-worksheet-fields)

## Acquisition order

Prioritize **volatile** evidence before shutdown or remediation when safe and authorized:

```
memory → network state → running processes → disk/logical → cloud exports → backups
```

| Priority | Source | Notes |
|---|---|---|
| 1 | RAM / hibernation | Lost on power-off |
| 2 | Network connections, ARP, DNS cache | Time-sensitive |
| 3 | Live process list, logged-on users | Correlate with EDR |
| 4 | Disk image or targeted collection | Use write blocker for physical |
| 5 | Centralized logs (SIEM, IdP, cloud audit) | Export before retention expiry |
| 6 | Backups / snapshots | Verify point-in-time and integrity |

If IR already isolated a host, document **pre-acquisition state** (what changed, when).

## Collection methods

| Artifact | Preferred approach | Integrity |
|---|---|---|
| Workstation/server disk | Forensic image (E01/RAW) or vendor triage | Hash at acquisition |
| Mobile | Logical or full file system per policy and device | Screen lock / legal constraints |
| Cloud VM | Hypervisor snapshot + memory if offered | Record API request IDs |
| SaaS | Native export APIs, audit logs, legal hold | Retention and completeness notes |
| Email | eDiscovery export per counsel | Preserve metadata |
| Logs | Raw export with timezone metadata | Hash export files |

Record **tool name, version, operator, start/end UTC** for every collection.

## Chain of custody

Maintain a **continuous record** from collection through analysis and storage:

1. **Unique evidence ID** (never reuse)
2. **Description** (host, user, serial, cloud resource ID)
3. **Acquisition** — date/time UTC, location, method, collector
4. **Hash** — algorithm (SHA-256 minimum) of acquired object
5. **Storage** — encrypted location, access controls
6. **Transfers** — each handoff: from, to, date/time, purpose, signature or ticket ID
7. **Analysis access** — who mounted or parsed, read-only copies preferred
8. **Disposition** — retention schedule per legal hold

Rules:

- **Sealed media** — tamper-evident bags or encrypted containers where required
- **Working copies** — analyze copies; preserve original sealed set
- **No undocumented access** — every open/export logged

## Evidence worksheet fields

Per item, capture at minimum:

| Field | Example |
|---|---|
| Evidence ID | EV-2026-0142-001 |
| Case / ticket | IR-4521 |
| Description | Laptop ABC123 disk image |
| Custodian | Jane Analyst |
| Acquired UTC | 2026-05-20T14:32:00Z |
| Method | FTK Imager, write-blocked USB |
| Source location | Building 2, desk 4B |
| Hash (SHA-256) | `a1b2…` |
| Storage path | `vault/cases/IR-4521/EV-…` |
| Legal hold | Yes — ref LH-88 |
| Notes | Host powered on; memory not collected (policy) |

Attach worksheets to the master evidence log; cross-reference in the forensic report.
