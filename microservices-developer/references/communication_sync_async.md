# Communication: sync and async

## Table of contents

1. [When to use sync](#when-to-use-sync)
2. [When to use async](#when-to-use-async)
3. [Hybrid patterns](#hybrid-patterns)
4. [Gateway and mesh](#gateway-and-mesh)

## When to use sync

**HTTP/REST or gRPC** when the caller needs an immediate outcome or strong read-after-write.

| Use sync | Avoid sync when |
|---|---|
| User-facing query with low latency budget | Long-running work blocks thread pool |
| Validate-then-commit in one request | Chain of 4+ services on critical path |
| Small, stable contracts between two teams | Caller only needs notification later |

**Rules:**

- Set **end-to-end deadline** shorter than client timeout
- Propagate **correlation ID** and **trace context** on every hop
- Return **429/503** with `Retry-After` when overloaded; document retry safety

## When to use async

**Message bus, log, or outbox** when decoupling, buffering, or fan-out matters.

| Use async | Patterns |
|---|---|
| Notify many subscribers | Pub/sub topic |
| Work queue with competing consumers | Queue + DLQ |
| Guaranteed publish after DB commit | Transactional outbox |
| Cross-service workflow with compensations | Saga (choreography or orchestration) |

**Rules:**

- Design **idempotent consumers** (`event_id`, business key)
- Define **ordering** scope (partition key = aggregate id)
- Plan **poison message** handling—DLQ, replay tooling, alerts

## Hybrid patterns

| Pattern | Flow |
|---|---|
| Sync + async notification | API returns 202 or 200 with resource id; completion via event/webhook |
| CQRS | Commands via API; queries from read store or materialized view |
| API composition (BFF) | Edge aggregates multiple sync calls; avoid deep chains in core |
| Request–reply over messaging | Temporary reply queue; use only with strict timeouts |

**Choreography vs orchestration (sagas):**

- **Choreography** — each service reacts to events; fewer central failures; harder to debug
- **Orchestration** — coordinator drives steps; clearer state machine; coordinator is critical path

Pick orchestration when steps, timeouts, and compensation are complex.

## Gateway and mesh

| Layer | Responsibility |
|---|---|
| API gateway | AuthN/Z at edge, rate limits, routing, TLS termination, versioning |
| Service mesh | mTLS, retries (careful), traffic split, telemetry sidecars |
| BFF | Client-specific aggregation; not a second monolith |

Version APIs with **URL prefix** (`/v2/`) or **header** (`Accept-Version`); never break consumers without deprecation window.

For OpenAPI governance at enterprise scale → `enterprise-integration-api-developer`.
