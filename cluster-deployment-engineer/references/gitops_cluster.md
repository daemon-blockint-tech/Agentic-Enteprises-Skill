# GitOps at cluster scope

## Table of contents

1. [Repository layout](#repository-layout)
2. [Sync ordering](#sync-ordering)
3. [Drift and rollback](#drift-and-rollback)

## Repository layout

```
clusters/
  prod/
    infrastructure/    # add-ons, CRDs
    apps/                # team workloads
  staging/
    ...
```

Or **app-of-apps** root Application pointing at child paths.

Separate **platform** repo (cluster infra) from **application** repos when blast radius differs.

## Sync ordering

Argo CD sync waves (annotation `argocd.argoproj.io/sync-wave`):

| Wave | Examples |
|---|---|
| 0 | CRDs, namespaces |
| 1 | CNI-adjacent, cert-manager |
| 2 | Ingress, observability |
| 3+ | Application releases |

Use `Sync` hooks for DB migrations only when idempotent and owned by app team.

## Drift and rollback

- Manual `kubectl edit` creates drift—revert Git or disable auto-sync temporarily with incident record
- Rollback = revert Git commit or Helm revision in GitOps values
- Pipeline that only pushes images must still update Git tag for GitOps flow

CI pipeline mechanics → `devops`.
