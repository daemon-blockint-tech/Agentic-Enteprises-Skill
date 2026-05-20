# Cloud evidence collection

## Table of contents

1. [Evidence principles](#evidence-principles)
2. [Source catalog](#source-catalog)
3. [Collection cadence](#collection-cadence)
4. [Population sampling](#population-sampling)

## Evidence principles

- **Primary artifacts** from APIs or immutable log store
- **Timestamp** and collector version in metadata
- **Tamper-evident** storage (WORM bucket, object lock)
- **Redact** customer data in shared audit folders
- Link to **control ID** and framework requirement

Broader non-cloud sources (HRIS, ticketing) → `compliance-engineer` evidence catalog.

## Source catalog

| Evidence need | AWS | GCP | Azure |
|---|---|---|---|
| Org audit trail | CloudTrail org | Admin Activity log | Activity Log |
| Config posture | Config + Security Hub | SCC findings | Defender / Policy |
| IAM inventory | IAM credential report, Access Analyzer | IAM policy analyzer | Entra + RBAC exports |
| Encryption | KMS key policies, S3 bucket encryption | CMEK usage, bucket IAM | Key Vault policies |
| Network | SG rules export, VPC Flow enabled | Firewall rules, VPC Flow | NSG rules, flow logs |
| Backup | Backup vault jobs, RDS snapshots | Backup DR reports | Recovery Services |
| Vuln scan | Inspector / third-party | SCC vuln | Defender vuln |
| Change | CloudTrail API events + CI deploy log | Audit + Cloud Build | Activity + pipeline |

Automate collectors where possible; manual export only with named owner and checksum.

## Collection cadence

| Cadence | Examples |
|---|---|
| Continuous | CSPM findings, public exposure rules |
| Daily | Critical misconfig alerts |
| Weekly | CCM dashboard review |
| Monthly | IAM credential report, encryption compliance |
| Quarterly | Access review attestation, restore test proof |
| Annual | Full population samples for Type II |

Align cutoff dates with **observation period** start/end.

## Population sampling

For Type II populations (e.g., all prod changes):

- Define **population query** (date range, account filter)
- Document **sample size** and selection method (random, risk-based)
- Retain **seed** and script for reproducibility
- Note **exceptions** removed from population with reason

Auditors prefer repeatable selection over ad-hoc picks.
