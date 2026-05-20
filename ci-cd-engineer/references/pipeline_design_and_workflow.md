# Pipeline design and workflow

## Table of contents

1. [Design principles](#design-principles)
2. [Standard stage graph](#standard-stage-graph)
3. [Branching models](#branching-models)
4. [Reusable workflows and templates](#reusable-workflows-and-templates)
5. [Monorepo vs polyrepo](#monorepo-vs-polyrepo)
6. [Performance and cost](#performance-and-cost)
7. [Anti-patterns](#anti-patterns)
8. [Platform comparison notes](#platform-comparison-notes)

## Design principles

1. **Pipeline as code** — versioned with the app or a pinned template repo; no click-ops-only definitions for production paths.
2. **Immutable artifacts** — build once, promote many; never rebuild for production without explicit exception.
3. **Fail fast** — lint and unit tests before integration, container builds, and deploy jobs.
4. **Least privilege** — scoped tokens per job; no shared mega-credentials across org.
5. **Auditable** — who approved production, which digest deployed, which tests passed.
6. **Idempotent deploy** — redeploying the same digest is safe; pipelines tolerate retries.

## Standard stage graph

```
checkout
  → static analysis / lint
  → unit tests (parallel shards)
  → build (compile / image)
  → integration & contract tests
  → security scans (parallel where possible)
  → publish artifact (registry / package feed)
  → deploy non-prod
  → e2e / smoke (non-prod)
  → manual or policy gate
  → deploy staging / canary
  → synthetic / metric gate
  → deploy production
  → post-deploy smoke + notify
```

Optional branches: preview environments per PR, scheduled nightly full suites, performance benchmarks on main only.

## Branching models

| Model | When to use | CI implications |
|---|---|---|
| Trunk-based | Continuous delivery, small batches | All checks on main; short-lived feature branches |
| GitHub Flow | Single production line, web services | PR checks + deploy on merge to default branch |
| Release branches | Mobile, quarterly enterprise | Cherry-pick hotfixes; versioned pipeline inputs |
| GitFlow | Legacy regulated releases | More environments; higher coordination cost |

**Hotfix lane**: tag or branch from production commit; run abbreviated test suite; promote hotfix digest through same prod gate as normal releases.

## Reusable workflows and templates

- Central **callable workflows** (`workflow_call`) or shared Jenkins libraries with semver tags.
- Pin template version in consumer repos; changelog for breaking changes.
- Parameters: language, service tier, regions, feature flags for optional stages.
- Document escape hatches when teams must override (requires platform review).

**Contract per template:**

| Input | Output |
|---|---|
| Repo, ref, paths | Pass/fail checks |
| Service name, tier | Artifact coordinates |
| Target environment | Deploy job summary URL |

## Monorepo vs polyrepo

### Monorepo

- **Path filters** — run jobs only when relevant directories change.
- **Affected detection** — Nx/Turborepo/Bazel/graph tools to map dependency closure.
- **Shared versioning** — coordinate breaking changes across packages in one PR.
- **Risk** — long main-branch pipelines; mitigate with sharding and remote cache.

### Polyrepo

- **Standard template** — every service repo inherits same base pipeline.
- **Cross-repo releases** — orchestrate with meta-pipeline or release train manifest.
- **Dependency updates** — Renovate/bot PRs with required checks before merge.

## Performance and cost

| Technique | Benefit |
|---|---|
| Dependency cache keyed on lockfile | Faster install/compile |
| Docker layer cache / buildkit | Faster image builds |
| Test sharding + parallel runners | Shorter wall clock |
| `concurrency` cancel-in-progress on PRs | Saves minutes on rapid pushes |
| Self-hosted runners for large builds | Cost/latency tradeoff vs GitHub-hosted |
| Scheduled off-peak heavy jobs | Spreads load |

Track **queue time** vs **run time** separately—queue indicates runner capacity issues.

## Anti-patterns

| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| `latest` image tags in prod | Non-reproducible deploys | Digest pinning |
| Secrets in repo or logs | Credential leak | OIDC + secret manager |
| Skipping tests on `[skip ci]` for prod path | Quality escape | Policy: skip only for docs |
| One giant sequential job | Slow feedback | Split stages, parallelize |
| Different build per environment | Drift and surprises | Single build, promote artifact |
| Fork PRs with secret access | Supply-chain risk | Restrict workflows, approval labels |
| Manual prod deploy without record | Audit gap | Pipeline gate + ticket link |

## Platform comparison notes

| Platform | Strengths | CI/CD engineer focus |
|---|---|---|
| GitHub Actions | Ecosystem, environments, reusable workflows | OIDC, environments, cache, permissions model |
| GitLab CI | Built-in registry, environments, DAG | Includes, rules, protected branches |
| Jenkins | Plugins, on-prem, custom agents | Pipeline libraries, credential binding, agent pools |
| Buildkite | Agent model, monorepo scale | Pipeline upload, dynamic pipelines |
| CircleCI | Orbs, Docker-first | Contexts, workflows, parallelism |

Choose platform capabilities deliberately; migrating later is expensive—abstract only where multi-platform is a real requirement.
