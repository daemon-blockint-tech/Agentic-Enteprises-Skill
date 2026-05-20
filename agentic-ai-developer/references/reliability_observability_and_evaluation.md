# Reliability, observability, and evaluation

## Table of contents

1. [Reliability primitives](#reliability-primitives)
2. [Cancellation](#cancellation)
3. [Observability model](#observability-model)
4. [Trajectory evaluation](#trajectory-evaluation)
5. [CI and release gates](#ci-and-release-gates)
6. [Operational SLOs](#operational-slos)

## Reliability primitives

| Primitive | Purpose | Implementation hints |
|---|---|---|
| **Retry** | Transient upstream failures | Exponential backoff; max 2–3; idempotent reads only |
| **Idempotency key** | Safe retries on writes | Client-generated key; store outcome 24h |
| **Timeout** | Per tool, per model call, per session | Shorter on user-facing sync paths |
| **Circuit breaker** | Failing MCP/server | Open after error rate threshold |
| **Bulkhead** | Noisy neighbor tools | Separate pools per tool class |
| **Budget** | Cost/runaway loops | Steps, tokens, dollars—hard stop |

**Idempotency checklist for write tools:**

- [ ] Key required in schema for create/charge/send
- [ ] Server returns same result for duplicate key
- [ ] Model instructed not to change key on retry

## Cancellation

Support user cancel and admin drain:

1. Propagate `cancel` flag to in-flight tool tasks
2. Stop scheduling new model turns
3. Persist terminal state: `cancelled` with partial artifacts
4. Revoke long-running external jobs if possible

Cooperative cancellation: tools poll cancel token; hard kill only for sandboxed workers.

Do not leave HITL queues orphaned—expire pending approvals on cancel.

## Observability model

**Trace hierarchy:**

```
session (session_id)
  └── run (run_id)
        └── step (model | tool)
              └── span attributes
```

**Minimum span attributes:**

| Field | Notes |
|---|---|
| `session_id`, `run_id`, `thread_id` | Correlation |
| `agent_role` | supervisor, worker, … |
| `model`, `prompt_version`, `graph_version` | Reproducibility |
| `tool_name`, `latency_ms`, `status` | Tool SLOs |
| `input_tokens`, `output_tokens`, `cost_usd` | Economics |
| `error_code` | Taxonomy, not stack traces to users |

**Redaction:** strip secrets, tokens, PII from span payloads; keep hash or length only.

**Dashboards:**

- Success rate by task type
- Steps-to-completion distribution
- Tool error rate by tool
- p50/p95 latency and cost per successful task
- HITL queue depth and approval time

Integrate with OpenTelemetry-style exporters where available; align with `ai-lead-ops` for incident rituals.

## Trajectory evaluation

Evaluate **trajectories**, not single final strings.

| Level | What you measure |
|---|---|
| **Outcome** | Task success (human label or rubric) |
| **Process** | Correct tools called in sensible order |
| **Safety** | No policy violations; refusals when needed |
| **Efficiency** | Steps and cost within budget |

**Dataset types:**

| Type | Use |
|---|---|
| Golden tasks | Fixed prompts + expected outcome |
| Golden tool traces | Expected tool names/args (fuzzy match) |
| Adversarial | Injection in tool results (with `ai-redteam`) |
| Regression | Prior production failures |

**Scoring:**

- Exact match on structured final output where possible
- LLM-as-judge with rubric + human calibration sample
- Tool-call F1: precision/recall on tool name and critical args

Store eval runs with pinned `prompt_version` and `graph_version`.

## CI and release gates

Pipeline stages:

```
unit (schemas) → contract (tools/MCP) → offline eval (golden) → canary (prod traffic sample)
```

Block release if:

- Golden outcome pass rate drops &gt; agreed delta
- Safety set regressions
- New tool without contract test
- p95 cost per task exceeds threshold on canary

Coordinate eval policy with `ai-lead-ops` and safety sign-off with `ai-risk-governance` for tier-2+ features.

## Operational SLOs

Example targets (tune per product):

| Metric | Starter target |
|---|---|
| Task success (golden) | ≥ 90% |
| Tool error rate | &lt; 5% per session |
| p95 end-to-end latency (sync) | Product-specific |
| Cost per successful task | Budget cap |
| HITL time-to-approve p95 | &lt; 4h business hours |

Alert on:

- Success rate drop vs 7-day baseline
- Spike in loop length (possible runaway)
- Single tool dominating errors (circuit breaker)
