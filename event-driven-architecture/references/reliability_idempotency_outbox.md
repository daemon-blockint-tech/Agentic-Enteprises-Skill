# Reliability, idempotency, and outbox

## Table of contents

1. [Delivery guarantees](#delivery-guarantees)
2. [Idempotent consumer](#idempotent-consumer)
3. [Exactly-once semantics](#exactly-once-semantics)
4. [Transactional outbox](#transactional-outbox)
5. [Inbox pattern](#inbox-pattern)
6. [Failure handling](#failure-handling)

## Delivery guarantees

| Guarantee | Meaning | Typical implementation |
|---|---|---|
| **At-most-once** | May lose messages | Fire-and-forget; rare for business events |
| **At-least-once** | No loss; duplicates possible | Ack after process; retries on failure |
| **Effectively exactly-once** | No duplicate side effects | Idempotent handlers + dedup store |

Brokers usually provide **at-least-once**. Exactly-once **processing** is an application concern.

## Idempotent consumer

**Idempotency key sources:**

- Business key: `paymentId`, `orderId` + `operation`
- Broker metadata: message id, offset (weaker for redelivery across topics)
- Event envelope: `eventId` UUID (preferred for integration events)

**Implementation checklist:**

1. Persist processed keys in **dedup table** (TTL ≥ max redelivery window)
2. Make downstream writes **upserts** or compare-and-set on version
3. Return success on duplicate key (do not double-charge, double-ship)
4. Log duplicate at debug/metric—not error storm

**Side-effectful operations:** use outbox + single-writer or external idempotent APIs (Stripe idempotency keys).

## Exactly-once semantics

True end-to-end exactly-once across services is **expensive and rare**.

Pragmatic approach:

- **Kafka transactional produce** + idempotent producer (broker scope)
- **Consume-transform-produce** with transactions (stream apps)
- **Outbox + idempotent consumer** for cross-service (most common)

Document **which layer** provides which guarantee in the ADR.

## Transactional outbox

**Problem:** DB commit and message publish must not diverge.

**Pattern:**

1. In same DB transaction: update business rows + insert row into `outbox` table
2. Relay process polls outbox and publishes to broker
3. Mark outbox row published (or delete) after broker ack

**Relay options:**

- Polling publisher (simple; watch DB load)
- Log-based CDC (Debezium) reading outbox table or WAL
- In-process relay (only if crash safety understood)

**Ordering:** publish in outbox insertion order per aggregate if consumers depend on it.

## Inbox pattern

For **incoming** messages:

- Store message id in `inbox` in same transaction as domain update
- Skip processing if id already present
- Complements idempotency when handler has multiple steps

## Failure handling

| Failure | Response |
|---|---|
| Transient (network, throttle) | Retry with exponential backoff + jitter |
| Poison (schema mismatch, bad data) | Route to **DLQ**; alert owner team |
| Partial saga step failure | Compensating event or orchestrator retry policy |
| Broker unavailable | Buffer in outbox; backpressure producers |

**Retry storms:** cap retries; use circuit breaker on publisher relay.

**Ordering + retry:** retries may reorder—consumers must tolerate or use partition stickiness.
