# Backup and restore operations

## Table of contents

1. [Backup verification](#backup-verification)
2. [Restore procedures](#restore-procedures)
3. [Restore drills](#restore-drills)
4. [Ransomware considerations](#ransomware-considerations)

## Backup verification

Daily/weekly checks:

- Backup jobs **success rate** (RDS, VM snapshots, vault)
- **Retention** meets policy; no silent policy drift
- Cross-region copy status if required
- **Encryption** on snapshots and vaults

Alert on failed backup jobs as **high priority**.

## Restore procedures

Before restore in prod:

1. **Incident ticket** with approver
2. Identify **target time** (PITR timestamp or snapshot ID)
3. **Isolate** — restore to new instance/volume first when possible
4. **Validate** — app team confirms data integrity
5. **Cutover** — DNS/connection string change per runbook
6. **Retain** old resource until stable; then decommission

Document **RPO** achieved vs target.

## Restore drills

Quarterly (per tier):

- Restore random snapshot to isolated environment
- Time the procedure; update runbook gaps
- Report to leadership + `compliance-engineer` if audit requires

## Ransomware considerations

- **Immutable** backups where policy requires
- Do not restore prod without security clearance if encryption event suspected
- Preserve logs and snapshots for investigation — security leads
