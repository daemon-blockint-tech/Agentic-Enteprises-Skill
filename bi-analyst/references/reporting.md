# Reporting & Metrics

## KPI Framework

### Metric Hierarchy

```
Business Objective
  └── Strategic KPIs (lagging indicators)
        └── Operational KPIs (leading indicators)
              └── Tactical Metrics (diagnostics)
```

**Example:**
```
Increase revenue by 20%
  └── Monthly Recurring Revenue (MRR)
        └── Customer Acquisition Rate
              └── Marketing Qualified Leads (MQLs)
              └── Lead-to-Customer Conversion Rate
        └── Customer Retention Rate
              └── 30-Day Activation Rate
              └── Support Ticket Volume
        └── Average Revenue Per User (ARPU)
              └── Upsell/Cross-sell Rate
              └── Product Usage Frequency
```

## Metric Definition Standards

### Required Fields

| Field | Description | Example |
|---|---|---|
| Name | Clear, concise name | "Monthly Recurring Revenue" |
| Business context | Why this matters | "Primary indicator of business health" |
| Formula | Unambiguous calculation | `SUM(subscription_amount) WHERE status = 'active'` |
| Unit | Currency, count, percentage | USD, count, % |
| Dimensions | How to slice it | by plan, by region, by acquisition channel |
| Data source | System of record | `subscriptions` table |
| Owner | Who is responsible | Finance team |
| Update frequency | How often refreshed | Daily |
| Target / benchmark | Goal or comparison | $1M/month, +10% YoY |

### Metric Categories

| Type | Characteristics | Examples |
|---|---|---|
| Count | Raw volume | Orders, users, sessions |
| Sum | Aggregated value | Revenue, page views |
| Ratio / Rate | Normalized comparison | Conversion rate, CTR, retention |
| Average | Central tendency | AOV, session duration |
| Percentile | Distribution insight | P95 latency, P90 session duration |

## Report Templates

### Weekly Business Review
```markdown
# Week of [Date]

## Executive Summary
- Key takeaway 1
- Key takeaway 2
- Action required from leadership

## KPIs vs Targets
| KPI | Current | Target | Status | Trend |
|---|---|---|---|---|
| Revenue | $1.2M | $1.1M | ✅ Ahead | ↑ 5% |

## Deep Dives
### [Topic 1]
- Observation
- Root cause (if known)
- Recommended action

## Actions & Owners
| Action | Owner | Due |
|---|---|---|
| Investigate churn spike | @analyst | Friday |
```

### Monthly Performance Report
```markdown
# [Month] Performance Report

## Highlights
Top 3 wins and top 3 concerns

## Trends (6-month view)
[Insert key trend charts]

## Segment Performance
| Segment | Revenue | Growth | Notes |
|---|---|---|---|
| Enterprise | $500K | +12% | Strong upsell |
| SMB | $300K | -3% | Churn in Q2 cohort |

## Forecast vs Actual
| Metric | Forecast | Actual | Variance |
|---|---|---|---|

## Next Month Focus
1. Priority 1
2. Priority 2
```

## Root Cause Analysis Template

When a metric moves unexpectedly:

```markdown
## Metric: [Name]
## Observation: [What changed and by how much]
## Timeframe: [When did it start]

### Hypotheses
1. [Hypothesis 1] — [How to test]
2. [Hypothesis 2] — [How to test]
3. [Hypothesis 3] — [How to test]

### Analysis
[Data and charts supporting or refuting each hypothesis]

### Conclusion
[Most likely cause with confidence level]

### Recommended Action
[What should be done, by whom, by when]
```

## Data Quality Disclaimers

Always include when relevant:
- Data latency: "Data refreshes daily at 6 AM UTC"
- Known gaps: "Refund data lags by 48 hours"
- Scope limitations: "Excludes test accounts and internal users"
- Methodology notes: "Cohort defined by first purchase date"

## Report Automation

| Approach | When | Tools |
|---|---|---|
| Scheduled email | Static report, broad audience | BI tool scheduling, Python scripts |
| Live dashboard | Interactive, self-service | Tableau, Looker, Power BI |
| Alert-driven | Exception-based reporting | dbt + Slack, Monte Carlo |
| Embedded | Product analytics | Metabase, Looker, custom apps |
