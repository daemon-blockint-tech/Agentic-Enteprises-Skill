# Platform Operations

## Monitoring Stack

### Metrics by Layer

**Infrastructure:**
| Metric | Alert When | Severity |
|---|---|---|
| CPU utilization | >80% for 10 min | P3 |
| Memory utilization | >85% for 5 min | P3 |
| Disk utilization | >85% | P2 |
| Network I/O | >baseline +50% | P3 |

**Data warehouse:**
| Metric | Alert When | Severity |
|---|---|---|
| Query queue depth | >20 for >10 min | P2 |
| Failed queries/min | >5 | P2 |
| Connection count | >90% of max | P2 |
| Replication lag | >30s | P1 |
| Long-running queries | >30 min | P3 |

**Data pipelines:**
| Metric | Alert When | Severity |
|---|---|---|
| Job failure | Any failure on critical path | P1 |
| Job duration | >150% of baseline | P3 |
| Late start | >30 min after scheduled | P3 |
| Row count anomaly | >20% delta vs expected | P2 |
| Data quality score | <95% | P2 |

### Alerting Best Practices
- Alert on symptoms, not causes (when possible)
- Every alert must have a runbook link
- Page only for P1-P2; P3-P4 to ticket queue
- Threshold review monthly (reduce false positives)

## SLA Framework

### SLA Definitions

| Tier | Description | Availability | Freshness | RTO |
|---|---|---|---|---|
| Tier 1 | Business-critical | 99.9% | <1 hour | 1 hour |
| Tier 2 | Operational | 99.5% | <4 hours | 4 hours |
| Tier 3 | Analytics | 99% | <24 hours | 24 hours |
| Tier 4 | Development | Best effort | <7 days | 72 hours |

### SLA Monitoring Dashboard

```markdown
## SLA Dashboard — [Week]

### Availability
| System | Uptime | Incidents | Status |
|---|---|---|---|
| Data warehouse | 99.95% | 0 | On track |
| Pipeline platform | 99.2% | 1 (P3) | At risk |

### Freshness
| Dataset | SLA | Actual | Breaches |
|---|---|---|---|
| f_orders | <1h | 45 min | 0 |
| d_customer | <4h | 6h | 2 |

### Action Items
| Issue | Owner | Due | Status |
|---|---|---|---|
| Customer dim latency | @ops-team | Friday | In progress |
```

## Incident Response Runbooks

### P1 Response (Critical)

**0-15 minutes: Detection & Triage**
1. Acknowledge page/alert
2. Assess scope: which systems, users, data affected
3. Create war room (Slack/Zoom) with bridge number
4. Notify stakeholders (status page, executive if needed)

**15-60 minutes: Mitigation**
1. Identify root cause (don't fix yet, just understand)
2. Apply temporary fix (rollback, redirect, scale up)
3. Confirm mitigation with monitoring
4. Communicate status every 15 minutes

**1-4 hours: Resolution**
1. Deploy permanent fix or plan for later
2. Verify all systems stable
3. Close incident when stable for >1 hour
4. Schedule post-mortem within 48 hours

### Runbook Template
```markdown
# [System/Alert Name] Runbook

## Alert
[What triggers this alert]

## Symptoms
- [ ] Symptom 1
- [ ] Symptom 2

## Immediate Checks
1. Check dashboard: [link]
2. Check logs: [query/link]
3. Check recent changes: [deployment log]

## Resolution Steps
1. [Step 1 with command]
2. [Step 2 with command]
3. Verify: [how to confirm]

## Escalation
If unresolved in [X] minutes:
- Escalate to: [person/team]
- With: [what information to provide]

## Post-Resolution
- [ ] Update status page
- [ ] Document in incident log
```

## Capacity Planning

### Monthly Review
- Review utilization trends (CPU, storage, memory)
- Identify bottlenecks and forecast growth
- Plan for known upcoming workloads (launches, migrations)

### Quarterly Planning
- Project growth based on business forecasts
- Evaluate reserved capacity / committed use discounts
- Right-size infrastructure (scale up or down)

### Capacity Triggers

| Trigger | Action |
|---|---|
| CPU >70% sustained | Scale compute or optimize queries |
| Storage >80% | Archive cold data or add capacity |
| Memory >85% | Add memory or reduce concurrency |
| Network >75% | Evaluate data locality, compression |
| Cost >110% budget | Review queries, optimize, negotiate |

## Backup & Disaster Recovery

### Backup Strategy

| Data Tier | Method | Frequency | Retention | RTO |
|---|---|---|---|---|
| Tier 1 (Critical) | Snapshots + transaction logs | Continuous | 30 days | 1 hour |
| Tier 2 (Important) | Daily snapshots | Daily | 14 days | 4 hours |
| Tier 3 (Standard) | Weekly full backup | Weekly | 7 days | 24 hours |

### DR Patterns
- **Active-Passive**: Lower cost, hours RTO
- **Active-Active**: Higher cost, minutes RTO
- **Pilot Light**: Core always on, scale up on failover

## Data Quality Monitoring

### Automated Checks
| Check | Threshold | Action |
|---|---|---|
| Row count delta | >20% vs expected | Alert + hold downstream |
| Null rate | >5% for critical columns | Alert + investigate |
| Duplicate keys | >0.1% | Alert + deduplicate |
| Schema drift | New column detected | Alert + catalog update |
| Freshness | >SLA threshold | PagerDuty alert |

### Quality Scorecard
```markdown
| Dataset | Completeness | Uniqueness | Validity | Timeliness | Score |
|---|---|---|---|---|---|
| f_orders | 99% | 100% | 97% | 92% | 97 |
| d_customer | 98% | 99.9% | 96% | 100% | 98 |
```
