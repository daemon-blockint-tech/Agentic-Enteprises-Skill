# Reference architectures

## Table of contents

1. [Pattern selection](#pattern-selection)
2. [Enterprise Q&A RAG](#enterprise-qa-rag)
3. [Task agent with tools](#task-agent-with-tools)
4. [Workflow automation](#workflow-automation)
5. [Anti-patterns](#anti-patterns)

## Pattern selection

| Pattern | Best for | Avoid when |
|---|---|---|
| **RAG Q&A** | Knowledge lookup, citations needed | Real-time transactional writes |
| **Agent + tools** | Multi-step tasks, APIs | Simple FAQ; unbounded tool risk |
| **Fine-tune** | Style/format, domain jargon stable | Facts change weekly; small data |
| **Rules + LLM** | Deterministic guardrails | Need open-ended reasoning |
| **Human-in-loop** | High stakes actions | Latency-sensitive chat only |

Default: **RAG + small model router** before full agent autonomy.

## Enterprise Q&A RAG

```
[Sources] → ingest → chunk → embed → vector store (partitioned)
                                              ↑
User → API → authz filter → retrieve → rerank → LLM → response + citations
                ↓
           audit log (ids, not full doc body if sensitive)
```

**Design choices:**

- Sync vs async ingest; SLA for freshness
- Chunk strategy per doc type (PDF vs wiki)
- Citation required for external-facing answers
- Grounding failure → "I don't know" not hallucinate

Implement with `ai-engineer`; index design with `data-architect` if warehouse-backed.

## Task agent with tools

```
User → orchestrator → [plan] → tool calls (CRM, ticket, search) → synthesize
              ↓
        policy layer (allowlist tools, max steps, budgets)
```

**Controls:**

- Tool allowlist per role/tenant
- Idempotent tools where possible
- Confirmation step before write tools
- Token and step caps (`ai-token-improvement-plan-engineer` for program)

## Workflow automation

Long-running flows (batch summarization, ticket triage):

- Queue + worker; not synchronous chat path
- Batch API for cost
- Dead-letter and human review queue

## Anti-patterns

- **One giant prompt** with all docs — use retrieval
- **Shared vector index** across tenants without hard filters
- **Agent with internet** on enterprise corp data path
- **Logging full prompts** with PII to third-party analytics
- **Fine-tune** to replace access control — model cannot enforce ACLs
