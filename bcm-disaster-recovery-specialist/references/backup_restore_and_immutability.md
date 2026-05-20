# Backup, restore, and immutability

## Table of contents

1. [Backup scope](#backup-scope)
2. [Immutability and isolation](#immutability-and-isolation)
3. [Retention and legal hold](#retention-and-legal-hold)
4. [Restore test program](#restore-test-program)
5. [Restore procedure pattern](#restore-procedure-pattern)
6. [Evidence for audit](#evidence-for-audit)
7. [Common failures](#common-failures)

## Backup scope

Include in **BCM backup inventory** (minimum):

| Category | What to back up | Owner |
|---|---|---|
| Identity | IdP config, federation metadata, conditional access policies | IAM team |
| Keys | KMS policies, HSM config (not raw keys in plaintext exports) | Security eng |
| Detection | SIEM content packs, parser configs, SOAR playbooks | SOC platform |
| Endpoints | EDR policy baselines, exclusion lists (versioned) | Security eng |
| Infrastructure | IaC state, firewall rulesets, DNS zones | Platform |
| SaaS | Vendor export APIs, admin settings snapshots | App owner |
| Evidence | Log archive indices, ticket/case metadata | SOC/GRC |

**Exclude** from standard DR backups: ephemeral caches, non-prod unless tiered.

Align scope with **RPO register**—every tier-0/1 row must map to a backup job or replication stream.

## Immutability and isolation

Implement **defense against ransomware touching backups**:

1. **Object lock / WORM** — minimum retention aligned to longest RPO + investigation window
2. **Separate admin account** — backup admins not in domain users; MFA on backup plane
3. **Network isolation** — backup network unreachable from corp VLAN except required ports
4. **Air-gap or offline copy** — periodic for tier-0 (tape, vault, second cloud account)
5. **Immutable snapshots** — cloud snapshot lock; verify delete API cannot bypass without break-glass
6. **Versioning** — protect against poisoned backup chains; test restore from **older** point

Document **break-glass** procedure to shorten retention (requires two-person approval).

Execution partners: `cloud-system-administrator`, `information-security-engineer`.

## Retention and legal hold

| Driver | Action |
|---|---|
| RPO | Minimum backup frequency |
| Regulatory log retention | Retain archives even if RPO shorter |
| Litigation hold | Suspend deletion; coordinate legal |
| Insurance | Map to policy evidence requirements |

On hold: **freeze** automated lifecycle deletion; tag affected backups in catalog.

## Restore test program

### Cadence

| Tier | Minimum frequency | Scope |
|---|---|---|
| 0 | Semi-annual | Full functional restore to isolated env |
| 1 | Annual | Full or partial per risk |
| 2 | Annual | Sampled systems |
| 3+ | Risk-based | Optional |

### Test types

1. **Tabletop restore** — walkthrough with timestamps (quarterly for tier-0)
2. **Technical restore** — actual data/system recovery
3. **Failover** — DNS/regional flip where applicable
4. **Cyber-specific** — restore from pre-dwell backup sample; malware scan restored image

### Pass criteria

Record for each test:

- **Target RPO achieved** (Y/N; actual data timestamp)
- **Target RTO achieved** (Y/N; RTA minutes)
- **Integrity checks** — auth, ingest, agent check-in, sample queries
- **Issues** — ticket IDs, owners, due dates

Failed test = **risk acceptance** or remediation by due date—escalate tier-0 failures to leadership.

## Restore procedure pattern

Standard runbook sections (delegate execution to ops):

1. **Authorize** — change ticket, incident link, approvers
2. **Isolate target** — recovery VLAN, no production routes until validated
3. **Select recovery point** — document timestamp and reason
4. **Restore** — per vendor steps; verify checksums where available
5. **Validate** — functional tests from service owner checklist
6. **Scan** — AV/EDR on restored systems before join production
7. **Cutover** — maintenance window, rollback plan documented
8. **Report** — RPO/RTO achieved, logs attached

For **SaaS**: document export/import limits; test vendor restore support annually.

## Evidence for audit

Maintain **6–12 months** of:

- Restore test reports with pass/fail and approver
- Backup job success dashboards (tier-0/1)
- Immutability configuration screenshots or IaC references
- Risk acceptances for known gaps

Route control mapping to `compliance-engineer` or `compliance-specialist`—this skill supplies **operational proof**, not control matrices.

## Common failures

| Failure | Mitigation |
|---|---|
| Backups succeed but restore untested | Mandate semi-annual tier-0 tests |
| Same admin for domain and backups | Separate backup admin plane |
| Replication includes malware | Known-good points; isolated restore scan |
| SaaS "backup" is recycle bin only | Contractual export; secondary copy |
| Log backup deleted for cost | BIA tier-1 minimum retention |
| DR docs on encrypted file share | Out-of-band copies |

After real incident, compare **actual RPO** to test results; update test scope if gap > 1 tier.
