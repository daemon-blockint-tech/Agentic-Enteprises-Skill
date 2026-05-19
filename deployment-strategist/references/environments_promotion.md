# Environments and promotion

## Table of contents

1. [Topology patterns](#topology-patterns)
2. [Promotion rules](#promotion-rules)
3. [Config and secrets](#config-and-secrets)

## Topology patterns

| Pattern | Use when |
|---|---|
| Linear | dev → staging → prod |
| PR previews | Every PR gets ephemeral env |
| Prod-like staging | Mandatory for payments, auth, perf-sensitive |
| DR passive | Standby region; test failover quarterly |

## Promotion rules

- Promote **artifact digest** built once in CI
- Staging must run same digest intended for prod
- No hot patches on prod without backport to git
- Tag release in git matching deployed digest

## Config and secrets

| Layer | Source |
|---|---|
| Default | Git (non-secret config) |
| Env overlay | Kustomize / Helm values per env |
| Secrets | Vault / cloud secret manager only |

Parity: staging uses same secret *shape* as prod; different values.
