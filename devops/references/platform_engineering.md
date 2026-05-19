# Platform engineering

## Table of contents

1. [IDP scope](#idp-scope)
2. [Golden paths](#golden-paths)
3. [Metrics](#metrics)

## IDP scope

Typical internal developer platform includes:

- Template repositories and scaffolding CLI
- Standard CI/CD workflows
- Environment provisioning APIs
- Service catalog and ownership metadata

## Golden paths

Document the blessed way to:

- Create a service
- Add observability
- Ship to production

Discourage snowflake pipelines unless exception approved.

## Metrics

| Metric | Why |
|---|---|
| Lead time to deploy | Velocity |
| Change failure rate | Stability |
| Time to restore | Resilience |
| Developer satisfaction survey | Adoption |
