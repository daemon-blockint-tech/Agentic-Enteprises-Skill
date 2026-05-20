# Integration patterns and consistency

## Table of contents

1. [Pattern selection](#pattern-selection)
2. [Sync integration research](#sync-integration-research)
3. [Async and events research](#async-and-events-research)
4. [Consistency models](#consistency-models)
5. [Distributed workflows at research level](#distributed-workflows-at-research-level)
6. [Failure and UX semantics](#failure-and-ux-semantics)
7. [Anti-patterns](#anti-patterns)

## Pattern selection

| Need | Research recommendation | Deep dive peer |
|---|---|---|
| Immediate read-your-writes | Sync API; co-locate or single DB if justified | `senior-system-architecture` |
| Loose coupling, fan-out | Events + idempotent consumers | `event-driven-architecture` |
| Partner callbacks | Webhooks + signature + idempotency keys | `enterprise-integration-api-developer` |
| Bulk/historical sync | CDC, file drop, or batch API—not chatty CRUD | `data-architect` |
| Mobile/SPA aggregation | BFF per client class—not domain rules in BFF | `senior-software-engineer` |

Document **per journey** which pattern applies; avoid global "we are event-driven" without exceptions.

## Sync integration research

For REST/GraphQL/gRPC boundaries, research should specify:

- **Timeout budget** vs caller SLO (cascade failure analysis)
- **Idempotency** for retried mutations (keys, dedup store)
- **Versioning** and deprecation (see `api_contracts_and_evolution.md`)
- **Auth model** — mTLS, OAuth scopes, service identity
- **Circuit breaking** policy when dependency error rate spikes

**Choreography risk:** deep sync chains (A→B→C→D) on user path—research should quantify p99 latency sum and failure modes.

## Async and events research

At research level, define—not implement:

| Element | Research output |
|---|---|
| Event vs command | Which messages are facts vs requests |
| Delivery expectation | At-least-once default; ordering scope (partition key) |
| Ownership | Producer team owns schema; consumer lag SLO |
| Idempotency | Natural key or dedup strategy per consumer |
| Poison handling | DLQ + replay policy (hand off to `event-driven-architecture`) |

**Outbox/inbox:** recommend when business write and publish must not diverge; note operational cost.

## Consistency models

| Model | When to recommend | User-visible effect |
|---|---|---|
| **Strong (single transaction)** | Invariants inside one aggregate/service | Immediate consistency |
| **Read-your-writes (session stickiness)** | Same user, short window | No stale self-read |
| **Eventual** | Cross-context notification acceptable | Lag on reads; document SLO |
| **Causal** | Ordering matters per entity stream | Requires partition key design |

**Research rule:** state **maximum acceptable staleness** on read models (e.g., "catalog search ≤ 30s behind writes").

### Saga vs two-phase commit (2PC)

| Approach | Research when to favor | Risks |
|---|---|---|
| **2PC / XA** | Rare—homogeneous stack, short transactions, strong ops | Availability, lock contention, cloud-unfriendly |
| **Choreographed saga** | Few steps, clear compensations, mature event discipline | Hard to observe; implicit ordering |
| **Orchestrated saga** | Many steps, human tasks, need visibility | Orchestrator becomes coupling point |
| **Process manager + events** | Long-running business processes | State machine ownership |

**Default research stance:** prefer **saga with compensating actions** over 2PC across microservices; document **compensation UX** (what user sees on partial failure).

Do not specify framework code—reference `event-driven-architecture` for saga/outbox implementation patterns.

## Distributed workflows at research level

For each multi-step business process, deliver:

1. **Steps** — services involved, sync vs async per step
2. **Compensations** — reversible actions or manual intervention
3. **Terminal states** — success, failed, pending, needs-ops
4. **Idempotency keys** — per step correlation
5. **Observability** — correlation ID across boundaries

## Failure and UX semantics

Research must answer for partial failure:

- Can user **retry** safely?
- Is state **visible** (pending payment, order processing)?
- Who **reconciles** orphaned events (ops playbook outline)?

## Anti-patterns

- **Distributed monolith** — independent deploy labels but shared DB and library coupling
- **Events without schema policy** — implicit JSON contracts
- **Sync mesh** — N×M point-to-point without gateway or events
- **2PC by default** — locks across services for convenience
- **Saga without compensation design** — "rollback" undefined for human steps
