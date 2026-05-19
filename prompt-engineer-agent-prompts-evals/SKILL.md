---
name: prompt-engineer-agent-prompts-evals
description: |
  Guides prompt engineering for tool-using agents—system and developer prompts, tool schemas,
  handoffs and subagents, golden datasets, offline eval harnesses, regression CI, LLM-as-judge
  rubrics, and release gates for prompt changes.
  Use when authoring agent prompts, building eval suites for agents or copilots, debugging
  tool-selection failures, designing judge rubrics, or gating prompt deploys—not for general
  few-shot/CoT patterns only (prompt-engineer), full RAG pipelines (ai-engineer), adversarial
  red-team campaigns (ai-redteam), or AI ops SLOs (ai-lead-ops).
  For managing prompt/eval teams, release policy, and hiring, use
  engineering-manager-agent-prompts-evals—not this skill.
---

# Prompt Engineer — Agent Prompts & Evals

## When to Use

- Write or refactor **system/developer prompts** for agents with tools
- Design **tool descriptions** and parameter schemas the model must choose correctly
- Build **golden datasets** and scenario suites (multi-turn, failures, edge cases)
- Implement **offline eval harnesses** and CI regression for prompts
- Define **LLM-as-judge** rubrics and human calibration samples
- Set **release gates** when prompts or tool lists change
- Debug **wrong tool**, **looping**, or **format break** in agent traces

## When NOT to Use

- General prompt patterns without agent/eval focus → `prompt-engineer`
- End-to-end RAG indexing, retrieval, serving → `ai-engineer`
- Jailbreak and abuse red-team engagements → `ai-redteam`
- Org-wide model rollout and incident ops → `ai-lead-ops`
- Token cost program across product → `ai-token-improvement-plan-engineer`
- Vertical squad management and launch PM → `engineering-manager-vertical-ai-products`
- Prompt/eval team management and governance → `engineering-manager-agent-prompts-evals`

## Related skills

| Need | Skill |
|---|---|
| Broad prompt design and production guardrails | `prompt-engineer` |
| RAG, agents in production code | `ai-engineer` |
| Launch eval gates (manager view) | `engineering-manager-vertical-ai-products` |
| Risk tier and policy | `ai-risk-governance` |
| Adversarial testing | `ai-redteam` |

## Core Workflows

### 1. Agent prompt structure

System vs developer messages, tools block, constraints, handoffs.

**See `references/agent_system_prompts.md`.**

### 2. Eval datasets

Golden sets, coverage matrix, synthetic and SME-labeled examples.

**See `references/eval_dataset_design.md`.**

### 3. Harness and metrics

Offline runs, pass/fail, tool accuracy, trajectory checks.

**See `references/eval_harness_patterns.md`.**

### 4. Judges and rubrics

LLM judge design, bias controls, human agreement.

**See `references/llm_judge_rubrics.md`.**

### 5. Versioning and regression

Prompt semver, baselines, CI gates, rollback.

**See `references/prompt_versioning_regression.md`.**

### 6. Scenario catalog

Multi-turn, tool error, refusal, escalation cases.

**See `references/agent_eval_scenarios.md`.**

## Output standards

- Every eval case has **input**, **expected behavior** (not always exact text), **tags**
- Tool schema changes include **eval delta** in PR description
- Judge rubrics published with **scoring scale** and known failure modes
- No production prompt change without **baseline comparison** on golden set

## When to load references

- **Prompts** → `references/agent_system_prompts.md`
- **Data** → `references/eval_dataset_design.md`
- **Harness** → `references/eval_harness_patterns.md`
- **Judges** → `references/llm_judge_rubrics.md`
- **CI** → `references/prompt_versioning_regression.md`
- **Scenarios** → `references/agent_eval_scenarios.md`
