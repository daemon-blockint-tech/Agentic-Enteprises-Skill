---
name: ai-context-engineer
description: |
  Guides context engineering for LLM systems—assembling prompts, budgeting tokens, prioritizing
  sources, compressing history, caching, structured context blocks, and debugging context-related
  failures (lost instructions, overflow, distraction).
  Use when designing what enters the model context each turn, optimizing cost/latency via context
  strategy, building context pipelines for agents, implementing summarization or compaction, or
  fixing "model ignored X" issues—not for persistent memory store design (ai-memory-developer),
  full RAG index pipelines (ai-engineer), or AI org operations (ai-lead-ops). For a structured
  token/cost improvement roadmap with phased initiatives and KPIs, use
  ai-token-improvement-plan-engineer. For commercial/enterprise AI solution architecture (RAG, copilots,
  platform selection), use applied-ai-architect-commercial-enterprise. Token research and
  compression ablations: research-engineer-scientist-tokens.
---

# AI Context Engineer

## When to Use

- Designing what enters the model context each turn
- Optimizing cost/latency via context strategy and token budgeting
- Building context pipelines for agents (prefix, retrieval, history, user input)
- Implementing summarization, compaction, or rolling history
- Debugging context-related failures (lost instructions, overflow, distraction, ignored constraints)
- Choosing delimiters, XML blocks, or structured context formats

## When NOT to Use

- Persistent memory store design or long-term recall architecture → `ai-memory-developer`
- Full RAG ingest/chunk/embed/index pipelines → `ai-engineer`
- AI org operations, release governance, or SLOs → `ai-lead-ops`
- Structured token/cost improvement roadmaps with phased KPIs → `ai-token-improvement-plan-engineer`
- Commercial/enterprise AI solution architecture → `applied-ai-architect-commercial-enterprise`

## Related skills

| Need | Skill |
|---|---|
| Memory stores and long-term recall | `ai-memory-developer` |
| RAG ingest/chunk/embed | `ai-engineer` |
| System and tool prompts | `prompt-engineer` |
| Red-team injection via context | `ai-redteam` |
| Cost and production SLAs | `ai-lead-ops` |
| Token reduction program and roadmap | `ai-token-improvement-plan-engineer` |
| Commercial/enterprise AI architecture | `applied-ai-architect-commercial-enterprise` |
| Token efficiency research and ablations | `research-engineer-scientist-tokens` |

## Core Workflows

### 1. Context budget and layout

**Allocate tokens (example 128k window):**

| Block | Budget % | Priority |
|---|---|---|
| System policy + tools | 15–25% | Fixed, never truncated |
| Retrieved docs / memory | 30–45% | High, reranked |
| Conversation history | 25–40% | Compress oldest first |
| User current message | 5–10% | Never drop |

Use explicit XML/markdown sections: `<policy>`, `<tools>`, `<context>`, `<history>`, `<user>`.

**See `references/context_layout.md` for templates and delimiter rules.**

### 2. History management

| Strategy | When |
|---|---|
| Full recent window | Short chats, high-stakes instructions in last N turns |
| Rolling summary | Long sessions; summarize every K turns |
| Anchor messages | Pin system + key user constraints; summarize middle |
| Structured state | Replace chat with JSON task state for agents |

Preserve: user goals, constraints, unresolved tool errors, pending confirmations.

**See `references/history_compression.md` for summarization prompts and pitfalls.**

### 3. Retrieval into context

1. Query from user message + state summary
2. Retrieve candidates (RAG chunks, memories, tool outputs)
3. Deduplicate overlapping passages
4. Order by relevance; add source labels
5. Truncate with sentence boundaries; show "[truncated]" when cut

**See `references/retrieval_packing.md` for packing algorithms and citation format.**

### 4. Caching and prefetch

- Cache stable prefix (system + tools) where provider supports prompt caching
- Prefetch retrieval while user types (optional)
- Invalidate cache on prompt version change

**See `references/caching_prefetch.md` for provider notes and invalidation.**

### 5. Debug context failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Ignored instruction | Buried in middle / summarized away | Move to system or last user turn |
| Hallucinated doc | Weak retrieval | Raise threshold; require citation |
| Overflow error | No budget enforcement | Pre-flight token count; compress |
| Tool confusion | Ambiguous schemas in context | Separate tool block; shorten descriptions |

Log token counts per block in dev/staging.

**See `references/debugging_context.md` for instrumentation checklist.**

## When to load references

- **Layout and budgets** → `references/context_layout.md`
- **Summarization** → `references/history_compression.md`
- **RAG/memory packing** → `references/retrieval_packing.md`
- **Caching** → `references/caching_prefetch.md`
- **Debugging** → `references/debugging_context.md`
