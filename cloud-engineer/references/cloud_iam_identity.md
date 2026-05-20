# Cloud IAM and identity

## Table of contents

1. [Role design](#role-design)
2. [Federation](#federation)
3. [Workload identity](#workload-identity)
4. [Secrets](#secrets)

## Role design

- **One role per workload** (service, job, function)—not shared admin roles
- **Least privilege** — start deny-all, add actions with resource ARNs
- Use **conditions**: `aws:SourceAccount`, `aws:PrincipalArn`, IP allowlist where appropriate
- **No long-lived access keys** for compute; prefer instance/profile or workload identity
- Audit **IAM Access Analyzer** / policy simulator before prod

Cross-account:

- **AssumeRole** with external ID for third parties
- Resource policies on buckets/keys where needed

## Federation

- Human access via **SSO** (IAM Identity Center, Google Workspace, Entra ID)
- Break-glass accounts MFA + logging to SIEM — `information-security-engineer`
- CI/CD **OIDC** to cloud — implement with `devsecops` / `devops`

## Workload identity

| Platform | Pattern |
|---|---|
| AWS | IAM role for service account (EKS), instance profile (EC2) |
| GCP | Service account + workload identity binding |
| Azure | Managed identity on VM, AKS, Functions |

Map identity to **minimum** API permissions per service.

## Secrets

- Secrets Manager / Secret Manager / Key Vault
- **Rotation** automated where supported
- Never commit secrets; scan repos — `devsecops`

KMS keys: separate keys per env; key policy least privilege.
