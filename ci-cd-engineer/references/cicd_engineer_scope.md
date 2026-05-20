# CI/CD engineer scope

## Table of contents

1. [Role definition](#role-definition)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Stakeholders and handoffs](#stakeholders-and-handoffs)
5. [Deliverables](#deliverables)
6. [Success criteria](#success-criteria)

## Role definition

The CI/CD engineer owns **how software moves from commit to production** through automated pipelines: stage design, workflow maintenance, environment promotion, artifact integrity, deployment automation at the pipeline layer, and delivery metrics. The role partners with application teams, platform engineering, security, and SRE—it does not replace them.

Primary systems: GitHub Actions, GitLab CI, Jenkins, CircleCI, Buildkite, Azure Pipelines, and adjacent registries, artifact stores, and deploy hooks (Helm, Argo CD triggers, serverless deploy plugins).

## In scope

| Area | Examples |
|---|---|
| Pipeline architecture | Reusable workflows, job graphs, caching, matrix builds |
| Branch and release | Trunk-based vs release branches, tag promotion, hotfix lanes |
| Build and test orchestration | Stage ordering, parallelization, test splitting, flaky quarantine |
| Artifact lifecycle | Immutable tags, digests, retention, promotion between envs |
| Deploy automation | Rolling/blue-green/canary **as coded in pipelines** |
| CI credentials | OIDC to cloud, short-lived tokens, secret rotation in runners |
| Quality gates | Required checks, environment approvals, policy-as-code in CI |
| Delivery metrics | DORA collection, pipeline duration, queue time, failure taxonomy |
| Release mechanics | Rollback runbooks tied to artifacts, release notes hooks |
| Repo layout | Monorepo path filters, affected-target detection, polyrepo standards |

## Out of scope

| Area | Route to |
|---|---|
| Application business logic and feature code | `senior-software-engineer` |
| Cluster bootstrap, CNI, control plane, node ops | `cloud-engineer`, `cluster-deployment-engineer` |
| SLO/error-budget program and burn-rate alerting | `site-reliability-engineer` |
| Enterprise security policy, IdP, KMS operations | `information-security-engineer` |
| Deep supply-chain threat modeling and pentest | `devsecops`, `penetration-tester` |
| Developer portal, scaffolders, paved-road product | `platform-engineer` |
| Cutover playbooks and change-advisory tiers | `deployment-strategist` |
| End-to-end GitOps platform and observability stack | `devops` |
| Architecture go/no-go without pipeline delivery | `build-validator` |

## Stakeholders and handoffs

| Partner | CI/CD engineer provides | Partner provides |
|---|---|---|
| Application team | Pipeline templates, deploy hooks, test stage contracts | Tests, app config, feature flags |
| Platform engineer | Consumes golden-path templates; feedback on friction | Runner pools, registries, standard modules |
| DevSecOps | Scan stage integration points, artifact exports | Tooling, severity SLAs, exception process |
| SRE | Release windows, rollback hooks, canary metric gates | SLOs, error budget policy, incident comms |
| Compliance engineer | Evidence artifacts from pipeline runs | Control mapping, audit calendar |
| Infrastructure engineer | Deploy credentials scope, env accounts | Accounts, networking, IAM boundaries |

Escalate **production incidents** to on-call/SRE; CI/CD engineer supports rollback execution and pipeline fixes, not incident command unless explicitly dual-hatted.

## Deliverables

- Pipeline-as-code in application or shared template repositories
- Documented stage diagram and promotion flow per service tier
- Gate catalog: what blocks merge vs production deploy
- Runbook: hotfix, rollback, and manual promotion exception process
- Dashboard or export for DORA and pipeline reliability metrics
- Onboarding guide for new services (required checks, secrets, environments)

## Success criteria

- **Reproducible**: same commit produces same artifact digest
- **Fast feedback**: median PR pipeline within team target; critical path identified
- **Safe promotion**: production receives only approved digests; no env drift rebuilds
- **Observable**: failed stages categorized (infra, test, security, deploy)
- **Recoverable**: rollback tested; last-known-good digest documented
- **Measurable**: DORA and change-fail trends visible; regressions investigated
