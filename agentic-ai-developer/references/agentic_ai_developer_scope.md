# Agentic AI developer scope

## Table of contents

1. [Mission](#mission)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Typical deliverables](#typical-deliverables)
5. [Quality bar](#quality-bar)
6. [Handoffs to peer roles](#handoffs-to-peer-roles)

## Mission

Build and harden **agentic applications**: software where an LLM (or small model ensemble) repeatedly decides actions, calls tools, observes results, and terminates with an auditable outcome. The agentic AI developer owns the **runtime behavior**—loops, tools, state, orchestration, reliability, and production wiring—not corporate strategy or foundation-model training.

## In scope

| Area | Examples |
|---|---|
| Agent loop | ReAct-style, plan-then-execute, tool-first loops with explicit stop rules |
| Tools & MCP | JSON schemas, MCP server wiring, auth, rate limits, result shaping |
| Orchestration | Supervisor/worker, router, handoffs, parallel fan-out, graph nodes |
| State | Thread state, checkpoints, resume after crash, session isolation |
| Memory | Scratchpad vs durable memory; what to write/read and when |
| HITL | Approve/edit/reject on dangerous tools; escalation on repeated failure |
| Prompts | System instructions, tool-use policy, refusal and escalation text |
| Reliability | Retries, idempotency, cancellation, partial failure recovery |
| Observability | Traces, structured logs, cost/step metrics, debug replay |
| Evaluation | Golden trajectories, tool-call checks, task-success judges |
| Security basics | Sandboxing, injection awareness, least-privilege tool creds |
| Deployment | HTTP API, async workers, durable workflows, feature flags |

## Out of scope

| Topic | Route to |
|---|---|
| Pretraining, fine-tuning, dataset curation | `ai-engineer`, `ai-researcher` |
| Product vision, roadmap, OKRs | `cpo-advisor` (external) |
| Architecture-only workshops with no implementation | agent-designer (external) |
| CRUD APIs and services with no agent loop | `senior-software-engineer` |
| Red-team campaigns and exploit reproduction | `ai-redteam` |
| Enterprise AI policy and regulatory mapping | `ai-risk-governance` |
| AI ops rituals, vendor management, SLAs | `ai-lead-ops` |
| IDP, Backstage, cluster platform | `platform-engineer` |
| Pre-execution plan review without build | `build-validator` |

## Typical deliverables

1. **Runtime design doc** — loop diagram, tool catalog, state model, failure modes (1–3 pages)
2. **Tool/MCP contracts** — schemas, auth model, timeout/retry policy, example payloads
3. **Orchestration spec** — roles, handoff JSON, routing rules, parallelism limits
4. **Checkpoint & HITL spec** — what persists, approval matrix, timeout behavior
5. **Observability plan** — trace fields, dashboards, alert thresholds
6. **Eval suite** — golden tasks, expected tool sequences, pass/fail rubric
7. **Deployment runbook** — sync vs async, scaling, kill switch, rollback

## Quality bar

Before calling work production-ready:

- [ ] Stop conditions tested (max steps, final-answer tool, user cancel)
- [ ] Side-effecting tools are idempotent or guarded with keys/locks
- [ ] Secrets never appear in logs, traces, or model-visible tool output
- [ ] Tenancy enforced on state and tool credentials (org/user/thread)
- [ ] HITL path exists for irreversible or high-blast-radius actions
- [ ] Regression eval passes on CI for golden set
- [ ] p95 latency and cost per successful task within budget
- [ ] Incident runbook: disable tools, pin prompt version, drain queue

## Handoffs to peer roles

| When you need… | Engage… |
|---|---|
| RAG index design, embedding strategy, retrieval eval | `ai-engineer` |
| Release gates, on-call, vendor incidents | `ai-lead-ops` |
| Shared deploy templates, portal, platform SLOs | `platform-engineer` |
| Service-layer code review, API standards | `senior-software-engineer` |
| Jailbreak/tool-abuse test cases | `ai-redteam` |
| Risk tier and policy requirements | `ai-risk-governance` |
| Independent architecture go/no-go | `build-validator` |
| Long-horizon memory product design | `ai-memory-developer` |
