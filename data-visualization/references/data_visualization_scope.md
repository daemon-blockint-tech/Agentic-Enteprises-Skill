# Data visualization scope

## Table of contents

1. [Purpose](#purpose)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Deliverable types](#deliverable-types)
5. [Tool posture](#tool-posture)
6. [Quality bar](#quality-bar)

## Purpose

Turn verified data into **honest, decision-ready** visuals. The skill owns **what** to show and **how** to encode it—not upstream modeling, pipeline build, or narrative-only comms.

## In scope

| Area | Examples |
|---|---|
| Chart choice | Bar vs line vs slope; when tables win |
| Encoding | Axes, color, facets, sort, aggregation level |
| Design integrity | Baselines, units, labels, annotations |
| Accessibility | Palettes, contrast, alt text patterns |
| Dashboard layout | KPI hierarchy, density, drill paths |
| Actuarial viz | Triangles, A/E panels, scenario bands |
| Ethics | Truncation, dual axes, cherry-pick detection |
| Handoff | Engineer viz spec; slide chart outline |

## Out of scope

| Area | Route to |
|---|---|
| Hypothesis tests, ML, causal inference | `data-scientist` |
| Story arc and executive wording | `storytelling` |
| Metric definitions and BI SQL | `bi-analyst` |
| dbt models and warehouse design | `analytics-data-engineer` |
| Assumption governance | `assumption-setting` |
| Cloud cost programs | `finops-analyst` |
| BI server admin, row-level security, extract schedules | Platform owners; `bi-analyst` for requirements |
| ETL orchestration | `data-warehouse-engineer` |

## Deliverable types

| Type | Contents |
|---|---|
| **Chart recommendation** | Question → chart family → encodings → caveats |
| **Viz spec (engineering)** | Fields, grain, filters, chart type, sort, null handling, refresh |
| **Dashboard wireframe** | Zones, KPIs, chart list, interactions, alert thresholds |
| **Slide outline** | Headline per visual, one proof point, appendix list |
| **Audit memo** | Misleading elements found; fix list with rationale |

## Tool posture

Guidance is **tool-agnostic**. Map concepts to the user's stack:

| Concept | matplotlib / seaborn | plotly | Tableau / Looker / Power BI |
|---|---|---|---|
| Encoding | `x`, `y`, `hue`, `col` | `x`, `y`, `color`, `facet_col` | Columns, shelves, marks |
| Small multiples | `facetgrid`, `subplots` | `facet_col` / subplots | Trellis, small multiples |
| Interactivity | Limited in static | Native | Filters, actions |

Prefer the team's **standard palette and template** when one exists.

## Quality bar

Before delivery:

- [ ] Primary message stated in title or callout
- [ ] Definitions aligned with metric owner (`bi-analyst` if needed)
- [ ] Axes and units correct; transformations disclosed
- [ ] Sample size and suppression rules documented
- [ ] Ethics checklist passed (`references/misleading_viz_and_ethics.md`)
- [ ] Accessibility: color + non-color cues; contrast checked for exports
