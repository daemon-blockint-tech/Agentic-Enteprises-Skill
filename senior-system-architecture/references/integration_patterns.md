# Integration patterns

## Table of contents

1. [Choosing a pattern](#choosing-a-pattern)
2. [Sync integration](#sync-integration)
3. [Async and events](#async-and-events)
4. [Distributed workflows](#distributed-workflows)
5. [Anti-patterns](#anti-patterns)

## Choosing a pattern

| Need | Prefer | Avoid when |
|---|---|---|
| Strong immediate consistency | Sync API + single DB transaction | High fan-out or fragile chains |
| Loose coupling, scale consumers | Events + idempotent handlers | Need read-your-writes across services |
| External partner callbacks | Webhooks + signature verification | No retry/idempotency story |
| Mobile/SPA many backends | BFF or API gateway aggregation | BFF becomes god service |
| Bulk data movement | File/object + pipeline or CDC | Chatty row-by-row APIs |

## Sync integration

**REST/GraphQL/gRPC:**

- Version APIs; never break without deprecation window
- Set timeouts < client patience; retry only idempotent ops
- Use correlation IDs across calls
- Circuit break when dependency error rate spikes

**BFF:**

- Own aggregation and response shaping for one client class
- Do not own business rules that belong in domain services
- Cache with explicit TTL and invalidation rules

## Async and events

**Event contract:**

- Schema registry or documented JSON/Avro/Protobuf
- `eventType`, `schemaVersion`, `occurredAt`, `correlationId`, `idempotencyKey`
- Define ordering guarantees (per partition key only)

**Consumer rules:**

- Idempotent processing (natural key or dedup store)
- Poison message: DLQ + alert + replay tooling
- At-least-once is default; design for duplicates

**Outbox pattern:**

- Write business row + outbox in same DB transaction
- Publisher reads outbox—avoids dual-write races

## Distributed workflows

**Saga (orchestrated or choreographed):**

- Each step compensates or marks terminal failure
- Document partial failure: what the user sees
- Avoid long synchronous chains across services

**CQRS (when justified):**

- Separate write model and read projections
- Accept eventual consistency on reads; document lag SLO

## Anti-patterns

- **Distributed monolith** — many services, one database, coupled deploys
- **Chatty sync mesh** — N×M point-to-point without gateway or events
- **Events as command bus** — fire-and-forget without consumer contract
- **Shared library for domain logic** — hides boundaries; use contracts instead

For service-level boundary heuristics, see `senior-software-engineer` references.
