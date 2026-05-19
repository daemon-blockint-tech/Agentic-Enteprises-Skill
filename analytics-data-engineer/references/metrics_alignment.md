# Metrics Alignment

## Definition of done for a metric

| Field | Example |
|---|---|
| **Name** | Net revenue |
| **Definition** | Sum of line revenue after discounts, ex tax |
| **Grain** | Order line |
| **Dimensions** | Product, region, order date |
| **Source mart** | `fct_order_lines` |
| **Owner** | Finance analytics |
| **Cadence** | Daily by 6am UTC |

Document in metric catalog or mart YAML `meta`.

## Reconciliation workflow

When dashboard ≠ mart:

1. Confirm **same grain** and filters
2. Confirm **same time zone** and date field
3. Compare SQL from BI tool vs mart query
4. Check incremental watermark and late data
5. Log root cause (definition change vs bug)

## Roles

| Role | Responsibility |
|---|---|
| `business-analyst` | Business rule sign-off |
| `bi-analyst` | Dashboard and explore experience |
| Analytics data engineer | Mart SQL and tests |
| `data-warehouse-engineer` | Source load and platform issues |

## Changing a metric

1. Propose definition change with before/after SQL
2. Impact exposures and dashboards
3. Version or communicate breaking change
4. Update tests to match new rule

## Semantic layer note

If Looker/MetricFlow/semantic layer exists:

- Prefer **single definition** in semantic layer OR mart, not both diverging
- Analytics engineer owns mart; BI may own explores — align in writing

## PII and aggregation

- Minimum necessary dimensions in marts
- Aggregates for broad self-serve; row-level restricted roles
