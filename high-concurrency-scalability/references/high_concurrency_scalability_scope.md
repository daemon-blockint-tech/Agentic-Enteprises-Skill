# High concurrency and scalability scope

## Table of contents

1. [Role focus](#role-focus)
2. [Typical deliverables](#typical-deliverables)
3. [Workload dimensions](#workload-dimensions)
4. [Decision boundaries](#decision-boundaries)
5. [Anti-patterns](#anti-patterns)

## Role focus

| In scope | Out of scope (peer skills) |
|---|---|
| Concurrency models, pools, lock contention, partitioning | Service boundary decomposition → `microservices-developer` |
| Caching, stampede control, read replicas, sharding concepts | Event broker topology and schema governance → `event-driven-architecture` |
| Backpressure, queues, rate limits, bulkheads | Flame graphs and load-test harness ownership → `performance-engineer` |
| Horizontal scale, LB, autoscaling triggers | Org SLO/error-budget program → `site-reliability-engineer` |
| Capacity models tied to throughput and tail latency | K8s platform product and golden paths → `platform-engineer` |
| Multi-region read/CDN architecture (design level) | VPC/IaC and managed service build → `cloud-engineer` |
| Connection pool and FD tuning | FinOps unit economics only → `cloud-economist` |

## Typical deliverables

- Traffic and concurrency profile (RPS, burst factor, fan-out, payload size)
- Bottleneck assessment with evidence (profile, queue depth, pool wait)
- Concurrency architecture note (threads vs async vs actors; partition keys)
- Cache hierarchy diagram with TTL, invalidation, and stampede controls
- Data-scale plan (replicas, routing, shard keys, hot-key mitigations)
- Overload playbook (rate limits, shedding order, bulkhead map)
- Autoscaling policy draft (metrics, thresholds, min/max, warm pool)
- Capacity spreadsheet or headroom model with growth scenarios

## Workload dimensions

Capture these before recommending scale patterns:

| Dimension | Questions |
|---|---|
| **Arrival pattern** | Steady, diurnal, flash crowd; sync vs async consumers |
| **Request shape** | Read-heavy vs write-heavy; idempotent vs transactional |
| **Latency SLO** | p50/p95/p99 targets; acceptable degradation under load |
| **State** | Session sticky vs stateless; where authoritative state lives |
| **Dependencies** | Fan-out count; slowest downstream on critical path |
| **Data hotness** | Skewed keys; cacheable vs always-fresh reads |
| **Failure tolerance** | Shedding vs hard fail; partial availability acceptable? |

## Decision boundaries

**Invest in horizontal scale when:**

- Work is embarrassingly parallel or partitionable by key
- Single-node CPU/memory/network saturates before SLO is met
- Stateless tiers can scale behind a load balancer
- Data tier supports read scale-out or shard routing

**Prefer vertical scale or optimization first when:**

- Strong single-node affinity (large in-memory working set)
- Cross-shard transactions dominate and cannot be redesigned
- Coordination overhead of many small instances exceeds benefit
- Profiling shows algorithmic or query inefficiency—not saturation

**Add async queues when:**

- Producers can outpace consumers temporarily
- Work can be processed with acceptable lag (clear lag SLO)
- Backpressure at the edge protects synchronous path

## Anti-patterns

- **Unbounded resources**—threads, connections, or queues with no ceiling
- **Scale without measure**—more replicas while pool wait or lock time dominates
- **Cache as database**—no invalidation story; stale reads violate product rules
- **Retry amplification**—retries on overloaded dependencies without jitter or caps
- **CPU-only autoscaling**—ignores latency, errors, or queue depth until users suffer
- **Shared mutable hot row**—all writers on one key regardless of “microservices”
- **Thundering herd**—mass expiry or deploy cold cache with no coalescing
