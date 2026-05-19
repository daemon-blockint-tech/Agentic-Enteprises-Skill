---
name: applied-ai-architect-commercial-enterprise
description: |
  Guides applied AI solution architecture for commercial (B2B SaaS, multi-tenant product) and
  enterprise (internal copilots, regulated corp data) contexts—reference patterns for RAG, agents,
  and copilots, platform and model selection, data boundaries, identity, observability, cost at
  scale, and POC-to-production hardening with security and governance gates.
  Use when designing customer-facing AI features, enterprise knowledge assistants, vendor LLM
  integration architecture, AI ADRs for commercial or IT stakeholders, or mapping AI components to
  SSO/DLP/residency requirements—not for implementing RAG code (ai-engineer), generic multi-service
  ADRs without AI (senior-system-architecture), AI policy registers (ai-risk-governance), or
  contract redlines (commercial-counsel).
  For engineering management of vertical AI product squads (hiring, roadmap, launch governance),
  use engineering-manager-vertical-ai-products. Labeling PM:
  product-management-human-data-platform—not this skill.
---

# Applied AI Architect — Commercial & Enterprise

## When to Use

- Design end-to-end AI architecture for a B2B product feature or internal copilot
- Choose between RAG, fine-tuning, agents, or workflow orchestration for a use case
- Define multi-tenant isolation, data boundaries, and customer data handling for AI
- Map enterprise requirements: SSO, audit logs, residency, DLP, human oversight
- Compare cloud AI platforms (managed endpoints, private networking, quotas)
- Author AI-specific ADRs for engineering, security, and procurement
- Plan POC → pilot → production with eval, safety, and ops gates

## When NOT to Use

- Write application code, prompts, or eval harnesses → `ai-engineer`, `prompt-engineer`
- General non-AI integration ADRs → `senior-system-architecture`
- Context packing and token budgets → `ai-context-engineer`
- Memory store implementation → `ai-memory-developer`
- AI risk tiering and policy documents → `ai-risk-governance`
- SOC 2 evidence packs → `compliance-engineer`
- Token cost improvement program → `ai-token-improvement-plan-engineer`
- AI ops cadence and release governance → `ai-lead-ops`
- Business case and operating model → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| Build and ship RAG/agents | `ai-engineer` |
| Cross-service platform ADRs | `senior-system-architecture` |
| Governance and use-case classification | `ai-risk-governance` |
| Security architecture and controls | `cybersecurity`, `information-security-engineer` |
| Data platform for embeddings/warehouse | `data-architect` |
| Product tenant isolation | `product-infrastructure-security-engineer` |
| Red-team before launch | `ai-redteam` |
| Commercial contract terms | `commercial-counsel` |

## Core Workflows

### 1. Classify context: commercial vs enterprise

| Lens | Commercial (product) | Enterprise (internal IT) |
|---|---|---|
| Users | Customer tenants | Employees, partners |
| Data | Customer content + config | Corp IP, HR, regulated data |
| Identity | Product auth + tenant ID | IdP (Entra/Okta), groups |
| Isolation | Strong multi-tenancy | Network/VPC, private endpoints |
| Buying | SKU, usage metering | EA, private offer, on-prem option |

**See `references/commercial_vs_enterprise.md`.**

### 2. Shape the solution

1. **Job** — user outcome in one sentence; success metric
2. **Pattern** — Q&A RAG, task agent, workflow automation, codegen assist
3. **Data** — sources, freshness, PII, retention, who may see what
4. **Model** — capability vs cost; routing; fallback
5. **Control plane** — prompts, tools, policies, human approval points
6. **Plane separation** — ingestion ≠ inference ≠ logging (scale independently)

**See `references/reference_architectures.md`.**

### 3. Non-functional requirements

Document targets for:

- Latency (p95 first token, end-to-end task)
- Availability and DR for inference path
- Cost per tenant/session and guardrails
- Auditability (prompt, retrieval IDs, model version—no secrets in logs)
- Safety (tier, blocked topics, escalation)
- Compliance (residency, retention, subprocessors)

**See `references/enterprise_nfr_integration.md`.**

### 4. Platform and vendor selection

Score options on: data handling, private link, model catalog, SLAs, metering, exit strategy.

**See `references/platform_selection.md`.**

### 5. AI ADR and review

For one-way doors (vendor, data leaves region, autonomous agents):

- Options, NFR impact, security, cost model
- Migration and rollback

**See `references/ai_architecture_decision.md`.**

Pair with `senior-system-architecture` for org-wide integration standards.

### 6. POC → production path

| Stage | Architecture focus |
|---|---|
| POC | Single tenant, manual eval, no prod data |
| Pilot | Tenant isolation, observability, limited users |
| GA | SLOs, rate limits, on-call, eval in CI, red-team for tier-2+ |

**See `references/poc_to_production.md`.**

## When to load references

- **Commercial vs enterprise** → `references/commercial_vs_enterprise.md`
- **RAG, agent, copilot patterns** → `references/reference_architectures.md`
- **SSO, DLP, logging, residency** → `references/enterprise_nfr_integration.md`
- **Cloud AI platform choice** → `references/platform_selection.md`
- **AI ADR template** → `references/ai_architecture_decision.md`
- **Production hardening** → `references/poc_to_production.md`
