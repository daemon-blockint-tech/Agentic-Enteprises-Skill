# Chart selection and message

## Table of contents

1. [Start with the question](#start-with-the-question)
2. [Question-to-chart map](#question-to-chart-map)
3. [Composition and part-to-whole](#composition-and-part-to-whole)
4. [Ranking and comparison](#ranking-and-comparison)
5. [Time and trends](#time-and-trends)
6. [Distribution and uncertainty](#distribution-and-uncertainty)
7. [Relationship and correlation](#relationship-and-correlation)
8. [Geography](#geography)
9. [When tables beat charts](#when-tables-beat-charts)
10. [Anti-patterns](#anti-patterns)

## Start with the question

Write one sentence: **"After seeing this, the audience will ___."**

If the sentence needs two unrelated verbs, split into two views.

| Input | Decide |
|---|---|
| Metric definition unclear | Stop; align with `bi-analyst` |
| Many segments, one message | Small multiples, not rainbow pie |
| Sparse or tiny n | Table + footnote; avoid precise-looking charts |

## Question-to-chart map

| Analytical question | Primary charts | Notes |
|---|---|---|
| How much / how many? | KPI card, bar (horizontal for long labels) | Show context vs target or prior period |
| How does it change over time? | Line, area (stacked only if parts sum to whole) | Label inflection points sparingly |
| How is it distributed? | Histogram, box/violin, ECDF | State n; watch outliers |
| How do parts relate to whole? | Stacked bar (few segments), treemap (explore only) | Avoid pie beyond 3–4 slices |
| How do two variables relate? | Scatter, bubble (size = third var) | Add trend line only if justified |
| How do categories compare? | Grouped bar, dot plot, slope chart (two times) | Sort by value or importance |
| Where geographically? | Choropleth (rates), symbol map (counts) | Normalize by population or exposure |
| What's the flow / funnel? | Funnel, sankey (few steps) | Show step conversion explicitly |

## Composition and part-to-whole

- **Stacked bar**: parts sum to 100% or total; max ~5 segments
- **Pie / donut**: last resort; max 3–4 slices; label values directly
- **Treemap**: exploration, not executive proof; label large cells only
- **Waterfall**: explain variance bridge (budget, revenue walk)

Always show **absolute** and **rate** when stakes are high (claims, revenue).

## Ranking and comparison

- Sort bars by **value** or **business priority**, not alphabetically
- **Dot plot** beats bar when many categories (12+)
- **Slope chart** for exactly two periods per category
- **Dumbbell** for range between two values (before/after)

Avoid dual y-axes; see ethics reference.

## Time and trends

| Pattern | Chart | Caution |
|---|---|---|
| Continuous metric | Line | Don't connect missing periods without gap |
| Discrete periods | Column per period | Align fiscal vs calendar labels |
| Seasonality | Line + reference band or YoY overlay | State comparison basis |
| Index rebased | Line indexed to 100 | Name base period |
| Forecast | Actual solid, forecast dashed + band | Label model and as-of |

Use **log scale** only when multiplicative change matters; label axis as log.

## Distribution and uncertainty

- **Histogram**: bin width matters; try consistent bins across facets
- **Box plot**: show median and IQR; explain outliers
- **Violin**: density estimate—disclose method for technical audiences
- **Error bars**: define CI vs SE vs SD in caption
- **Fan chart / ribbon**: scenarios or prediction intervals

Never imply false precision (four decimal places on noisy estimates).

## Relationship and correlation

- Scatter with **transparency** or jitter for overplotting
- Color third dimension only when pattern survives without color
- Regression line: state functional form and exclusions
- Heatmap of correlation: order variables logically; diverging scale centered at 0

Correlation charts are **not** causation—pair with `storytelling` for narrative if needed.

## Geography

- Choropleth for **rates** (per exposure, per capita), not raw counts
- Use consistent projection; avoid extreme color breaks
- Offer **table** backup for small regions suppressed in map

## When tables beat charts

Use tables when:

- Exact values required (regulatory, accounting, audit)
- Many dimensions (>2) without a single comparison story
- Mixed units or footnotes per row
- Small n where chart implies false continuity

Enhance tables with **heat scales** on numeric columns sparingly.

## Anti-patterns

| Pattern | Why it fails | Prefer |
|---|---|---|
| 3D bars or pies | Distorts area perception | 2D bar or dot |
| Chartjunk / heavy gradients | Hides data | Flat color, direct labels |
| Dual y-axis | Invites false correlation | Indexed lines or separate panels |
| Truncated y-axis without flag | Exaggerates change | Full axis or inset with label |
| Map for 5 regions | Table or bar often clearer | Sorted bar |
