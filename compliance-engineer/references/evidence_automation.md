# Evidence automation

## Table of contents

1. [Source catalog](#source-catalog)
2. [Collection cadence](#collection-cadence)
3. [Storage](#storage)

## Source catalog

| Source | Typical evidence |
|---|---|
| IdP (Okta, Entra) | MFA status, group membership |
| Git | Branch protection, PR approvals |
| CI/CD | Build logs, signed artifacts |
| Cloud APIs | IAM, encryption, network config |
| Ticketing | Access review tickets, incidents |
| HRIS | Terminations within SLA |

Automate pull via scheduled job; manual attestation only where API insufficient.

## Collection cadence

| Frequency | Examples |
|---|---|
| Continuous | Drift detection, MFA enforcement |
| Weekly | Vuln scan summary |
| Monthly | Access review completion |
| Per change | Emergency access tickets |
| Annual | Policy approval, BCP test |

## Storage

- Dedicated audit bucket with versioning and restricted IAM
- Folder per control ID and period
- Manifest file: hash, collector version, timestamp
