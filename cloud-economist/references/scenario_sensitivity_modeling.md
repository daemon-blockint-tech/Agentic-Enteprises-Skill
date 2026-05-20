# Scenario and sensitivity modeling

## Table of contents

1. [Scenario set](#scenario-set)
2. [Key drivers](#key-drivers)
3. [Sensitivity tornado](#sensitivity-tornado)
4. [Model hygiene](#model-hygiene)

## Scenario set

Standard three scenarios:

| Scenario | Usage | Price/discount | One-time |
|---|---|---|---|
| Low | −20% growth, higher efficiency | List or weak EA | Low migration |
| Base | Planned roadmap | Expected EA/discount | Planned migration |
| High | +30% growth, new products | Full EA utilization | Full migration + DR |

Add **stress** for regulatory or outage-driven duplication if relevant.

## Key drivers

Rank for cloud spend variance:

1. **Compute hours** (instance type, count, region)
2. **Storage growth** (class, lifecycle)
3. **Egress** (architecture-dependent)
4. **Commit utilization** and true-up
5. **New services** (AI/GPU, analytics)
6. **FX** (multi-currency billing)
7. **Labor** (if hybrid ops included)

Document correlation — drivers rarely move independently.

## Sensitivity tornado

One-at-a-time % change on base annual spend:

```
driver: +10% API traffic → +$X (+Y%)
driver: −5% rightsizing → −$Z
```

Shows where leadership should focus governance vs accept variance.

## Model hygiene

- **Version** models; date stamp assumptions
- Separate **one-time** from **run-rate**
- Link assumptions to named owner (product, infra, finance)
- Reconcile base case to `finops-analyst` trailing 12m actuals
- Avoid false precision — round to meaningful $ for exec audience

When model diverges >15% from actuals for 2 quarters, refresh assumptions before next commit decision.
