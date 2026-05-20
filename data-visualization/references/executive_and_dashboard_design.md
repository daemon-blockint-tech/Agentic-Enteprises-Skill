# Executive and dashboard design

## Table of contents

1. [Executive vs operational](#executive-vs-operational)
2. [Executive summary layout](#executive-summary-layout)
3. [Operational monitoring layout](#operational-monitoring-layout)
4. [KPI design](#kpi-design)
5. [Interactions and drill](#interactions-and-drill)
6. [Refresh and trust](#refresh-and-trust)
7. [Slide vs live dashboard](#slide-vs-live-dashboard)
8. [Handoff to BI](#handoff-to-bi)

## Executive vs operational

| Dimension | Executive | Operational |
|---|---|---|
| Goal | Decide, allocate, explain variance | Detect, triage, act |
| Horizon | Weeks–quarters; scenarios | Hours–days; alerts |
| Density | Low; 3–5 KPIs + 2 charts | Higher; filters and drill |
| Comparison | Target, plan, prior year | Thresholds, SLA, run rate |
| Failure mode | Hides uncertainty | Alert fatigue |

Do not paste operational dashboards into board decks without redesign.

## Executive summary layout

Suggested zones (top to bottom):

1. **Headline strip** — 3 KPIs with delta vs plan and prior period
2. **Primary chart** — one trend or bridge answering the meeting question
3. **Supporting chart** — breakdown or driver (small multiple or ranked bar)
4. **Risks / actions** — bullets, not another chart
5. **Appendix link** — detail tables and definitions

Rules:

- One **ask** per page (continue, investigate, approve spend)
- Show **ranges** or scenarios when decisions are sensitive to assumptions
- Footnote **definitions**; align with finance or actuarial owners

## Operational monitoring layout

1. **Alert banner** — breaches only (color + text)
2. **Throughput KPIs** — volume, error rate, latency, backlog
3. **Time series** — last 24h / 7d with event markers
4. **Breakdown** — top contributors to current anomaly
5. **Drill** — to entity list (account, claim, service)

Avoid:

- More than **two** accent colors for status (ok / warn / critical)
- Charts without defined **owner** and runbook link

## KPI design

Each KPI tile documents:

| Field | Example |
|---|---|
| Name | Gross written premium |
| Value | $142M |
| Comparison | vs plan +2%; vs PY +8% |
| Period | MTD, closed month |
| Definition link | Metric catalog ID |

Visual:

- Large number, small comparison line
- Sparkline optional when trend adds decision value
- Red/green only with numeric sign and icon

Coordinate definitions with `bi-analyst`.

## Interactions and drill

Add interaction only when it changes action:

| Interaction | When useful |
|---|---|
| Date range filter | Standard for ops; fixed period for exec snapshots |
| Segment filter | LOB, region, product |
| Drill to detail | Investigation workflows |
| Cross-filter | Exploratory dashboards only |
| Tooltip | Precision for analysts; duplicate in table for accessibility |

Spec **default filter** state and **empty state** behavior.

## Refresh and trust

Display on every dashboard:

- **Last refresh** timestamp (timezone labeled)
- **Data latency** (T+1, near real-time)
- **Known gaps** (missing region, partial day)

If refresh fails, show **stale badge**—do not show silent old data as current.

## Slide vs live dashboard

| Element | Slide | Live dashboard |
|---|---|---|
| Title | Insight headline | Metric name + status |
| Data | Frozen snapshot date | Rolling window |
| Interactivity | None | Filters, drill |
| Detail | Appendix | Linked tab |
| Spec output | Outline per slide | Wireframe + KPI list |

For slides, deliver **section intent + chart type + headline**; full visual design may sit with brand or design skills.

## Handoff to BI

Viz spec minimum for `bi-analyst` or BI implementers:

```markdown
## View: [Name]
**Audience:** [role]
**Refresh:** [cadence]
**Filters:** [list + defaults]

### KPIs
| KPI | Source field | Aggregation | Comparison |

### Charts
| # | Type | Title (insight) | X | Y | Color | Sort | Notes |

### Edge cases
- Null handling:
- Suppression rules:
- RLS / scope:
```

Pair with metric definitions from `bi-analyst` before build.
