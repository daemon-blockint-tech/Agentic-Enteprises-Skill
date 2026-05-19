# Vendor & Tool Management

## Vendor Evaluation

### Evaluation Criteria

| Dimension | Weight | Questions |
|---|---|---|
| Technical capability | 25% | Does it meet requirements? Scale? Integrations? |
| Reliability | 20% | Uptime SLA? Support quality? Incident history? |
| Cost | 20% | TCO? Pricing model? Hidden costs? |
| Security | 15% | Certifications? Data handling? Compliance? |
| Vendor health | 10% | Financial stability? Market position? |
| Ease of use | 10% | Learning curve? Documentation? Community? |

### Vendor Scorecard

```markdown
| Vendor | Tech | Reliability | Cost | Security | Health | Ease | Total |
|---|---|---|---|---|---|---|---|
| Vendor A | 4 | 3 | 2 | 4 | 3 | 4 | 3.2 |
| Vendor B | 3 | 4 | 4 | 3 | 4 | 3 | 3.4 |
```

### Due Diligence Checklist
- [ ] Financial statements (if critical vendor)
- [ ] Security questionnaire (SOC 2, ISO 27001)
- [ ] Reference customers (similar size/use case)
- [ ] Support SLA and escalation path
- [ ] Data residency and GDPR/CCPA compliance
- [ ] Exit strategy (data portability, format)

## Cost Optimization

### Cost Attribution

**Tagging strategy:**
- Environment: `prod`, `staging`, `dev`
- Team: `analytics`, `engineering`, `science`
- Project: `feature-name`, `migration`
- Data tier: `tier1`, `tier2`, `tier3`

**Chargeback models:**
1. **Showback**: Visibility only (recommended starting point)
2. **Chargeback**: Teams billed for usage
3. **Hybrid**: Base allocation + overage chargeback

### Optimization Techniques

| Technique | Savings | Implementation |
|---|---|---|
| Reserved instances / CUDs | 30-70% | Commit to 1-3 year term |
| Storage tiering | 50-80% | Hot → warm → cold → archive |
| Query optimization | 20-50% | Tune SQL, materialize views |
| Right-sizing | 10-30% | Downsize over-provisioned resources |
| Spot/preemptible | 60-90% | Fault-tolerant workloads only |
| Auto-shutdown | 20-40% | Dev/test environments off-hours |

### Monthly Cost Review

```markdown
## Cost Review — [Month]

### Actual vs Budget
| Category | Budget | Actual | Variance |
|---|---|---|---|
| Compute | $5K | $5.5K | +10% |
| Storage | $3K | $2.8K | -7% |
| Egress | $1K | $1.2K | +20% |

### Per-Unit Costs
| Metric | This Month | Last Month | Trend |
|---|---|---|---|
| Cost per TB queried | $12 | $14 | ↓ |
| Cost per pipeline run | $0.05 | $0.06 | ↓ |

### Optimization Opportunities
1. [Opportunity] — Estimated savings: $X/month

### Contract Renewals (Next 6 Months)
| Vendor | Renewal Date | Current Spend | Action |
|---|---|---|---|
| Snowflake | March | $4K/mo | Evaluate alternatives |
```

## Tool Selection

### Monitoring & Alerting

| Tool | Best For | Cost |
|---|---|---|
| Datadog | Full-stack, SaaS | High |
| Prometheus + Grafana | Open source, flexible | Medium (hosting) |
| New Relic | APM-heavy | Medium |
| PagerDuty | Incident management | Medium |
| Opsgenie | Atlassian integration | Low |

### Data Observability

| Tool | Focus | Cost |
|---|---|---|
| Monte Carlo | Data quality | High |
| Bigeye | Data observability | Medium |
| Soda | Open source data quality | Low |
| Elementary | dbt-native observability | Low |

### Automation & Orchestration

| Tool | Best For | Cost |
|---|---|---|
| Airflow | Workflow orchestration | Free (self-hosted) |
| Prefect | Modern alternative | Freemium |
| Dagster | Data-aware orchestration | Freemium |
| dbt Cloud | Analytics engineering | Medium |

### Backup & DR

| Tool | Best For | Cost |
|---|---|---|
| AWS Backup | AWS-native | Low |
| Veeam | Enterprise multi-cloud | Medium |
| Commvault | Comprehensive | High |
| Native snapshots | Simple use cases | Low |

## Contract Management

### Key Terms to Negotiate
- **Pricing**: Per-unit vs flat rate, annual vs monthly
- **SLA**: Uptime guarantee, credit structure
- **Support**: Response time, escalation path, dedicated CSM
- **Termination**: Notice period, data return format
- **Liability**: Cap on damages, indemnification
- **Auto-renewal**: Opt-in vs opt-out

### Renewal Timeline
- **T-90 days**: Evaluate current vendor performance
- **T-60 days**: Research alternatives, issue RFP if needed
- **T-30 days**: Negotiate terms, prepare fallback
- **T-14 days**: Final decision, notify stakeholders
- **T-0**: Execute or migrate

## Automation Strategy

### Automation Priorities
1. **High volume + low complexity** (first target)
   - Example: Daily backup verification
2. **Error-prone manual tasks**
   - Example: Schema drift detection
3. **Time-sensitive responses**
   - Example: Auto-remediation for known issues

### Automation Framework
```
Trigger → Validation → Action → Verification → Notification
```

**Example: Auto-remediation**
```python
def auto_remediate_disk_full():
    if disk_usage > 90%:
        # Validate: check it's not a known growth pattern
        if growth_rate < threshold:
            # Action: clean old logs
            clean_old_logs(days=7)
            # Verification
            if disk_usage < 85%:
                notify("Auto-remediated disk full")
            else:
                page_oncall("Disk still full after cleanup")
```

## Exit Strategy

### Vendor Migration Planning
1. **Inventory**: All integrations, users, data formats
2. **Alternative evaluation**: At least 2 options
3. **Migration plan**: Timeline, data migration, testing
4. **Parallel run**: Run both systems for validation period
5. **Cutover**: Defined go/no-go criteria
6. **Decommission**: Secure data deletion, contract closure

### Data Portability Checklist
- [ ] Export in open format (Parquet, CSV, JSON)
- [ ] Document schema and transformations
- [ ] Verify completeness of export
- [ ] Test import into alternative system
- [ ] Update all downstream consumers
