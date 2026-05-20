---
name: multi-agent-system-engineer
description: |
  Guides engineering of multi-agent systems—agent roles and specialization, orchestration topologies
  (supervisor, peer-to-peer, hierarchical, blackboard), task decomposition and routing, inter-agent
  messaging (A2A-style patterns), shared vs partitioned state, fan-out/fan-in and DAG workflows,
  synchronization and consensus, conflict resolution, fault tolerance and retries across agents,
  cost/latency/token budgets, cross-agent observability, testing multi-agent flows, and deployment
  (queues, durable workflows). Framework-agnostic; high-level LangGraph, Deep Agents,
  and agenthub—not single-agent loops (agentic-ai-developer), ML training (ai-engineer),
  strategy-only whiteboard (enterprise-strategist), or PM planning (technical-program-manager).
  Use for multi-agent system, multi-agent engineer, agent orchestration, supervisor agent, agent
  topology, fan-out fan-in, agent handoff protocol, multi-agent workflow, agent coordination,
  blackboard pattern, hierarchical agents, A2A, agent DAG, multi-agent architecture.
---

# Multi-Agent System Engineer

## When to Use

- Designing multi-agent topology: supervisor, hierarchical, peer-to-peer, or blackboard
- Decomposing work across specialized agents with routing, delegation, and merge rules
- Defining inter-agent message schemas, handoff payloads, and protocol boundaries
- Partitioning vs sharing state, scratchpads, artifacts, and consensus across agents
- Building fan-out/fan-in, DAG workflows, and synchronization barriers in agent graphs
- Resolving conflicts when agents disagree or duplicate work
- Engineering fault tolerance: retries, partial failure, compensation, and saga-style recovery
- Setting system-level budgets: tokens, latency, parallelism, and cost per workflow run
- Observability across agent traces, correlation IDs, and multi-step workflow debugging
- Testing and simulating multi-agent flows before production
- Deploying multi-agent runtimes on queues, durable workflows, and scaled workers

## When NOT to Use

- Single-agent loop, tools, MCP, checkpoints, and one runtime only → `agentic-ai-developer`
- Foundation model training, fine-tuning, classical ML pipelines → `ai-engineer`, `ai-researcher`
- AI ops cadence, vendor contracts, rollout governance without system design → `ai-lead-ops`
- Internal developer platform, golden paths, portals—no agent orchestration → `platform-engineer`
- Cross-team milestones, RAID, program status without agent architecture → `technical-program-manager`
- Corporate AI policy, risk tiering, model cards without system build → `ai-risk-governance`
- Pre-flight go/no-go or architecture review without implementing topology → `build-validator`
- Enterprise strategy, portfolio, and org design whiteboard only → `enterprise-strategist`

## Related skills

| Need | Skill |
|---|---|
| Implement single-agent loop, tools, MCP, HITL, eval harness | `agentic-ai-developer` |
| LLM apps, RAG, model routing, embedding strategy | `ai-engineer` |
| AI production ops, incidents, release gates | `ai-lead-ops` |
| Platform golden paths, IDP, developer portals | `platform-engineer` |
| Program delivery, dependencies, launch readiness | `technical-program-manager` |
| Governance, risk tiers, policy mapping | `ai-risk-governance` |
| Independent architecture or build go/no-go | `build-validator` |
| Persistent memory stores and retrieval design | `ai-memory-developer` |
| Context packing and token budgeting per call | `ai-context-engineer` |
| Prompt templates and judge rubrics | `prompt-engineer` |

## Core Workflows

### 1. Frame the multi-agent system

1. Define the end-to-end job, success metric, and SLA (latency, cost, quality)
2. List agents by **role** (planner, executor, critic, specialist)—not by model name
3. Choose topology and justify: supervisor, hierarchical, P2P, blackboard, or hybrid
4. Map trust boundaries: which agent may call which tools and external systems
5. Set system budgets: max parallel agents, tokens per run, wall time, dollars per task

