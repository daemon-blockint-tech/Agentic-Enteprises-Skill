# Roadmap and Prioritization

## Platform value levers

| Lever | Product moves |
|-------|----------------|
| **Quality** | Gold tasks, adjudication, reviewer tiers, auto-QA |
| **Speed** | Task UX, prefetch, batching, SLA dashboards |
| **Cost** | Pre-labeling, active learning, tiered workforce |
| **Scale** | Multi-language, 24/7 queues, API throughput |
| **Trust** | PII handling, audit trails, customer isolation |

## Personas (typical)

| Persona | Jobs to be done |
|---------|-----------------|
| **ML lead / PM (customer)** | Ship model with labeled data on deadline |
| **Annotation manager (customer)** | Run projects, hit quality bar, report up |
| **Contributor** | Earn fairly, clear tasks, minimal friction |
| **Reviewer / QA** | Catch errors fast, consistent rubric |
| **Ops / workforce** | Staff queues, handle disputes, compliance |
| **Platform admin** | Tenancy, billing, access, integrations |

## Roadmap themes (examples)

- **Core labeling** — task types, media support, shortcuts
- **Quality** — consensus, gold injection, analytics
- **Delivery** — exports, API, versioning, lineage metadata
- **Workforce** — skills tests, tiers, incentives, appeals
- **Enterprise** — SSO, VPC, private workforce, DPA features
- **GenAI-era** — RLHF pairs, rubric ranking, red-team data collection

## Prioritization framework (RICE-lite)

| Factor | Question |
|--------|----------|
| Reach | # projects or labels affected per quarter |
| Impact | Effect on quality, speed, or revenue retention |
| Confidence | Evidence from customers, pilots, metrics |
| Effort | Eng + ops + policy review |

Force-rank **one primary lever** per epic to avoid "everything is P0."

## PRD skeleton

```markdown
## Problem
## Personas
## Success metrics (baseline → target)
## Scope (in / out)
## User stories
## Task/quality implications
## Dependencies (eng, legal, ops)
## Launch plan (alpha → GA)
## Risks
```

## Discovery inputs

- Customer QBR themes and churn reasons
- Contributor NPS and task-abandon funnels
- Quality regressions (IAA drops, rework rate)
- Competitive gaps (modalities, pricing model)
- Cost per label trend by project type

## Anti-patterns

- Roadmap driven only by largest customer's custom ask without platform abstraction
- Features without quality metric definition
- Ignoring contributor experience when optimizing customer dashboards only
