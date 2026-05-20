# Timeline and evidence handling

## Table of contents

1. [Timeline principles](#timeline-principles)
2. [Timeline table format](#timeline-table-format)
3. [Evidence sources](#evidence-sources)
4. [Collection and preservation](#collection-and-preservation)
5. [Chain of custody](#chain-of-custody)
6. [Common pitfalls](#common-pitfalls)

## Timeline principles

- Use **UTC** for all timestamps; note analyst local TZ only in metadata if needed
- Separate **attacker**, **defender**, and **business** lanes in the narrative
- Label each entry **fact** (sourced) vs **hypothesis** (pending validation)
- Version the timeline when scope changes; never silent edits
- Tie entries to **evidence IDs** (log query, screenshot hash, ticket)

## Timeline table format

| UTC time | Lane | Event | Source / evidence ID | Confidence |
|---|---|---|---|---|
| 2026-05-20 14:02 | Attacker | Successful login from anomalous ASN | IdP log export E-014 | Fact |
| 2026-05-20 14:18 | Defender | Account disabled by SOC | Ticket INC-4421 | Fact |
| 2026-05-20 14:30 | Business | Customer report received | Support ticket S-99102 | Fact |

Add columns as needed: **affected entity**, **IOC**, **action owner**.

## Evidence sources

Prioritize by fidelity and retention:

| Source | Typical use |
|---|---|
| IdP / SSO sign-in and admin logs | Account compromise, MFA bypass |
| EDR / XDR | Process, persistence, lateral movement |
| Cloud audit (CloudTrail, Activity Log, Audit Logs) | API abuse, IAM changes, data access |
| Application audit logs | Tenant admin actions, API keys |
| Email security gateway | Phishing delivery, rule forwarding |
| Proxy / WAF / CDN | Exfil, C2, exploit attempts |
| SIEM correlated alerts | Starting points—not sole evidence |
| Backup and VM snapshots | Malware forensics (immutable copy) |
| Ticketing and chat exports | Decision record |

Coordinate with `cloud-security-engineer` for cloud-native exports; `information-security-engineer` for tooling access.

## Collection and preservation

1. **Identify** sources before containment destroys artifacts (volatile memory, live sessions)
2. **Snapshot** where appropriate: disk image, VM snapshot, memory dump—per legal guidance
3. **Export** logs with original timestamps; record query window and export job ID
4. **Hash** files (SHA-256); store in write-once or access-controlled bucket
5. **Document** who collected, when, from which system, and storage path
6. **Avoid** modifying original systems; work from copies
7. **Legal hold**: engage legal before broad deletion or retention changes

## Chain of custody

Maintain a log for each artifact:

| Field | Value |
|---|---|
| Evidence ID | E-### |
| Description | e.g., EDR export host-abc 2026-05-20 |
| Collected by | Name / role |
| Collected at (UTC) | |
| Source system | |
| Hash | SHA-256 |
| Storage location | |
| Access log | Who accessed, when, purpose |

Transfer only through approved secure channels; no personal cloud drives.

## Common pitfalls

- Rebuilding or reimaging hosts before imaging when forensics may be needed
- Letting log retention expire during long investigations—extend retention early
- Conflating detection time with attacker start time—state both explicitly
- Publishing unverified IOCs externally before legal/comms review
