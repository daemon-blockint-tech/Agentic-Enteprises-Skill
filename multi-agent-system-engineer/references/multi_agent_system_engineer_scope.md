# Multi-agent system engineer scope

## Table of contents

1. [Mission](#mission)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Boundary vs agentic-ai-developer](#boundary-vs-agentic-ai-developer)
5. [Typical deliverables](#typical-deliverables)
6. [Quality bar](#quality-bar)
7. [Handoffs to peer roles](#handoffs-to-peer-roles)

## Mission

Engineer **multi-agent systems** as coherent distributed applications: multiple LLM-backed (or hybrid) agents coordinated by explicit topology, protocols, and shared runtime policies. Own **system-level** concerns—who talks to whom, how work is split and merged, how state and failures propagate—not the implementation details of a single ReAct loop in isolation.

## In scope

| Area | Examples |
|---|---|
| Topology | Supervisor, hierarchical tree, peer-to-peer, blackboard, hybrid |
| Roles | Planner, executor, critic, router, specialist, human proxy |
| Routing | Task decomposition, capability-based dispatch, load-aware assignment |
| Messaging | Handoff envelopes, schema versioning, correlation IDs |
| Workflows | DAGs, fan-out/fan-in, barriers, conditional branches |
| State model | Partitioned thread state, shared blackboard, artifact store |
| Coordination | Quorum, voting, supervisor override, conflict policies |
| Fault tolerance | Cross-agent retries, partial completion, compensation |
| Budgets | System token caps, parallelism limits, cost attribution per agent |
| Observability | Workflow traces, span hierarchy, cross-agent debug replay |
| Testing | Simulation, golden DAG paths, chaos on workers |
| Deployment | Queue workers, durable workflows, horizontal scale |

## Out of scope

| Topic | Route to |
|---|---|
| Single-agent loop, tool schemas, MCP wiring | `agentic-ai-developer` |
| Model training, fine-tuning, eval of base models | `ai-engineer`, `ai-researcher` |
| AI ops rituals, vendor SLAs, on-call without design | `ai-lead-ops` |
| IDP, Backstage, K8s platform product | `platform-engineer` |
| Sprint planning, RAID, milestone tracking | `technical-program-manager` |
| Enterprise strategy, portfolio, M&A narrative | `enterprise-strategist` |
| Policy mapping, risk tiers, regulatory memos | `ai-risk-governance` |
| Independent go/no-go without building graph | `build-validator` |
| Adversarial jailbreak campaigns | `ai-redteam` |

## Boundary vs agentic-ai-developer

| Dimension | `agentic-ai-developer` | Multi-agent system engineer |
|---|---|---|
| Unit of design | One runtime / one loop | Fleet of agents + orchestration graph |
| Primary artifact | Tool contracts, checkpoint spec | Topology diagram, routing table, message schemas |
| Failure focus | Tool retry, step cap, HITL on one agent | Partial DAG failure, merge on incomplete fan-in |
| State | Thread checkpoint for one graph node | Shared vs partitioned state across agents |
| Testing | Golden trajectory for one agent | End-to-end DAG + per-edge handoff tests |
| When user says… | "Build an agent with tools" | "Design supervisor + 5 workers with fan-in merge" |

**Rule of thumb:** If removing one agent leaves no "system" (only a loop), use `agentic-ai-developer`. If agents are peers in a coordinated fleet, use this skill.

## Typical deliverables

1. **System context diagram** — agents, external systems, data stores, trust boundaries
2. **Topology ADR** — chosen pattern, alternatives rejected, scaling implications
3. **Role catalog** — responsibility, inputs, outputs, allowed tools, SLAs
4. **Routing specification** — rules, fallbacks, human escalation paths
5. **Message schema registry** — versioned handoff types with examples
6. **State partition map** — what is shared, per-thread, or immutable artifact
7. **Failure and compensation matrix** — per node: retry, skip, compensate, abort DAG
8. **Observability contract** — required trace fields, dashboards, alert thresholds
9. **Test plan** — unit agent, edge, full golden DAG, load and chaos scenarios
10. **Deployment topology** — sync API vs queue vs durable engine, scaling knobs

## Quality bar

Before calling a multi-agent system production-ready:

- [ ] Every agent role has a single accountable owner in the org (team or service)
- [ ] Handoff schemas are versioned; unknown versions fail closed at boundaries
- [ ] Fan-out always defines fan-in merge semantics and timeout for stragglers
- [ ] Workflow runs are idempotent or keyed; duplicate delivery does not double-charge
- [ ] One correlation ID ties all agent spans for a user-visible task
- [ ] System budgets enforced (parallelism, tokens, wall time, cost)
- [ ] Conflict policy documented when agents disagree
- [ ] Regression suite covers full DAG and critical partial-failure paths
- [ ] Kill switch disables graph version or individual agent without orphaning state

## Handoffs to peer roles

| When you need… | Engage… |
|---|---|
| Implement individual agent loops, tools, MCP | `agentic-ai-developer` |
| Retrieval, embeddings, model selection | `ai-engineer` |
| Production rollout, incidents, vendor issues | `ai-lead-ops` |
| Shared deploy templates, secrets platform | `platform-engineer` |
| Cross-team delivery dates and dependencies | `technical-program-manager` |
| Risk tier and required human gates | `ai-risk-governance` |
| Independent architecture review | `build-validator` |
