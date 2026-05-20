# Backup, restore, and immutability

## Table of contents

1. [Design goals](#design-goals)
2. [Backup topology](#backup-topology)
3. [Immutability patterns](#immutability-patterns)
4. [Encryption and keys](#encryption-and-keys)
5. [Restore validation](#restore-validation)
6. [SaaS and cloud-native](#saas-and-cloud-native)
7. [Anti-patterns](#anti-patterns)

## Design goals

- **Recoverability** under ransomware, insider, and operator error
- **Integrity** — detect tampering before restore
- **Isolation** — backup plane not reachable from compromised production credentials
- **Provable RPO** — measurable lag, not assumed schedule success
- **Evidence** — audit-ready test and restore logs

## Backup topology

| Layer | Purpose | Typical controls |
|---|---|---|
| **Primary** | Production data | Encryption, access logging |
| **Replica** | Low RPO | Separate account/subscription; no prod admin path |
| **Backup vault** | Point-in-time recovery | Immutable retention, MFA delete |
| **Air-gap / offline** | Last resort | Tape, offline copy, break-glass account |
| **Gold images** | Rebuild | Signed, scanned, versioned IaC and AMIs |

**3-2-1-1-0 variant for cyber:** 3 copies, 2 media types, 1 offsite/immutable, **1 offline or logically air-gapped**, **0** unverified restores.

Document **backup admin** as separate identity from production admin; no standing shared roles.

## Immutability patterns

| Pattern | Platform examples | Notes |
|---|---|---|
| **Object lock / WORM** | S3 Object Lock, Azure immutable blob | Compliance mode vs governance mode |
| **Backup vault immutability** | AWS Backup Vault Lock, Azure Backup | Min retention; legal hold |
| **Snapshot policies** | GCE snapshot schedules + org policies | Prevent delete without break-glass |
| **Tape / offline** | Physical or cloud egress copy | Long RTA; ransomware safe |
| **Append-only log archive** | WORM bucket for SIEM cold | Investigation history |

**Retention:** align legal hold and regulatory minimums with BCM (`bcm-disaster-recovery-specialist`); engineering sets **technical** retention and lock duration.

## Encryption and keys

- Encrypt backups with **CMK** or HSM-backed keys; separate key admin from backup admin
- Document **key recovery** procedure—KMS loss is tier-0 event
- Rotate keys on schedule; test restore **after** rotation
- For ransomware: assume prod keys compromised—vault keys and offline copies use **different trust path**

## Restore validation

Every tier-1+ system needs a **restore test profile**:

| Check | Pass criteria |
|---|---|
| **Completeness** | Expected objects/databases present |
| **Integrity** | Checksums, DB consistency, app smoke test |
| **RPO achieved** | Data timestamp within documented RPO |
| **RTA** | Wall-clock restore within RTO or documented gap |
| **Security** | Restored env isolated; no prod routing until cleared |
| **Secrets** | Rotated if backup may be tainted |

**Types of tests:**

- **Tabletop** — walkthrough only
- **Technical restore** — isolated environment, no prod cutover
- **Failover** — production switch with rollback plan
- **Full game day** — multi-team, comms, metrics

Failed tests → **remediation ticket** with priority from tier.

## SaaS and cloud-native

Maintain a **SaaS recovery register**:

| Field | Why |
|---|---|
| Vendor RTO/RPO claims | Contract vs reality |
| Export/backup API | Automation feasibility |
| Admin break-glass | Out-of-band if IdP down |
| Data residency | Restore region options |
| Immutable export | For SIEM, IdP, ticketing |

For `cloud-engineer` patterns: multi-region, cross-account backups, private endpoints for backup APIs, deny delete via org policy.

**Control-plane loss:** pre-stage runbooks for DNS, identity, and console access via alternate account and out-of-band credentials.

## Anti-patterns

- Single admin role over prod **and** backups
- Immutable backup with **same** SSO session as production
- Restore test only at **file** level, never app consistency
- Relying on vendor "backup included" without **restore** proof
- Keeping backups on **same domain** as ransomware entry
- Skipping restore after **major version** upgrade of backup software

Pair operational execution with `cloud-system-administrator`; you own **design and test criteria**.
