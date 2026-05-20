# Fault tolerance, observability, and testing

## Table of contents

1. [Failure taxonomy](#failure-taxonomy)
2. [Retry and compensation](#retry-and-compensation)
3. [Partial failure in fan-out](#partial-failure-in-fan-out)
4. [Observability](#observability)
5. [Testing strategy](#testing-strategy)
6. [SLOs and alerting](#slos-and-alerting)

## Failure taxonomy

| Class | Examples | Typical response |
|---|---|---|
| **Transient** | Rate limit, network blip, worker OOM restart | Retry with backoff |
| **Agent logic** | Bad plan, wrong tool args | Re-prompt, swap agent, human |
| **Tool / external** | API 5xx, timeout | Retry tool, circuit break |
| **Policy** | Refusal, PII leak attempt | Fail closed, audit |
| **System** | Queue loss, corrupt state | Alert, manual replay |
| **Budget** | Token or time cap exceeded | Graceful degrade or cancel |

Classify per **DAG node** in the failure matrix—not only per HTTP request.

## Retry and compensation

### Retry layers

| Layer | Scope | Notes |
|---|---|---|
| Tool retry | Single tool call | Idempotency keys required |
| Agent retry | Re-run node with same input | Cap attempts; change prompt on 2nd try |
| Message retry | Queue redelivery | Dedup on consumer |
| Workflow retry | Restart from checkpoint | Only for deterministic nodes |

**Backoff:** exponential with jitter; max attempts per node in config, not buried in prompts.

### Compensation (saga-style)

For nodes with irreversible side effects, define compensating actions:

| Forward | Compensate |
|---|---|
| Reserve inventory | Release reservation |
| Charge payment | Refund (if API supports) |
| Send email | Send correction (cannot unsend—document) |
| Create ticket | Close ticket with reason |

Not all steps are compensatable—mark **pivot points** where workflow must halt and human intervenes.

## Partial failure in fan-out

| Policy | Behavior |
|---|---|
| **All-or-nothing** | Any branch fail → fail fan-in |
| **Best-effort** | Merge successes; flag gaps in output |
| **K-of-n** | Proceed when k successes |
| **Fallback branch** | Alternate cheaper path on timeout |

Document user-visible behavior: does the user see partial research or an error?

**Straggler handling:** cancel slow branches after T seconds; include `cancelled` in merge metadata.

## Observability

### Trace hierarchy

```
workflow_run (correlation_id)
  ├── span: router
  ├── span: fan-out
  │     ├── span: worker-1
  │     └── span: worker-2
  ├── span: merge
  └── span: critic
```

**Required attributes:**

- `workflow_run_id`, `graph_version`, `tenant_id`
- `agent_role`, `agent_instance_id`, `model` (if applicable)
- `input_tokens`, `output_tokens`, `cost_usd` (estimated)
- `tool_calls` count, `error_code`
- `payload_version` on handoffs

**Redaction:** secrets, PII, and raw tool payloads off by default in production; enable debug tier for support.

### Dashboards

| Metric | Question |
|---|---|
| Workflow success rate | Are DAGs completing? |
| p95 end-to-end latency | User SLA met? |
| Cost per successful workflow | Budget sustainable? |
| Fan-out straggler rate | Timeouts tuned? |
| Conflict / HITL rate | Routing or policy issue? |
| Per-agent error heatmap | Which role breaks? |

### Debug replay

Store: graph version, inputs hash, artifact refs, routing decisions, model versions.

Replay modes: **dry-run** (no side effects), **single-node** re-execute, **full** (dangerous in prod).

## Testing strategy

### Test pyramid for multi-agent systems

| Level | What | How |
|---|---|---|
| **Unit** | One agent with mocked tools | Fixed prompts, schema validation |
| **Contract** | Handoff between two roles | Golden JSON payloads both directions |
| **Integration** | Subgraph (e.g., fan-out→merge) | Stub workers returning fixtures |
| **E2E** | Full DAG | Recorded or live with sandbox tools |
| **Chaos** | Kill worker, delay queue | Assert compensation or fail policy |
| **Load** | Parallel workflow runs | Budget and queue depth |

### Simulation

- **Stub agents:** deterministic responses from fixtures
- **Property checks:** fan-in always receives ≤ N messages
- **Policy tests:** critic must reject forbidden tool plans

### Golden DAG paths

Maintain versioned scenarios:

```yaml
scenario: crm_research_v3
graph_version: "2025.04.1"
steps:
  - expect_route: specialist_pool
  - expect_fan_out: 3
  - expect_artifact: comparison_table.v1
  - max_cost_usd: 2.50
  - max_latency_sec: 120
```

Run on CI for every graph or prompt change affecting routing.

### Regression gates

Block release if:

- Success rate drops > X% vs baseline on golden set
- Cost per task increases > Y% without approval
- New schema breaks contract tests

## SLOs and alerting

| SLO | Example target |
|---|---|
| Workflow availability | 99.5% successful completion (excl. user cancel) |
| p95 latency | < 90s for interactive tier |
| Partial failure rate | < 2% best-effort merges with gaps |

**Alerts:**

- Spike in supervisor retries (routing broken)
- Merge timeouts (fan-out sizing wrong)
- Cost burn anomaly per tenant
- HITL queue age > threshold

Pair with `ai-lead-ops` for incident response; this skill defines **what to measure**.
