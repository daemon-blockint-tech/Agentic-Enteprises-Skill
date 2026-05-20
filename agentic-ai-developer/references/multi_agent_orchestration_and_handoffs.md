# Multi-agent orchestration and handoffs

## Table of contents

1. [When to use multiple agents](#when-to-use-multiple-agents)
2. [Topology patterns](#topology-patterns)
3. [Handoff contracts](#handoff-contracts)
4. [Routing and delegation](#routing-and-delegation)
5. [Parallelism](#parallelism)
6. [Anti-patterns](#anti-patterns)

## When to use multiple agents

Use multiple agents when:

- **Specialists** beat one generalist (legal vs code vs data)
- **Context isolation** prevents one huge transcript (researcher → writer)
- **Critique loops** need a separate role (executor vs reviewer)
- **Parallel research** shortens wall time

Prefer a **single agent + good tools** when the task is narrow and tool count is small.

## Topology patterns

```
Supervisor → [Worker A, Worker B] → Supervisor merges
```

```
Router → Specialist (one of N) → optional return to Router
```

```
Pipeline: Planner → Executor → Verifier (linear)
```

```
Fan-out: Coordinator → parallel Workers → Reducer
```

| Pattern | Best for | Watch out for |
|---|---|---|
| Supervisor | Dynamic task decomposition | Supervisor bottleneck / cost |
| Router | Intent classification | Mis-routes; need confidence threshold |
| Pipeline | Repeatable workflows | Rigid; hard to recover mid-pipeline |
| Fan-out | Research, multi-source gather | Merge quality; duplicate work |

## Handoff contracts

Pass **structured** handoffs, not prose-only summaries.

Recommended payload:

```json
{
  "goal": "string",
  "constraints": ["string"],
  "artifacts": [{ "type": "file|url|id", "ref": "...", "summary": "..." }],
  "completed_steps": ["string"],
  "open_questions": ["string"],
  "allowed_tools": ["tool_name"],
  "risk_tier": 0
}
```

Rules:

- Receiver agent gets a **fresh** system prompt slice for its role
- Include only artifacts the receiver needs; link large blobs
- Set `allowed_tools` to least privilege for the sub-role
- Log handoff id for trace correlation

## Routing and delegation

**Router inputs:** user message, session metadata, prior failures, risk tier.

**Routing policies:**

| Policy | Mechanism |
|---|---|
| Rule-based | Keywords, tenant flags, compliance mode |
| Classifier | Small model or LLM with JSON route + confidence |
| Embedding | Nearest specialist description |

If confidence &lt; threshold → clarify with user or default safe specialist.

**Delegation limits:**

- Max depth (e.g., 2 hops supervisor → worker → no further)
- Max total agents invoked per user request
- Single owner for final user-facing reply (avoid conflicting voices)

## Parallelism

Fan-out pattern:

1. Coordinator splits work items (explicit list)
2. Workers run with isolated thread ids
3. Reducer merges via schema (table of findings, ranked list)

Reducer should:

- Deduplicate citations and URLs
- Flag contradictions between workers
- Never execute write tools unless authorized post-merge

Cap parallel workers (e.g., 3–5) to control cost and rate limits.

## Anti-patterns

| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| Chatty handoffs | Token bloat, lost structure | JSON contract + artifact refs |
| Duplicate write tools on all agents | Double mutations | Centralize writes in one role |
| Unbounded supervisor recursion | Cost, loops | Step cap + same-task detection |
| Identical system prompts | No role separation | Role-specific goals and tools |
| Hidden shared mutable state | Race conditions | Per-worker state + explicit merge |

**External reference:** agent-designer (not in this repo) is useful for topology whiteboards; this file covers implementable contracts.
