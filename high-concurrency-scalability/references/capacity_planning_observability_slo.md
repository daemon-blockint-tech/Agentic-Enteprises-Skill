# Capacity planning, observability, and SLO-driven scale

## Table of contents

1. [Capacity planning process](#capacity-planning-process)
2. [Headroom and growth models](#headroom-and-growth-models)
3. [Profiling and bottleneck analysis](#profiling-and-bottleneck-analysis)
4. [Observability for scale](#observability-for-scale)
5. [SLO-driven scaling](#slo-driven-scaling)
6. [Game days and validation](#game-days-and-validation)

## Capacity planning process

1. **Baseline** current peak (RPS, concurrent users, messages/sec) with seasonality
2. **Model** per-tier capacity (RPS per instance at target p99)
3. **Apply growth** — marketing events, tenant onboarding, compound monthly growth
4. **Add headroom** — typically 30–50% below saturation for unexpected bursts
5. **Price tradeoffs** — replica count vs larger instances vs cache spend
6. **Document triggers** — when to scale manually vs autoscale vs procure capacity

**Capacity planning** outputs: instance count ranges, DB size/IOPS, cache memory, network egress, runbook thresholds.

## Headroom and growth models

Simple model:

```
required_instances = ceil(peak_rps / rps_per_instance_at_slo) × burst_factor
```

Refine with:

- **Burst factor** — flash sale multiplier over steady peak
- **Efficiency loss** — deploys, noisy neighbors, retry traffic
- **Dependency ceilings** — DB connections, partner rate limits

Track **utilization** at the constraining resource (not average CPU across idle cores).

## Profiling and bottleneck analysis

Order of investigation for throughput collapse:

1. **Saturation** — CPU, memory, disk I/O, network, FDs, thread pools
2. **Queueing** — pool acquire wait, broker lag, servlet queue
3. **Lock contention** — mutex wait, DB row locks, hot keys
4. **Algorithmic** — O(n²) paths, N+1 queries, serialization overhead
5. **External** — slowest dependency on critical path

Use traces to find **critical path**; use profiles for **hot functions**.

Deep tool ownership → `performance-engineer`; this skill frames **what to measure** and **architectural fixes**.

## Observability for scale

| Signal | Indicates |
|---|---|
| Request rate, error rate, duration (RED) | Service health |
| Pool active / pending / timeout | Connection starvation |
| Queue depth, oldest age | Consumer lag |
| Cache hit ratio, evictions | Cache effectiveness |
| DB replication lag | Stale read risk |
| GC pause, heap | Memory pressure |
| SYN backlog, accept queue drops | Edge overload |

**USE method** for resources: Utilization, Saturation, Errors.

Correlate deploys with metric shifts; keep **synthetic probes** for edge-to-origin path.

## SLO-driven scaling

Define SLIs (latency, availability, freshness) and SLO targets.

- Tie **autoscaling** to SLI burn (error budget consumption), not vanity metrics
- **Scale policies** should cite which SLO is protected (e.g., checkout p99 < 300ms)
- **Error budget** policy: when budget is low, freeze risky changes; favor stability over new capacity experiments

| Burn signal | Action |
|---|---|
| Elevated p99 with flat CPU | Scale may not help—fix queueing, DB, or cache |
| Rising 5xx with pool timeouts | Scale out **and** reduce per-instance pool or add DB capacity |
| Lagging consumers | Scale workers or reduce publish rate (backpressure) |

Program-level SLO governance → `site-reliability-engineer`.

## Game days and validation

Before production peaks:

- **Load test** to declared peak × burst factor (harness detail → `performance-engineer`)
- Validate **autoscaling** lag and cold-start impact on p99
- Exercise **degradation** and shedding paths
- Fail a zone or replica—confirm LB health checks and traffic shift
- Run **cache expiry** drill with stampede protections enabled

Record results in the capacity plan; update `rps_per_instance` constants quarterly.
