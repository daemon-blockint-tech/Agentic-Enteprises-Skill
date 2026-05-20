---
name: Data Visualization
description: |
  Guides data visualization design—chart type selection for message and audience, honest scales
  and labeling, color and accessibility, executive and operational dashboard layout, actuarial and
  insurance charts (loss triangles, trends, distributions), ethics and misleading-viz avoidance,
  and visualization specs for engineers versus slides. Tool-agnostic patterns (matplotlib, plotly,
  Tableau concepts).
  Use when the user says "data visualization", "chart type", "dashboard design", "visualize this
  data", "which chart should I use", "misleading chart", "accessible chart", "executive dashboard",
  "loss triangle chart", or "data viz spec"—not full statistical analysis, BI platform admin, ETL
  pipelines, narrative-only storytelling, or hands-on warehouse or dbt modeling.
---

# Data Visualization

## When to Use

- Choose **chart types** that match the analytical question and audience decision
- Apply **design principles**: honest axes, labels, color, hierarchy, small multiples
- Meet **accessibility** needs: colorblind-safe palettes, contrast, alt-text guidance
- Design **executive** summaries and **operational** monitoring dashboards (layout and viz layer)
- Build **actuarial/insurance** views: loss triangles, trend panels, distributions, scenario bands
- Audit or fix **misleading** charts (truncated axes, dual-axis abuse, cherry-picking)
- Write **viz specs** for engineers (data bindings, encodings) or **slide** narrative outlines
- Review matplotlib, plotly, ggplot, or BI tool outputs for clarity and integrity

## When NOT to Use

- Full **exploratory analysis**, modeling, A/B tests, or MLOps → `data-scientist`
- **Narrative arc**, key messages, and storytelling without chart design focus → `storytelling`
- **Cloud cost** allocation, CUR analysis, or FinOps cadence → `finops-analyst`
- **Dashboard SQL**, KPI definitions, cohort/funnel queries, or BI tool admin → `bi-analyst`
- **dbt marts**, warehouse modeling, tests, and lineage → `analytics-data-engineer`
- **Assumption** selection, governance packs, or change control → `assumption-setting`
- **ETL/ELT** pipeline build, orchestration, or data quality frameworks → `data-warehouse-engineer`
- **Interactive HTML** dashboard products with filters and deployment → route to frontend or product skills if present; pair with `bi-analyst` for metric definitions

## Related skills

| Need | Skill |
|---|---|
| ML, statistics, experiments, production models | `data-scientist` |
| Story spine, executive narrative, data story wording | `storytelling` |
| Cloud spend charts tied to allocation and optimization | `finops-analyst` |
| KPI definitions, analytical SQL, BI delivery | `bi-analyst` |
| Warehouse marts and analytics engineering | `analytics-data-engineer` |
| Assumption packs, sensitivity grids, governance | `assumption-setting` |
| Pricing, reserving, triangle mechanics | `actuary` |

## Core Workflows

### 1. Frame message, audience, and medium

1. State the **decision** or question the viz must support
2. Identify **audience** (exec, ops, regulator, engineer) and **medium** (slide, dashboard, report, spec)
3. List **metrics** with definitions; confirm numerator/denominator with `bi-analyst` if unclear
4. Note **uncertainty** (ranges, confidence, scenarios) before choosing encodings
5. Pick **one primary message** per view; defer secondary points to appendix or drill-down

**See `references/data_visualization_scope.md`.**

### 2. Select chart type and encoding

1. Map question type (comparison, trend, distribution, relationship, composition, geography) to chart family
2. Prefer **simplest** chart that carries the message; add small multiples before exotic forms
3. Document **encoding**: x, y, color, size, facet, and sort order
4. Flag when **tables** beat charts (exact lookup, many dimensions, audit trails)

**See `references/chart_selection_and_message.md`.**

### 3. Apply design and accessibility

1. Set **axis** baselines, units, and tick density; justify log scales
2. Choose **color** for meaning (not decoration); test colorblind and contrast
3. Write **labels**, titles that state the insight, and source/refresh footnotes
4. Provide **alt text** or long descriptions for static exports

**See `references/design_principles_and_accessibility.md`.**

### 4. Design dashboards and executive views

1. Apply visual **hierarchy** (F-pattern, KPI strip, drill paths)
2. Limit **density**; separate monitoring vs exploratory layouts
3. Add **context**: targets, prior period, benchmarks, annotations for events
4. Specify **interactions** only when they change decisions (filters, drill, alerts)

**See `references/executive_and_dashboard_design.md`.**

### 5. Actuarial and insurance visualization

1. Use standard **loss triangle** layouts; label development and valuation periods
2. Show **trends** and **distributions** with explicit basis (accident year, calendar year)
3. Present **scenarios** as bands or small multiples—not false point precision
4. Coordinate labels with `assumption-setting` and `actuary` for technical definitions

**See `references/actuarial_insurance_visualization.md`.**

### 6. Ethics check and handoff

1. Run **misleading-viz** checklist before publish
2. Produce **engineer spec** (data schema, encodings, refresh) or **slide outline** (headline per chart)
3. Separate **exploration** drafts from **production** assets

**See `references/misleading_viz_and_ethics.md`.**

## Output standards

- One **primary insight** per chart; title states the takeaway
- Axes labeled with **units**; zero baseline when magnitude comparisons matter
- **Source**, as-of date, and filters documented on every external-facing viz
- No **fabricated** data or smoothed series without disclosure
- Accessibility: do not rely on color alone; meet contrast targets for text and UI chrome
- Specs list **fields**, **aggregations**, **sort**, and **edge cases** (nulls, small n)

## When to load references

| Topic | Reference |
|---|---|
| Scope, boundaries, tool posture | `references/data_visualization_scope.md` |
| Chart selection and message fit | `references/chart_selection_and_message.md` |
| Design, color, accessibility | `references/design_principles_and_accessibility.md` |
| Executive and dashboard layout | `references/executive_and_dashboard_design.md` |
| Actuarial and insurance charts | `references/actuarial_insurance_visualization.md` |
| Misleading viz and ethics | `references/misleading_viz_and_ethics.md` |
