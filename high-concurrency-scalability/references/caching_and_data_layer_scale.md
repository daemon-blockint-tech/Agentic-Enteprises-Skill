# Caching and data-layer scale

## Table of contents

1. [Cache hierarchy](#cache-hierarchy)
2. [Stampede and thundering herd](#stampede-and-thundering-herd)
3. [Invalidation strategies](#invalidation-strategies)
4. [Read replicas and routing](#read-replicas-and-routing)
5. [Sharding concepts](#sharding-concepts)
6. [Connection pool tuning](#connection-pool-tuning)
7. [Hot keys and skew](#hot-keys-and-skew)

## Cache hierarchy

Typical layers (closest to client first):

1. **CDN / edge** — static and cacheable API responses; respect `Cache-Control`
2. **Application local** — Caffeine, in-process LRU; watch memory and consistency
3. **Distributed cache** — Redis/Memcached; shared across instances
4. **Database buffer pool** — not a substitute for app cache design

**Cache-aside (lazy load):** App reads cache → on miss, load DB → populate cache. Simple; risk of stampede on miss.

**Read-through / write-through:** Cache library coordinates DB. Stronger consistency options; more coupling.

**Write-behind:** Fast writes to cache; async flush. High throughput; complex failure handling.

## Stampede and thundering herd

Mitigations when many clients miss the same key simultaneously:

| Technique | Mechanism |
|---|---|
| **Probabilistic early expiration** | Spread expiry (Jitter TTL) so keys don’t die together |
| **Single-flight / request coalescing** | One loader per key; others await same future |
| **Lock per key** | Mutex around recompute (use short timeout) |
| **Stale-while-revalidate** | Serve stale briefly while one worker refreshes |
| **Pre-warm** | Populate cache before TTL mass expiry or launch events |

For **caching stampede** incidents: log miss rate spikes, key cardinality, and loader latency; fix coalescing before adding cache memory.

## Invalidation strategies

- **TTL-only** — acceptable eventual staleness; simplest ops
- **Explicit delete** — on write path; risk missed invalidation bugs
- **Versioned keys** — `entity:{id}:v{ver}`; invalidate by bumping version
- **Pub/sub fan-out** — local cache purge on change events; handle delivery gaps
- **Tag-based purge** — invalidate groups (e.g., all keys for `tenant:42`)

Document **maximum staleness** product can tolerate per entity type.

## Read replicas and routing

- Route **read-only** queries to replicas; writes to primary
- Handle **replication lag** — “read your writes” may require primary stickiness or session tokens
- Use **connection pool per target** (primary vs replica); don’t share one pool blindly
- Monitor replica **lag seconds**; shed replica traffic when lag exceeds SLO
- **Read replica** scale helps read-heavy workloads; does not fix write hot spots

## Sharding concepts

- Choose **shard key** with high cardinality and even distribution (avoid monotonic insert hotspots where possible)
- **Consistent hashing** or directory service for routing; plan resharding early
- Cross-shard queries are expensive—design APIs to be **single-shard** when possible
- **Sharding** is not free: ops complexity, rebalancing, cross-shard transactions avoided or sagas

## Connection pool tuning

- Pool size ≈ `(expected_concurrent_requests × avg_query_time) / target_latency`—validate with load tests
- Too large pools **hurt** DB (context switch, lock contention on DB side)
- Set **acquire timeout**; fail fast rather than hang threads
- Recycle connections on **firewall idle timeout** mismatches
- Separate pools for **OLTP** vs **analytics** or long reports

## Hot keys and skew

Symptoms: one shard or replica at 100% while peers idle.

Mitigations:

- **Split hot key** into sub-keys (e.g., `counter:42:0..N` aggregate)
- **Local combine** — batch increments in app memory, flush periodically
- **Dedicated partition** for celebrity/tenant outliers
- **Rate limit per key** at edge to protect shared infrastructure
