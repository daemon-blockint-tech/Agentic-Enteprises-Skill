# Marginal cost and elasticity

## Table of contents

1. [Marginal cost](#marginal-cost)
2. [Elastic workloads](#elastic-workloads)
3. [Unit economics link](#unit-economics-link)
4. [Egress and data economics](#egress-and-data-economics)

## Marginal cost

Marginal cost = incremental cloud spend for **one more unit** of business output.

Examples:

- Cost per additional 1k MAU (compute + DB + bandwidth)
- Cost per new microservice at steady traffic
- Cost per TB stored per month

Calculate from:

```
marginal = (total_cost_at_Q2 - total_cost_at_Q1) / (Q2 - Q1)
```

Use **tagged** workloads where possible; allocate shared platform separately.

## Elastic workloads

Plot cost vs utilization:

| Shape | Economic note |
|---|---|
| Flat + step | Over-provisioned baseline; FinOps rightsizing |
| Linear | Healthy for serverless/pay-go |
| Super-linear | Egress, cross-AZ, unbounded logs — architect review |

**Peak-to-average ratio** drives commit suitability — high ratio → less RI, more on-demand/spot.

## Unit economics link

Bridge to product and finance:

```
gross_margin = revenue_per_unit - (cloud_cogs_per_unit + allocated_platform)
```

Cloud economist supplies **cloud_cogs** assumptions; `finops-analyst` tracks actuals; `compute-accounting-manager` maps to GL.

Flag when cloud COGS % threatens target margin at roadmap scale.

## Egress and data economics

Often dominant marginal cost:

- Cross-AZ replication
- Internet egress
- Cross-region DR
- SaaS analytics export

Model **$/GB** by path; compare architecture alternatives (CDN, compression, regional aggregation).

Partner with `cloud-architect` for data flow changes.
