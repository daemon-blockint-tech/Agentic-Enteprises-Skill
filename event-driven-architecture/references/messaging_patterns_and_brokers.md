# Messaging patterns and brokers

## Table of contents

1. [Pattern selection](#pattern-selection)
2. [Pub/sub vs point-to-point](#pubsub-vs-point-to-point)
3. [Partitioning and ordering](#partitioning-and-ordering)
4. [Broker comparison](#broker-comparison)
5. [Kafka-oriented notes](#kafka-oriented-notes)

## Pattern selection

| Pattern | Use when | Watch out for |
|---|---|---|
| **Pub/sub (fan-out)** | Many independent consumers of same fact | Consumer lag; schema coupling |
| **Point-to-point (queue)** | Exactly one worker processes each message | Competing consumers need idempotency |
| **Request-reply** | Command needs ack or query result | Timeouts; do not block user path on broker |
| **Event-carried state transfer** | Consumers need embedded snapshot | Stale data; large messages |
| **Event notification** | Consumers load from API/DB on signal | Thundering herd on hot keys |

## Pub/sub vs point-to-point

**Pub/sub (topics):**

- Log-based retention (Kafka, Pulsar) enables **replay** and multiple consumer groups
- Ordering is **per partition** only—choose partition key deliberately
- Consumers in same group share load; different groups read independently

**Point-to-point (queues):**

- Message removed (or hidden) after ack—typical for **task queues**
- Competing consumers scale horizontally; use **visibility timeout** and idempotency
- Dead-letter after max receives (SQS) or retry policy (Rabbit)

## Partitioning and ordering

| Requirement | Approach |
|---|---|
| Strict order per entity | Partition key = `orderId`, `accountId`, etc. |
| Global order | Single partition (limits throughput)—avoid unless tiny volume |
| No order needed | Round-robin partitions; maximize parallelism |
| Cross-entity workflow | Saga/orchestrator stores state; do not rely on global order |

**Hot partitions:** monitor skew; split keys or salt high-volume tenants.

## Broker comparison

| Broker | Strengths | Typical gaps |
|---|---|---|
| **Apache Kafka** | High throughput, log retention, stream processing | Ops complexity; consumer lag discipline |
| **Pulsar** | Multi-tenancy, geo-replication, tiered storage | Smaller talent pool than Kafka |
| **RabbitMQ** | Flexible routing, classic queues | Not a long-retention event log by default |
| **AWS SNS/SQS** | Managed, simple fan-out + queue | Ordering/fifo limits; cross-region design |
| **Azure Service Bus** | Sessions for ordering, DLQ built-in | Throughput tiers and quota planning |
| **Google Pub/Sub** | Managed scale, ordering keys | Ordering key scope and quota |

Pick broker based on **retention, ordering, ops model, and team skill**—not hype.

## Kafka-oriented notes

When users mention **Kafka events**:

- **Topic** = contract boundary; **partition** = parallelism + ordering unit
- **Consumer group** = scaling unit; lag per partition is the alert signal
- **Compaction** for keyed changelog topics (CQRS projections), not all domain topics
- **Headers** for correlation id, schema id, trace context, idempotency key
- Prefer **Schema Registry** (Avro/Protobuf/JSON Schema) over undocumented JSON

**Stream processing vs discrete events:**

- **Discrete business events** — one fact per message (`OrderPlaced`)
- **Stream processing** — continuous transforms, windows, joins (Kafka Streams, Flink)
- Use streams for **analytics/enrichment**; use domain events for **integration contracts**
