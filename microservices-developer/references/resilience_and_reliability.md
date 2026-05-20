# Resilience and reliability

## Table of contents

1. [Timeouts and deadlines](#timeouts-and-deadlines)
2. [Retries](#retries)
3. [Circuit breakers and bulkheads](#circuit-breakers-and-bulkheads)
4. [Load shedding and fallbacks](#load-shedding-and-fallbacks)

## Timeouts and deadlines

| Layer | Practice |
|---|---|
| Client | Timeout &lt; user-facing SLA; include connect + read |
| Server | Honor upstream `Deadline` / `grpc-timeout` |
| Pool | Align pool wait with service timeout |

**Never** use infinite waits. Document per-dependency budgets in a table:

```
Dependency | p99 latency | Timeout | Notes
-----------|-------------|---------|------
payments   | 120ms       | 300ms   | retry idempotent GET only
inventory  | 80ms        | 200ms   | breaker after 50% errors
```

## Retries

Retry only when:

- Operation is **idempotent** (safe key, dedup store, or read)
- Failure is **transient** (timeouts, connection reset, 503, gRPC UNAVAILABLE)

| Setting | Guidance |
|---|---|
| Max attempts | 2–3 for sync paths; more only on async workers |
| Backoff | Exponential + **full jitter** |
| Retry-After | Respect on 429/503 when present |

**Do not retry:** 4xx business errors, validation failures, or when breaker is open.

## Circuit breakers and bulkheads

**Circuit breaker** states: closed → open (fail fast) → half-open (probe).

- Open after error rate or consecutive failures exceed threshold
- Half-open allows limited probes before closing again

**Bulkhead** isolates resources:

- Separate thread pools / connection pools per dependency
- Queue depth limits; reject early under pressure

**Bulkhead + breaker** prevent one slow dependency from starving the service.

## Load shedding and fallbacks

| Technique | Use |
|---|---|
| Rate limiting | Protect service and downstreams (token bucket at gateway and service) |
| Concurrency limits | Cap in-flight requests per tenant or route |
| Shed load | Return 503 when queue full; prioritize critical routes |
| Cached fallback | Stale read for non-critical data; mark degraded in response |
| Feature flag off | Disable optional path when dependency unhealthy |

Log **degraded mode** with metric `degraded=true` for SRE visibility.

Reliability program ownership (SLO burn, PRR) → `site-reliability-engineer`.
