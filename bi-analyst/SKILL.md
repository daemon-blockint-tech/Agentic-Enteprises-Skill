---
name: bi-analyst
description: |
  Design dashboards, write analytical SQL, define KPIs, and manage stakeholder analytics requirements.
  Cover chart selection, data storytelling, cohort/funnel analysis, metric definitions, and BI tool patterns
  (Tableau, Looker, Power BI).
  Triggers on "build dashboard", "design dashboard", "write analytical SQL", "cohort analysis",
  "funnel analysis", "define KPI", "define metric", "reporting requirements",
  "data storytelling", "stakeholder analytics", "retention analysis", or "BI report".
  For business model canvas, TAM/SAM/SOM, and competitor monetization research, use
  business-model-researcher—not bi-analyst.
  For building warehouse marts, dbt models, tests, and lineage—not dashboards—use
  analytics-data-engineer.
---

# Business Intelligence Analyst

## Overview

Design dashboards, write analytical SQL, define KPIs, and manage stakeholder analytics requirements.
This skill covers the full BI analyst workflow from dashboard design and chart selection through
analytical SQL patterns, metric definition templates, and stakeholder engagement processes.

## Features

- Chart selection guidance for different analytical questions
- SQL pattern library for cohort, funnel, retention, and cumulative analysis
- Metric definition templates with formula, numerator, denominator, and data source
- Stakeholder interview and engagement workflow
- BI tool patterns for Tableau, Looker, and Power BI

## Usage

1. Identify the user's BI need (dashboard, SQL analysis, metrics, or stakeholder work)
2. Follow the corresponding workflow below
3. Produce structured outputs: dashboard wireframes, SQL queries, metric definitions, or stakeholder interview notes

## Examples

- **User**: "Build a retention dashboard"
  **Agent**: Runs Dashboard Design workflow, selects line chart for retention curves, applies F-pattern hierarchy, adds benchmark context

- **User**: "Write SQL for cohort analysis"
  **Agent**: Runs Analytical SQL workflow, uses self-join on first-event date pattern, returns cohort retention table

- **User**: "Define our churn metric"
  **Agent**: Runs Reporting & Metrics workflow, fills metric definition template with formula, numerator, denominator, data source

## When to Use

- Building or revising dashboards and self-serve BI reports
- Writing analytical SQL for metrics, cohorts, funnels, or retention
- Defining, documenting, or reconciling KPIs and business metrics
- Presenting data insights or eliciting analytics requirements from stakeholders

## When NOT to Use

- Enterprise data platform, mesh, or governance architecture → use `data-architect`
- Warehouse ETL design, incremental loads, or platform-specific tuning → use `data-warehouse-engineer`
- dbt marts, incremental models, data tests, and docs/lineage → use `analytics-data-engineer`
- Predictive modeling, experiment design, or ML productionization → use `data-scientist`
- Business process mapping or BRD/FRD requirements without analytics delivery → use `business-analyst`
- Business model research, market sizing, unit economics modeling → use `business-model-researcher`

## Core Workflows

### 1. Dashboard Design

**Design checklist:**

1. **Define the audience and action**
   - Who uses this dashboard? How often?
   - What decision does it support?
   - What action should they take after viewing?

2. **Choose the right charts**
   | Question | Chart Type |
   |---|---|
   | How much/many? | KPI cards, bar charts |
   | How does it change over time? | Line charts, area charts |
   | How is it distributed? | Histograms, box plots |
   | How do parts relate to the whole? | Pie charts (limited), treemaps, stacked bars |
   | How do variables relate? | Scatter plots, heatmaps |
   | Where is it happening? | Maps, geo charts |

3. **Apply visual hierarchy**
   - Most important metrics at top left (F-pattern reading)
   - Use size and color for emphasis, not decoration
   - Limit to 3-5 colors per dashboard
   - Consistent formatting across all dashboards

4. **Add context**
   - Benchmarks, targets, or prior period comparisons
   - Annotations for significant events
   - Last refresh timestamp

### 2. Analytical SQL

**Common analysis patterns:**

| Analysis | SQL Pattern |
|---|---|
| Month-over-month growth | `LAG()` window function |
| Running total | `SUM() OVER (ORDER BY date)` |
| Top N per group | `ROW_NUMBER() OVER (PARTITION BY group ORDER BY metric DESC)` |
| Cohort retention | Self-join on first-event date |
| Funnel conversion | `COUNT(DISTINCT CASE WHEN step = N THEN user_id END)` |
| Cumulative distinct | `COUNT(DISTINCT user_id) OVER (ORDER BY date)` |

### 3. Reporting & Metrics

**Metric definition template:**
```markdown
## [Metric Name]

**Definition:** [Clear, unambiguous description]
**Formula:** [Mathematical formula or SQL pseudocode]
**Numerator:** [What is counted]
**Denominator:** [The population, if a rate/ratio]
**Data source:** [Table(s) used]
**Dimensions:** [How it can be sliced: date, region, product]
**Owner:** [Who maintains this definition]
**Last updated:** [Date]
```

### 4. Stakeholder Management

**Engagement workflow:**

1. **Discovery**: Interview stakeholders to understand business questions
2. **Prototype**: Build a quick draft with sample data
3. **Review**: Walk through with stakeholders; capture feedback
4. **Refine**: Iterate based on feedback (limit to 2-3 rounds)
5. **Deliver**: Deploy with documentation and training
6. **Maintain**: Schedule quarterly reviews for relevance
