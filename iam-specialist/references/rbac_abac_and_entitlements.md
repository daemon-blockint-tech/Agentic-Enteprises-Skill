# RBAC, ABAC, and entitlements

## Table of contents

1. [Model selection](#model-selection)
2. [Role engineering](#role-engineering)
3. [Separation of duties](#separation-of-duties)
4. [Entitlement catalog](#entitlement-catalog)

## Model selection

| Model | Use when | Avoid when |
|---|---|---|
| RBAC | Stable job functions; SaaS with built-in roles | Fine-grained resource rules explode role count |
| ABAC | Dynamic attributes (dept, clearance, resource tags) | Mature attribute pipeline missing |
| PBAC | Policy-as-code (OPA, Cedar, cloud ABAC) | No CI for policy tests |
| Hybrid | RBAC bundles + ABAC constraints on sensitive data | Undocumented precedence rules |

Default: **RBAC for humans**, **scoped roles for machines**, **ABAC/PBAC** only where audit requires attribute-level proof.

## Role engineering

1. **Inventory** — list permissions per app/cloud; group by function not by person
2. **Define roles** — verb-noun names (`billing-read`, `deploy-prod`); one purpose per role
3. **Least privilege** — start deny-all; add minimum actions; avoid `*` wildcards
4. **Role mining** — analyze access logs; merge roles with > 95% overlap; split toxic combos
5. **Birthright vs requestable** — document which roles auto-assign from job code
6. **Version and deprecate** — sunset roles with migration window and comms

**Anti-patterns:**

- “Super user” or “admin clone” roles for convenience
- Nested groups without visibility (group-in-group sprawl)
- Direct user permissions outside role model

## Separation of duties

Build a **SoD matrix** for financial, IAM, and production paths:

| Function A | Function B | Risk | Control |
|---|---|---|---|
| Create vendor | Approve payment | Fraud | Different approvers |
| Grant admin | Approve access review | Self-approve | Manager + IAM |
| Write IaC | Apply to prod | Backdoor | CI approval + separate deploy role |
| Issue cert | Operate TLS endpoint | MITM | Split PKI roles |

1. List **incompatible permission pairs** per system
2. Detect in IdP/group assignments and cloud policy attachments
3. Block at request time where possible; else monitor + remediate
4. Document **compensating controls** for approved conflicts (monitoring, dual control)

## Entitlement catalog

Maintain one row per entitlement:

| Field | Purpose |
|---|---|
| ID / name | Stable reference for reviews |
| System | App, cloud account, directory |
| Permissions | API actions, scopes, groups |
| Risk tier | Drives review frequency |
| Owner | Business + technical |
| SoD tags | Linked matrix rules |
| Provisioning method | SCIM, group, manual |
| Review cadence | Quarterly / annual |

Publish catalog to request portal and auditors; sync changes via change management.
