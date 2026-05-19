# Reporting & SaaS Metrics

## Core SaaS Metrics

### Revenue Metrics

| Metric | Formula | What It Tells You |
|---|---|---|
| ARR | MRR × 12 | Run-rate annual revenue |
| MRR | Sum of monthly subscription values | Monthly recurring base |
| Net New ARR | New ARR + Expansion - Churn - Contraction | Growth in period |
| Net Revenue Retention | (Starting ARR + Expansion - Churn - Contraction) / Starting ARR | Revenue growth from existing customers |
| Gross Revenue Retention | (Starting ARR - Churn - Contraction) / Starting ARR | How much revenue you keep |
| ACV | Total contract value / Number of contracts (annualized) | Average deal size |
| TCV | Total contract value (all years) | Total booking commitment |
| RPO | Deferred revenue + Backlog (invoiced but not recognized) | Future revenue visibility |
| cRPO | Current RPO (next 12 months) | Near-term revenue visibility |
| nRPO | Non-current RPO (beyond 12 months) | Long-term revenue visibility |

### Efficiency Metrics

| Metric | Formula | Benchmark |
|---|---|---|
| CAC | Sales + Marketing spend / New customers acquired | Varies by segment |
| CAC Payback | CAC / (Gross margin × ARPU) | <12 months ideal |
| LTV | Average revenue per customer × Gross margin / Logo churn rate | >3× CAC |
| LTV:CAC Ratio | LTV / CAC | >3:1 |
| Magic Number | Net New ARR × 4 / Previous quarter S&M spend | >1.0 = efficient growth |
| Rule of 40 | Revenue growth % + EBITDA margin % | >40% = healthy |
| Burn Multiple | Net burn / Net New ARR | <1.5 = efficient |

### Unit Economics

```
Monthly Revenue per Customer (ARPU) = MRR / Customer count
Gross Margin = (Revenue - COGS) / Revenue (target: 75-85% for SaaS)
Net Margin = Net Income / Revenue
Expansion Rate = Expansion ARR / Starting ARR
Churn Rate = Churned ARR / Starting ARR
Logo Churn = Churned customers / Starting customers
```

## Revenue Recognition Reporting

### Revenue Disaggregation

**By timing:**
```
Revenue:
  Subscription — over time          $XXX
  Professional services — over time $XXX
  License — point in time           $XXX
  Usage/transaction-based           $XXX
  Total revenue                     $XXX
```

**By geography:**
```
Revenue by region:
  Americas                          $XXX (XX%)
  EMEA                              $XXX (XX%)
  APAC                              $XXX (XX%)
  Total                             $XXX
```

**By contract type:**
```
  Annual upfront                    $XXX
  Annual quarterly billing          $XXX
  Monthly                           $XXX
  Multi-year                        $XXX
  Total                             $XXX
```

### Contract Asset / Liability

| Item | Classification | Recognition |
|---|---|---|
| Deferred revenue (cash received, not earned) | Liability | Recognize as performance satisfied |
| Contract asset (earned, not billed) | Asset | Bill and convert to receivable |
| Receivable (billed, not collected) | Asset | Collect cash |
| Refund liability | Liability | Estimate and adjust |

## Board Reporting

### SaaS Board Package Structure

```markdown
# Board Package — [Quarter]

## Executive Summary
- ARR: $XXM (+XX% YoY)
- NRR: XXX%
- Net New ARR: $XM
- Cash: $XXM (Runway: XX months)

## Financial Highlights
| Metric | Q[X] | Q[X-1] | YoY | vs Plan |
|---|---|---|---|---|
| Revenue | | | | |
| Gross Margin | | | | |
| OpEx | | | | |
| Net Income | | | | |
| Cash Flow | | | | |

## SaaS Metrics
| Metric | Current | Prior | Change |
|---|---|---|---|
| ARR | | | |
| NRR | | | |
| GRR | | | |
| Logo Churn | | | |
| CAC | | | |
| LTV | | | |
| Payback Period | | | |
| Customers | | | |
| ACV | | | |

## Revenue Bridge
Starting ARR: $XX
+ New Business: +$X
+ Expansion: +$X
- Contraction: -$X
- Churn: -$X
= Ending ARR: $XX

## Key Initiatives
1. [Initiative 1 — status]
2. [Initiative 2 — status]

## Risks & Mitigations
| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| [Risk 1] | High | Medium | [Action] |
```

## Forecasting

### Revenue Forecast Methods

| Method | Best For | Approach |
|---|---|---|
| Bottom-up (pipeline) | Short-term (1-3 months) | Weighted pipeline + historical close rates |
| ARR build | Annual planning | Customers × ARPU × NRR assumptions |
| Cohort-based | Medium-term | By acquisition cohort, apply retention curves |
| Historical trend | Stable businesses | Growth rate applied to base |

### Forecast Components
```
Revenue forecast =
  Existing customer base (known renewals)
  + Expected expansion from existing
  + New business (sales forecast × probability)
  + Usage/variable revenue (trend + seasonality)
  - Expected churn (by cohort)
```

### Variance Analysis
```
Actual vs Forecast:
  Forecast: $500K
  Actual:   $520K
  Variance: +$20K (+4%)

Drivers:
  + New business beat by $15K (2 deals closed early)
  + Expansion higher by $10K (1 large upsell)
  - Churn $5K higher than expected (1 mid-market)
```

## KPI Dashboards

### Daily Monitoring
- Cash balance and runway
- New bookings (sales closed)
- Billing exceptions
- Failed payments

### Weekly Monitoring
- MRR movement
- Churn events
- Expansion pipeline
- Collections (DSO trend)
- Close progress

### Monthly Monitoring
- Full close package
- SaaS metrics (ARR, NRR, CAC, LTV)
- Financial statements
- Budget vs actual
- Forecast updates

### Quarterly Monitoring
- Board metrics
- Audit preparation
- Strategic planning inputs
- Compensation accruals
- Tax provision estimates

## SaaS Revenue-Specific Disclosures

### Required Disclosures (ASC 606)
1. Revenue disaggregated by timing, geography, product
2. Opening/closing balances of receivables, contract assets, deferred revenue
3. Performance obligations: description, timing, significant judgments
4. Transaction price allocated to remaining obligations
5. Significant payment terms

### Practical Disclosure Format
```
Note X — Revenue from Contracts with Customers

Performance Obligations:
- SaaS subscriptions: recognized ratably over contract term
- Professional services: recognized as services are performed
- Support: recognized ratably over contract term

Revenue Disaggregation:
  Subscription: $XXX (XX%)
  Services: $XXX (XX%)
  Total: $XXX

Geographic:
  US: $XXX
  International: $XXX

Timing:
  Over time: $XXX
  Point in time: $XXX

Remaining Performance Obligation: $XXX
  Expected recognition:
    Next 12 months: $XXX
    13-24 months: $XXX
    >24 months: $XXX
```
