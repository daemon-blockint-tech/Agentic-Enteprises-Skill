---
name: ci-cd-engineer
description: |
  Guides CI/CD engineering—pipeline design, build/test/deploy stages, branch and environment strategy,
  artifact promotion, workflow-level deploy patterns (rolling, blue-green, canary), CI secrets, security
  gates, flaky tests, monorepo/polyrepo layout, DORA metrics, and rollback/release coordination with
  platform/SRE.
  Use when designing or fixing delivery pipelines, GitHub Actions, GitLab CI, Jenkins, release automation,
  deployment gates, or delivery metrics—not app implementation (senior-software-engineer), K8s cluster
  internals only (cloud-engineer), SRE on-call/SLO programs (site-reliability-engineer), security policy
  only (information-security-engineer), or IDP/golden paths (platform-engineer).
  Triggers: CI/CD, continuous integration, continuous delivery, pipeline design, GitHub Actions,
  deployment pipeline, build and deploy, release pipeline, DORA metrics, canary deployment, pipeline gates.
---

# CI/CD Engineer

## When to Use

- Design, implement, or refactor CI/CD pipelines (build, test, publish, deploy)
- Define branch strategy, environment promotion, and artifact immutability
- Add or tune pipeline gates: tests, approvals, security scans, policy checks
- Configure deployment workflows (rolling, blue-green, canary) at the automation layer
- Manage secrets, OIDC, and least-privilege credentials in CI systems
- Handle flaky tests, parallelization, caching, and monorepo/polyrepo pipeline layout
- Frame DORA metrics and delivery dashboards; coordinate releases with SRE/platform
- Document rollback paths and release runbooks tied to pipeline artifacts

## When NOT to Use

- Implement application features, APIs, or business logic → `senior-software-engineer`
- Operate Kubernetes control plane, node pools, or cluster add-ons only → `cloud-engineer`, `cluster-deployment-engineer`
- Own SLI/SLO programs, error budgets, and on-call reliability → `site-reliability-engineer`
- Author enterprise security policy, IdP, KMS, or SIEM programs → `information-security-engineer`
- Add SAST/SBOM/supply-chain controls as the primary task → `devsecops`
- Build internal developer portals, golden paths, or paved-road templates → `platform-engineer`
- Pre-flight architecture or go/no-go review without pipeline work → `build-validator`
- Broad GitOps, observability stack, and delivery-infra SRE as the main scope → `devops`

## Related skills

| Need | Skill |
|---|---|
| Broader delivery, GitOps, observability, on-call for infra | `devops` |
| IDP, golden paths, developer portal, platform APIs | `platform-engineer` |
| Pre-merge plan/design/production-readiness gates | `build-validator` |
| SLOs, error budgets, PRR, reliability ownership | `site-reliability-engineer` |
| Pipeline security gates, SBOM, OIDC hardening | `devsecops` |
| Security controls, IAM, KMS, SIEM implementation | `information-security-engineer` |
| Rollout cutover strategy and change tiers | `deployment-strategist` |
| Cloud networking, core IaC modules | `infrastructure-engineer` |
| Managed cloud services and networking | `cloud-engineer` |
| K8s cluster deploy and platform Helm | `cluster-deployment-engineer` |
| Compliance evidence from controls and audits | `compliance-engineer` |

## Core Workflows

### 1. Pipeline discovery and baseline

1. Inventory repos, pipeline entry points, and deploy targets per environment
2. Map current stage order: checkout → build → test → publish → deploy
3. Identify manual steps, floating tags, and missing gates
4. Capture DORA baselines (deployment frequency, lead time, change fail %, MTTR)
5. Document owners: app team, platform, security, SRE

**See `references/cicd_engineer_scope.md` for role boundaries and handoffs.**

### 2. Pipeline design

1. Choose branching model aligned to release cadence (trunk, GitFlow, release branches)
2. Standardize reusable workflows/templates; pin tool and runner versions
3. Parallelize independent jobs; cache dependencies with lockfile keys
4. Emit immutable artifacts (digest-pinned images, versioned packages)
5. Fail fast on lint/unit; defer expensive suites with policy

**See `references/pipeline_design_and_workflow.md` for patterns and anti-patterns.**

### 3. Build, test, and deploy stages

1. **Build**: reproducible compilers/images; SBOM/provenance hooks where required
2. **Test**: unit → integration → contract/e2e; quarantine flaky tests with SLA
3. **Publish**: push to registry/artifact store; sign when policy requires
4. **Deploy**: environment-specific jobs; smoke tests after each promotion
5. **Verify**: synthetic checks or canary metrics before full traffic shift

**See `references/build_test_deploy_stages.md` for stage contracts and artifacts.**

### 4. Environments, gates, and promotion

1. One promotion path: dev → staging → prod (no skip without exception)
2. Use environment protection rules and required reviewers for production
3. Gate on test results, security scans, policy (OPA/conftest), and change tickets
4. Promote the **same** artifact digest across environments
5. Record promotion audit trail (who, what digest, when)

**See `references/environments_gates_and_promotion.md` for gate catalog and promotion flows.**

### 5. Security and compliance in CI

1. Inject secrets via OIDC/vault—not long-lived PATs in variables
2. Run SAST/SCA/secrets/IaC scans on PR and default branch
3. Block merge on critical findings per SLA; document exceptions
4. Export scan artifacts for `devsecops` / `compliance-engineer` evidence
5. Harden fork PR workflows (no secret access, label-gated runs)

**See `references/security_and_compliance_in_ci.md` for credential and scan patterns.**

### 6. Release coordination and reliability metrics

1. Align release windows with SRE capacity and error-budget policy
2. Define rollback: redeploy previous digest vs rebuild; test quarterly
3. Post-release: update change log, close tickets, capture DORA data point
4. Blameless review when change fail rate spikes; feed pipeline fixes
5. Coordinate with `deployment-strategist` for cutover; with `site-reliability-engineer` for canary SLO gates

**See `references/reliability_metrics_and_release_coordination.md` for DORA and handoffs.**

## When to load references

| Topic | Reference |
|---|---|
| Scope, boundaries, stakeholders | `references/cicd_engineer_scope.md` |
| Workflow layout, branching, reuse | `references/pipeline_design_and_workflow.md` |
| Stage design, artifacts, testing | `references/build_test_deploy_stages.md` |
| Environments, gates, promotion | `references/environments_gates_and_promotion.md` |
| Secrets, scans, compliance hooks | `references/security_and_compliance_in_ci.md` |
| DORA, rollback, SRE coordination | `references/reliability_metrics_and_release_coordination.md` |
