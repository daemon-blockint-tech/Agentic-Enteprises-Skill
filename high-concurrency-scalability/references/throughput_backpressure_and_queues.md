# Throughput, backpressure, and queues

## Table of contents

1. [Throughput vs latency](#throughput-vs-latency)
2. [Backpressure fundamentals](#backpressure-fundamentals)
3. [Queueing patterns](#queueing-patterns)
4. [Rate limiting](#rate-limiting)
5. [Bulkheads and isolation](#bulkheads-and-isolation)
6. [Load shedding and degradation](#load-shedding-and-degradation)

## Throughput vs latency

- **Throughput** — work completed per unit time (RPS, messages/sec)
- **Latency** — time per unit of work (p50/p95/p99)
- Under load, queueing theory applies: as utilization → 100%, latency grows nonlinearly (Kingman-style behavior)
- Optimizing throughput alone can **inflate tails** if queues grow unbounded
- Define success as **both** SLO latency and sustainable throughput at peak factor

## Backpressure fundamentals

**Backpressure** signals upstream that downstream cannot accept more work yet.

Mechanisms:

| Layer | Example |
|---|---|
| **TCP / HTTP** | Window size, `429`, `503` with `Retry-After` |
| **Application** | Block on bounded channel; return “server busy” |
| **Message broker** | Consumer prefetch limits, nack/requeue with cap |
| **Database** | Pool acquire timeout, statement timeout |

**Without backpressure:** memory grows, GC thrashes, timeouts cascade, retries amplify load.

Implement backpressure **closest to the bottleneck** and propagate a consistent error contract to callers.

## Queueing patterns

| Pattern | Use when | Watch for |
|---|---|---|
| **Bounded in-memory queue** | Short bursts between stages in one process | OOM if consumer stalls |
| **External durable queue** | Decouple producers/consumers across deploys | Lag SLO, poison messages, ordering |
| **Priority queue** | Urgent work preempts bulk | Starvation of low priority |
| **Delay queue** | Scheduled retries, rate smoothing | Clock skew, duplicate delivery |

**Queue depth metrics:** depth, age (oldest message), consumer rate, DLQ rate.

Set **max depth** alerts before consumers are hours behind.

## Rate limiting

**Rate limiting** protects shared resources and enforces fairness.

Algorithms:

- **Token bucket** — smooth bursts with sustained cap
- **Leaky bucket** — constant outflow; stricter smoothing
- **Fixed/sliding window** — simple per-interval caps
- **Distributed counters** — Redis/sidecar; watch clock and failure modes

Dimensions: per **IP**, **API key**, **user**, **tenant**, **endpoint**, **downstream**.

Return `429` with `Retry-After`; prefer **reject fast** over slow timeout.

Combine with **admission control** at the edge (API gateway, service mesh).

## Bulkheads and isolation

**Bulkhead** — partition resources so one tenant or feature cannot exhaust shared pools.

Examples:

- Separate thread pools per dependency or tenant tier
- Dedicated connection pool for admin vs customer traffic
- Cell-based architecture (failure and load isolation by slice)

Pair bulkheads with **timeouts** on cross-bulkhead calls.

## Load shedding and degradation

When limits are hit, shed in **priority order**:

1. Non-critical features (recommendations, analytics beacons)
2. Expensive optional paths (full-text enrichments)
3. New requests while finishing in-flight critical work
4. Hard fail only when safety or consistency requires it

Document **degradation modes** in the scale brief; test them in game days.

Avoid **retry storms**: cap retries, use jitter, retry only on idempotent operations and specific error classes.
