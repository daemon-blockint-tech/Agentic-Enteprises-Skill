---
name: analytics-data-engineer
description: |
  Guides analytics engineering—dbt (or equivalent) project structure, staging/intermediate/mart
  models, dimensional and wide-mart patterns, incremental and CDC loads, data tests and contracts,
  documentation and lineage, CI for analytics code, and handoff to BI semantic layers.
  Use when building or refactoring analytics models, writing dbt SQL, defining tests and
  exposures, debugging mart freshness, or aligning warehouse tables to business metrics—not for
  leading product-embedded analytics teams or launch roadmaps (analytics-data-engineering-manager-product),
  enterprise data platform ADRs (data-architect), deep warehouse platform tuning only
  (data-warehouse-engineer), dashboard design (bi-analyst), or ML modeling (data-scientist).
---

# Analytics Data Engineer

## When to Use

- Structure a **dbt project** (layers, naming, materializations)
- Build **staging → intermediate → mart** pipelines in the warehouse
- Implement **incremental**, snapshot, or CDC-driven models
- Add **tests** (unique, not null, relationships, custom SQL) and freshness checks
- Document models and expose **lineage** for BI and stakeholders
- Define **marts** that map to metrics and dashboards
- Set up **CI** for analytics SQL (compile, test, slim CI)
- Debug **metric mismatches** between mart and dashboard

## When NOT to Use

- Enterprise mesh, governance program, platform selection → `data-architect`
- Partition/cluster tuning without dbt context → `data-warehouse-engineer`
- Chart choice, executive dashboards, stakeholder storytelling → `bi-analyst`
- Feature engineering, training, experiments → `data-scientist`
- Data org roadmap and steward operations → `data-manager`
- Analytics eng hiring, squad roadmap, launch governance → `analytics-data-engineering-manager-product`
- Generic app CI/CD without analytics patterns → `devops`

## Related skills

| Need | Skill |
|---|---|
| Warehouse SQL tuning, star schema theory | `data-warehouse-engineer` |
| KPI definitions and dashboards | `bi-analyst` |
| Platform and domain architecture | `data-architect` |
| Pipeline on-call and platform SLOs | `data-system-ops-lead` |
| ML and advanced stats | `data-scientist` |
| Requirements and metric business rules | `business-analyst` |

## Core Workflows

### 1. Project layout and conventions

Layering, naming (`stg_`, `int_`, `fct_`, `dim_`), materialization defaults, env targets.

**See `references/dbt_project_structure.md`.**

### 2. Modeling for analytics

Facts, dimensions, wide marts, grain, degenerate dimensions, bridge tables.

**See `references/analytics_modeling.md`.**

### 3. Incremental and CDC

Merge strategies, full-refresh exceptions, late-arriving facts.

**See `references/incremental_cdc.md`.**

### 4. Quality and contracts

Tests, severity, source freshness, optional contracts with downstream.

**See `references/testing_quality.md`.**

### 5. Docs, lineage, exposures

Model descriptions, column docs, exposures to BI tools.

**See `references/docs_lineage_exposures.md`.**

### 6. Metrics alignment

Grain, definitions, ownership with `bi-analyst` and `business-analyst`.

**See `references/metrics_alignment.md`.**

## Output standards

- Every mart documents **grain** and **primary key** in YAML
- Tests on keys and critical business rules before merge
- PR includes: models changed, test plan, backfill impact, downstream exposures
- No breaking grain change without migration note to BI

## When to load references

- **dbt layout** → `references/dbt_project_structure.md`
- **Modeling** → `references/analytics_modeling.md`
- **Incremental** → `references/incremental_cdc.md`
- **Tests** → `references/testing_quality.md`
- **Docs/CI** → `references/docs_lineage_exposures.md`
- **Metrics** → `references/metrics_alignment.md`
