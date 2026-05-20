# Concurrency models and synchronization

## Table of contents

1. [Model selection](#model-selection)
2. [Threads and thread pools](#threads-and-thread-pools)
3. [Async and coroutines](#async-and-coroutines)
4. [Actors and message passing](#actors-and-message-passing)
5. [Locks, contention, and lock-free patterns](#locks-contention-and-lock-free-patterns)
6. [Resource limits](#resource-limits)

## Model selection

| Model | Strengths | Risks | Typical fit |
|---|---|---|---|
| **OS threads + pool** | Simple blocking I/O; CPU-bound pools | Context switch cost; pool exhaustion | Blocking SDKs, moderate concurrency |
| **Async/await** | High connection count; low thread count | Blocking call in async path; debug complexity | I/O-bound gateways, HTTP fan-out |
| **Green threads / coroutines** | Lightweight tasks (language/runtime specific) | Runtime quirks; FFI blocking | High fan-in event loops |
| **Actors** | Isolated state; natural backpressure per mailbox | Routing; distributed actor overhead | Stateful partitions, game/session shards |
| **Processes** | Hard isolation; crash containment | IPC cost; heavier scale | Untrusted workloads, CPU isolation |

**Rule:** Match the model to the dominant wait type (I/O vs CPU) and team operability—not fashion.

## Threads and thread pools

- Size pools from **measured** queue wait and dependency latency, not `cores × constant` alone
- Separate pools for **CPU-bound** vs **blocking I/O** work to avoid starvation
- Use **bounded** submit queues; reject or shed when saturated (`CallerRuns` is often a latency trap)
- Avoid unbounded `new Thread per request`; cap in-flight work at the edge
- For servlet-style stacks: align **accept queue**, **worker pool**, and **downstream pool** limits

## Async and coroutines

- Never call **blocking** APIs on the event loop without a dedicated executor bridge
- Limit **in-flight** async operations per request and globally (semaphores)
- Propagate **cancellation** and timeouts through the async tree
- Watch **head-of-line blocking** on single-loop designs; consider sharded loops or processes
- For **async scalability**: scale out replicas; each instance still has one loop’s constraints

## Actors and message passing

- One actor owns mutable state; communicate via **immutable messages**
- Mailbox depth is implicit queue—monitor and apply **backpressure** (drop, shed, or slow producers)
- Partition by **stable key** (user_id, session_id) for locality and even load
- Supervision: define restart vs escalate policy for poison messages

## Locks, contention, and lock-free patterns

**Reduce contention:**

- Shrink critical sections; prefer **read-copy-update** or per-shard locks
- **Partition data** so hot paths rarely share locks (striped counters, per-bucket maps)
- Use **lock ordering** discipline to prevent deadlocks when multiple locks are unavoidable

**Lock-free / low-lock (use carefully):**

- Atomic counters and compare-and-swap for stats and id generation
- **Ring buffers** for single-producer/single-consumer paths
- Verify **ABA** and memory-order semantics; test under ARM weak memory

**When locks are fine:** Low contention, short sections, clear invariants—simplicity beats exotic structures.

## Resource limits

| Resource | What to bound | Observability |
|---|---|---|
| Threads | Pool max, async executor size | Pool active/queued, task wait time |
| Connections | DB/HTTP pool max per host | Pool borrowed count, acquire timeout |
| File descriptors | ulimit vs expected connections | Open FD metrics |
| Memory | Per-request buffers, aggregate cache | Heap, GC pause, OOM kills |
| Goroutines / tasks | Semaphore on spawn | Scheduler lag, runnable queue |

Document limits in runbooks; alert on **sustained** pool wait before exhaustion.
