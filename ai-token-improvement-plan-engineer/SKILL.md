---
name: ai-token-improvement-plan-engineer
description: |
  Guides creation of AI token and cost improvement plans—baseline audits, spend attribution,
  optimization initiative backlog (prompt, context, model routing, RAG, agents), impact estimates,
  quality guardrails, measurement KPIs, and phased rollout with owners.
  Use when building a token reduction roadmap, cost optimization program, LLM unit-economics
  improvement plan, or executive brief on cutting inference spend without breaking evals—not for
  hands-on context layout implementation (ai-context-engineer), single-prompt rewrites
  (prompt-engineer), RAG pipeline build (ai-engineer), or AI ops cadence and vendor governance
  (ai-lead-ops). For end-to-end commercial/enterprise AI solution architecture before cost programs,
  use applied-ai-architect-commercial-enterprise. Empirical token studies and ablations:
  research-engineer-scientist-tokens.
---

# AI Token Improvement Plan Engineer

## When to Use

- Audit where tokens are spent (by feature, model, tenant, turn type)
- Prioritize cost-saving initiatives with estimated savings and risk
- Draft a phased improvement plan with metrics and rollback criteria
- Define eval gates so cost cuts do not regress quality or safety
- Brief leadership on trade-offs (model tier, context size, agent depth)

## When NOT to Use

- Implement context packing or compression code → `ai-context-engineer`
- Rewrite one prompt or agent tool schema → `prompt-engineer`
- Build RAG ingest, chunking, or agent runtime → `ai-engineer`
- Weekly cost review ritual and release governance → `ai-lead-ops`
- Memory store architecture → `ai-memory-developer`
- Adversarial safety testing → `ai-redteam`
- AI policy and regulatory mapping → `ai-risk-governance`

## Related skills

| Need | Skill |
|---|---|
| Context budget and truncation | `ai-context-engineer` |
| Prompt patterns and eval of wording | `prompt-engineer` |
| RAG and agent implementation | `ai-engineer` |
| Production ops and cost reviews | `ai-lead-ops` |
| Memory write/read policy | `ai-memory-developer` |
| Safety regression testing | `ai-redteam` |
| AI solution architecture (commercial/enterprise) | `applied-ai-architect-commercial-enterprise` |
| Token efficiency experiments and benchmarks | `research-engineer-scientist-tokens` |

## Core Workflows

### 1. Scope and baseline

Define:

- **Surface area** — chat, copilot, batch, agents, embeddings-only
- **Time window** — 7/30 days; exclude anomalies (launches, incidents)
- **Segmentation** — model, feature flag, tenant tier, environment

Collect baseline metrics (see `references/token_audit.md`).

Deliverable: **current state** table with top 5 cost drivers (≥70% of spend if possible).

### 2. Categorize spend

Bucket each driver:

| Category | Examples |
|---|---|
| Input bloat | Long system prompts, duplicated docs, full chat history |
| Output bloat | Verbose defaults, no max_tokens, unconstrained agents |
| Model choice | Opus-class for simple classification |
| Retrieval | Over-fetching chunks, huge tool results in context |
| Agent loops | Extra tool rounds, retry storms |
| Infrastructure | Re-embedding unchanged corpora, log payloads in prompts |

Tag **fixed per request** vs **scales with users/sessions**.

### 3. Initiative backlog

For each idea record:

- Description and owner team
- **Estimated savings** (% tokens or $/month) with assumptions
- **Effort** (S/M/L) and dependencies
- **Quality risk** (low/med/high) and required evals
- **Measurement** — metric that proves success

Prioritize with impact × confidence ÷ effort; never ship without eval plan.

**See `references/improvement_backlog.md` and `references/optimization_playbook.md`.**

### 4. Quality and safety guardrails

Every initiative must list:

- Golden-set evals (task accuracy, format)
- Safety set (if user-facing)
- Latency check (p95)
- Rollback trigger (e.g., CSAT drop, eval regression >X%)

**See `references/measurement_and_kpis.md`.**

### 5. Phased plan

Typical phases:

| Phase | Focus | Duration |
|---|---|---|
| 0 — Measure | Instrumentation, dashboards, attribution | 1–2 weeks |
| 1 — Quick wins | max_tokens, model routing, prompt trim, cache | 2–4 weeks |
| 2 — Structure | RAG top-k, history compression, tool output limits | 4–8 weeks |
| 3 — Architecture | Agent budget caps, routing policies, batch/offline | 8+ weeks |

Each phase: goals, initiatives, owners, exit criteria.

**See `references/rollout_plan.md`.**

### 6. Executive summary

```markdown
## Situation — spend and growth rate
## Target — $ or tokens/session goal by date
## Top drivers — ranked list
## Plan — 3–5 initiatives per phase
## Risks — quality, latency, eng capacity
## Asks — budget, headcount, eval time
```

Hand ongoing ops to `ai-lead-ops` after plan approval.

## When to load references

- **Baseline and attribution** → `references/token_audit.md`
- **Backlog template and scoring** → `references/improvement_backlog.md`
- **Technique catalog** → `references/optimization_playbook.md`
- **KPIs and eval gates** → `references/measurement_and_kpis.md`
- **Phasing and rollback** → `references/rollout_plan.md`
