# Build, test, and deploy stages

## Table of contents

1. [Stage contracts](#stage-contracts)
2. [Build stage](#build-stage)
3. [Test pyramid in CI](#test-pyramid-in-ci)
4. [Flaky test handling](#flaky-test-handling)
5. [Publish and artifact registry](#publish-and-artifact-registry)
6. [Deploy stage](#deploy-stage)
7. [Deployment strategies in workflows](#deployment-strategies-in-workflows)
8. [Smoke and verification](#smoke-and-verification)
9. [Artifacts between jobs](#artifacts-between-jobs)

## Stage contracts

Each stage should declare:

| Field | Purpose |
|---|---|
| Inputs | Commit SHA, cache keys, prior artifact URIs |
| Outputs | Exit code, junit/coverage, image digest, SBOM path |
| Timeout | Prevent hung jobs from blocking runners |
| Retry policy | Transient infra only—not test failures |
| Required for | `merge`, `deploy-staging`, `deploy-prod` |

Document stage contracts in pipeline README or inline comments for template consumers.

## Build stage

**Goals:** reproducible compile or image from locked dependencies.

Checklist:

- [ ] Pin base images and tool versions (compiler, Node, Go, JDK)
- [ ] Use lockfiles (`package-lock.json`, `go.sum`, `poetry.lock`)
- [ ] Multi-stage Docker builds; minimal runtime image
- [ ] Build args only for non-secret metadata (version, git SHA)
- [ ] Label images: `org.opencontainers.image.revision`, version
- [ ] Fail on warnings only when policy requires (avoid noisy flakiness)

**Outputs:** OCI image digest, binary tarball, or package version string—never a floating tag alone.

## Test pyramid in CI

| Layer | Typical trigger | Duration budget | Failure action |
|---|---|---|---|
| Lint / format | Every PR | Minutes | Block merge |
| Unit | Every PR | Minutes | Block merge |
| Integration | PR + main | Tens of minutes | Block merge or main only |
| Contract / API | Main, release | Tens of minutes | Block deploy |
| E2E | Nightly or pre-prod | Long | Block prod promotion |

**Test data:** ephemeral databases, containers, or mocks—no shared mutable state between parallel shards.

**Coverage:** publish coverage artifacts; do not use arbitrary % as sole merge gate without team agreement.

## Flaky test handling

1. **Detect** — track flaky rate per test (retry plugins, test analytics).
2. **Quarantine** — mark flaky tests skipped in default PR path with ticket link.
3. **SLA** — fix or delete quarantined tests within agreed days.
4. **Retry policy** — limit automatic retries to known infra flakes, not assertions.
5. **Report** — weekly flaky leaderboard to engineering managers.

Never silently retry failed assertions in production deploy paths without visibility.

## Publish and artifact registry

After build + required tests:

1. Push image to registry with immutable digest
2. Upload SBOM/provenance when `devsecops` policy requires
3. Store Helm chart, Terraform bundle, or package to artifact store
4. Retention policy: PR artifacts short TTL; release artifacts per compliance

**Signing:** cosign/notary or platform equivalent before prod promotion gate.

## Deploy stage

Deploy jobs should:

- Download **exact** artifact from publish stage (digest verification)
- Target one environment per job (dev/staging/prod separation)
- Use infrastructure credentials scoped to that environment
- Emit deployment record (version, digest, timestamp, actor)
- Run **smoke tests** immediately after deploy

Avoid rebuilding application in deploy job unless deployable is infrastructure-only (e.g., `terraform apply` with same modules).

## Deployment strategies in workflows

Implement at workflow/orchestration layer; pair with runtime config from platform/SRE.

| Strategy | Workflow pattern | Rollback |
|---|---|---|
| Rolling | Sequential instance/job updates | Redeploy previous digest |
| Blue-green | Deploy idle stack → switch traffic job | Switch traffic back |
| Canary | Deploy small % → metric gate → full | Scale canary to 0 |
| Feature flags | Deploy once; flag controls exposure | Disable flag |

Metric gates for canary belong in coordination with `site-reliability-engineer` (error rate, latency SLO).

## Smoke and verification

Minimum post-deploy checks:

- Health endpoint returns 200
- Critical read-only API path
- Database migration status (if applicable)
- Queue consumer heartbeat (if applicable)

Run from CI job or delegated synthetic monitor; failures trigger automatic rollback when policy allows.

## Artifacts between jobs

| Mechanism | Use when |
|---|---|
| Workflow artifacts | Logs, reports, small bundles between jobs |
| Registry / package feed | Images, charts, binaries for promotion |
| Object storage | Large test fixtures, compliance exports |
| Cache | Dependencies—not deployable artifacts |

**Rule:** production promotion references registry digest or versioned package ID, not workflow artifact zip from a different commit.
