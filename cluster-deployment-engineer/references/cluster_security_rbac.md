# Cluster security and RBAC

## Table of contents

1. [Namespace tenancy](#namespace-tenancy)
2. [RBAC](#rbac)
3. [Secrets](#secrets)
4. [Pod Security Admission](#pod-security-admission)

## Namespace tenancy

Per team or env:

```yaml
# ResourceQuota example fields
requests.cpu, requests.memory, limits.cpu, limits.memory, pods, services
```

Use **LimitRange** for default container limits in dev namespaces.

## RBAC

- Bind `Role`/`RoleBinding` in namespace; avoid `ClusterRoleBinding` to `cluster-admin` for apps
- CI deploy SA: create/update in target namespace only
- Humans: read-only default; break-glass cluster-admin via PAM group

Audit: `kubectl auth can-i --list -n <ns> --as=system:serviceaccount:<ns>:<sa>`

## Secrets

- Do not commit Secrets; use External Secrets / CSI driver / cloud secret manager
- Rotate on compromise; prefer short-lived tokens (IRSA, workload identity)

## Pod Security Admission

| Level | Typical use |
|---|---|
| privileged | system namespaces only |
| baseline | most internal tools |
| restricted | customer-facing workloads |

Enforce at namespace labels; validate with `kubectl label` dry-run before cutover.

Admission webhooks and image policies → `devsecops`.
