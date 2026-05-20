# Event-driven integration and reliability

## Table of contents

1. [Messaging patterns](#messaging-patterns)
2. [Outbox and transactional messaging](#outbox-and-transactional-messaging)
3. [Idempotency](#idempotency)
4. [Sagas and compensation](#sagas-and-compensation)
5. [Failure handling](#failure-handling)

## Messaging patterns

| Pattern | Description | Typical use |
|---|---|---|
| Pub/sub | Fan-out to many subscribers | Domain events, notifications |
| Queue | Competing consumers | Work distribution, load leveling |
| Request/reply | RPC over messaging | Rare; prefer sync API when simple |
| Event-carried state transfer | Full payload in event | Small entities; avoid chatty sync |
| Event notification | ID + type only | Large aggregates; consumers fetch |

Define **ordering** needs (per aggregate key), **retention**, and **dead-letter** policy up front.

## Outbox and transactional messaging

**Problem:** DB commit and message publish must not diverge.

**Outbox pattern:**

1. Business transaction writes domain row + outbox row in same DB transaction
2. Relay process publishes outbox rows to broker and marks published
3. Consumers process with idempotency

Alternatives: transactional outbox in same service; avoid dual-write without reconciliation.

## Idempotency

Every consumer at an integration boundary should support **at-least-once** delivery.

| Layer | Mechanism |
|---|---|
| HTTP | `Idempotency-Key` + store response by key TTL |
| Message | Dedupe on `messageId` or business key in idempotency store |
| DB | Unique constraints on natural keys |

Store idempotency records with TTL ≥ max redelivery window. Return same response on duplicate HTTP keys.

## Sagas and compensation

**Choreography:** services react to events; no central orchestrator. Fits autonomous domains; requires clear event contracts.

**Orchestration:** central coordinator issues commands and tracks state. Fits strict workflows and partner SLAs.

At pattern level:

- Define **compensating actions** (cancel reservation, reverse hold)—not only forward steps
- Use **timeouts** and **escalation** when a step does not complete
- Persist saga state for replay and operator visibility

Do not implement distributed 2PC across heterogeneous systems without strong operational justification.

## Failure handling

| Failure | Handling |
|---|---|
| Transient (network, throttle) | Retry with exponential backoff + jitter |
| Poison message | Max deliveries → DLQ; alert on DLQ depth |
| Schema mismatch | Reject to DLQ; block consumer version until fixed |
| Partial batch | Per-item error reporting; do not fail entire batch silently |

**Webhook reliability:** verify signatures, enforce timestamp skew, support replay protection (nonce or event ID store).

Operational playbooks → `references/operations_observability_and_lifecycle.md`.
