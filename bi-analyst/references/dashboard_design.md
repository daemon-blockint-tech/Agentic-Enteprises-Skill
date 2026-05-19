# Dashboard Design

## Layout Patterns

### Executive Summary Dashboard
**Purpose:** High-level health check for leadership
**Layout:**
- Top row: 3-5 KPI cards (current value, vs target, vs prior period)
- Middle: Trend line for primary metric (revenue, users, etc.)
- Bottom: Breakdown by key dimension (region, product, channel)
**Refresh:** Daily or weekly

### Operational Dashboard
**Purpose:** Monitor daily operations and catch issues
**Layout:**
- Left: Real-time metrics with alerts (queue depth, error rates)
- Center: Hourly/daily trends
- Right: Detailed table for drill-down
**Refresh:** Hourly or near real-time
**Interaction:** Filtering by date, team, status

### Analytical/Exploratory Dashboard
**Purpose:** Enable self-service analysis
**Layout:**
- Filters on top (date range, dimensions)
- Multiple charts with cross-filtering
- Summary table with export option
**Refresh:** Daily or on-demand

## Chart Selection Guide

### Avoid These Common Mistakes

| Bad Choice | Why | Better Alternative |
|---|---|---|
| Pie chart with >5 slices | Hard to compare angles | Bar chart, treemap |
| 3D charts | Distorts perception | 2D with color/size encoding |
| Dual-axis charts | Different scales confuse | Side-by-side panels, indexed lines |
| Rainbow color scales | Not perceptually uniform | Viridis, sequential single-hue |
| Truncated y-axis | Exaggerates differences | Start at zero, or use dots |
| Too many data points | Overwhelming | Aggregate, filter, or use sparklines |

## Color & Accessibility

**Rules:**
- Use color intentionally: red/green only for good/bad status
- Ensure 4.5:1 contrast ratio for text
- Don't rely on color alone; add patterns or labels
- Colorblind-friendly palettes: Tableau 10, ColorBrewer

**Dashboard color roles:**
| Role | Color | Usage |
|---|---|---|
| Primary metric | Brand color | Main KPIs, highlighted series |
| Secondary | Neutral gray | Supporting data, grid lines |
| Positive | Green | On-target, growth |
| Negative | Red | Off-target, decline |
| Warning | Orange/Yellow | Attention needed |
| Comparison | Light blue | Prior period, benchmark |

## Tool-Specific Tips

### Tableau
- Use extracts for performance; live connections for real-time
- Set up publishing permissions by project
- Use parameters for user-driven filtering
- Avoid excessive calculated fields; pre-compute in database when possible

### Looker
- Define once in LookML; reuse across dashboards
- Use explores to prevent user confusion
- Set up content validation for production
- Use `sql_always_where` for row-level security

### Power BI
- Use DAX carefully; complex measures can be slow
- Import mode for performance; DirectQuery for large datasets
- Set up row-level security (RLS) by role
- Use bookmarks and drill-through for interactivity

### Looker Studio (Data Studio)
- Blend data sparingly; prefer single source
- Use community visualizations cautiously
- Set up data credentials for sharing

## Dashboard Performance

| Issue | Fix |
|---|---|
| Slow load time | Reduce data granularity, use extracts, limit filters |
| Too many sheets | Consolidate; one dashboard = one purpose |
| Complex calculations | Move to database layer (dbt, SQL views) |
| Excessive interactivity | Simplify; not every chart needs to filter every other |

## Documentation Template

```markdown
# [Dashboard Name]

## Purpose
What question does this answer?

## Audience
Who uses it and how often?

## Data Sources
- [Source 1] — refresh frequency
- [Source 2] — refresh frequency

## Key Metrics
| Metric | Definition | Owner |
|---|---|---|
| Revenue | Sum of order_value | Finance |

## Filters
- Date range: defaults to last 30 days
- Region: all by default

## Known Issues / Limitations
- Data lags by 24 hours
- Excludes refunds (see separate dashboard)

## Changelog
| Date | Change | Author |
|---|---|---|
| 2024-01-15 | Added region filter | @analyst |
```
