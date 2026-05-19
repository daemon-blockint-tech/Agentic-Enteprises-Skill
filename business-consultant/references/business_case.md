# Business case

## Table of contents

1. [Options summary](#options-summary)
2. [Benefits and costs](#benefits-and-costs)
3. [ROI and sensitivity](#roi-and-sensitivity)
4. [Risk register](#risk-register)
5. [Recommendation slide](#recommendation-slide)

## Options summary

Compare **at least two** distinct options plus status quo:

| | Status quo | Option A | Option B |
|---|---|---|---|
| Summary | | | |
| Time to value | | | |
| NPV / payback (if modeled) | | | |
| Strategic fit | | | |
| Implementation risk | Low/Med/High | | |

## Benefits and costs

**Benefits** (annualized where recurring):

- Revenue uplift (volume × price × attach)
- Cost takeout (FTE, vendor, infra)
- Risk reduction (avoided fines, churn, downtime)—state assumptions

**Costs:**

- One-time: implementation, migration, change management
- Run rate: licenses, headcount, support
- Opportunity cost: what we stop doing

Label **hard** vs **soft** benefits; do not double-count.

For detailed revenue recognition or contract accounting, involve `senior-revenue-accountant`.

## ROI and sensitivity

Simple model when data allows:

```
NPV = Σ (benefits_t - costs_t) / (1 + r)^t
Payback = first period cumulative net benefit > 0
```

Sensitivity table (vary ±20%):

| Variable | Base | Low | High | NPV impact |
|---|---|---|---|---|
| Adoption rate | | | | |
| Cost savings | | | | |

State **confidence** (high/medium/low) per line item.

## Risk register

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Adoption failure | | | Pilot + training | |
| Vendor delay | | | Contract milestones | |

## Recommendation slide

```markdown
**We recommend Option [X]** because [primary reason].

- Delivers [metric] by [date] with [confidence]
- Requires [investment] and [key dependency]
- Main risk: [risk]; mitigated by [action]

**Not recommended:** Option Y — [one-line why]
```
