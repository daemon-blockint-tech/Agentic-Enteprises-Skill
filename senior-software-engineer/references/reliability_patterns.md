# Reliability patterns

## Table of contents

1. [Outbound calls](#outbound-calls)
2. [Idempotency](#idempotency)
3. [Queues and events](#queues-and-events)
4. [Performance](#performance)

## Outbound calls

```text
timeout → retry (idempotent only) → circuit open → fallback or fail fast
```

Set timeouts < client deadline; propagate cancellation tokens.

## Idempotency

- Accept `Idempotency-Key` on creates
- Store key → result mapping with TTL
- Consumers process messages at-least-once; dedupe by event ID

## Queues and events

- Outbox pattern for DB + publish atomicity
- Poison queue after N failures; alert
- Schema versioning for events (additive fields)

## Performance

1. Trace slow request end-to-end
2. DB: EXPLAIN, indexes, batch queries
3. App: allocation hotspots, unnecessary serialization
4. Cache only with measured hit rate and invalidation plan
