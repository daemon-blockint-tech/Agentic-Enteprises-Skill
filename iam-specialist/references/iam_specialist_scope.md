# IAM specialist scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Identity domains](#identity-domains)
3. [RACI](#raci)
4. [Deliverables](#deliverables)

## Role boundary

| iam-specialist | Partner skill |
|---|---|
| Entitlement design, access reviews, federation, PAM, cloud IAM policy | `information-security-engineer` — deploy SIEM/EDR/KMS/WAF and security-as-code |
| Org SCPs, CSPM, network segmentation, encryption program | `cloud-security-engineer` |
| Access ticket execution, key rotation, patching, restores | `cloud-system-administrator` |
| VPC, databases, serverless without IAM-first scope | `cloud-engineer` |
| Multi-BU landing zone, CCoE, EA governance | `enterprise-cloud-architect` |
| SOC 2 evidence automation, CCM pipelines | `compliance-engineer` |
| GRC program, audit prep, questionnaires | `compliance-specialist` |
| CI OIDC and pipeline scan gates | `devsecops` |
| Risk register and residual scoring | `security-risk-analyst` |
| Pentest and exploit validation | `penetration-tester` |

**Do not** draft employment law, HR disciplinary policy, or provide legal attestations.

## Identity domains

Cover explicitly in scope memos:

| Domain | Examples | Typical owner |
|---|---|---|
| Workforce | Employees, contractors | HR + IT + IAM |
| Customer | B2C/B2B user directories | Product + IAM |
| Partner | B2B federation, guest users | Business + IAM |
| Machine | Service accounts, workloads, bots | Engineering + IAM |
| Privileged | Break-glass, root, domain admin | Security + IAM |
| Cloud | Cloud roles, workload identity | Cloud platform + IAM |

Document **authoritative source of truth** per domain (IdP, HRIS, cloud directory).

## RACI

| Activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| Entitlement model | CISO / IAM lead | iam-specialist | App owners, GRC | Engineering |
| Access reviews | IAM lead | iam-specialist + managers | `compliance-specialist` | Auditors |
| SSO onboarding | IAM lead | iam-specialist | App teams | Support |
| PAM policy | Security | iam-specialist | Ops, Audit | All admins |
| Cloud IAM standards | Cloud platform | iam-specialist | `cloud-security-engineer` | FinOps |
| Break-glass events | Security | `cloud-system-administrator` | iam-specialist | Leadership |

## Deliverables

Minimum artifacts for a mature IAM program:

1. Identity governance charter (approved)
2. Entitlement catalog with owners and review cadence
3. Access review playbook and campaign templates
4. Federation standards (SAML/OIDC/SCIM)
5. PAM and break-glass policy
6. Cloud IAM baseline and exception register
7. SoD matrix for high-risk functions
8. Service account and secrets hygiene standard
