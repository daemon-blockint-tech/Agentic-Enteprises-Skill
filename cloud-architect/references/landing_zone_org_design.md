# Landing zone and organization design

## Table of contents

1. [Organization structure](#organization-structure)
2. [Guardrails](#guardrails)
3. [Shared services](#shared-services)
4. [Identity baseline](#identity-baseline)

## Organization structure

Typical AWS/GCP/Azure patterns:

```
Organization / Management group
├── Security OU (log archive, audit, tooling)
├── Infrastructure OU (network hub, DNS)
├── Workloads OU
│   ├── Prod accounts / subscriptions
│   ├── Non-prod accounts
│   └── Sandbox (SCP-limited)
└── Suspended / quarantine
```

Decisions to document in ADR:

- **Account per env** vs **account per product**
- **Region allowlist**
- **Centralized vs distributed networking**

Implementation detail → `cloud-engineer`; module libraries → `infrastructure-engineer`.

## Guardrails

| Control | Example |
|---|---|
| SCP / org policy | Deny root API keys, restrict regions |
| Tag policy | Mandatory cost and owner tags |
| Encryption default | KMS/CMEK required |
| Public access | Block at org level |

**Exception process** — time-bound, approved, logged.

## Shared services

Centralize where economies of scale apply:

- **Logging** — CloudTrail, Activity Log, centralized SIEM feed
- **DNS** — public and private zones
- **Connectivity** — transit hub, VPN, Direct Connect
- **Secrets** — org-wide key management patterns
- **CI/CD roles** — OIDC federation from `devops` design

## Identity baseline

- Human access via **SSO** only; no IAM users in workload accounts
- **Break-glass** accounts monitored
- **Workload identity** standard per compute type
- Cross-account roles with **external ID** for vendors

Security architecture sign-off → `information-security-engineer`.
