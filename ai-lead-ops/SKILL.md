---
name: ai-lead-ops
description: |
  Guides AI ops leadership—LLM SRE, model/prompt releases, eval/incidents, cost/capacity, vendors, and
  cross-functional cadence. Use for AI platform ops, LLM SLAs, incidents, rollout governance, unit
  economics, red-team/eval gates, and team rituals—not memory (ai-memory-developer), context code
  (ai-context-engineer), security programs (cybersecurity), token roadmaps
  (ai-token-improvement-plan-engineer), solution architecture (applied-ai-architect-commercial-enterprise),
  skills portfolio (ai-skill-manager), or vertical AI product eng management
  (engineering-manager-vertical-ai-products).
  Prompt/eval team management and golden-set release policy: engineering-manager-agent-prompts-evals.
---

# AI Lead Ops

## When to Use

- Standing up AI platform operations and production service reliability
- Defining SLAs/SLOs for LLM-powered features
- Running AI incident reviews and post-mortems
- Governing model, prompt, and index rollouts with tiered gates
- Tracking AI unit economics (cost per session, tokens per feature)
- Coordinating red-team and evaluation gates before releases
- Building team rituals and cadence across engineering, research, risk, and product
- Managing AI vendor relationships, contracts, and bake-offs

## When NOT to Use

- Implementing memory stores or context packing code → `ai-memory-developer` / `ai-context-engineer`
- Building RAG pipelines or agent tools → `ai-engineer`
- Designing corporate AI policy or regulatory mapping → `ai-risk-governance`
- General network penetration testing or enterprise security programs → `cybersecurity`
- Structured token/cost improvement roadmaps with backlog → `ai-token-improvement-plan-engineer`
- Commercial/enterprise AI solution architecture → `applied-ai-architect-commercial-enterprise`
- Vertical AI product engineering managers and squad roadmaps → `engineering-manager-vertical-ai-products`

## Related skills

| Need | Skill |
|---|---|
| Build RAG, agents, eval harnesses | `ai-engineer` |
| Memory and context implementation | `ai-memory-developer`, `ai-context-engineer` |
| Risk tiering and policies | `ai-risk-governance` |
| Adversarial testing execution | `ai-redteam` |
| CI/CD and platform incidents | `devops` |
| Pipeline security | `devsecops` |
| Token optimization roadmap and initiative backlog | `ai-token-improvement-plan-engineer` |
| Commercial/enterprise AI architecture | `applied-ai-architect-commercial-enterprise` |
| Skills portfolio governance | `ai-skill-manager` |

## Core Workflows

### 1. Operating model and cadence

| Ritual | Frequency | Outcomes |
|---|---|---|
| AI ops standup | Daily | Blockers, incidents, deploys |
| Model/prompt change review | Per release | Approvers, eval delta |
| Cost review | Weekly | Spend vs budget, top features |
| Risk & safety sync | Bi-weekly | Incidents, policy gaps |
| Quarterly capacity | Quarterly | Model roadmap, vendor contracts |

Define RACI: who owns model, prompt, index, eval suite, on-call.

**See `references/operating_model.md` for roles and escalation.**

### 2. Release governance

**Production promotion checklist:**

- [ ] Eval regression passed on golden + safety set
- [ ] Red-team sign-off for tier-2+ use cases
- [ ] Model card / change log updated
- [ ] Canary with error and cost monitors
- [ ] Rollback procedure tested (previous prompt + model version pinned)
- [ ] Comms plan for customer-visible behavior change

**See `references/release_governance.md` for tiered gates and canary metrics.**

### 3. SLOs, incidents, and observability

**Example SLIs:**

| SLI | Notes |
|---|---|
| Availability | Successful completion / total requests |
| Latency | p95 end-to-end |
| Quality proxy | Thumbs-down rate, escalation rate |
| Safety | Policy violation rate post-deploy |
| Cost | USD per successful session |

**AI incident types:** toxic output, PII leak in logs, retrieval cross-tenant leak, runaway agent loop, vendor outage.

**See `references/incidents_slos.md` for severity matrix and post-incident template.**

### 4. Cost and capacity

- Track tokens by model, feature, tenant
- Set budgets and alerts at 80/100/110%
- Optimize via routing, caching, context engineering (partner with `ai-context-engineer`)
- Forecast from usage growth + model price changes

**See `references/cost_capacity.md` for unit economics worksheet.**

### 5. Vendor and eval program

- Maintain scorecard: quality, latency, safety, price, data terms
- Run structured bake-offs before annual renewals
- Own central eval harness ownership and dataset hygiene

**See `references/vendor_eval_program.md` for RFP topics and eval program maturity.**

## When to load references

- **Team cadence and RACI** → `references/operating_model.md`
- **Releases and canaries** → `references/release_governance.md`
- **SLOs and incidents** → `references/incidents_slos.md`
- **Cost and capacity** → `references/cost_capacity.md`
- **Vendors and eval ops** → `references/vendor_eval_program.md`
