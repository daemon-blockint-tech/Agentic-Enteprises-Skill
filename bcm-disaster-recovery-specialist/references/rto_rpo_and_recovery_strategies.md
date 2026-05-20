# RTO, RPO, and recovery strategies

## Table of contents

1. [Definitions](#definitions)
2. [Setting RTO and RPO](#setting-rto-and-rpo)
3. [Security service targets](#security-service-targets)
4. [Recovery strategies](#recovery-strategies)
5. [Activation criteria](#activation-criteria)
6. [Recovery sequencing](#recovery-sequencing)
7. [Metrics and reporting](#metrics-and-reporting)

## Definitions

| Term | Meaning |
|---|---|
| **RTO** | Maximum acceptable time to restore **service function** (not necessarily full performance) |
| **RPO** | Maximum acceptable **data loss** measured in time (last recoverable point) |
| **MTPD** | Maximum tolerable period of disruption before unacceptable impact |
| **RTA** | Actual recovery time achieved in test or incident |

RTO/RPO must be **approved** by service owner and risk/compliance where regulatory logging or identity is involved.

## Setting RTO and RPO

1. Start from **BIA tier** and MTPD
2. Subtract time for **assessment, decision, and team mobilization** (often 30–120 min for major events)
3. Set RTO ≤ remaining MTPD budget for restoration work
4. Set RPO from **backup frequency**, replication lag, and **legal log retention** minimums
5. Validate with **restore test** or tabletop—adjust if RTA consistently exceeds RTO

Document **exceptions** (e.g., "RPO 24h accepted for dev SIEM with risk ID").

## Security service targets

Use as **starting points**; calibrate to your BIA:

| Service | Suggested tier | RTO (indicative) | RPO (indicative) | Notes |
|---|---|---|---|---|
| Production IdP / SSO | 0 | 1–4 h | 0–15 min | Break-glass separate from RTO |
| MFA / PAM | 0–1 | 4 h | 0–1 h | Emergency access procedure |
| KMS / HSM | 0–1 | 4–8 h | 0 | Key ceremony may extend RTA |
| SIEM (hot) | 1 | 4–8 h | 15 min–1 h | Ingest gap = detection blind spot |
| Log archive (cold) | 2 | 24 h | 1–24 h | Investigation history |
| EDR console | 1 | 4 h | 1 h | Agents may buffer locally |
| SOAR | 2 | 24 h | 4 h | Manual playbooks interim |
| Secrets manager | 0–1 | 4 h | 0–15 min | Rotation dependencies |
| PKI / internal CA | 1 | 8–24 h | 1 h | Cert expiry cascade risk |

## Recovery strategies

| Strategy | When to use | Pros | Cons |
|---|---|---|---|
| **Active/active** | Tier-0 with budget | Lowest RTO | Cost, split-brain risk |
| **Warm standby** | Tier-0/1 SaaS or regional pair | Balanced | Drift, licensing |
| **Pilot light** | Tier-1/2 | Cheaper than warm | Longer RTA |
| **Backup restore** | Most security SaaS | Simple | RPO bound to backup |
| **Rebuild from gold** | Post-ransomware, untrusted estate | Trust | Longest RTO |
| **Manual workaround** | Short gaps | Fast to start | Weak security, not scalable |

**Cyber bias:** after confirmed compromise, default to **rebuild from known-good** rather than restore-in-place unless forensic and IR (`incident-responder`) approve.

## Activation criteria

Declare **DR mode** when any trigger is met (customize in BCP):

- Tier-0 service outage exceeding **50% of RTO** with no ETA
- **Ransomware or wiper** affecting production or backups
- **Identity platform** compromise or total loss of MFA
- **Regional/cloud** loss affecting multiple security controls
- **Regulatory** direction to preserve systems (coordinate legal)

Activation authority: BCM lead + IR commander + designated executive (document in BCP).

## Recovery sequencing

Default **security-first** order for cyber events:

1. **Stabilize command** — incident bridge, roles, comms cadence (`incident-responder`)
2. **Network isolation** — stop spread; preserve evidence paths
3. **Identity** — break-glass, disable compromised paths, restore IdP
4. **Secrets and keys** — rotate after identity trust re-established
5. **Logging and detection** — SIEM/EDR before broad app restore (avoid blind recovery)
6. **Critical apps** — per business BIA, not security skill alone
7. **Validate** — hunt for persistence; compare to pre-incident baseline
8. **Stand down DR** — document RTA vs RTO; update register

Parallel tracks: **comms** (`communication-lead`), **legal/regulatory prep** (compliance/legal).

## Metrics and reporting

Track quarterly:

| Metric | Definition |
|---|---|
| RTA vs RTO | Per service, test or incident |
| RPO achievement | Data timestamp restored vs objective |
| Test coverage | % tier-0/1 with restore test in last 6 months |
| Tabletop closure | % actions closed within SLA |
| Backup immutability | % critical backups with WORM/object lock |

Report trends to leadership and feed `cybersecurity` / `compliance-specialist` program reviews.
