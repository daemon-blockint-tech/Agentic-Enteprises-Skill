# Inter-agent protocols and messaging

## Table of contents

1. [Message envelope](#message-envelope)
2. [Handoff payload](#handoff-payload)
3. [A2A-style patterns (conceptual)](#a2a-style-patterns-conceptual)
4. [Versioning and compatibility](#versioning-and-compatibility)
5. [Delivery semantics](#delivery-semantics)
6. [Security and trust](#security-and-trust)

## Message envelope

Use a consistent envelope for **every** inter-agent message (in-process or via queue):

```json
{
  "envelope_version": "1.0",
  "message_id": "uuid",
  "correlation_id": "workflow-run-uuid",
  "causation_id": "parent-message-uuid",
  "timestamp": "ISO-8601",
  "from": { "agent_id": "planner-1", "role": "planner" },
  "to": { "agent_id": "executor-3", "role": "executor" },
  "intent": "assign_work",
  "payload_version": "2.1",
  "payload": { },
  "artifacts": [ { "uri": "...", "type": "application/json", "hash": "..." } ],
  "constraints": {
    "deadline": "ISO-8601",
    "token_budget": 8000,
    "must_not": ["call_delete_tool"]
  }
}
```

**Field rules:**

- `correlation_id` is stable for the user-visible job across all agents
- `causation_id` links to the message that triggered this one (trace tree)
- Large blobs go in `artifacts`, not inline in `payload`
- `constraints` are machine-enforced where possible, not suggestions

## Handoff payload

Minimum handoff content when transferring responsibility:

| Field | Purpose |
|---|---|
| `goal` | What success looks like for the receiver |
| `context_summary` | Compressed thread/history safe for receiver |
| `open_questions` | Explicit unknowns |
| `artifacts` | Files, code, retrieval results already produced |
| `decisions_made` | Irreversible choices upstream |
| `tool_results_digest` | Hashes or summaries, not raw secrets |

**Bad handoff:** "Continue the previous conversation" with full chat log pasted.

**Good handoff:** Structured work order referencing artifact URIs and schema version.

### Example work order

```json
{
  "work_order_id": "wo-42",
  "goal": "Produce vendor comparison table for 3 shortlisted CRMs",
  "inputs": {
    "requirements_artifact": "s3://bucket/reqs.v2.json",
    "shortlist": ["vendor_a", "vendor_b", "vendor_c"]
  },
  "output_schema": "crm_comparison_table.v1",
  "acceptance_criteria": [
    "All rows cite source URL",
    "No pricing without retrieved_at date"
  ]
}
```

## A2A-style patterns (conceptual)

Agent-to-agent (A2A) ecosystems emphasize **discoverable agents** with advertised capabilities. Adapt conceptually without binding to one vendor spec:

| Pattern | Description |
|---|---|
| **Agent card** | Metadata: name, skills, input/output schemas, auth requirements |
| **Task delegation** | Client sends task; remote agent returns task id + status |
| **Streaming updates** | Partial results for long tasks (progress events) |
| **Capability negotiation** | Receiver accepts or rejects task with reason |

**Mapping to internal systems:**

- Agent card → service registry or config manifest in repo
- Task delegation → queue message with `work_order` schema
- Streaming → event bus or webhook callbacks on `correlation_id`

**Interoperability checklist:**

- [ ] Schemas published in registry with owner team
- [ ] Auth between agents uses short-lived tokens scoped to workflow
- [ ] Timeouts and cancellation propagated on delegation chain

## Versioning and compatibility

| Rule | Rationale |
|---|---|
| Semantic version on `payload` types | Consumers declare supported range |
| Reject unknown `envelope_version` | Fail closed |
| Additive fields only in minor versions | Forward compatibility |
| Breaking changes require new message type | Avoid silent mis-parse |

**Migration:** support N and N-1 payload versions during rollout; log deprecation warnings.

## Delivery semantics

| Semantic | Multi-agent implication |
|---|---|
| **At-most-once** | May lose message; use when duplicate is worse than miss |
| **At-least-once** | Requires idempotent handlers and dedup keys |
| **Exactly-once** | Hard; approximate with idempotency store + outbox |

**Idempotency key:** `hash(correlation_id + intent + payload_hash + target_agent)`.

**Duplicate handling:**

- Executor checks idempotency store before side effects
- Merger uses deterministic reduce for same inputs

## Security and trust

- Treat **all** inter-agent payloads as potentially influenced by untrusted upstream agents or tools
- Validate against JSON Schema before acting
- Never pass raw credentials in messages—reference secret handles
- Sign or MAC messages crossing process boundaries when threat model requires
- Log message metadata; redact payload bodies in production traces by default

**Prompt injection across agents:** a compromised worker can poison handoffs. Mitigations:

- Schema validation and allowlisted fields
- Critic/supervisor with no tool access reviews handoffs for policy
- Separate context namespaces per agent (no full transcript sharing)
