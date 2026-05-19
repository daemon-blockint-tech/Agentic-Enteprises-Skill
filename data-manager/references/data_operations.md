# Data Operations & Reliability

## Monitoring & Alerting

### Key Metrics by System

**Data warehouse:**
| Metric | Alert When | Severity |
|---|---|---|
| Query queue depth | >20 queued for >10 min | P2 |
| Storage utilization | >85% | P2 |
| Failed login attempts | >10 in 5 min | P1 |
| Replication lag | >30 seconds | P1 |

**Data pipelines:**
| Metric | Alert When | Severity |
|---|---|---|
| Job failure | Any failure | P1-P3 (by tier) |
| Duration > expected | >150% of baseline | P2 |
| Row count anomaly | >20% delta vs expected | P2 |
| Late start | >30 min after scheduled | P3 |

**Data quality:**
| Metric | Alert When | Severity |
|---|---|---|
| Freshness SLA breach | Data older than threshold | P1-P3 |
| Null rate spike | >2x baseline | P2 |
| Duplicate key rate | >0.1% | P2 |
| Schema drift | New column detected | P3 |

## Incident Response

### Severity Definitions

| Severity | Impact | Response Time | Example |
|---|---|---|---|
| P1 (Critical) | Business halt, data loss | 15 min | Pipeline down, revenue data missing |
| P2 (High) | Significant degradation | 1 hour | Quality SLA breach, slow queries |
| P3 (Medium) | Minor impact | 4 hours | Delayed refresh, non-critical schema drift |
| P4 (Low) | Cosmetic/noise | 24 hours | Documentation error, test flake |

### Incident Response Runbook

**Step 1: Detect & Triage (0-15 min)**
- Acknowledge alert in PagerDuty/Opsgenie
- Assess severity using definitions above
- Create incident channel (Slack) or bridge
- Notify stakeholders if P1-P2

**Step 2: Mitigate (15 min - 2 hours)**
- Identify scope: which pipelines, tables, consumers affected
- Apply temporary fix: rollback, restart, manual backfill
- Do NOT root cause during mitigation
- Update status page if customer-facing

**Step 3: Resolve (2-24 hours)**
- Deploy permanent fix
- Verify fix with tests and monitoring
- Confirm data quality post-fix
- Close incident when stable for >1 hour

**Step 4: Review (24-48 hours)**
- Schedule post-mortem for P1-P2
- Document timeline, root cause, remediation
- Identify action items with owners and dates
- Share broadly; blameless culture

## Backup & Recovery

### Backup Strategy

| Data Tier | Backup Method | Frequency | Retention | RTO |
|---|---|---|---|---|
| Tier 1 (Critical) | Snapshots + transaction logs | Continuous | 30 days | 1 hour |
| Tier 2 (Important) | Daily snapshots | Daily | 14 days | 4 hours |
| Tier 3 (Standard) | Weekly full backup | Weekly | 7 days | 24 hours |
| Tier 4 (Archive) | Object storage replication | Monthly | Per policy | 72 hours |

**Backup verification:**
- Monthly restore test on non-production
- Validate data integrity post-restore
- Document restore procedures
- Test cross-region recovery annually

### Disaster Recovery Patterns

**Active-Passive:**
- Primary region active, secondary on standby
- Failover: Manual or automated
- Cost: Lower (secondary scaled down)
- RTO: Hours

**Active-Active:**
- Both regions serving traffic
- Automatic failover
- Cost: Higher (2x compute)
- RTO: Minutes

## Capacity Planning

### Planning Cycle

**Monthly:**
- Review utilization trends (CPU, storage, memory)
- Identify bottlenecks
- Plan for known upcoming workloads

**Quarterly:**
- Project growth based on business forecasts
- Evaluate reserved capacity / committed use discounts
- Right-size infrastructure (scale up or down)

**Annually:**
- Major architecture review
- Evaluate new technologies
- Budget planning for next fiscal year

### Capacity Triggers

| Trigger | Action |
|---|---|
| CPU >70% sustained | Scale compute or optimize queries |
| Storage >80% | Archive cold data or add capacity |
| Memory >85% | Add memory or reduce concurrency |
| Network >75% | Evaluate data locality, compression |
| Cost >110% budget | Review queries, optimize, negotiate |

## Change Management

### Change Types

| Type | Examples | Approval | Testing |
|---|---|---|---|
| Standard | New pipeline, schema addition | Team lead | Staging |
| Normal | Schema change, partition update | Manager | Staging + peer review |
| Emergency | Hotfix, security patch | Post-hoc | Minimal (risk accepted) |

### Change Request Template

```markdown
## Change Request

**Title:** __________
**Type:** Standard / Normal / Emergency
**Risk:** Low / Medium / High
**Rollback plan:** __________

**Description:**
What is changing and why?

**Impact:**
- Systems affected: __________
- Downtime expected: __________
- Consumers notified: __________

**Testing:**
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Staging validation complete
- [ ] Rollback tested

**Approvals:**
- [ ] Technical review
- [ ] Stakeholder sign-off
- [ ] Scheduled for: __________
```

## On-Call Operations

### On-Call Rotation
- Primary + secondary (overlapping)
- Weekly rotations preferred over daily
- Handoff: Document open issues, known risks
- Escalation: After 15 min unresolved → secondary → manager

### On-Call Checklist (Shift Start)
- [ ] Review open incidents from previous shift
- [ ] Check alert backlog (clear false positives)
- [ ] Review scheduled changes for shift
- [ ] Confirm runbook access and tooling
- [ ] Check capacity dashboard for anomalies
