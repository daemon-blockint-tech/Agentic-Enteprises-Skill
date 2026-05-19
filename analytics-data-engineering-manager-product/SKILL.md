---
name: analytics-data-engineering-manager-product
description: |
  Guides managers of product-embedded analytics engineering teams—org design, hiring and levels,
  roadmap and prioritization with product managers, analytics data product delivery, squad
  alignment, stakeholder forums, team KPIs, and escalation paths for metric and mart quality.
  Use when leading analytics engineers on product domains, planning analytics roadmaps per product
  area, resolving prioritization across squads, or defining how marts and metrics ship with
  features—not for hands-on dbt/SQL (analytics-data-engineer), enterprise data platform ADRs
  (data-architect), company-wide data governance ops (data-manager), or dashboard UX (bi-analyst).
  For vertical copilot/RAG product engineering management, use
  engineering-manager-vertical-ai-products—not analytics-data-engineering-manager-product.
---

# Analytics Data Engineering Manager, Product

## When to Use

- Design or scale a **product-embedded analytics engineering** org
- Prioritize analytics backlog with **product managers** and domain leads
- Define **analytics data products** (marts, metrics packs) tied to product launches
- Run delivery cadence: intake, estimation, dependencies with app/data platform teams
- Set **team KPIs** (freshness, test pass rate, time-to-metric for launches)
- **Hire, level, and develop** analytics engineers and leads
- Escalate cross-squad conflicts (metric definitions, shared dimensions, capacity)

## When NOT to Use

- Writing or refactoring dbt models → `analytics-data-engineer`
- Warehouse partition tuning or ETL platform design → `data-warehouse-engineer`
- Enterprise mesh, governance program, catalog policy → `data-architect` or `data-manager`
- Dashboard design and executive storytelling → `bi-analyst`
- Multi-portfolio technical programs (non-analytics) → `technical-program-manager`
- BRD/process mapping without analytics delivery → `business-analyst`

## Related skills

| Need | Skill |
|---|---|
| dbt implementation detail | `analytics-data-engineer` |
| Org-wide data ops and governance cadence | `data-manager` |
| BI and KPI storytelling | `bi-analyst` |
| Business rules sign-off | `business-analyst` |
| Platform architecture | `data-architect` |
| Large cross-functional program | `technical-program-manager` |

## Core Workflows

### 1. Org design and squad model

Embedded vs centralized analytics engineering; ratios; interfaces to DE and BI.

**See `references/team_org_design.md`.**

### 2. Roadmap and prioritization

Product-domain backlog, launch-aligned milestones, capacity trade-offs.

**See `references/roadmap_prioritization.md`.**

### 3. Delivery and launch alignment

Definition of done for analytics with feature releases; dependency management.

**See `references/delivery_launch_alignment.md`.**

### 4. Stakeholder partnerships

PM, product analytics, finance, legal/privacy, platform engineering forums.

**See `references/stakeholder_partnerships.md`.**

### 5. Hiring and career development

Levels, interview loops, growth plans, performance calibration inputs.

**See `references/hiring_development.md`.**

### 6. Metrics and accountability

Team scorecard, product analytics SLAs, incident and quality escalation.

**See `references/team_metrics_accountability.md`.**

## Output standards

- Roadmap items link **business outcome**, **metric/mart deliverable**, and **owner**
- Launch checklist signed by PM + analytics eng before GA
- Escalations documented with options and recommendation
- No redefining enterprise architecture without `data-architect` ADR

## When to load references

- **Org** → `references/team_org_design.md`
- **Roadmap** → `references/roadmap_prioritization.md`
- **Delivery** → `references/delivery_launch_alignment.md`
- **Stakeholders** → `references/stakeholder_partnerships.md`
- **People** → `references/hiring_development.md`
- **KPIs** → `references/team_metrics_accountability.md`
