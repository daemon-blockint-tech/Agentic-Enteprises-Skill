# Event-driven architecture scope

## Table of contents

1. [Role focus](#role-focus)
2. [Event taxonomy](#event-taxonomy)
3. [Typical deliverables](#typical-deliverables)
4. [Decision boundaries](#decision-boundaries)
5. [Anti-patterns](#anti-patterns)

## Role focus

| In scope | Out of scope (peer skills) |
|---|---|
| Event contracts, brokers, delivery semantics, EDA patterns | Microservice API/code implementation → `microservices-developer` |
| Event sourcing, CQRS, outbox, sagas at architecture level | Enterprise iPaaS hub, canonical enterprise model → `enterprise-integration-api-developer` |
| Schema versioning, DLQ, replay, stream vs discrete events | EDI X12/EDIFACT, AS2/VAN → `edi-engineer` |
| Partitioning, ordering, idempotency design | Generic CRUD/features → `senior-software-engineer` |
| Choreography vs orchestration tradeoffs | Classified promotion, ATO → `classified-software-devsecops-engineer` |
| Integration across service boundaries | VRP/MIP/solver formulation → `operations-research-algorithm-developer` |

## Event taxonomy

| Type | Definition | Examples |
|---|---|---|
| **Domain event** | Fact inside a bounded context; name in ubiquitous language | `OrderPlaced`, `PaymentCaptured` |
| **Integration event** | Cross-context notification; may map from domain events | `order.placed.v1` on shared topic |
| **Command** | Request to perform work; single logical handler | `ReserveInventory` (queue or RPC) |
| **Notification** | Lightweight signal; consumers fetch details if needed | `CatalogChanged` with entity id only |

**Rules:**

- Events are **immutable facts** (past tense); commands are **intent** (imperative).
- Do not publish **large payloads** when an id + schema version suffices.
- Classify **PII/regulated** fields in the catalog; avoid broadcasting secrets.

## Typical deliverables

- Event catalog (name, version, owner, schema registry id, retention)
- Producer/consumer matrix with delivery expectation and idempotency key
- Sequence diagrams for critical flows (happy path + compensation)
- ADR: sync vs async, broker choice, choreography vs orchestration
- Non-functional table: throughput, lag SLO, ordering needs, replay policy

## Decision boundaries

**Prefer event-driven integration when:**

- Multiple subscribers need the same fact without tight coupling
- Peak load must be absorbed (buffering) or systems have different availability
- Audit trail and temporal queries benefit from append-only history
- Teams can own schemas and evolve consumers independently

**Prefer sync (RPC/REST) when:**

- Strong immediate consistency required on user-facing path
- Simple request/response with one consumer and low latency budget
- Operation is a query with no side effect to broadcast

**Prefer event sourcing when:**

- Complete history is a product requirement (finance, compliance, dispute)
- Temporal queries and rebuild-from-history are common
- Team can invest in projections, snapshots, and operational complexity

## Anti-patterns

- **Event notification as integration database** — giant payloads replicated everywhere
- **Distributed monolith via events** — all services must deploy together for schema changes
- **Missing ownership** — no team owns topic schema or consumer lag
- **Fire-and-forget without DLQ** — poison messages block partitions indefinitely
- **Synchronous chains disguised as events** — request-reply over topics without timeouts
