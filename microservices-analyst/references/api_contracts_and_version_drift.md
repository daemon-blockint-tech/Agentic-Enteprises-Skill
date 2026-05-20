# API Contracts and Version Drift

## Contract artifacts to collect

| Type | Location examples |
|---|---|
| OpenAPI / Swagger | Repo, portal, gateway export |
| gRPC / Protobuf | Buf schema registry, `.proto` repos |
| GraphQL | Schema registry, stitched gateway |
| AsyncAPI / event schemas | Kafka schema registry, Pact broker |
| Consumer-driven contracts | Pact, custom compatibility suites |

## Drift categories

| Drift type | Description | Severity |
|---|---|---|
| **Undocumented** | Production behavior not in any contract | High for external APIs |
| **Stale contract** | Published spec older than implementation | Medium |
| **Breaking undeclared** | Field removed/renamed without version bump | High |
| **Multi-version prod** | v1 and v2 consumers on same cluster skew | High |
| **Regional skew** | EU vs US schema difference | High if unintended |

## Compatibility analysis workflow

1. Export **runtime** schema (gateway, mesh, reflection) where allowed.
2. Diff against **published** contract (git tag or registry version).
3. List **consumers** per API version (mesh, logs, client SDK repos).
4. Classify changes: safe additive, deprecated, breaking.
5. Note missing **deprecation headers**, sunset dates, or consumer outreach.

## Breaking-change consumer map

| Producer API | Version | Known consumers | Breaking change | Mitigation status |
|---|---|---|---|---|
| `/orders` | v2 | billing-job, mobile-bff | removed `discountCode` | 1/3 migrated |

Unknown consumers → flag as **discovery gap** (tracing, gateway logs, static search).

## Version skew across estate

Check:

- Mobile/web clients pinned to old API versions
- BFFs calling deprecated internal routes
- Event schema versions mixed in one topic
- Feature flags masking half-migrated contracts

## Contract testing maturity

| Level | Characteristics |
|---|---|
| 0 | No contracts; integration tests only in prod-like env |
| 1 | OpenAPI exists; not enforced in CI |
| 2 | CI breaks on breaking diff; partial consumer coverage |
| 3 | Pact or equivalent per critical consumer/producer pair |

Recommend target level per tier-0 API—not blanket level 3 everywhere.

## API gateway and mesh signals

- Routes pointing to retired services
- Timeout/retry defaults masking failures
- Rate limits absent on tier-0 paths
- mTLS identity mismatch between documented and actual callers

## Deliverables

- **Drift report** per service (summary + diffs)
- **Consumer compatibility matrix**
- **Deprecation backlog** with owners and dates
- **Standardization gaps** for platform (lint rules, registry) → `platform-engineer`

## Handoffs

- Greenfield versioning **strategy** (not estate audit) → `microservice-researcher`
- Implementing registry, breaking-change CI → `senior-software-engineer`, `microservices-developer`
