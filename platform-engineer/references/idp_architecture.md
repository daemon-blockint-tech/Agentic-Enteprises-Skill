# IDP architecture

## Table of contents

1. [Component map](#component-map)
2. [Platform contracts](#platform-contracts)
3. [Anti-patterns](#anti-patterns)

## Component map

```
Developers
    ↓
Portal (catalog, docs, create)
    ↓
Control plane (GitOps / IaC / APIs)
    ↓
Runtime (K8s, serverless, DB patterns)
    ↓
Observability + security baselines (automatic)
```

## Platform contracts

Document for each capability:

- Inputs teams provide (name, tier, region)
- Outputs guaranteed (URLs, dashboards, IAM roles)
- SLAs and support channel
- Cost allocation model

## Anti-patterns

- Platform team becomes ticket queue for raw Terraform
- No versioning on templates—silent drift
- Portal without working self-service (catalog-only)
- One giant cluster with no tenant guardrails
