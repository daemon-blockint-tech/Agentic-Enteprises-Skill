---
name: event-driven-architecture
description: |
  Guides event-driven systems—pub/sub, point-to-point, event sourcing, CQRS, schema versioning
  (Avro/JSON Schema), ordering, partitioning, delivery guarantees, idempotency, exactly-once
  tradeoffs, transactional outbox/inbox, choreography vs orchestration, sagas, dead-letter queues,
  replay, stream vs discrete events, microservice boundaries. Use when the user asks for
  event-driven architecture, event sourcing, CQRS, pub/sub, Kafka events, outbox pattern,
  idempotent consumer, event choreography, saga orchestration, dead letter queue, or event schema
  versioning—not microservice code only (microservices-developer), enterprise API/iPaaS only
  (enterprise-integration-api-developer), EDI (edi-engineer), classified promotion
  (classified-software-devsecops-engineer), solvers (operations-research-algorithm-developer),
  generic CRUD (senior-software-engineer).
---

# Event-Driven Architecture

## When to Use

- Design **event-driven** integration between bounded contexts or microservices
- Choose **pub/sub vs point-to-point**, topics vs queues, and broker capabilities
- Model **domain events**, integration events, and command vs event semantics
- Apply **event sourcing** or **CQRS** at architecture level (not framework tutorials only)
- Define **schemas**, compatibility rules, and **event schema versioning** strategy
- Specify **ordering**, **partition keys**, and **delivery guarantees** (at-least-once, etc.)
- Design **idempotent consumers**, deduplication, and **exactly-once** tradeoffs
- Implement **transactional outbox** or **inbox** for reliable publish/consume
- Decide **choreography vs orchestration** and **saga** compensation at pattern level
- Operate **dead-letter queues**, replay, and stream reprocessing safely
- Distinguish **stream processing** (Kafka Streams, Flink) from **discrete business events**

## When NOT to Use

- Implement microservice code, gRPC/REST APIs, or twelve-factor deployables only → `microservices-developer`
- Design enterprise iPaaS hubs, canonical models, B2B partner APIs, or API gateway programs only → `enterprise-integration-api-developer`
- Map X12/EDIFACT segments, AS2/VAN, or EDI partner certification → `edi-engineer`
- Build generic application features without event/messaging architecture → `senior-software-engineer`
- Operate classified air-gapped pipelines, ATO evidence, cleared promotion → `classified-software-devsecops-engineer`
- Formulate VRP, MIP, scheduling, or optimization solvers → `operations-research-algorithm-developer`
- CI/CD YAML, GitOps, and release automation only → `devops`
- Landing zone, VPC, and managed cloud provisioning → `cloud-engineer`

## Related skills

| Need | Skill |
|---|---|
| Service boundaries, gRPC/REST, circuit breakers, contract tests | `microservices-developer` |
| Enterprise integration hub, OpenAPI/AsyncAPI, iPaaS, B2B gateways | `enterprise-integration-api-developer` |
| EDI standards and partner file exchange | `edi-engineer` |
| Application code and refactoring without EDA focus | `senior-software-engineer` |
| Classified DevSecOps and artifact promotion | `classified-software-devsecops-engineer` |
| OR models, routing, allocation solvers | `operations-research-algorithm-developer` |
| Kafka/Rabbit operational platform (brokers, K8s) | `platform-engineer`, `devops` |
| Cross-system ADRs and NFR sign-off | `senior-system-architecture` |
| Pipeline security and supply chain | `devsecops` |

## Core Workflows

### 1. Scope and event boundaries

Define event types, producers/consumers, sync vs async boundaries, and non-goals.

**See `references/event_driven_architecture_scope.md`.**

### 2. Messaging and brokers

Select patterns, topics/queues, partitioning, and broker fit (Kafka, Pulsar, SNS/SQS, etc.).

**See `references/messaging_patterns_and_brokers.md`.**

### 3. Event sourcing and CQRS

When to use write models, projections, snapshots, and read-model consistency.

**See `references/event_sourcing_and_cqrs.md`.**

### 4. Reliability, idempotency, outbox

Delivery semantics, deduplication, outbox/inbox, and failure handling.

**See `references/reliability_idempotency_outbox.md`.**

### 5. Orchestration, choreography, sagas

Coordinate long-running flows without turning the bus into a distributed monolith.

**See `references/orchestration_choreography_sagas.md`.**

### 6. Schema governance and operations

Version events, operate DLQs, replay, and observability for event pipelines.

**See `references/schema_governance_operations.md`.**

## Outputs

- **Event catalog** — event name, schema version, producer, consumers, SLAs, PII classification
- **Context diagram** — services, topics/queues, sync fallbacks, trust zones
- **Consistency note** — outbox/saga/choreography choice with compensation and idempotency keys
- **Partitioning and ordering spec** — keys, guarantees, hot-partition risks
- **Schema compatibility matrix** — backward/forward rules, deprecation timeline
- **Operations runbook** — DLQ drain, replay procedure, lag alerts, poison-message handling

## Principles

- Prefer **explicit contracts** (schemas, AsyncAPI/CloudEvents metadata) over implicit JSON blobs
- Design consumers **idempotent by default**; treat exactly-once as a bounded, measured goal
- Keep **commands and events** distinct—events are facts; commands request work
- Avoid **chatty orchestration** over the bus; sagas compensate, they do not hide missing boundaries
- Make **failure observable**—correlation ID, structured errors, DLQ with actionable payloads
- **Replay is a product feature**—document ordering, side effects, and deduplication before reprocessing
