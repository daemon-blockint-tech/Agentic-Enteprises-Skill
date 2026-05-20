# Schema governance and operations

## Table of contents

1. [Schema design](#schema-design)
2. [Event schema versioning](#event-schema-versioning)
3. [Registry and compatibility](#registry-and-compatibility)
4. [Dead-letter queues](#dead-letter-queues)
5. [Replay and reprocessing](#replay-and-reprocessing)
6. [Observability](#observability)

## Schema design

**Envelope fields (recommended):**

- `eventId`, `eventType`, `schemaVersion`, `occurredAt`
- `correlationId`, `causationId`, `producer`
- `payload` (versioned body)

**Conventions:**

- Use **past-tense** event names; version in type or separate field (`order.placed.v1`)
- Prefer **Avro/Protobuf/JSON Schema** over schemaless JSON for integration topics
- Document **required vs optional** fields and default semantics
- Align with **CloudEvents** where teams already standardize on it

## Event schema versioning

| Change type | Compatibility | Example |
|---|---|---|
| Add optional field | Backward compatible | New `shippingTier` optional |
| Remove field | Breaking | Drop `legacyCode` |
| Rename field | Breaking | `customerId` → `buyerId` |
| Change type | Breaking | string → number |
| Add enum value | Usually backward | New status if consumers ignore unknown |

**Strategies:**

1. **Single topic, multiple schema versions** in registry (Confluent BACKWARD/FULL)
2. **New topic** per major version (`orders.v1` → `orders.v2`) for clean cutover
3. **Dual-write** during migration; consumers upgrade before producer drops old fields

Publish **deprecation timeline** in event catalog; never break consumers without notice.

## Registry and compatibility

| Mode | Producer | Consumer |
|---|---|---|
| **BACKWARD** | New schema; old consumers read new | Add fields only with defaults |
| **FORWARD** | Old producer; new consumers | New consumers tolerate old |
| **FULL** | Both directions | Strict discipline |

**CI gates:**

- Schema diff on PR
- Compatibility check against registry rules
- Contract tests for sample payloads

## Dead-letter queues

**When to DLQ:**

- Deserialization failure (poison schema)
- Business rule rejection after max retries
- Handler bug (fix forward, then replay)

**DLQ operations:**

- Retain original headers, payload, stack trace, failure reason
- Alert on DLQ depth threshold
- **Drain procedure:** fix consumer → replay to main topic or dedicated replay topic
- Access control on DLQ (may contain PII)

**Kafka:** separate topic `orders.dlq` or use retry topics with backoff tiers.

## Replay and reprocessing

**Use cases:**

- New projection/read model
- Bug fix in consumer logic
- Regulatory audit export

**Checklist before replay:**

1. Confirm **idempotency** and dedup window cover replay window
2. Define **offset/time range** and ordering expectations
3. Isolate **side effects** (emails, charges)—use dry-run or sandbox
4. Rate-limit replay to protect downstream DBs
5. Metric: `replay_lag`, `duplicate_suppressed_count`

**Never** replay production charges without explicit business approval.

## Observability

| Signal | Purpose |
|---|---|
| Consumer lag (per partition) | Capacity and stuck consumers |
| Publish error rate | Outbox relay health |
| DLQ rate | Schema or logic defects |
| End-to-end latency | `occurredAt` → handler complete |
| Schema rejections | Registry mismatch |

**Tracing:** propagate `traceparent` in headers; link producer span to consumer span.

**Dashboards per event type**—not only per broker cluster.
