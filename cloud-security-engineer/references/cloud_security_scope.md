# Cloud security scope

## Table of contents

1. [Shared responsibility](#shared-responsibility)
2. [Role boundary](#role-boundary)
3. [Multi-account model](#multi-account-model)
4. [Compliance hooks](#compliance-hooks)

## Shared responsibility

| Layer | Customer typically owns | Provider owns |
|---|---|---|
| Data classification | Yes | — |
| IAM and access | Yes | — |
| Network config in VPC | Yes | Physical network |
| OS and app on IaaS | Yes | Hypervisor |
| Managed service config | Yes | Service software |
| Physical DC | — | Yes |

Document which controls apply per workload (IaaS vs PaaS vs SaaS).

## Role boundary

| cloud-security-engineer | Partner skill |
|---|---|
| SCPs, org policies, Config rules | `cloud-architect` designs landing zone shape |
| Cloud IAM hardening | `cloud-system-administrator` executes access tickets |
| CSPM remediation | `cloud-engineer` implements non-security infra |
| Pipeline OIDC, image scan gates | `devsecops` |
| Corp IdP, EDR, email security | `information-security-engineer` |
| Audit binder and control mapping | `compliance-engineer` |

## Multi-account model

Typical secure structure:

```
org root (SCPs)
 ├── security / audit (log archive, Security Hub admin)
 ├── shared services (DNS, egress, CI artifacts)
 ├── workload prod / non-prod (separate accounts)
 └── sandbox (strict SCP, auto-cleanup)
```

Principles:

- **No workloads in management account**
- **Centralized logging** — immutable log archive account
- **Separate security tooling account** for delegated admin
- **SCPs deny** dangerous APIs (disable root keys, restrict regions)

## Compliance hooks

Implement technical controls; partner with `compliance-engineer` for:

- Control ID mapping (SOC 2, ISO 27001, CIS)
- Evidence retention periods
- Exception register with expiry

Use CIS Benchmarks and provider **Well-Architected Security** pillar as baselines—not as sole authority without business context.
