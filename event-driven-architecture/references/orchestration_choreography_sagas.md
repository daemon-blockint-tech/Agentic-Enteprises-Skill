# Orchestration, choreography, and sagas

## Table of contents

1. [Choreography vs orchestration](#choreography-vs-orchestration)
2. [Saga pattern](#saga-pattern)
3. [Compensation](#compensation)
4. [State machines and timeouts](#state-machines-and-timeouts)
5. [Anti-patterns](#anti-patterns)

## Choreography vs orchestration

| Style | How it works | Pros | Cons |
|---|---|---|---|
| **Choreography** | Services react to events; no central coordinator | Loose coupling; simple flows | Hard to trace; implicit distributed state |
| **Orchestration** | Coordinator sends commands/steps | Visible workflow; easier debugging | Coordinator availability; can become god-service |

**Choose choreography when:**

- Few steps, clear event chain, each service owns compensation
- Flow rarely changes; observability via correlation id is enough

**Choose orchestration when:**

- Many steps, timeouts, human tasks, or conditional branches
- Need central view of saga state for support and audits
- **Saga orchestration** with explicit state machine (Temporal, Camunda, custom)

**Event choreography** is not “no design”—document the **expected event chain** and failure branches.

## Saga pattern

A **saga** is a sequence of local transactions coordinated by events or an orchestrator.

| Saga type | Coordination | Visibility |
|---|---|---|
| **Choreography-based** | Each service publishes/consumes events | Distributed logs + tracing |
| **Orchestration-based** | Orchestrator invokes participants | Central saga instance store |

**Rules:**

- Each step has a **compensating action** (semantic undo, not always DB rollback)
- Sagas are **long-running**—design for partial completion
- Never assume ACID across services; use **eventual consistency**

## Compensation

| Forward action | Compensation examples |
|---|---|
| Reserve inventory | Release reservation |
| Capture payment | Refund / void (idempotent) |
| Ship order | Cancel shipment request |
| Send email | Send correction (no true undo) |

Compensations are **business operations**, not generic rollbacks.

Document in saga spec:

- Which steps are **retryable** vs **non-retryable**
- **Pivot transaction** (point of no return) after which compensation changes
- Idempotency keys for compensate commands

## State machines and timeouts

**Orchestrator should track:**

- Current step, started_at, deadline
- Correlation id, business id (orderId)
- Failure reason and last compensating step attempted

**Timeouts:**

- Per-step SLA; escalate to human or compensating path
- Use **delay queues** or scheduler (not busy-loop polling topics)
- Distinguish **technical failure** (retry) vs **business rejection** (compensate)

**Observability:**

- Emit `SagaStarted`, `SagaStepCompleted`, `SagaFailed`, `SagaCompensated` integration events
- Trace span per step with same correlation id

## Anti-patterns

- **God topic** — every service listens to everything
- **Synchronous saga** — blocking HTTP chain labeled “async”
- **Missing compensation** — forward-only flows in money-moving domains
- **Orchestrator in the database** — stored procedures driving cross-service flow
- **Infinite retry** on business validation errors (poison without DLQ)

For enterprise hub-style orchestration (iPaaS), see `enterprise-integration-api-developer`.
