# Event sourcing and CQRS

## Table of contents

1. [Concepts](#concepts)
2. [When to apply](#when-to-apply)
3. [Write model and event store](#write-model-and-event-store)
4. [Read models and projections](#read-models-and-projections)
5. [Consistency and snapshots](#consistency-and-snapshots)

## Concepts

| Term | Meaning |
|---|---|
| **Event sourcing** | Persist state as append-only sequence of domain events |
| **CQRS** | Separate write model (commands → events) from read models (queries) |
| **Projection** | Materialized view built by consuming events |
| **Snapshot** | Periodic aggregate state to speed replay |

Event sourcing answers **what happened**. CQRS answers **how we query efficiently**.

## When to apply

**Strong fit:**

- Audit, dispute, regulatory replay requirements
- Complex domain with rich history (orders, ledger, workflows)
- Multiple read shapes over same write stream (reports, search, APIs)

**Weak fit:**

- Simple CRUD with one read/write shape
- Team lacks ops maturity for projections and replay drills
- Strong cross-aggregate ACID on every user click

CQRS without event sourcing is valid—**multiple read DBs** fed by integration events.

## Write model and event store

**Aggregate rules:**

- Commands validate against current aggregate state (loaded from events or snapshot)
- Emit **one or more domain events** per successful command
- Enforce invariants inside aggregate boundary—no cross-aggregate transactions

**Event store options:**

- Dedicated event store (EventStoreDB, custom append log)
- Kafka topic as log (with compaction for keyed aggregates)
- RDBMS `events` table with monotonic version per aggregate id

**Versioning:** each event carries `aggregateId`, `version`, `eventType`, `schemaVersion`.

## Read models and projections

| Projection type | Update path | Consistency |
|---|---|---|
| **Synchronous** | Same transaction as event append (outbox → projector) | Stronger; couples write latency |
| **Asynchronous** | Consumer builds read model | Eventual; document lag SLO |
| **On-demand** | Replay stream to rebuild | Used for new views or recovery |

**Idempotent projection handlers:**

- Key by `(aggregateId, version)` or event id
- Store last processed position in inbox/offset table
- Design projections to tolerate **at-least-once** delivery

## Consistency and snapshots

- **Eventual consistency** between write and read is normal—UI must handle stale reads or use read-your-writes patterns
- **Snapshots** every N events reduce replay time; snapshot + tail events on load
- **Global ordering** across aggregates is usually unnecessary; per-aggregate version is enough
- **Deletion/GDPR:** legal hold and tombstone strategies must be designed upfront—not bolted on

**Integration with microservices:**

- Publish **integration events** at bounded context edge; do not expose raw internal event store to all consumers
- See `microservices-developer` for service ownership; this skill covers **pattern choice**
