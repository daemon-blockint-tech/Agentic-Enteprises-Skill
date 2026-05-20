# Agent loop, tools, and MCP

## Table of contents

1. [Loop patterns](#loop-patterns)
2. [Stop conditions](#stop-conditions)
3. [Tool schema design](#tool-schema-design)
4. [MCP integration](#mcp-integration)
5. [Execution sandbox](#execution-sandbox)
6. [Error handling](#error-handling)

## Loop patterns

| Pattern | When to use | Risk |
|---|---|---|
| **ReAct** | General tasks; model picks tools each turn | Runaway loops if stop rules weak |
| **Plan-then-execute** | Multi-step projects with stable plan | Plan drift if world changes mid-run |
| **Tool-first** | Deterministic pipelines with LLM routing | Less flexible for novel tasks |
| **Graph nodes** | Branching, retries, human interrupts | Higher implementation cost |

Minimal loop invariant:

```
while not done:
  model → (tool_call | final_message)
  if tool_call: execute → append observation
  else: done = validate(final_message)
```

Keep **one authoritative stop signal** (final tool, structured output, or explicit `done` flag).

## Stop conditions

Enforce at least two independent limits:

- **Step cap** (e.g., 8–15 tool rounds for interactive; higher for batch)
- **Token or cost budget** per session
- **Wall-clock timeout** (client + server)
- **Final-answer tool** or JSON schema that ends the loop

Reject “silent stop” when the model returns prose without calling the completion tool.

## Tool schema design

**Do:**

- Name tools by outcome (`search_incidents`, not `tool1`)
- Description: when to use **and** when **not** to use
- Required fields explicit; use enums for fixed sets
- Return **structured** JSON; truncate large payloads with pointers
- Version tools when breaking (`search_v2`)

**Avoid:**

- Mega-tools that bundle unrelated actions
- Free-form string blobs where enums suffice
- Returning raw credentials, PII, or full HTTP bodies by default

Example policy block in system prompt:

> Call at most one write tool per turn. Prefer read tools to gather facts before `create_*` or `delete_*`.

## MCP integration

Model Context Protocol servers expose tools/resources to agents. Integration checklist:

| Step | Action |
|---|---|
| Discover | List tools from server; map to internal registry |
| Auth | Per-user or per-tenant tokens; never global superuser in prod |
| Transport | stdio (local), SSE/HTTP (remote); handle reconnect |
| Schema | Normalize MCP tool schema → your runtime’s tool format |
| Limits | Rate limit per server; circuit-break on 5xx bursts |
| Testing | Contract tests with recorded fixtures |

**Pointer:** LangGraph / Deep Agents / Cursor SDK each wrap MCP differently—implement the same contracts (auth, timeout, redaction) in your adapter layer.

## Execution sandbox

| Tool class | Sandbox |
|---|---|
| Read-only search | Network egress allowlist; no shell |
| DB query | Read replica; row-level security; query timeout |
| Write / delete | Idempotency key; HITL for prod |
| Code execution | Isolated VM or WASM; no host filesystem |
| Browser | Dedicated browser MCP; domain allowlist |

Run tools **out of process** when possible; pass only sanitized args and cap output bytes.

## Error handling

| Error type | Model sees | Runtime does |
|---|---|---|
| Transient (429, timeout) | Short error + retry hint | Backoff retry (max 2–3) |
| Validation | Field-level message | No retry; fix args |
| Authorization | “Not permitted” | No retry; audit log |
| Unknown | Generic failure | Stop or HITL after N failures |

Rules:

- Surface each tool error **once** per attempt; do not spam duplicate observations
- After **K** consecutive tool failures, stop and escalate (HITL or user message)
- Log full error server-side; redact secrets in model-facing text
