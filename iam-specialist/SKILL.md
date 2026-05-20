---
name: iam-specialist
description: |
  Guides identity and access management—workforce and machine identity lifecycle, RBAC/ABAC/PBAC
  entitlement design, access reviews and recertification, SSO/SAML/OIDC federation, privileged
  access (PAM/JIT), cloud IAM least privilege (AWS/GCP/Azure concepts), service accounts and secrets
  hygiene, and separation of duties. Use for IAM, identity governance, access review, RBAC, least
  privilege, SSO federation, PAM, privileged access, cloud IAM policy, service account, or SoD—not
  full cloud landing zone architecture (enterprise-cloud-architect), broad cloud security controls
  (cloud-security-engineer), day-2 break-glass ticket execution only (cloud-system-administrator),
  pentest (penetration-tester), or legal/HR policy drafting only.
---

# IAM Specialist

## When to Use

- Design **workforce and machine identity lifecycle** — joiner/mover/leaver, contractors, service principals
- Model **RBAC, ABAC, or PBAC** entitlements, roles, and permission sets with least privilege
- Run **access reviews and recertification** — campaigns, risk-based sampling, manager attestation
- Architect **SSO federation** — SAML, OIDC, SCIM provisioning, app onboarding patterns
- Implement **privileged access** — PAM vaulting, JIT elevation, session recording, break-glass policy
- Author **cloud IAM** roles, policies, permission boundaries, trust relationships (AWS/GCP/Azure)
- Govern **service accounts and secrets** — naming, rotation, no human keys, workload identity
- Define **separation of duties** matrices and toxic-combination detection
- Align IAM controls to **audit and risk** narratives (with GRC partners)

## When NOT to Use

- Multi-BU landing zone, CCoE, EA, or executive cloud governance → `enterprise-cloud-architect`
- Org SCPs, CSPM, network segmentation, KMS program, detective controls → `cloud-security-engineer`
- Access ticket fulfillment, key rotation runbooks, patching, restores → `cloud-system-administrator`
- VPC/RDS/serverless build without IAM as primary deliverable → `cloud-engineer`
- SIEM/EDR deployment, WAF, broad security tooling → `information-security-engineer`
- SOC 2 evidence pipelines and automated control checks → `compliance-engineer`
- CI OIDC and pipeline scan gates only → `devsecops`
- Inherent/residual risk scoring and risk register → `security-risk-analyst`
- Authorized exploitation or pentest validation → `penetration-tester`
- Legal interpretation, employment policy, or contract redlines → `commercial-counsel`

## Related skills

| Need | Skill |
|---|---|
| Cloud org guardrails, CSPM, network/KMS security | `cloud-security-engineer` |
| Cloud resource build and workload identity wiring | `cloud-engineer` |
| Day-2 IAM tickets, rotation, break-glass execution | `cloud-system-administrator` |
| Enterprise landing zone and CCoE governance | `enterprise-cloud-architect` |
| SIEM, EDR, encryption, security-as-code guardrails | `information-security-engineer` |
| GRC program, framework scope, audit coordination | `compliance-specialist` |
| Audit evidence automation from IdP and cloud APIs | `compliance-engineer` |
| CI/CD OIDC federation and pipeline least privilege | `devsecops` |
| Risk register, treatment, and executive heat maps | `security-risk-analyst` |
| Cloud framework evidence and residency packages | `cloud-compliance-specialist` |
| Security program strategy | `cybersecurity` |

## Core Workflows

### 1. Scope and governance model

Identity domains, RACI, and boundaries vs cloud security and ops.

**See `references/iam_specialist_scope.md`.**

### 2. Identity lifecycle and access governance

Joiner/mover/leaver, provisioning, reviews, and exceptions.

**See `references/identity_lifecycle_and_governance.md`.**

### 3. Entitlements and authorization models

RBAC/ABAC/PBAC design, role engineering, and SoD.

**See `references/rbac_abac_and_entitlements.md`.**

### 4. Federation and SSO protocols

SAML, OIDC, SCIM, and SaaS onboarding.

**See `references/federation_sso_and_protocols.md`.**

### 5. Privileged access and PAM

JIT, vaulting, break-glass, and session controls.

**See `references/privileged_access_and_pam.md`.**

### 6. Cloud IAM and least privilege

Cross-cloud IAM patterns, policy review, and machine identity.

**See `references/cloud_iam_and_least_privilege.md`.**

## Outputs

- **Entitlement catalog** — roles, permissions, owners, review cadence
- **Access review campaign** — scope, attestations, remediation tracker
- **Federation design** — trust, claims, MFA, provisioning flow
- **PAM policy** — elevation paths, approval, monitoring, break-glass
- **Cloud IAM policy set** — least-privilege JSON with trust boundaries documented
- **SoD matrix** — incompatible duties, compensating controls, exceptions
- **Service account standards** — creation, rotation, audit queries

## Principles

- **Identity is the perimeter** — authenticate strongly; authorize minimally
- **No standing privilege** — prefer JIT and time-bound elevation for admin
- **Prove every grant** — reviews, logs, and SoD checks on sensitive entitlements
- **Humans ≠ machines** — separate lifecycle, credentials, and audit trails
- **Federation fails closed** — misconfigured trust denies access; monitor sync errors
- **Break-glass is rare, logged, and reviewed** — not a daily admin shortcut
