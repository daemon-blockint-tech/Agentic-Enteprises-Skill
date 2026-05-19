# Workload delivery

## Table of contents

1. [Helm](#helm)
2. [Kustomize](#kustomize)
3. [Rollout verification](#rollout-verification)

## Helm

```bash
helm upgrade --install <release> <chart> -n <ns> -f values.<env>.yaml --atomic --timeout 10m
helm history <release> -n <ns>
helm rollback <release> <revision> -n <ns>
```

**Values discipline:**

- Base `values.yaml` + env overlays (`values.prod.yaml`)
- Pin chart version in CI or GitOps; do not float `latest`
- Set `resources.requests/limits`, `liveness`/`readiness` probes, `podDisruptionBudget` where HA

## Kustomize

```
base/
  deployment.yaml
overlays/
  staging/kustomization.yaml
  prod/kustomization.yaml
```

- Use `images:` for tag promotion; `patches` for replicas and env
- `kubectl apply -k overlays/prod --dry-run=server` before merge

## Rollout verification

```bash
kubectl rollout status deployment/<name> -n <ns>
kubectl get pods -n <ns> -o wide
kubectl describe pod <pod> -n <ns>   # Events
```

Exit criteria: all replicas ready, Service has endpoints, ingress returns 200 on health path.

Application rollout **strategy** (canary %, traffic split) → `deployment-strategist`.
