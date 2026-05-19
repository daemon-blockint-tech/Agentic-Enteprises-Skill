# Operational Processes

## Change Management

### Change Types

| Type | Examples | Approval | Testing | Risk |
|---|---|---|---|---|
| Standard | New pipeline, schema addition | Team lead | Staging | Low |
| Normal | Schema change, partition update | Manager | Staging + peer review | Medium |
| Emergency | Hotfix, security patch | Post-hoc | Minimal (risk accepted) | High |
| Maintenance | OS patch, version upgrade | Team lead | Smoke test | Low |

### Change Request Template
```markdown
## Change Request

**Title:** [Brief description]
**Type:** Standard / Normal / Emergency / Maintenance
**Risk:** Low / Medium / High
**Rollback plan:** [Steps to undo]

**Description:**
What is changing and why?

**Impact:**
- Systems: [affected systems]
- Downtime: [expected duration or none]
- Users: [who is affected]

**Testing:**
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Staging validation complete
- [ ] Rollback tested

**Schedule:**
- Proposed window: [date/time]
- Duration: [expected]

**Approvals:**
- [ ] Technical review: [name]
- [ ] Stakeholder sign-off: [name]
```

### Maintenance Windows
- Schedule regularly (e.g., monthly Tuesday 02:00 UTC)
- Announce 1 week ahead
- Have rollback plan ready
- Post-results summary within 4 hours

## Deployment Procedures

### Deployment Checklist
- [ ] Change request approved
- [ ] Staging tests passed
- [ ] Runbook updated for new behavior
- [ ] Monitoring dashboards verified
- [ ] On-call team notified
- [ ] Rollback artifact ready
- [ ] Communication sent to stakeholders
- [ ] Post-deployment validation completed

### Blue-Green Deployment (Data Systems)
1. Deploy new version to green environment
2. Run parallel validation on green
3. Switch traffic/router to green
4. Monitor for 1 hour
5. Decommission blue (or keep for quick rollback)

### Canary Deployment
1. Deploy to 5% of pipelines/workload
2. Monitor metrics vs baseline
3. Gradually increase to 25%, 50%, 100%
4. Roll back immediately on anomaly detection

## Problem Management

### Problem vs Incident
- **Incident**: Single occurrence of service disruption
- **Problem**: Underlying cause that may cause multiple incidents

### Problem Lifecycle
1. **Identification**: Trend analysis, incident correlation
2. **Recording**: Document in problem ticket
3. **Investigation**: Root cause analysis
4. **Workaround**: Temporary fix to reduce impact
5. **Resolution**: Permanent fix
6. **Closure**: Verify fix, update documentation

### Trend Analysis
Review weekly:
- Recurring alerts (same alert >3 times in 7 days)
- Recurring incidents (same component, same symptoms)
- MTTR trends (increasing = skills or process gap)
- False positive rate (high = threshold tuning needed)

## Operational Reviews

### Weekly Operational Review

```markdown
## Ops Review — Week of [Date]

### Incidents
| ID | Severity | MTTR | Root Cause | Recurring? |
|---|---|---|---|---|
| INC-001 | P2 | 45 min | Disk full | Yes (3rd time) |

### Alerts
| Alert | Count | False Positive? | Action |
|---|---|---|---|
| Pipeline lag | 12 | 8 | Tune threshold |

### Changes
| Change | Status | Issues |
|---|---|---|
| DW upgrade | Successful | None |

### Capacity
| Resource | Utilization | Forecast |
|---|---|---|
| Storage | 82% | 90% in 14 days |

### Action Items
| Item | Owner | Due |
|---|---|---|
| Fix recurring disk issue | @alice | Friday |
```

### Monthly Business Review
- SLA performance vs target (6-month trend)
- Cost analysis (actual vs budget, per-unit trends)
- Incident trends (severity distribution, MTTR)
- Team health (on-call burden, burnout indicators)
- Roadmap review (upcoming projects, capacity impact)

## Process Improvement

### Kaizen for Operations
- Weekly: One small improvement per engineer
- Monthly: Team retrospective with action items
- Quarterly: Major process review (SLA definitions, escalation paths)

### Metrics for Improvement
- **MTTR** (Mean Time To Recovery): Target reduction 10% per quarter
- **MTBF** (Mean Time Between Failures): Target increase
- **Change success rate**: % of changes without rollback
- **Automation coverage**: % of manual tasks automated
- **Runbook completeness**: % of alerts with runbooks

## Documentation Standards

### Runbook Requirements
Every alert or recurring incident must have:
1. What triggers it
2. Immediate checks (commands, links)
3. Resolution steps (ordered, copy-paste where possible)
4. Escalation criteria and path
5. Post-resolution actions

### Change Log
Document all changes in central log:
```markdown
| Date | System | Change | Owner | Result |
|---|---|---|---|---|
| 2024-01-15 | Pipeline X | Added retry logic | @bob | Success |
```

### Knowledge Base
- Searchable (not buried in chat)
- Updated within 24 hours of new incident resolution
- Peer-reviewed quarterly for accuracy
