---
name: engineering-manager-agent-prompts-evals
description: |
  Guides engineering managers leading teams that own agent prompts, tool schemas, golden eval
  suites, judge programs, and prompt regression CI—org design, hiring, roadmap with PM/risk,
  release governance, and team KPIs for eval quality and prompt stability.
  Use when managing prompt/eval engineers, prioritizing eval backlogs, staffing harness and
  judge programs, or governing prompt releases—not for writing prompts or harnesses
  (prompt-engineer-agent-prompts-evals), vertical AI squad management
  (engineering-manager-vertical-ai-products), or AI platform SRE (ai-lead-ops).
---

# Engineering Manager, Agent Prompts & Evals

## When to Use

- Build or scale a **prompt + eval** engineering function (central or embedded)
- Prioritize **golden set**, harness, and judge work with PM and risk
- Define **release policy** for prompt/tool changes (gates, waivers, rollback)
- **Hire and level** prompt engineers, eval engineers, and tech leads
- Resolve capacity conflicts between **new agents** and **eval debt**
- Report **eval health** (pass rate, slice regressions, judge drift) to leadership
- Partner with `ai-lead-ops` on production incidents tied to prompts

## When NOT to Use

- Author system prompts, tool schemas, or eval cases → `prompt-engineer-agent-prompts-evals`
- General prompt patterns (CoT, few-shot) → `prompt-engineer`
- Full RAG/agent application code → `ai-engineer`
- Vertical AI product roadmap and GTM launches → `engineering-manager-vertical-ai-products`
- Adversarial red-team execution → `ai-redteam`
- Org-wide data or analytics management → `data-manager`

## Related skills

| Need | Skill |
|---|---|
| IC prompt/eval implementation | `prompt-engineer-agent-prompts-evals` |
| Vertical AI EM (broader) | `engineering-manager-vertical-ai-products` |
| AI ops and rollouts | `ai-lead-ops` |
| Risk tier and policy | `ai-risk-governance` |
| Token cost programs | `ai-token-improvement-plan-engineer` |

## Core Workflows

### 1. Org design

Central eval platform vs embedded prompt owners; ratios and interfaces.

**See `references/team_org_prompt_eval.md`.**

### 2. Roadmap and prioritization

Eval debt, new agent coverage, judge calibration, CI investment.

**See `references/roadmap_prioritization.md`.**

### 3. Release governance

Prompt semver gates, waivers, coordination with risk and ops.

**See `references/release_governance.md`.**

### 4. Stakeholder partnerships

PM, applied architect, risk, red-team, platform eng.

**See `references/stakeholder_partnerships.md`.**

### 5. Hiring and development

Levels for prompt/eval specialists.

**See `references/hiring_development.md`.**

### 6. Team metrics

Pass rate, coverage, time-to-golden-case, incident linkage.

**See `references/team_metrics_accountability.md`.**

## Output standards

- Roadmap items name **eval slice**, **prompt surface**, and **risk tier**
- No prompt prod change without documented **baseline vs candidate**
- Waivers require risk sign-off for Tier 1–2 customer-facing agents
- Escalations include trade-offs (scope, date, headcount)

## When to load references

- **Org** → `references/team_org_prompt_eval.md`
- **Roadmap** → `references/roadmap_prioritization.md`
- **Release** → `references/release_governance.md`
- **Stakeholders** → `references/stakeholder_partnerships.md`
- **People** → `references/hiring_development.md`
- **KPIs** → `references/team_metrics_accountability.md`
