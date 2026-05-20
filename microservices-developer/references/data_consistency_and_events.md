# Data consistency and events

## Table of contents

1. [Data ownership](#data-ownership)
2. [Consistency models](#consistency-models)
3. [Transactional outbox](#transactional-outbox)
4. [Sagas](#sagas)

## Data ownership

| Rule | Rationale |
|---|---|
| One writer per aggregate | Avoid conflicting updates |
| No cross-service DB joins | Coupling and schema leakage |
| Expose data via API or events | Consumers stay decoupled |
| Cache is not source of truth | Invalidate on events or TTL with eyes open |

**Shared database** is a temporary migration state only—document exit criteria.

## Consistency models

| Model | When |
|---|---|
| Strong (single service) | In-aggregate transactions |
| Read-your-writes | Route reads to primary or sync replica after write |
| Eventual | Cross-service facts; UI shows pending states |
| Causal | Order related events per aggregate partition |

Avoid **two-phase commit (2PC)** across services unless platform mandates and team can operate it.

## Transactional outbox

**Problem:** DB commit and message publish must not diverge.

**Pattern:**

1. Business row + `outbox` row in **same DB transaction**
2. Relay process polls outbox → publishes to broker → marks sent
3. Consumers idempotent on `event_id`

| Component | Notes |
|---|---|
| Outbox schema | `id`, `aggregate_type`, `payload`, `created_at`, `sent_at` |
| Relay | At-least-once publish; dedup on consumer |
| Ordering | Same partition key as aggregate |

Alternative: **CDC** (Debezium) from DB log—ops-heavy, strong for analytics pipelines.

## Sagas

Long-running business processes across services.

**Choreography saga:**

- Each service listens and emits events
- Compensation events (`PaymentFailed` → `OrderCancelled`)
- Requires clear event catalog and idempotency

**Orchestration saga:**

- Coordinator stores state machine (`PENDING_PAYMENT`, `COMPLETED`)
- Calls participants with timeouts; runs compensating calls on failure
- Easier tracing; coordinator must be HA

| Step | Forward | Compensate |
|---|---|---|
| Reserve inventory | `Reserve` | `Release` |
| Charge payment | `Capture` | `Refund` |
| Create shipment | `Create` | `Cancel` |

**Idempotency keys** on every participant command.

Duplicate saga/outbox depth at enterprise integration layer → `enterprise-integration-api-developer`.
