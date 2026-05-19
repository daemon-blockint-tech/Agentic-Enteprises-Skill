---
name: engineering-manager-vertical-ai-products
description: |
  Guides engineering managers leading vertical AI product teams—industry or domain-specific
  copilots and AI features (not horizontal platform)—org design, hiring, roadmap with PM and GTM,
  vertical launch governance (eval, safety, cost), squad capacity, and escalation across shared
  AI platform and domain experts.
  Use when managing engineers shipping vertical AI products, prioritizing domain AI backlogs,
  staffing vertical squads, or aligning AI feature GA with sales and compliance—not for AI
  architecture ADRs (applied-ai-architect-commercial-enterprise), hands-on RAG/agents
  (ai-engineer), AI platform SRE and model rollout ops (ai-lead-ops), analytics marts
  (analytics-data-engineering-manager-product), or generic TPM programs   (technical-program-manager).
  For agent prompt and eval harness work (not people management), use
  prompt-engineer-agent-prompts-evals.
  For managing the prompt/eval function (hiring, golden CI policy, judge program), use
  engineering-manager-agent-prompts-evals.
---

# Engineering Manager, Vertical AI Products

## When to Use

- Build or scale **vertical AI product engineering** (domain squads, not central platform only)
- Prioritize vertical backlog with **PM, GTM, and domain SMEs**
- Staff and develop **AI engineers, fullstack, and tech leads** on vertical lines
- Run **launch governance** for customer-facing AI (eval, risk tier, kill switch)
- Resolve **platform vs vertical** build conflicts and shared component roadmaps
- Set **team KPIs** (ship cadence, eval regression, incidents, cost per vertical)
- Escalate vertical-specific compliance or data-boundary issues

## When NOT to Use

- AI solution architecture and multi-tenant ADRs → `applied-ai-architect-commercial-enterprise`
- Implement RAG, agents, eval code → `ai-engineer`
- AI production ops, vendor SLOs, org-wide model release process → `ai-lead-ops`
- AI policy registers and regulatory mapping → `ai-risk-governance`
- Analytics engineering and dbt marts → `analytics-data-engineering-manager-product`
- Company-wide non-AI programs → `technical-program-manager`
- UX research and interaction design → `product-designer`

## Related skills

| Need | Skill |
|---|---|
| Commercial/enterprise AI architecture | `applied-ai-architect-commercial-enterprise` |
| Build and ship AI features | `ai-engineer` |
| AI ops, incidents, rollout governance | `ai-lead-ops` |
| Risk tiering and policy | `ai-risk-governance` |
| Red-team before major launch | `ai-redteam` |
| Token/cost improvement program | `ai-token-improvement-plan-engineer` |
| Vertical fullstack delivery | `senior-fullstack-developer` |
| Product analytics data | `analytics-data-engineering-manager-product` |

## Core Workflows

### 1. Vertical squad org design

Hub platform vs vertical pods; domain SME interfaces; ratios.

**See `references/vertical_team_org.md`.**

### 2. Roadmap and vertical bets

Platform leverage vs bespoke vertical logic; capacity and bet sizing.

**See `references/vertical_roadmap_prioritization.md`.**

### 3. AI feature launch governance

Eval gates, risk tier, rollback, hypercare — coordinate with ops and risk.

**See `references/ai_feature_launch_governance.md`.**

### 4. Stakeholder partnerships

PM, sales, solutions, legal, horizontal AI platform.

**See `references/stakeholder_vertical_partnerships.md`.**

### 5. Hiring and development

IC/lead levels for vertical AI product engineering.

**See `references/hiring_development_vertical.md`.**

### 6. Team metrics and accountability

Delivery, quality, safety, unit economics by vertical.

**See `references/team_metrics_vertical_ai.md`.**

## Output standards

- Roadmap items: **vertical outcome**, **AI capability**, **platform dependency**, **owner**
- No GA without signed eval/risk checklist for customer-facing AI
- Escalations include trade-offs (scope, date, platform build vs fork)
- Architecture changes route through `applied-ai-architect-commercial-enterprise`

## When to load references

- **Org** → `references/vertical_team_org.md`
- **Roadmap** → `references/vertical_roadmap_prioritization.md`
- **Launch** → `references/ai_feature_launch_governance.md`
- **Stakeholders** → `references/stakeholder_vertical_partnerships.md`
- **People** → `references/hiring_development_vertical.md`
- **KPIs** → `references/team_metrics_vertical_ai.md`
