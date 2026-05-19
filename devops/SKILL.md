---
name: devops
description: |
  Guides DevOps—CI/CD pipelines, GitOps, release management, container delivery, observability,
  and SRE practices for build/deploy systems.
  Use when building or fixing pipelines, implementing GitOps, tuning alerts and SLOs, or managing
  on-call/incidents for delivery infrastructure—not for IDP/golden paths/developer portals
  (platform-engineer), raw VPC/IaC design (infrastructure-engineer), rollout cutover planning
  (deployment-strategist), security gates (devsecops), app features (senior-fullstack-developer),
  multi-team program coordination (technical-program-manager), or incident program design
  (severity, on-call, postmortems, paging integrations—incident-management-engineer). For Kubernetes
  cluster bootstrap, Helm releases, add-ons, and cluster-level debugging, use cluster-deployment-engineer.
---

# DevOps

## When to Use

- Build, fix, or optimize CI/CD pipelines and release automation
- Implement GitOps, artifact promotion, container delivery, or environment automation
- Set up service observability, SLOs, alerting, and runbooks for delivery infrastructure
- Operate on-call workflows for build, deploy, and runtime reliability issues
- Standardize deployment mechanics for application teams

## When NOT to Use

- Design rollout strategy, cutover, rollback triggers, or release risk tiers → `deployment-strategist`
- Build internal developer portals, golden paths, or platform-as-product roadmaps → `platform-engineer`
- Provision core cloud networks, IAM, or Terraform modules as the main task → `infrastructure-engineer`
- Add security gates, SBOMs, artifact signing, or CI threat modeling → `devsecops`
- Design SEV programs, paging policy, or postmortem process → `incident-management-engineer`

## Related skills

| Need | Skill |
|---|---|
| Cloud VPC, IAM, Terraform modules | `infrastructure-engineer` |
| SAST, SBOM, OIDC hardening, pipeline security | `devsecops` |
| Data pipeline SLAs and warehouse ops | `data-system-ops-lead` |
| App code, APIs, UI | `senior-fullstack-developer` |
| Rollout strategy, cutover plans, change tiers | `deployment-strategist` |
| IDP, golden paths, developer portal, platform APIs | `platform-engineer` |
| Cross-team milestones, RAID, launch council | `technical-program-manager` |
| SEV model, on-call program, postmortem process | `incident-management-engineer` |
| K8s cluster deploy and operations | `cluster-deployment-engineer` |

## Core Workflows

### 1. CI/CD pipeline design

**Standard stage order:**

```
checkout → lint/test → build → publish artifact → deploy non-prod → integration/e2e → promote prod
```

**Checklist:**

- [ ] Pipeline as code in repo; versioned with application
- [ ] Reproducible builds (locked deps, pinned base images)
- [ ] Parallelize independent jobs; cache dependencies
- [ ] Artifact immutability (digest, not floating tag)
- [ ] Manual or policy gate before production
- [ ] Rollback path documented and tested quarterly

**See `references/cicd_releases.md` for GitHub Actions, GitLab CI, and deployment patterns.**

### 2. GitOps and environments

1. Declare desired state in git (Helm, Kustomize, Terraform for apps)
2. Sync via Argo CD or Flux; drift detection enabled
3. One branch or path per environment; promotion via PR
4. Secrets never in git—use External Secrets / sealed secrets
5. Audit sync events and failed reconciliations

**See `references/gitops_environments.md` for promotion flows and config layering.**

### 3. Observability and SRE

**Minimum observability per service:**

| Signal | What to capture |
|---|---|
| Metrics | RED/USE: rate, errors, duration, saturation |
| Logs | Structured JSON, correlation ID, no secrets |
| Traces | Critical paths and cross-service calls |

**SLO workflow:** pick SLI → set target and error budget → alert on burn rate → review in weekly ops.

**See `references/observability_sre.md` for SLI examples, alert hygiene, and runbook links.**

### 4. Incident and on-call

1. Triage severity (customer impact, data risk)
2. Mitigate (rollback, scale, feature flag)
3. Communicate status on cadence
4. Post-incident review within 48h for SEV1–2
5. Track action items to closure

**See `references/incident_oncall.md` for severity matrix and handoff template.**

### 5. Developer platform (optional)

- Golden paths: template repos, standard pipelines, local dev parity
- Self-service environments with guardrails
- Cost and quota visibility per team

**See `references/platform_engineering.md` for IDP scope and build-vs-buy.**

## When to load references

- **Pipelines and releases** → `references/cicd_releases.md`
- **GitOps and env promotion** → `references/gitops_environments.md`
- **Metrics, SLOs, alerts** → `references/observability_sre.md`
- **Incidents and on-call** → `references/incident_oncall.md`
- **Internal developer platform** → `references/platform_engineering.md`
