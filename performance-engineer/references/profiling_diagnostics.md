# Profiling and diagnostics

## Table of contents

1. [Triage checklist](#triage-checklist)
2. [CPU profiling](#cpu-profiling)
3. [Memory and leaks](#memory-and-leaks)
4. [I/O and blocking](#io-and-blocking)
5. [Concurrency](#concurrency)

## Triage checklist

| Symptom | First checks |
|---|---|
| High p99, normal p50 | Tail dependency, lock, GC pause, cold path |
| Throughput collapse | Thread pool, DB pool, rate limits, backpressure |
| CPU pegged | Hot loop, regex, serialization, compression |
| Memory growth | Leak, unbounded cache, large payloads |
| Disk wait | Logs, fsync, local DB, temp files |
| External slowness | DNS, TLS, third-party API, geo |

Capture **request ID**, **release version**, **traffic mix**, and **data volume** before profiling.

## CPU profiling

- Sample at steady state under **representative load**, not idle
- Prefer **wall-clock + CPU** profiles when I/O-bound
- Compare profiles **before/after** change on same machine class
- Attribute cost to **frames you own** vs libraries vs runtime

Document: profiler tool, duration, sample rate, build flags (debug symbols).

## Memory and leaks

- Heap dumps or allocation profiles at peak and after GC
- Track **RSS vs heap**, off-heap (Netty, mmap), container limits
- Watch for **retained collections**, session caches, global singletons
- Validate **object churn** driving GC pressure

For leaks: reproduce with soak test; bisect release; fix and verify with 2× soak duration.

## I/O and blocking

- Trace **syscall wait** vs application time
- Check connection pool **wait time** metrics
- N+1 queries and synchronous fan-out show as wide span trees
- Large payloads: compression, pagination, streaming

## Concurrency

- Lock profiling: mutex, RW lock, channel blocking
- Thread/goroutine pool exhaustion
- Unbounded parallelism amplifying downstream load
- Coordinated omission in benchmarks — use open-loop with care

Pair with `latency_slo_budgets.md` for queueing theory context (Little's law: L = λW).
