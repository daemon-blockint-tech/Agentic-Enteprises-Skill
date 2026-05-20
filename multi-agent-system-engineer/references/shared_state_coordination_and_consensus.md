# Shared state, coordination, and consensus

## Table of contents

1. [State categories](#state-categories)
2. [Partitioning model](#partitioning-model)
3. [Blackboard pattern](#blackboard-pattern)
4. [Synchronization](#synchronization)
5. [Consensus and conflict resolution](#consensus-and-conflict-resolution)
6. [Human-in-the-loop at system level](#human-in-the-loop-at-system-level)

## State categories

| Category | Lifetime | Visibility | Examples |
|---|---|---|---|
| **Ephemeral scratchpad** | Single agent step | One agent | Current reasoning, draft text |
| **Thread / workflow state** | Whole run | Orchestrator + assigned agents | Plan, status flags, budgets consumed |
| **Shared blackboard** | Whole run or session | Subscribed agents | Report sections, hypothesis list |
| **Artifact store** | Durable | By reference URI | Files, tables, codegen output |
| **Long-term memory** | Cross-session | Policy-gated retrieval | User prefs, org facts |

**Design principle:** default **partitioned** state; share only through schemas and artifact refs.

## Partitioning model

Keys should include at minimum:

```
tenant_id / org_id
user_id or principal_id
thread_id or workflow_run_id
agent_instance_id (optional)
```

**Rules:**

- Workers read only slices of state for their work order
- Supervisor holds routing and global budget counters
- No agent reads another agent's scratchpad unless explicitly passed in handoff

**Checkpointing (system view):**

- Checkpoint after each DAG node completion, not only after each LLM call
- Resume reloads workflow state + artifact index; re-invoke only failed nodes when safe

## Blackboard pattern

Structured shared surface agents read/write:

```json
{
  "board_version": 3,
  "sections": {
    "requirements": { "owner": "planner", "content_ref": "..." },
    "findings": { "entries": [ { "agent": "research-2", "claim": "...", "evidence_ref": "..." } ] },
    "open_risks": [ { "id": "r1", "severity": "high", "status": "open" } ]
  },
  "locks": { "findings": "research-1" }
}
```

**Concurrency:**

- Section-level locks or optimistic concurrency with `board_version`
- Append-only logs for findings to reduce write conflicts
- Supervisor compacts board periodically into summary artifact

## Synchronization

### Barriers

Pause DAG until condition met:

| Barrier type | Condition |
|---|---|
| **All-complete** | All fan-out branches succeeded |
| **K-of-n** | At least k successes |
| **Quorum data** | Required artifacts present on board |
| **Human** | Approval record in workflow state |

### Timeouts

- Barrier timeout triggers policy: fail workflow, proceed with partial, or escalate
- Document default: **fail closed** for regulated domains; **best-effort partial** for research

### Clocks and ordering

- Use logical workflow step numbers, not wall clock, for ordering events
- If using event bus, partition by `correlation_id` for per-workflow ordering

## Consensus and conflict resolution

When agents disagree (facts, plan, priority):

| Policy | When to use |
|---|---|
| **Supervisor decides** | Default for production workflows |
| **Vote (majority)** | Ensemble classification |
| **Weighted by confidence** | Requires calibrated scores—often brittle |
| **Critic tie-break** | Quality-critical outputs |
| **Escalate to human** | High stakes or repeated disagreement |
| **Fail workflow** | Safety: no silent merge of conflicts |

**Conflict record** (audit):

```json
{
  "conflict_id": "c-9",
  "topic": "vendor_pricing",
  "positions": [
    { "agent": "research-1", "claim": "...", "evidence_ref": "..." },
    { "agent": "research-2", "claim": "...", "evidence_ref": "..." }
  ],
  "resolution": "supervisor_chose",
  "resolved_by": "supervisor-1",
  "rationale": "research-2 source more recent"
}
```

## Human-in-the-loop at system level

System-level HITL differs from single-tool approval:

| Gate | Scope |
|---|---|
| **Workflow gate** | Cannot proceed past node until human approves plan |
| **Agent gate** | Any message to `human_proxy` role pauses DAG |
| **Budget gate** | Spend over threshold triggers approval |
| **Policy gate** | Critic fail routes to human review queue |

**Timeouts:** stalled human gates should default **deny** or **cancel workflow** per risk tier—document in `ai-risk-governance` alignment.

**Queue fairness:** prioritize by SLA tier; expose correlation id and condensed context for reviewers.
