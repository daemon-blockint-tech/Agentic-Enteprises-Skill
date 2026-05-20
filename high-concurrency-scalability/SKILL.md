---
name: high-concurrency-scalability
description: |
  Design and optimize systems for high concurrency, throughput, scalability, and elastic scale—concurrency models (threads, async/await, actors), lock-free patterns, connection pooling, caching stampede mitigation, horizontal scaling, load balancing, backpressure, queueing, rate limiting, bulkheads, read replicas, sharding, pool tuning, profiling, capacity planning, SLO-driven autoscaling, multi-region and CDN edge architecture. Use when the user asks about high concurrency, scalability, throughput, horizontal scaling, connection pooling, backpressure, rate limiting, caching stampede, read replica, sharding, autoscaling, capacity planning, lock contention, async scalability, or load balancing—not service decomposition (microservices-developer), event buses only (event-driven-architecture), generic CRUD (senior-software-engineer), SRE on-call only (site-reliability-engineer), load tests without architecture (performance-engineer), or cost-only FinOps (cloud-economist).
---

# High Concurrency & Scalability

## When to Use

- Choose or refactor **concurrency models**—threads, async/await, actors, coroutines—for target throughput and latency
- Reduce **lock contention** and design low-contention, lock-free, or partitioned data paths
- Size **connection pools**, file descriptors, thread pools, and memory limits per dependency
- Design **caching** layers, TTL strategy, and **stampede** / thundering-herd mitigation
- Plan **horizontal scaling**, **load balancing**, session affinity, and stateless vs sticky tradeoffs
- Apply **backpressure**, bounded queues, **rate limiting**, and bulkheads under overload
- Scale the **data layer**—read replicas, routing, sharding concepts, pool tuning, hot keys
- Profile bottlenecks, model **capacity**, and tie scale triggers to **SLOs** and error budgets
- Define **autoscaling** signals, warm pools, and cold-start vs cost tradeoffs
- Architect **multi-region** read paths and CDN/edge caching at a design level

## When NOT to Use

- Decompose monoliths into bounded contexts and inter-service contracts only → `microservices-developer`
- Event schemas, broker selection, and messaging topology only → `event-driven-architecture`
- General feature delivery, RFCs, or CRUD without scale focus → `senior-software-engineer`
- Org-wide SLO program, on-call, incident response, and error-budget policy → `site-reliability-engineer`
- Deep flame graphs, load-test harnesses, and p99 regression hunts as the main task → `performance-engineer`
- Kubernetes platform golden paths and IDP product work → `platform-engineer`
- VPC, managed service provisioning, and landing-zone IaC → `cloud-engineer`
- Cloud spend optimization and unit economics only → `cloud-economist`, `finops-analyst`

## Related skills

| Need | Skill |
|---|---|
| Service boundaries, sagas, circuit breakers between services | `microservices-developer` |
| Brokers, topics, event contracts, outbox | `event-driven-architecture` |
| Profiling, load/soak tests, latency budgets | `performance-engineer` |
| SLI/SLO programs, incident reliability, toil | `site-reliability-engineer` |
| Internal platform, K8s abstractions, golden paths | `platform-engineer` |
| Cloud compute, networking, DR multi-region deploy | `cloud-engineer` |
| Application design and refactoring | `senior-software-engineer` |

## Core Workflows

### 1. Scope and constraints

Clarify traffic shape, SLOs, statefulness, and failure modes.

**See `references/high_concurrency_scalability_scope.md`.**

### 2. Concurrency and synchronization

Pick execution model; partition work; minimize shared mutable state.

**See `references/concurrency_models_and_synchronization.md`.**

### 3. Caching and data-layer scale

Cache hierarchy, replica routing, sharding and hot-key mitigation.

**See `references/caching_and_data_layer_scale.md`.**

### 4. Throughput, backpressure, and queues

Bounded queues, shedding, rate limits, and async pipelines.

**See `references/throughput_backpressure_and_queues.md`.**

### 5. Horizontal scale and load distribution

Replicas, LB algorithms, affinity, autoscaling triggers.

**See `references/horizontal_scaling_and_load_distribution.md`.**

### 6. Capacity, observability, and SLO-driven scale

Metrics, headroom models, scale policies tied to objectives.

**See `references/capacity_planning_observability_slo.md`.**

## Outputs

- **Scale brief** — workload profile, bottlenecks, target RPS/latency, state assumptions
- **Concurrency note** — model choice, pool sizes, contention risks, partitioning plan
- **Cache and data plan** — layers, TTL, invalidation, replica/shard routing, hot-key mitigations
- **Overload matrix** — backpressure, rate limits, bulkheads, degradation modes
- **Capacity model** — headroom, scale triggers, cold-start impact, cost sensitivity
- **Observability checklist** — saturation, queue depth, pool wait, cache hit rate, tail latency

## Principles

- **Measure saturation**—CPU, memory, I/O, pool wait, queue depth—not averages alone
- **Bound everything**—connections, threads, queue length, in-flight requests
- **Prefer partition over lock**—shard by key, actor mailbox, or isolated replica
- **Design for overload**—shed load deliberately; never unbounded retry or queue growth
- **Scale on SLO signals**—error rate and tail latency, not CPU alone
- **Keep hot paths stateless** where possible; isolate stateful tiers explicitly
