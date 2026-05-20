# Cloud IAM and least privilege

## Table of contents

1. [Cross-cloud concepts](#cross-cloud-concepts)
2. [AWS IAM](#aws-iam)
3. [GCP IAM](#gcp-iam)
4. [Azure RBAC](#azure-rbac)
5. [Machine identity and secrets](#machine-identity-and-secrets)
6. [Policy review workflow](#policy-review-workflow)

## Cross-cloud concepts

Apply uniformly:

| Principle | Implementation |
|---|---|
| Deny by default | SCP / org policy / management group deny |
| Scope by account/project/subscription | Blast radius containment |
| No long-lived human keys | SSO + role assumption |
| Workload identity | IRSA, GKE WI, managed identity — no static keys in code |
| Permission boundaries | Cap max permissions on assumable roles |
| Tag-based access | ABAC where teams mature |

`cloud-security-engineer` owns **org guardrails and CSPM**; `iam-specialist` owns **role/permission design and reviews**.

## AWS IAM

1. **Human access** — IAM Identity Center (SSO) to permission sets; no console IAM users
2. **Roles** — `sts:AssumeRole` with externalId for third parties; session tags for ABAC
3. **Policies** — prefer managed AWS job functions as baseline; trim with policy simulator
4. **Permission boundaries** — on all custom roles; prevent privilege escalation
5. **Service control policies** — deny root, restrict regions, require MFA for sensitive APIs
6. **Access keys** — ban on humans; rotate service keys; prefer IAM Roles Anywhere / IRSA

Review: `iam:PassRole`, `*:*`, `kms:Grant`, `lambda:UpdateFunctionCode` on broad principals.

## GCP IAM

1. **Hierarchy** — org → folder → project; inherit deny policies carefully
2. **Groups** — Google Groups as principal; avoid user-specific bindings
3. **Custom roles** — minimal permission set; test with Policy Analyzer
4. **Service accounts** — one workload per SA; disable key creation org-wide if possible
5. **Workload Identity Federation** — GitHub/GitLab/CircleCI to GCP without keys
6. **Privileged Access Manager** — JIT for sensitive roles

Review: `roles/owner`, `roles/editor`, `iam.serviceAccountKeys.create`, `setIamPolicy` on folders.

## Azure RBAC

1. **Entra ID** — PIM for privileged roles; conditional access for admins
2. **Management groups** — policy inheritance; deny assignments for guardrails
3. **Custom roles** — actions/notActions explicit; avoid broad `*` on data actions
4. **Managed identities** — system-assigned per workload where possible
5. **Subscription RBAC** — separate prod/non-prod; no standing Owner in prod
6. **Key Vault** — RBAC + purge protection; access via MI not users

Review: User Access Administrator, Role Based Access Control Administrator at root scope.

## Machine identity and secrets

1. **Inventory** — all service accounts, API keys, SP secrets, certificates
2. **Naming** — `svc-<app>-<env>-<purpose>`; owner and expiry in tags
3. **Rotation** — automated where supported; max 90-day manual keys
4. **Secrets stores** — Vault, Secrets Manager, Key Vault — no secrets in repos
5. **CI/CD** — OIDC to cloud (`devsecops` for pipeline wiring)
6. **Cross-cloud** — federated identity over duplicated long-lived keys

## Policy review workflow

For each new role or policy change:

1. Document **intent** — who, what resource, which actions, duration
2. Run **simulator / analyzer** — effective permissions on sample resources
3. Check **SoD matrix** and external exposure (public trust policies)
4. Peer review by security or platform
5. Deploy via IaC; tag with owner and ticket
6. Schedule **recertification** in next access review campaign

Export **effective policy JSON** and approval record for auditors.
