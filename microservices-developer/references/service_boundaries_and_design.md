# Service boundaries and design

## Table of contents

1. [Bounded contexts](#bounded-contexts)
2. [Context mapping](#context-mapping)
3. [Service API design](#service-api-design)
4. [Decomposition workflow](#decomposition-workflow)

## Bounded contexts

A **bounded context** is a model boundary where terms and rules are consistent.

| Concept | Guidance |
|---|---|
| Ubiquitous language | Name entities the same inside the context; translate at edges |
| Aggregate | Cluster consistency boundary; one transaction per aggregate where possible |
| System of record | Exactly one service owns writes for a business fact |
| Read model | Other services consume via API or events; no direct DB access |

## Context mapping

Relationships between contexts (from strategic DDD):

| Pattern | When | Integration |
|---|---|---|
| Partnership | Two teams evolve together | Shared roadmap; joint contracts |
| Customer–supplier | Upstream sets API; downstream adapts | Versioned contracts, SLAs |
| Conformist | Downstream accepts upstream model | Minimize translation |
| Anti-corruption layer (ACL) | Legacy or foreign model | Adapter translates to local model |
| Open host service | Many consumers | Published language, strict versioning |
| Published language | Shared interchange format | Events or canonical DTOs with governance |

Document on a **context map** diagram before cutting services.

## Service API design

**REST (HTTP):**

- Resource-oriented URLs; use `POST` for commands when actions are not CRUD
- Standard error envelope: `code`, `message`, `details`, `trace_id`
- Pagination: cursor preferred for large sets; stable sort keys
- Idempotency: `Idempotency-Key` header on mutating operations

**gRPC:**

- Prefer for internal high-throughput, typed contracts
- Define deadlines on every call; propagate metadata (`traceparent`, tenant)
- Use `UNAVAILABLE` / `DEADLINE_EXCEEDED` for retry decisions; not for business errors

**Events:**

- Name events in past tense (`OrderPlaced`); include schema version
- Partition keys preserve per-entity ordering
- Consumers must be idempotent (`event_id` dedup)

## Decomposition workflow

1. Identify **core domains** and supporting/generic subdomains
2. Draw **context map**; mark ACLs where legacy exists
3. List **transactions** that must stay atomic vs can be eventual
4. Prototype **strangler** route: extract read path or async boundary first
5. Define **contract tests** before splitting databases
6. Migrate data with **dual-write or CDC** only with explicit cutover plan

For enterprise-wide integration hubs and canonical models → `enterprise-integration-api-developer`.
