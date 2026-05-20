# Deployment, cost, and governance

## Table of contents

1. [Runtime deployment modes](#runtime-deployment-modes)
2. [Queues and durable workflows](#queues-and-durable-workflows)
3. [Scaling and isolation](#scaling-and-isolation)
4. [Cost and token budgets](#cost-and-token-budgets)
5. [Governance and release](#governance-and-release)
6. [Framework mapping (high level)](#framework-mapping-high-level)

## Runtime deployment modes

| Mode | Latency | Duration | When |
|---|---|---|---|
| **Sync API** | Low | Seconds | Small DAG, interactive UI |
| **Async API + poll** | Medium | Minutes | User can wait; avoid holding HTTP |
| **Task queue** | Medium | Minutes–hours | Bursty load, worker pool |
| **Durable workflow engine** | Medium | Hours–days | Long-running, must survive restarts |
| **Scheduled / batch** | N/A | Batch | Periodic reports |

**Rule:** match orchestration engine to **workflow lifetime**, not individual LLM call latency.

## Queues and durable workflows

### Message queue pattern

```
API → enqueue(workflow_start) → workers consume node tasks → state store
```

**Properties:**

- Visibility timeout > p99 node duration
- Dead-letter queue (DLQ) for poison messages
- Poison handling: alert, quarantine, do not infinite redrive

### Durable workflow pattern

Engine persists **workflow state** and replays from last checkpoint on crash.

**Use when:**

- Human gates may wait hours
- Fan-out with many branches
- Legal/audit need of execution history

**Design:**

- Activities (side effects) separated from orchestration logic
- Activities must be idempotent
- Version workflow definitions; pin running instances to version

### Comparison

| Concern | Queue + custom | Durable engine |
|---|---|---|
| Operational maturity | You own state machine | Engine owns replay |
| Flexibility | High | Constrained to engine model |
| Debugging | Harder distributed traces | Built-in history often |
| Cost | Infra + eng time | License + simpler code |

## Scaling and isolation

| Knob | Guidance |
|---|---|
| **Worker pool per role** | Scale research workers independently of writers |
| **Concurrency cap** | Per-tenant and global limits |
| **Model pool** | Route cheap tasks to small models |
| **Noisy neighbor** | Fair queue per tenant |
| **Sandbox** | Separate tool credentials per environment |

**Multi-tenancy:** enforce `tenant_id` on every enqueue and state read; never share blackboards across tenants.

**Blue/green:** deploy new `graph_version` alongside old; route fraction of traffic for canary.

## Cost and token budgets

### Budget hierarchy

```
org_budget
  └── workflow_run_budget
        └── per_node_budget
              └── per_agent_call_budget
```

**Enforcement points:**

- Router refuses expensive subgraph if remaining budget low
- Supervisor stops fan-out when projected cost exceeds cap
- Hard kill switch when global org burn rate spikes

### Attribution

Record per span: model, tokens, tool API cost, wall time.

Roll up to: **cost per successful workflow**, **cost per agent role**, **cost per tenant**.

### Optimization (system level)

| Technique | Effect |
|---|---|
| Route to smaller model first | Lower average cost |
| Cache retrieval across workers | Dedup fan-out fetches |
| Speculative fan-out only when needed | Reduce parallel LLM calls |
| Merge early | Fewer tokens in downstream agents |
| Batch similar work orders | Amortize overhead |

Coordinate with `ai-context-engineer` for per-call packing; this skill owns **fleet-level** caps.

## Governance and release

### Configuration registry

Version and audit:

- Graph topology definition
- Agent role → prompt + model + tool allowlist
- Routing rules and feature flags
- Message schema versions

### Release process

1. Contract tests + golden DAG pass in CI
2. Canary on % traffic with compare metrics
3. Full rollout with rollback pin to previous `graph_version`
4. Post-release: cost and success rate review at 24h

### Policy alignment

Engage `ai-risk-governance` for:

- Required HITL gates by risk tier
- Data residency and cross-border agent calls
- Logging retention for inter-agent messages
- Prohibited tool combinations across roles

### Access control

- Which teams may publish new agent cards or graph versions
- Separation: **operators** scale workers; **developers** change graphs; **security** approves tool allowlists

## Framework mapping (high level)

Framework-agnostic contracts first; map concepts as follows:

| Concept | LangGraph-style | Deep Agents-style | agenthub-style |
|---|---|---|---|
| DAG nodes | Graph nodes / Send | Subagent tasks | DAG tasks |
| State | Thread state / store | Filesystem + store backends | Workflow state board |
| Fan-out | Send API, map branches | Parallel subagents | Fan-out tasks |
| Checkpoint | Checkpointer per thread | Store + middleware | Task checkpoints |
| HITL | Interrupt / resume | HITL middleware | Human approval nodes |
| Persistence | Postgres / Redis saver | Composite backends | Workflow DB |

**Do not** let framework defaults replace explicit:

- Handoff schemas
- Merge policies
- Failure matrices
- Budget enforcement

Implement those in your orchestration layer or shared library regardless of framework.

**Single-agent depth:** once topology is set, use `agentic-ai-developer` to implement each node's loop, tools, and eval harness inside the graph.
