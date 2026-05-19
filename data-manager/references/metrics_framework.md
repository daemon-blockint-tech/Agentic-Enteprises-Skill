# Metrics & SLA Framework

## Data Quality Scorecard

### Dimensions & Weights

| Dimension | Weight | Metric | Target |
|---|---|---|---|
| Completeness | 25% | % mandatory fields populated | >99% |
| Uniqueness | 20% | % duplicate keys | <0.1% |
| Validity | 20% | % rows passing business rules | >98% |
| Timeliness | 20% | % pipelines meeting SLA | >95% |
| Consistency | 15% | % cross-system matches | >99% |

**Overall quality score = weighted average of dimension scores**

### Scorecard Template

```markdown
## Data Quality Scorecard — [Month]

### Overall Score: 94/100 (-2 from last month)

| Dataset | Completeness | Uniqueness | Validity | Timeliness | Consistency | Score |
|---|---|---|---|---|---|---|
| f_orders | 99% | 100% | 97% | 92% | 99% | 97 |
| d_customer | 98% | 99.9% | 96% | 100% | 98% | 98 |
| f_inventory | 95% | 100% | 99% | 85% | 99% | 94 |

### Issues
1. f_orders timeliness: Shopify API delay caused 8% late loads
   - Owner: @data-eng-shopify
   - Action: Implement retry with exponential backoff
   - Due: [date]

2. d_customer validity: 4% invalid phone numbers
   - Owner: @data-steward-customer
   - Action: Update regex validation rule
   - Due: [date]
```

## SLA Framework

### SLA Definitions

**Availability:** % of time system is operational
- Formula: `(Total time - Downtime) / Total time × 100`
- Target: 99.9% (8.76 hours downtime/year)

**Freshness:** Time from source event to availability for query
- Formula: `MAX(event_time) - NOW()` for each dataset
- Tier 1: <1 hour, Tier 2: <4 hours, Tier 3: <24 hours

**Latency:** Query response time
- P50 (median) and P95 targets
- Dashboard queries: P95 <5 seconds
- Ad-hoc queries: P95 <30 seconds

**Accuracy:** % of correct data (vs source of truth)
- Measured by sampling and reconciliation
- Target: 99.5% for Tier 1, 99% for Tier 2

### SLA Monitoring Dashboard

```markdown
## SLA Dashboard — [Week of]

### Availability
| System | Uptime | Incidents | Status |
|---|---|---|---|
| Snowflake | 99.95% | 0 | 🟢 On track |
| Airflow | 99.2% | 1 (P3) | 🟡 At risk |

### Freshness
| Dataset | SLA | Actual | Breaches | Status |
|---|---|---|---|---|
| f_orders | <1h | 45 min | 0 | 🟢 On track |
| d_customer | <4h | 6h | 2 | 🔴 Breached |

### Latency
| Query Type | P50 | P95 | Target P95 | Status |
|---|---|---|---|---|
| Dashboard | 1.2s | 3.5s | <5s | 🟢 On track |
| Ad-hoc | 5s | 25s | <30s | 🟢 On track |
```

## Team Productivity Metrics

### Engineering Metrics (DORA-inspired)

| Metric | Definition | Target |
|---|---|---|
| Deployment frequency | Deployments per week | >2/week |
| Lead time | Commit to production | <3 days |
| Change failure rate | % deployments causing incident | <5% |
| MTTR | Mean time to recovery | <2 hours |

### Analyst Productivity

| Metric | Definition | Target |
|---|---|---|
| Time to insight | Request received → dashboard live | <2 weeks |
| Query reuse | % queries used by >1 person | >30% |
| Self-serve ratio | % requests fulfilled without engineering | >50% |

### Operational Metrics

| Metric | Definition | Target |
|---|---|---|
| On-call burden | Incidents per person per month | <3 |
| Alert fatigue | Alerts per day per on-call | <10 |
| Documentation coverage | % datasets with full documentation | >80% |
| Tech debt ratio | Debt items / total backlog | <20% |

## Cost Management Metrics

### Cost Per Unit

| Unit | Calculation | Target |
|---|---|---|
| Cost per TB processed | Total compute cost / TB queried | Trend down |
| Cost per pipeline run | Pipeline cost / successful runs | Trend down |
| Cost per user | Total cost / active data consumers | Trend flat/down |
| Storage growth rate | % month-over-month storage growth | <10% |

### Cost Attribution

**Tagging strategy:**
- Environment: `prod`, `staging`, `dev`
- Team: `analytics`, `engineering`, `science`
- Product: `revenue`, `marketing`, `operations`
- Project: `feature-name`, `migration`

**Chargeback model options:**
1. Showback: Visibility only (recommended starting point)
2. Chargeback: Teams billed for their usage
3. Hybrid: Base allocation + overage chargeback

## Reporting Cadence

| Report | Audience | Frequency | Owner |
|---|---|---|---|
| Quality scorecard | Data team + stakeholders | Monthly | Data quality lead |
| SLA review | Engineering + leadership | Weekly | SRE/on-call lead |
| Cost report | Finance + engineering managers | Monthly | FinOps/operations |
| Team productivity | Engineering leadership | Quarterly | Engineering manager |
| Incident summary | All data team | Weekly | Incident commander |
