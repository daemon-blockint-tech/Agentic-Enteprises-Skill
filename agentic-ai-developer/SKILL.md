---
name: agentic-ai-developer
description: |
  Guides hands-on development of agentic AI systems—agent loops (plan → act → observe), tool and MCP
  schemas, multi-agent orchestration and handoffs, state/checkpointing, HITL gates, agent prompts,
  reliability (retries, idempotency, cancellation), observability, trajectory evaluation, tool
  sandboxing, injection awareness, and deployment (API, queue, durable workflows). Framework-agnostic
  with optional LangGraph, Deep Agents, and Cursor SDK pointers—not full framework docs. Use for
  agentic AI, build an agent, agent loop, tool use, MCP integration, multi-agent, agent orchestration,
  LangGraph, agentic workflow, AI agent developer, agent handoff, agent memory, HITL agent, evaluate
  agent, or agentic application—not model training (ai-engineer), ML research (ai-researcher), product
  strategy only (cpo-advisor), architecture whiteboard only (agent-designer, external), generic
  backend without agent loops (senior-software-engineer), or red-team only (ai-redteam).
---

# Agentic AI Developer

## When to Use

- Implementing agent loops with tools: plan → act → observe → stop
- Designing tool/MCP schemas, auth, timeouts, and sandbox boundaries
- Building multi-agent workflows with routing, handoffs, and fan-out/fan-in
- Persisting agent state, checkpoints, thread memory, and resume semantics
- Adding human-in-the-loop approval, edit, or reject gates on risky tool calls
- Hardening agents: retries, idempotency keys, cancellation, and budget caps
- Instrumenting traces, spans, and trajectory logs for debugging and eval
- Running trajectory evals, golden sets, and regression gates before release
- Shipping agentic apps via API, queue workers, or durable workflow engines

## When NOT to Use

- Training or fine-tuning foundation models, classical ML pipelines → `ai-engineer`, `ai-researcher`
- AI ops cadence, vendor contracts, rollout governance without implementation → `ai-lead-ops`
- Internal developer platform, golden paths, Backstage—no agent runtime → `platform-engineer`
- Generic service/API work with no agent loop, tools, or orchestration → `senior-software-engineer`
- Adversarial red-team campaigns and jailbreak harnesses only → `ai-redteam`
- Corporate AI policy, risk tiering, model cards without build → `ai-risk-governance`
- Pre-flight architecture or production-readiness review without building → `build-validator`
- Multi-agent **system** topology, routing, protocols, and fleet-level failure at architecture/engineering depth → `multi-agent-system-engineer`
- High-level multi-agent whiteboard without implementation → **agent-designer** (external skill; use conceptually)

## Related skills

| Need | Skill |
|---|---|
| Broader LLM apps, RAG, model routing, cost/latency | `ai-engineer` |
| AI production ops, incidents, release gates | `ai-lead-ops` |
| Platform golden paths, IDP, developer portals | `platform-engineer` |
| Service design, APIs, code quality without agent focus | `senior-software-engineer` |
| Prompt injection, tool abuse, safety eval campaigns | `ai-redteam` |
| Governance, risk tiers, policy mapping | `ai-risk-governance` |
| Go/no-go plan or architecture validation | `build-validator` |
| Persistent memory stores and retrieval design | `ai-memory-developer` |
| Context packing and token budgeting | `ai-context-engineer` |
| Prompt templates and judge rubrics | `prompt-engineer` |
| Multi-agent system topology, routing, DAG, fleet observability | `multi-agent-system-engineer` |
| Multi-agent whiteboard without code (conceptual) | agent-designer (external) |

## Core Workflows

### 1. Shape the agent runtime

1. Define the user job, success metric, and stop conditions
2. Choose runtime shape: single loop, supervisor + workers, or graph/DAG
3. List tools/MCP servers; classify read vs write vs irreversible
4. Set budgets: max steps, tokens, wall time, cost per session
5. Decide checkpoint/resume and tenancy (thread_id, org_id)

**See `references/agentic_ai_developer_scope.md` for scope boundaries and deliverables.**

### 2. Implement loop + tools

```
receive task → plan (optional) → select tool → execute → observe → repeat | finalize
```

**Checklist:**

- [ ] Tool schemas are narrow; descriptions say when **not** to call
- [ ] Timeouts, retries, and idempotency on side effects
- [ ] Errors surfaced once to the model; no infinite retry loops
- [ ] Secrets never returned in tool results or traces

**See `references/agent_loop_tools_and_mcp.md` for MCP and schema patterns.**

### 3. Orchestrate multiple agents

- Assign roles: planner, executor, critic, specialist
- Handoff payload: goal, constraints, artifacts, open questions
- Avoid duplicate tool access unless idempotent; centralize dangerous tools
- Use fan-out/fan-in for parallel research; merge with structured reducer

**See `references/multi_agent_orchestration_and_handoffs.md` for routing and handoff contracts. For system-level topology, fan-in policy, and cross-agent failure matrices, use `multi-agent-system-engineer`.**

### 4. State, memory, and HITL

- Separate ephemeral scratchpad vs durable thread state vs long-term memory
- Checkpoint after each tool batch or subgraph node for resume
- HITL on tier-2+ actions: approve, edit args, or reject with reason
- Time out stalled human approvals; default-deny on expiry

**See `references/state_memory_and_hitl.md` for checkpoint and approval patterns.**

### 5. Reliability, observability, and evaluation

- Trace: session_id, span per model/tool step, redacted inputs/outputs
- Metrics: success rate, steps to completion, tool error rate, p95 latency, cost
- Eval: golden trajectories, tool-call correctness, task success (human or judge)
- Gate releases on regression suite; canary new prompts/graph versions

**See `references/reliability_observability_and_evaluation.md` for eval and SLO patterns.**

### 6. Security and production deployment

- Sandboxed tool execution; least-privilege credentials per tool
- Treat tool results and retrieved docs as untrusted input (injection aware)
- Deploy: sync API for short tasks; queue or durable workflow for long runs
- Kill switch, feature flags, and versioned prompts/graph definitions

**See `references/security_and_production_deployment.md` for deployment topologies.**

## When to load references

| Topic | Reference |
|---|---|
| Role scope, deliverables, boundaries | `references/agentic_ai_developer_scope.md` |
| Agent loop, tools, MCP | `references/agent_loop_tools_and_mcp.md` |
| Multi-agent routing and handoffs | `references/multi_agent_orchestration_and_handoffs.md` |
| State, memory, checkpoints, HITL | `references/state_memory_and_hitl.md` |
| Retries, tracing, trajectory eval | `references/reliability_observability_and_evaluation.md` |
| Sandboxing, injection, deployment | `references/security_and_production_deployment.md` |

## Framework pointers (optional)

Use framework docs for API specifics; this skill stays pattern-first:

| Pattern | Typical home |
|---|---|
| Stateful graph, interrupts, checkpointing | LangGraph-style graphs |
| Subagents, filesystem memory, HITL middleware | Deep Agents-style harness |
| Programmatic cloud/local agents, MCP in CI | Cursor SDK-style agents |

Do not duplicate full framework tutorials—implement the contracts above in the stack the team chose.
