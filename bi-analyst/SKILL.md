---
name: bi-analyst
description: |
  Guides business intelligence analysts through dashboard design, analytical SQL, reporting,
  and stakeholder management. Covers chart selection, data storytelling, cohort/funnel analysis,
  metric definitions, and BI tool patterns (Tableau, Looker, Power BI).
  Use when building dashboards, writing analytical SQL, defining business metrics,
  presenting data insights, or gathering requirements from stakeholders.
---

# Business Intelligence Analyst

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

**See `references/dashboard_design.md` for layout patterns, tool-specific tips, and anti-patterns.**

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

**See `references/sql_analysis.md` for full SQL templates, optimization tips, and common analytical queries.**

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

**See `references/reporting.md` for KPI frameworks, report templates, and metric hierarchies.**

### 4. Stakeholder Management

**Engagement workflow:**

1. **Discovery**: Interview stakeholders to understand business questions
2. **Prototype**: Build a quick draft with sample data
3. **Review**: Walk through with stakeholders; capture feedback
4. **Refine**: Iterate based on feedback (limit to 2-3 rounds)
5. **Deliver**: Deploy with documentation and training
6. **Maintain**: Schedule quarterly reviews for relevance

**See `references/stakeholder_management.md` for interview techniques, presentation frameworks, and feedback management.**

## When to Load References

- **Dashboard design** → `references/dashboard_design.md`
- **SQL analysis** → `references/sql_analysis.md`
- **Reporting & metrics** → `references/reporting.md`
- **Stakeholder management** → `references/stakeholder_management.md`
