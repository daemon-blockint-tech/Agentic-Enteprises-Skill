# Data protection and KMS

## Table of contents

1. [Encryption at rest](#encryption-at-rest)
2. [Encryption in transit](#encryption-in-transit)
3. [Key management](#key-management)
4. [Secrets](#secrets)

## Encryption at rest

Defaults to enforce:

- **Block storage** — encrypted volumes/disks; no unencrypted snapshots shared
- **Object storage** — SSE-KMS or CMEK; block public ACLs/buckets at org level
- **Databases** — TDE or managed encryption; no public endpoints
- **Backups** — encrypted; cross-account copy with key policy

SCP/org policy: deny `s3:PutObject` without encryption headers where applicable.

## Encryption in transit

- TLS **1.2+** on all customer and internal APIs
- Managed certs (ACM, etc.) with auto-renewal
- **mTLS** for high-risk service mesh where required
- Disable legacy protocols on load balancers

## Key management

| Control | Practice |
|---|---|
| CMK ownership | Security or dedicated keys account |
| Key policy | Least privilege; separate encrypt vs admin |
| Rotation | Annual or on compromise; document process |
| Separation of duties | Key admins ≠ data admins |
| Audit | CloudTrail KMS events to SIEM |

Avoid hardcoded keys in AMIs, user-data, or templates — scan in CI (`devsecops`).

## Secrets

- **Secrets Manager / Parameter Store / Key Vault** — not plain env in task defs
- Rotation lambdas or native rotation enabled
- RBAC on secret read; audit `GetSecretValue`
- No secrets in CloudFormation/Terraform state unencrypted — use references + backend encryption

App-layer secret design for multi-tenant products → `product-infrastructure-security-engineer`.