**See `references/multi_agent_system_engineer_scope.md` for scope, deliverables, and boundaries vs `agentic-ai-developer`.**

### 2. Topology, roles, and routing

```
ingress → router/supervisor → {workers} → reducer/merger → egress
```

**Checklist:**

- [ ] Each agent has one primary responsibility and explicit inputs/outputs
- [ ] Routing rules are deterministic where safety matters; LLM routing elsewhere is logged
- [ ] Fan-out has a matching fan-in with merge semantics (vote, concat, structured reduce)
- [ ] Dangerous tools are centralized or gated—not duplicated on every worker

**See `references/agent_roles_topology_and_routing.md` for topology patterns and routing tables.**

### 3. Protocols and messaging

- Define message envelope: `correlation_id`, `from`, `to`, `intent`, `payload`, `artifacts`, `constraints`
- Version schemas; reject unknown versions at boundaries
- Prefer structured payloads over free-text handoffs for machine agents
- Document idempotency keys for retried messages

**See `references/inter_agent_protocols_and_messaging.md` for handoff contracts and A2A-style patterns.**

### 4. State, coordination, and consensus

- Classify state: ephemeral scratchpad, workflow state, shared blackboard, durable store
- Partition tenant and thread keys on every read/write
- Use barriers or quorum when parallel agents must align before the next phase
- Resolve conflicts with explicit policy: supervisor wins, vote, or escalate to human

**See `references/shared_state_coordination_and_consensus.md` for blackboard vs partitioned models.**

### 5. Fault tolerance, observability, and testing

- Retry at message and workflow level with caps; distinguish transient vs terminal errors
- Compensate or mark partial success; never leave workflows stuck without timeout
- Trace: one `workflow_run_id` spanning all agent spans; redact secrets in cross-agent logs
- Test: unit agents, pairwise handoffs, full DAG golden paths, chaos on one worker

**See `references/fault_tolerance_observability_and_testing.md` for test matrices and SLOs.**

### 6. Deployment, cost, and governance

- Short synchronous graphs for interactive UX; queue or durable engine for long DAGs
- Scale workers horizontally; pin graph version and agent config per deployment
- Attribute cost per agent step; alert on budget burn rate
- Gate releases on multi-agent regression suite and policy checks

**See `references/deployment_cost_and_governance.md` for queue vs durable workflow tradeoffs.**

## When to load references

| Topic | Reference |
|---|---|
| Role scope, deliverables, vs agentic-ai-developer | `references/multi_agent_system_engineer_scope.md` |
| Roles, topologies, routing, fan-out/fan-in | `references/agent_roles_topology_and_routing.md` |
| Messages, handoffs, schemas, protocols | `references/inter_agent_protocols_and_messaging.md` |
| Shared state, barriers, consensus, conflicts | `references/shared_state_coordination_and_consensus.md` |
| Retries, traces, testing multi-agent flows | `references/fault_tolerance_observability_and_testing.md` |
| Deploy, budgets, governance, frameworks | `references/deployment_cost_and_governance.md` |

## Framework pointers (optional)

Use framework docs for API specifics; this skill stays pattern-first:

| Pattern | Typical home |
|---|---|
| Stateful graph, Send/fan-in, subgraph checkpointers | LangGraph-style graphs |
| Subagents, task middleware, filesystem routing | Deep Agents-style harness |
| DAG orchestration, merge nodes, status boards | agenthub-style workflows |

Do not duplicate full framework tutorials—encode the **system contracts** (topology, messages, state, failure) in the stack the team chose.

## Routing vs agentic-ai-developer

| Question | Use |
|---|---|
| One agent, tool loop, MCP, checkpoint resume | `agentic-ai-developer` |
| Multiple agents, topology, routing, system-level failure and observability | **this skill** |
| Both: implement loops in agentic-ai-developer; design the fleet here | Load both; start here for topology |
