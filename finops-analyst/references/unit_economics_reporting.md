# Unit economics and reporting

## Table of contents

1. [Unit definitions](#unit-definitions)
2. [Calculation patterns](#calculation-patterns)
3. [Executive narrative](#executive-narrative)
4. [Dashboards](#dashboards)

## Unit definitions

Pick units aligned to business model:

| Business | Example unit |
|---|---|
| SaaS | Cost per active customer / per MAU |
| API product | Cost per 1M requests |
| Data platform | Cost per TB stored or queried |
| Internal platform | Cost per engineering team or deploy |

Document **shared cost** allocation to units (platform tax).

## Calculation patterns

```
unit_cost = (direct_tagged_spend + allocated_shared_spend) / unit_count
```

Rules:

- Use **same period** for numerator and denominator
- Exclude **one-time** spikes from unit trend or footnote them
- **Gross margin** view: unit revenue − unit infra cost (with finance)

For multi-tenant: allocate by **usage meter** not equal split unless fair.

## Executive narrative

One-page monthly:

- Total cloud spend vs budget and vs last month
- Top 3 drivers of change
- Savings delivered (verified) vs backlog
- Commitment utilization %
- Untagged % and top offenders
- Forward look — launches, commits, risks

Avoid raw service lists without interpretation.

## Dashboards

Layers:

1. **Company** — total, by payer account, budget burn
2. **BU/product** — tagged allocation
3. **Service owner** — drill to resource level
4. **Optimization** — open recommendations $

Self-serve for engineering; FinOps maintains **data quality** and definitions.
