# Agent roles, topology, and routing

## Table of contents

1. [Agent roles](#agent-roles)
2. [Topology patterns](#topology-patterns)
3. [Routing strategies](#routing-strategies)
4. [Fan-out and fan-in](#fan-out-and-fan-in)
5. [DAG workflows](#dag-workflows)
6. [Anti-patterns](#anti-patterns)

## Agent roles

Define roles by **responsibility**, not model SKU:

| Role | Responsibility | Typical inputs | Typical outputs |
|---|---|---|---|
| **Ingress / router** | Classify intent, select subgraph | User message, session context | Route decision, sub-goal |
| **Planner** | Decompose task, assign work | Goal, constraints | Task graph or work orders |
| **Executor** | Perform bounded work with tools | Work order, artifacts | Result artifact, status |
| **Specialist** | Deep domain step (legal, code, data) | Scoped sub-goal | Structured finding |
| **Critic / verifier** | Check quality, policy, facts | Candidate output | Pass/fail, edits |
| **Merger / reducer** | Combine parallel outputs | N partial results | Single consolidated artifact |
| **Supervisor** | Orchestrate workers, handle exceptions | Events from workers | Next assignments, abort/continue |
| **Human proxy** | Represent human-in-the-loop | Approval request | Decision, edited payload |

**Rules:**

- One primary role per agent instance in a given workflow version
- Specialists should not also route—separation reduces prompt injection surface
- Critics should not have write tools to production systems unless explicitly required

## Topology patterns

### Supervisor (hub-and-spoke)

```
        ┌─────────────┐
        │ Supervisor  │
        └──────┬──────┘
     ┌─────────┼─────────┐
     ▼         ▼         ▼
  Worker A  Worker B  Worker C
```

- **Use when:** Clear delegation, centralized policy, need single point for HITL
- **Risks:** Supervisor bottleneck, single point of failure—replicate supervisor logic in code where possible

### Hierarchical

```
 CEO agent
    ├── Manager A → workers
    └── Manager B → workers
```

- **Use when:** Large task trees, org-like decomposition, staged planning
- **Risks:** Deep trees burn tokens; cap depth and require managers to emit structured sub-plans only

### Peer-to-peer (P2P)

```
 Agent A ←→ Agent B ←→ Agent C
```

- **Use when:** Negotiation, debate, iterative refinement between equals
- **Risks:** Non-termination—set max rounds and explicit stop tokens

### Blackboard

```
 Agents read/write shared structured board
```

- **Use when:** Multiple specialists contribute to one evolving artifact (report, plan)
- **Risks:** Write conflicts—use optimistic locking, sections, or supervisor merge

### Hybrid

Common production pattern: **router → parallel specialists → merger → critic → egress**.

## Routing strategies

| Strategy | Mechanism | Best for |
|---|---|---|
| **Rule-based** | If intent/tag → subgraph | Safety-critical, compliance |
| **Capability matrix** | Agent skills × task type | Specialist pools |
| **Load-aware** | Queue depth, latency SLO | High volume |
| **LLM router** | Small model or node classifies | Ambiguous user requests |
| **Cost-aware** | Route cheap model first, escalate | Budget-sensitive |

**Routing checklist:**

- [ ] Log routing decision with reason code (not only model prose)
- [ ] Fallback path when no agent accepts (human or safe default)
- [ ] Prevent circular routing (A→B→A) with visit counters or DAG enforcement
- [ ] Sticky routing when continuity matters (same specialist for a thread)

## Fan-out and fan-in

**Fan-out:** duplicate or split work across N workers.

| Pattern | Description |
|---|---|
| **Map** | Same prompt template, different inputs (e.g., N URLs) |
| **Diverse experts** | Different roles on same input (ensemble) |
| **Sharding** | Partition large input by chunk |

**Fan-in:** merge N results.

| Merge type | When |
|---|---|
| **Concat + summarize** | Research snippets |
| **Vote / majority** | Classification |
| **Structured reduce** | JSON merge with schema |
| **Critic picks best** | Qualitative outputs |
| **Supervisor synthesizes** | Narrative report |

**Required parameters:**

- `N` max parallelism
- Per-worker timeout
- Fan-in timeout (wait for k-of-n or all-n)
- Policy for partial fan-in (proceed with subset vs fail)

## DAG workflows

Represent multi-agent work as a **directed acyclic graph** (cycles only via explicit iteration node with cap):

```
        [plan]
           │
     ┌─────┴─────┐
     ▼           ▼
 [research]   [research]
     │           │
     └─────┬─────┘
           ▼
        [merge]
           ▼
        [draft]
           ▼
        [critic]──fail──► [revise] (loop max 3)
           │ pass
           ▼
        [publish]
```

**Node metadata:**

- `agent_role`, `input_schema`, `output_schema`
- `retry_policy`, `timeout`, `compensation` (optional)
- `conditional_edges` (e.g., critic pass/fail)

**Conditional branches:** encode as explicit edges, not implicit prompt luck.

## Anti-patterns

- **Agent soup** — many undifferentiated agents with overlapping tools
- **Chatty P2P without cap** — unbounded debate loops
- **Fan-out without fan-in** — orphaned partial results and billing leaks
- **Supervisor does all work** — workers become decorative
- **Routing only in natural language** — no structured route for audits
- **Per-agent secrets** — duplicate credentials across workers
