# Data-Driven Business Analysis

## Cost-Benefit Analysis

### Simple ROI
```
ROI = (Benefit - Cost) / Cost × 100%
```

### Multi-Year Analysis

| Year | Cost | Benefit | Net | Discounted (10%) |
|---|---|---|---|---|
| 0 | $100K | $0 | -$100K | -$100K |
| 1 | $20K | $80K | +$60K | +$54.5K |
| 2 | $20K | $100K | +$80K | +$66.1K |
| 3 | $20K | $120K | +$100K | +$75.1K |
| **NPV** | | | | **+$95.7K** |

**Payback period:** Year 1 (cumulative turns positive)

### Cost Categories

| Category | Examples |
|---|---|
| One-time | Software licenses, implementation, training, migration |
| Recurring | Subscription fees, maintenance, support, hosting |
| Hidden | Change management, productivity dip during transition, technical debt |
| Opportunity | What you could have done with the same resources |

### Benefit Categories

| Category | Measurement |
|---|---|
| Revenue increase | New sales, upsell, reduced churn |
| Cost reduction | Labor savings, error reduction, automation |
| Risk mitigation | Compliance fines avoided, audit readiness |
| Strategic | Market positioning, customer satisfaction, employee retention |

## SWOT Analysis

### Template

| **Strengths** (Internal, Positive) | **Weaknesses** (Internal, Negative) |
|---|---|
| What do we do well? | What could we improve? |
| What resources do we have? | Where do we lack resources? |
| What do others see as our strengths? | What do others see as our weaknesses? |

| **Opportunities** (External, Positive) | **Threats** (External, Negative) |
|---|---|
| What trends could we exploit? | What obstacles do we face? |
| What changes create openings? | What are competitors doing? |
| What customer needs are unmet? | What regulatory risks exist? |

**Action mapping:**
- Strengths + Opportunities → **Invest/Grow**
- Strengths + Threats → **Defend**
- Weaknesses + Opportunities → **Fix gaps**
- Weaknesses + Threats → **Avoid/Mitigate**

## Root Cause Analysis

### 5 Whys

```
Problem: Orders are shipping late.

Why? → Warehouse backlog.
Why? → Picking takes longer than planned.
Why? → Items are not in expected locations.
Why? → Receiving team doesn't update bin locations.
Why? → No process requires bin location confirmation.

Root cause: Missing receiving process step.
```

### Fishbone (Ishikawa) Diagram

Categories to investigate:
- **People**: Skills, training, staffing
- **Process**: Steps, handoffs, approvals
- **Technology**: Systems, integrations, data quality
- **Data**: Accuracy, timeliness, completeness
- **Environment**: Market, regulation, competition
- **Materials**: Suppliers, inputs, quality

## Forecasting Techniques

| Technique | When | Formula/Approach |
|---|---|---|
| Trend line | Stable growth | Linear regression on historical data |
| Moving average | Smoothing volatility | Average of last N periods |
| Seasonal decomposition | Repeating patterns | Decompose into trend + seasonal + residual |
| Scenario planning | High uncertainty | Best case, expected case, worst case |

**Forecast accuracy metrics:**
- MAPE (Mean Absolute Percentage Error): `mean(|actual - forecast| / actual)`
- Bias: Systematic over/under-forecasting

## Benchmarking

### Internal Benchmarking
Compare across teams, regions, or time periods

### External Benchmarking
| Source | What It Provides |
|---|---|
| Industry reports | Averages by sector (Gartner, Forrester) |
| Peer networks | Informal comparisons with similar companies |
| Public filings | Competitor performance metrics |
| Benchmarking services | Standardized comparisons (APQC, etc.) |

### Benchmarking Steps
1. Define what to benchmark (KPI, process, cost)
2. Identify comparison sources
3. Normalize for scale/context
4. Identify gaps
5. Set improvement targets

## Process Improvement

### Lean Principles
1. **Define value** from customer perspective
2. **Map value stream** — every step from request to delivery
3. **Create flow** — eliminate waiting and batching
4. **Establish pull** — produce only what is needed
5. **Pursue perfection** — continuous improvement

### Six Sigma DMAIC

| Phase | Activities |
|---|---|
| Define | Problem statement, scope, stakeholders, goal |
| Measure | Baseline metrics, data collection plan |
| Analyze | Root cause, statistical validation |
| Improve | Solution design, pilot, implementation |
| Control | Monitor, standardize, sustain gains |

### Kaizen Event (Rapid Improvement)
- Duration: 3-5 days
- Team: 5-8 people from affected areas
- Output: Implemented improvements, documented new standard
