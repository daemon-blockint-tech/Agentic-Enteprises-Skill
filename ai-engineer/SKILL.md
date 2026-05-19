---
name: ai-engineer
description: |
  Guides production AI engineering—LLM apps, RAG, agents, eval harnesses, observability, cost/latency,
  and safe deployment. Use when building chatbots, copilots, retrieval, agent workflows, model routing,
  or LLM API integration—not research synthesis (ai-researcher), AI policy (ai-risk-governance),
  red-team (ai-redteam), prompt-only work (prompt-engineer), non-AI ADRs (senior-system-architecture),
  token programs (ai-token-improvement-plan-engineer), solution architecture
  (applied-ai-architect-commercial-enterprise), skills portfolio (ai-skill-manager), or vertical AI
  engineering management (engineering-manager-vertical-ai-products).
  Agent prompt authoring and eval harness design: prompt-engineer-agent-prompts-evals.
---

# AI Engineer

## When to Use

- Building chatbots, copilots, or retrieval-augmented generation systems
- Designing multi-step agent workflows with tool use
- Integrating OpenAI, Anthropic, or local models into products
- Setting up RAG pipelines (chunk, embed, index, retrieve, rerank, generate)
- Building evaluation harnesses and regression suites for LLM features
- Optimizing cost/latency through model routing, caching, or context strategy
- Planning safe deployment of generative features (canary, kill switch, monitoring)

## When NOT to Use

- Academic literature synthesis or research methodology → `ai-researcher`
- Organizational AI policy, regulation, or risk tiering → `ai-risk-governance`
- Adversarial safety testing and jailbreak campaigns → `ai-redteam`
- Prompt-only tuning without system architecture changes → `prompt-engineer`
- Enterprise-wide non-AI system integration ADRs → `senior-system-architecture`
- Token/cost improvement program planning and roadmap → `ai-token-improvement-plan-engineer`
- Commercial/enterprise AI solution architecture → `applied-ai-architect-commercial-enterprise`
- Skills portfolio governance and batch validation → `ai-skill-manager`
- Agent prompts, golden evals, judge rubrics → `prompt-engineer-agent-prompts-evals`

## Related skills

| Need | Skill |
|---|---|
| Prompt templates and agent message design | `prompt-engineer` |
| Offline experiments, statistics, classical ML | `data-scientist` |
| Papers, benchmarks, research methodology | `ai-researcher` |
| Policies, model cards, governance | `ai-risk-governance` |
| Red-team and jailbreak campaigns | `ai-redteam` |
| Persistent memory design | `ai-memory-developer` |
| Context window and token budgeting | `ai-context-engineer` |
| Token cost improvement plan and roadmap | `ai-token-improvement-plan-engineer` |
| AI production ops and release governance | `ai-lead-ops` |
| Cross-system boundaries and platform ADRs | `senior-system-architecture` |
| Commercial/enterprise AI architecture | `applied-ai-architect-commercial-enterprise` |
| Agent skills catalog and validation | `ai-skill-manager` |

## Core Workflows

### 1. Solution shaping

1. Define user job, success metric, and failure modes
2. Decide: single LLM call vs RAG vs multi-step agent
3. Choose model tier (quality vs cost vs latency)
4. Identify data sources, PII boundaries, and retention
5. Plan human-in-the-loop for high-risk actions

**See `references/solution_patterns.md` for RAG vs fine-tune vs agent decision tree.**

### 2. RAG pipeline

```
ingest → chunk → embed → index → retrieve → rerank → generate → cite
```

**Checklist:**

- [ ] Chunk size tuned on eval set
- [ ] Metadata filters for tenancy/ACL
- [ ] Hybrid search if keyword matters
- [ ] Ground answers with citations; refuse when context insufficient
- [ ] Refresh index on source updates

**See `references/rag_pipeline.md` for chunking, eval metrics, and freshness.**

### 3. Agents and tools

- Tools: narrow schemas, idempotent where possible, timeouts
- Loop: plan → act → observe → stop condition
- Cap iterations and token budget
- Log tool calls for audit; redact secrets in traces

**See `references/agents_tools.md` for ReAct patterns and failure handling.**

### 4. Evaluation before launch

| Layer | Measure |
|---|---|
| Retrieval | Recall@k, MRR on golden questions |
| Generation | Faithfulness, answer relevance (LLM-judge + human sample) |
| Safety | Refusal rate on policy violations |
| Ops | p95 latency, cost per session |

Ship only when regression suite passes on CI for golden set.

**See `references/evaluation_ops.md` for datasets, CI eval, and monitoring.**

### 5. Production operations

- Version prompts and models; canary new versions
- Monitor drift, error rate, tool failures, spend
- Kill switch for model or feature flag
- Incident runbook for toxic output or data leak

**See `references/evaluation_ops.md` for production monitoring.**

## When to load references

- **Architecture choices** → `references/solution_patterns.md`
- **RAG implementation** → `references/rag_pipeline.md`
- **Agents and tools** → `references/agents_tools.md`
- **Eval and production** → `references/evaluation_ops.md`
