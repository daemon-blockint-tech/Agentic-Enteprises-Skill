# Environments, gates, and promotion

## Table of contents

1. [Environment model](#environment-model)
2. [Promotion flow](#promotion-flow)
3. [Gate catalog](#gate-catalog)
4. [Approvals and change control](#approvals-and-change-control)
5. [Configuration per environment](#configuration-per-environment)
6. [Preview and ephemeral environments](#preview-and-ephemeral-environments)
7. [Exceptions and break-glass](#exceptions-and-break-glass)
8. [Audit trail](#audit-trail)

## Environment model

Standard tiers (adjust names to org):

| Environment | Purpose | Data | Deploy source |
|---|---|---|---|
| dev | Integration, feature validation | Synthetic / anonymized | Every merge or PR |
| staging | Pre-prod parity, release candidate | Masked prod-like | Promoted digest from CI |
| production | Customer traffic | Real | Approved digest only |

Rules:

- **One account/project per prod** where cloud isolation policy requires
- No direct commits to prod config branches without pipeline
- Secrets scoped per environment in secret manager

## Promotion flow

```
build (once) → artifact v1@sha256:abc…
  → deploy dev (auto)
  → deploy staging (auto or RC tag)
  → gates pass
  → deploy production (approved)
```

**Same digest** crosses all environments. Config differences come from environment variables, Helm values, or parameter files—not rebuilds.

Document promotion in runbook:

1. Verify staging smoke green
2. Confirm change ticket / release notes
3. Approve production environment in CI
4. Monitor canary or post-deploy synthetics
5. Close release; tag repository

## Gate catalog

| Gate type | Blocks | Typical owner |
|---|---|---|
| Required status checks | Merge to default branch | App + CI/CD |
| Code review | Merge | Engineering |
| Security scan (SAST/SCA) | Merge or deploy | DevSecOps |
| Secrets scan | Merge | DevSecOps |
| IaC policy (OPA/conftest) | Deploy | Platform/security |
| Manual approval | Production deploy | EM or release manager |
| Change ticket link | Production deploy | Change management |
| Error budget / freeze | Production deploy | SRE |
| License/compliance scan | Merge (regulated) | Legal/compliance |

Order gates to minimize wasted work: cheap checks before image build when possible.

## Approvals and change control

- Use platform **environment protection** (GitHub Environments, GitLab protected environments, Jenkins input steps)
- Require two approvers for tier-1 services when policy demands
- Approvers must not be sole author of the change for regulated environments
- Link deployment to ticket: Jira/ServiceNow ID in workflow input or commit metadata

**Freeze windows:** pipeline reads calendar or flag file; production job skips or warns during freeze unless break-glass label.

## Configuration per environment

| Concern | Pattern |
|---|---|
| App config | Env-specific values file or sealed secrets |
| Feature flags | Lower env on; prod controlled |
| Scaling | Staging smaller; prod autoscaling |
| External integrations | Sandbox endpoints in non-prod |

Never store prod secrets in staging vault paths accessible to broader groups.

## Preview and ephemeral environments

**PR previews:**

- Deploy from PR head commit; unique URL per PR
- Tear down on PR close or TTL (24–72h)
- No production data; no production credentials
- Label-gated workflows for fork PRs

**Cost control:** limit concurrent previews per repo; shared preview cluster with quotas.

## Exceptions and break-glass

Document when manual promotion is allowed:

1. Pipeline platform outage with documented workaround
2. Critical security patch with abbreviated suite (pre-approved)
3. Rollback to previous digest (preferred over forward fix in incident)

Each exception requires:

- Ticket with approver
- Post-incident pipeline fix task
- Retrospective if customer-impacting

## Audit trail

Retain for compliance and debugging:

| Record | Retention hint |
|---|---|
| Workflow run URL, conclusion | Per SOC/ISO policy |
| Artifact digest deployed | Indefinite in deploy log |
| Approver identity and time | Match change management |
| Test reports (junit, coverage) | 30–90 days typical |
| Security scan reports | Per security policy |

Export to SIEM or evidence bucket when `compliance-engineer` requires continuous control monitoring.
