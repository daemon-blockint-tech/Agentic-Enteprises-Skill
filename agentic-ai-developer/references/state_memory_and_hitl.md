# State, memory, and human-in-the-loop

## Table of contents

1. [State layers](#state-layers)
2. [Checkpointing and resume](#checkpointing-and-resume)
3. [Memory types](#memory-types)
4. [Tenancy and isolation](#tenancy-and-isolation)
5. [Human-in-the-loop](#human-in-the-loop)
6. [Framework mapping](#framework-mapping)

## State layers

| Layer | Lifetime | Contents | Storage |
|---|---|---|---|
| **Turn context** | Single model call | Messages, tool defs | Ephemeral |
| **Session / thread** | User conversation | History, pending HITL, plan | DB or checkpointer |
| **Run checkpoint** | Durable workflow | Graph node, partial outputs | Checkpointer / workflow engine |
| **Long-term memory** | Cross-session | Preferences, facts, summaries | Vector + metadata store |

Do not stuff everything into the context window—**write** summaries to session state after tool bursts.

## Checkpointing and resume

Checkpoint after:

- Each tool batch or graph node completion
- Before irreversible side effects (pending HITL)
- On graceful shutdown signals

Resume requirements:

- Stable `thread_id` / `run_id`
- Versioned graph or prompt id (pin on resume)
- Serializable state (JSON); no opaque in-memory-only handles

Failure modes:

| Scenario | Behavior |
|---|---|
| Worker crash mid-run | Resume from last checkpoint |
| Deploy new graph version | New runs only; in-flight pinned to old version |
| Corrupt checkpoint | Fail closed; offer user restart with export |

**Pointer:** LangGraph checkpointers, Deep Agents StoreBackend, workflow engines (Temporal-style) each implement persistence—keep your state schema portable.

## Memory types

| Type | Use | Pitfalls |
|---|---|---|
| Scratchpad | Current task notes | Unbounded growth |
| Episodic summary | Prior turns compressed | Summary hallucination |
| Semantic memory | User/org facts | Stale or wrong facts |
| Artifact store | Files, codegen output | ACL leaks |

Policies:

- **Write memory** only via explicit tools (`remember`, `save_note`)
- **Read memory** with filters (user_id, project_id)
- TTL or revision for facts that change (pricing, policies)
- Show users what was remembered; allow delete

Deeper memory **product** design → `ai-memory-developer`; context packing → `ai-context-engineer`.

## Tenancy and isolation

Every persisted record should carry:

- `tenant_id` / `org_id`
- `user_id` (or service principal)
- `thread_id`
- Optional `workspace_id` / `project_id`

Enforce in:

- Checkpointer queries
- Tool credential resolution
- Memory retrieval filters

Never share checkpoints across tenants—even in “shared” dev environments.

## Human-in-the-loop

**When to require approval:**

| Tier | Examples |
|---|---|
| 0 | Read-only tools |
| 1 | Reversible writes (drafts, branches) |
| 2 | Customer-visible or financial actions |
| 3 | Destructive, legal, or security-sensitive |

HITL flow:

```
model requests tool → runtime intercepts → queue approval UI
→ approve | edit args | reject → resume or abort run
```

Implementation notes:

- **Edit args:** validate against schema before execute
- **Reject:** pass reason to model once; do not auto-retry same call
- **Timeout:** default deny or safe fallback; notify user
- Audit log: who approved, prior vs new args, timestamp

Interrupt patterns (graph runtimes): pause at named nodes; resume with `Command` carrying human decision.

## Framework mapping

| Concern | LangGraph-style | Deep Agents-style | Durable workflow |
|---|---|---|---|
| Thread state | Checkpointer + thread_id | StateBackend / StoreBackend | Workflow state |
| Interrupt | `interrupt()` | HITL middleware | Human task activity |
| Long memory | Store namespace | CompositeBackend routes | External DB |

Choose one primary persistence story per product; avoid dual writes without reconciliation.
