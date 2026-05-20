# Horizontal scaling and load distribution

## Table of contents

1. [Horizontal vs vertical scale](#horizontal-vs-vertical-scale)
2. [Stateless replicas](#stateless-replicas)
3. [Load balancing](#load-balancing)
4. [Sticky sessions and affinity](#sticky-sessions-and-affinity)
5. [Autoscaling](#autoscaling)
6. [Multi-region and CDN edge](#multi-region-and-cdn-edge)

## Horizontal vs vertical scale

| Approach | When it helps | Limits |
|---|---|---|
| **Vertical** | Quick win; single-node affinity; low ops churn | Hardware ceiling; blast radius |
| **Horizontal** | Linear capacity for stateless tiers; fault isolation | Coordination, data scale, cost step |

**Horizontal scaling** adds instances behind a load balancer. Requires **shared-nothing** app tier or externalized state.

## Stateless replicas

- Push session state to **Redis**, DB, or signed cookies (understand security/size limits)
- Externalize uploads to object storage; don’t rely on local disk
- Use **health checks** that reflect readiness (dependencies up), not only process alive
- **Graceful shutdown**: drain connections, stop accept, finish in-flight with deadline

## Load balancing

Placement options: hardware LB, cloud LB (ALB/NLB/GCLB), service mesh, client-side (gRPC xDS).

| Algorithm | Behavior | Notes |
|---|---|---|
| **Round robin** | Even rotation | Ignores load; fine for homogeneous work |
| **Least connections** | Send to fewest active | Better for long-lived connections |
| **Weighted** | Capacity-aware routing | Useful during rollouts or mixed instance sizes |
| **Consistent hash** | Sticky by key to backend | Reduces cache miss; resharding on membership change |
| **Latency-aware** | Pick faster backend | Needs telemetry; avoid oscillation |

**Load balancing** at L7 can route by path, header, or gRPC service name.

Enable **connection reuse** (HTTP/2, keep-alive) to reduce handshake overhead at high concurrency.

## Sticky sessions and affinity

**Sticky sessions** route the same client to the same backend (cookie, IP hash).

Pros: local cache warmth, legacy session in memory.

Cons: uneven load; painful deploys; lost stickiness on scale-in.

Prefer **state externalization** over stickiness when SLO and elasticity matter.

If affinity is required, use **consistent hashing** with bounded impact on node add/remove.

## Autoscaling

**Autoscaling** adjusts replica count (or serverless concurrency) from signals.

| Signal | Good for | Caveat |
|---|---|---|
| **CPU** | CPU-bound work | Misses I/O wait and latency |
| **RPS / requests in flight** | HTTP gateways | Needs stable per-instance capacity model |
| **Queue depth / lag** | Workers | Directly ties to backlog |
| **Custom metric** (p95 latency) | SLO-driven | Requires reliable telemetry pipeline |

Policies:

- **Scale-out fast, scale-in slow** — avoid flapping; protect cold instances
- **Min replicas > 0** for latency-sensitive paths; accept cost or use warm pools
- **Cold-start tradeoffs** — JVM/.NET warmup, serverless init; use provisioned concurrency or always-warm min
- **Predictive scale** — schedule ahead of known events (marketing, payroll)

Document **autoscaling** limits (max replicas, budget caps) in capacity plans.

## Multi-region and CDN edge

Architecture-level patterns (implementation → `cloud-engineer`):

- **Active-passive** — simpler consistency; failover RTO/RPO defined
- **Active-active** — lower latency globally; conflict resolution required
- **Read local, write global** — replicas per region; write routing to primary or CRDT/merge strategy
- **CDN** — cache static and cacheable API at edge; short TTL for semi-dynamic; purge APIs for incidents

Health-check **cross-region** dependencies; avoid circular failover. Measure **cross-region latency** on critical paths.
