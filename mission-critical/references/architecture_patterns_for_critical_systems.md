# Architecture patterns for critical systems

## Table of contents

1. [Pattern selection](#pattern-selection)
2. [Redundancy and active-active](#redundancy-and-active-active)
3. [Geographic and zone isolation](#geographic-and-zone-isolation)
4. [Determinism and overload behavior](#determinism-and-overload-behavior)
5. [Fail-safe, fail-closed, degradation](#fail-safe-fail-closed-degradation)
6. [Control plane vs data plane](#control-plane-vs-data-plane)
7. [Anti-patterns](#anti-patterns)

## Pattern selection

Choose patterns from **tier**, **failure modes**, and **integrity class**:

| Need | Pattern direction |
|---|---|
| Survive AZ/region loss | N+1 capacity, active-active or warm standby, geo DNS/traffic management |
| Survive operator error | Immutable deploy artifacts, config validation, progressive rollout |
| Survive dependency outage | Timeouts, bulkheads, circuit breakers, cached read models |
| Survive corruption | Append-only event log, point-in-time recovery, out-of-band verification |
| Survive overload | Admission control, fair queuing, shed load by tier |

Document decisions in ADRs; pair `senior-system-architecture` for general NFR templates.

## Redundancy and active-active

| Pattern | When | Caveats |
|---|---|---|
| **Active-passive** | RTO allows failover time; simpler consistency | Test failover; avoid stale secondary |
| **Active-active** | Low RTO; horizontal scale | Split-brain, write conflicts, clock skew |
| **N+1 / M-of-N** | Capacity + failure tolerance | Shared fate in one cluster |
| **Quorum systems** | Strong consistency requirements | Latency; operator complexity |

**Mission-critical default:** prefer **proven failover** over theoretical multi-master unless conflict resolution is specified and tested.

## Geographic and zone isolation

- **Failure domains** — account, region, AZ, cluster, rack; map on blast-radius diagram
- **Traffic steering** — health-based routing; avoid flapping during partial degradation
- **Data residency** — sovereignty constraints as hard requirements (generic regulatory framing)
- **Clocks and ordering** — use logical clocks or external coordination where wall-clock unsafe

Pair `cloud-engineer` for regional placement; you own **tier fit** and **continuity proof**.

## Determinism and overload behavior

Tier 0/1 systems should behave **predictably under stress**:

| Technique | Purpose |
|---|---|
| **Fixed thread pools / bounded queues** | Prevent retry storms |
| **Idempotent handlers** | Safe replay after partial failure |
| **Explicit state machines** | Reject illegal transitions |
| **Resource budgets per tenant** | Fairness; contain noisy neighbor |
| **Load shedding** | Drop or defer **non-critical** work first |

Avoid “best effort” background jobs on Tier 0 paths without isolation.

## Fail-safe, fail-closed, degradation

Align with `zero-tolerance-for-failure`:

| Mode | Default for Tier 0/1 |
|---|---|
| **Auth / authZ ambiguous** | Deny |
| **Safety interlock** | Safe physical/logical state |
| **Partial data** | Fail transaction; do not guess |
| **Degraded read** | Only if explicitly designed and labeled to users |

Define **degradation levels** (L0 full → L3 minimal) with customer-visible behavior and rollback triggers.

## Control plane vs data plane

| Plane | Tiering guidance |
|---|---|
| **Data plane** | User/mission traffic; highest redundancy |
| **Control plane** | Provisioning, identity, DNS, K8s API—often **shared fate**; tier as Tier 0 if many dependents |
| **Management / CI** | Compromise = widespread blast radius; isolate and harden |

Never assume “internal only” control planes are low tier if Tier 0 services depend on them.

## Anti-patterns

- **Stretch cluster across regions** without split-brain design
- **Shared database** for unrelated Tier 0 domains
- **Silent fail-open** on auth or validation for availability
- **Chaos in production** without tier approval and rollback (`site-reliability-engineer` coordinates)
- **Undocumented manual runbooks** as the only failover path
