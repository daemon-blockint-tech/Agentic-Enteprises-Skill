# CI/CD and releases

## Table of contents

1. [Branching](#branching)
2. [Deployment strategies](#deployment-strategies)
3. [GitHub Actions patterns](#github-actions-patterns)
4. [Rollback](#rollback)

## Branching

| Strategy | Use when |
|---|---|
| Trunk-based | Small teams, continuous delivery |
| GitHub Flow | Web apps, single production |
| Release branches | Scheduled versions, mobile clients |

## Deployment strategies

| Strategy | Risk | Rollback |
|---|---|---|
| Rolling | Low | Redeploy previous revision |
| Blue-green | Medium | Switch traffic back |
| Canary | Medium | Reduce canary weight to 0 |
| Feature flags | Low | Disable flag |

## GitHub Actions patterns

- Use environments with required reviewers for `production`
- Reuse workflows (`workflow_call`) for standard build
- Cache `node_modules` / pip with lockfile hash key
- Upload artifacts between jobs; deploy job downloads digest-pinned image

## Rollback

1. Identify last known good artifact digest
2. Redeploy without rebuilding when possible
3. Run smoke tests
4. Post-incident: fix forward plan and pipeline guard
