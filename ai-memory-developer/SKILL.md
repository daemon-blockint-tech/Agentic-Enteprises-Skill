---
name: ai-memory-developer
description: |
  Guides design and implementation of AI agent and application memory—short-term conversation state,
  long-term user/tenant memory, episodic vs semantic stores, consolidation, retrieval, forgetting,
  privacy retention, and eval of memory quality.
  Use when building persistent memory for copilots, designing memory APIs, choosing vector or graph
  stores, implementing memory write/read policies, debugging wrong or stale memories, or tuning
  what the model should remember across sessions—not for general RAG document search (ai-engineer),
  context window packing and token budgets (ai-context-engineer), AI team operations cadence
  (ai-lead-ops), or org-wide token cost improvement roadmaps (ai-token-improvement-plan-engineer).
---

# AI Memory Developer

## When to Use

- Building persistent memory for copilots, agents, or conversational AI
- Designing memory APIs (read/write/consolidate/forget)
- Choosing between vector stores, graph databases, or structured DBs for memory
- Implementing memory write/read policies and ACLs
- Debugging wrong, stale, or hallucinated memories
- Tuning what the model should remember across sessions (episodic vs semantic)
- Planning GDPR deletion paths and privacy retention for stored memories
- Evaluating memory quality (recall, precision, isolation)

## When NOT to Use

- General RAG document search or indexing pipelines → `ai-engineer`
- Context window packing, token budgets, or compression → `ai-context-engineer`
- AI team operations, release governance, or SLOs → `ai-lead-ops`
- Org-wide token cost improvement roadmaps → `ai-token-improvement-plan-engineer`

## Related skills

| Need | Skill |
|---|---|
| End-to-end LLM app, RAG, agents | `ai-engineer` |
| Context assembly and compression | `ai-context-engineer` |
| Prompt and tool message design | `prompt-engineer` |
| PII retention and governance | `ai-risk-governance` |
| Production monitoring and incidents | `ai-lead-ops` |
| Token cost program and phased savings plan | `ai-token-improvement-plan-engineer` |

## Core Workflows

### 1. Memory model design

**Classify memory types:**

| Type | Lifetime | Examples | Store |
|---|---|---|---|
| Working | Single turn / tool loop | Tool results, scratchpad | In-context only |
| Session | Chat session | Current task state | Redis / thread store |
| User long-term | Cross-session | Preferences, facts user stated | Vector + structured DB |
| Organizational | Shared | Docs, policies | RAG index (see `ai-engineer`) |

**Design decisions:**

1. What may be written automatically vs requires user confirmation?
2. Per-tenant isolation and ACL on every read/write
3. TTL and deletion (GDPR erase path)
4. Conflict resolution when new fact contradicts old

**See `references/memory_architecture.md` for patterns and anti-patterns.**

### 2. Write path (ingestion to memory)

```
observe → extract candidates → score importance → dedupe → persist → index
```

**Checklist:**

- [ ] Extract only durable facts, not transient chit-chat
- [ ] Attach provenance (message ID, timestamp, source)
- [ ] Dedupe with embedding similarity + entity linking
- [ ] Never store secrets, raw payment data, or full medical records unless required and approved

**See `references/write_consolidation.md` for extraction prompts and consolidation jobs.**

### 3. Read path (retrieval for generation)

1. Build query from current user message + session summary
2. Retrieve top-k memories with metadata filters (`user_id`, `tenant_id`)
3. Rerank; drop below relevance threshold
4. Inject into context in structured block (see `ai-context-engineer`)
5. Cite memory IDs in logs for debugging

**See `references/read_retrieval.md` for ranking and injection formats.**

### 4. Forgetting and maintenance

| Trigger | Action |
|---|---|
| User delete request | Hard delete all user memories |
| TTL expired | Archive or purge |
| Low usefulness score | Decay or summarize away |
| Contradiction | Supersede old record; keep audit trail |

Run nightly consolidation: merge episodic notes into semantic summaries.

**See `references/write_consolidation.md` for consolidation algorithms.**

### 5. Evaluation

| Test | Pass criteria |
|---|---|
| Write accuracy | Gold facts appear in store after session |
| Recall | Question answerable from prior session |
| Precision | Irrelevant memories not retrieved |
| Isolation | Tenant A never sees tenant B |
| Forgetting | Deleted user has zero retrievable memories |

**See `references/memory_eval.md` for datasets and regression harness.**

## When to load references

- **Architecture and stores** → `references/memory_architecture.md`
- **Write and consolidation** → `references/write_consolidation.md`
- **Read and ranking** → `references/read_retrieval.md`
- **Evaluation** → `references/memory_eval.md`
