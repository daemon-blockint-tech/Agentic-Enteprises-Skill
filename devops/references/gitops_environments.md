# GitOps and environments

## Table of contents

1. [Repository layout](#repository-layout)
2. [Promotion flow](#promotion-flow)
3. [Drift and secrets](#drift-and-secrets)

## Repository layout

```
apps/
  my-service/
    overlays/
      dev/
      staging/
      prod/
```

Or mono-repo `environments/prod/` with Kustomize bases.

## Promotion flow

1. PR changes `staging` overlay → auto-sync
2. Soak period + automated tests
3. PR promotes same image tag/digest to `prod`
4. Argo CD sync with manual sync option for prod

## Drift and secrets

- Enable auto-sync for dev only; prod may require manual sync
- Never commit plaintext secrets; use External Secrets Operator
- Alert on `OutOfSync` > N minutes for production apps
