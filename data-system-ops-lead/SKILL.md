---
name: data-system-ops-lead
description: |
  Guides data system operation leads in managing data platform operations and leading ops teams.
  Covers pipeline monitoring, SLA enforcement, incident response, capacity management, team scheduling,
  on-call management, runbook development, vendor management, and operational process design.
  Use when operating data platforms, managing data ops teams, responding to incidents, optimizing costs,
  designing operational processes, or leading shift-based data infrastructure teams.
---

# Data System Operation Lead

## Core Workflows

### 1. Platform Operations Oversight

**Daily operational cadence:**

| Activity | Time | Owner | Output |
|---|---|---|---|
| Morning health check | 08:00 | On-call lead | Status dashboard review |
| Pipeline run review | 09:00 | Operations engineer | Failed job triage |
| Capacity check | 10:00 | Platform engineer | Resource utilization report |
| SLA review | 14:00 | Operations lead | Breach investigation |
| End-of-day handoff | 17:00 | Outgoing on-call | Shift notes, open issues |

**Health check checklist:**
- [ ] All critical pipelines completed successfully
- [ ] Data freshness within SLA thresholds
- [ ] No critical or high alerts active >30 min
- [ ] Storage utilization <85%
- [ ] Query performance within baseline
- [ ] Backup jobs completed

**See `references/platform_operations.md` for monitoring setup, SLA frameworks, and capacity planning.**

### 2. Incident & Problem Management

**Incident severity matrix:**

| Severity | Impact | Response Time | Escalation |
|---|---|---|---|
| P1 (Critical) | Business halt, data loss | 15 min | Director immediately |
| P2 (High) | Significant degradation | 1 hour | Manager within 30 min |
| P3 (Medium) | Minor impact | 4 hours | Team lead by end of shift |
| P4 (Low) | Cosmetic/noise | 24 hours | Next business day |

**Incident lifecycle:**
1. Detect → 2. Triage → 3. Mitigate → 4. Resolve → 5. Review

**Post-incident review (within 48 hours for P1-P2):**
- Timeline of events
- Root cause (5 Whys)
- Impact assessment
- Action items with owners and dates
- Process improvements

**See `references/platform_operations.md` for runbook templates and escalation procedures.**

### 3. Team & Shift Leadership

**On-call rotation design:**
- Primary + secondary (overlapping coverage)
- Weekly rotations (not daily — too disruptive)
- Include weekend coverage in planning
- Escalation path: Engineer → Lead → Manager → Director

**Shift handoff template:**
```markdown
## Shift Handoff — [Date] [Shift]

### Active Incidents
| ID | Severity | Status | Owner | Notes |
|---|---|---|---|---|
| INC-001 | P2 | Mitigated | @alice | Awaiting permanent fix |

### Alerts Requiring Attention
- [ ] Storage forecast will hit 90% in 3 days

### Changes Deployed
- [ ] Pipeline X updated to v2.1 (stable)

### Planned Work Next Shift
- [ ] Apply security patches to warehouse

### Issues for Lead Attention
- Recurring alert on pipeline Y — may need threshold tuning
```

**See `references/team_leadership.md` for scheduling, burnout prevention, and team development.**

### 4. Vendor & Cost Management

**Monthly cost review:**
- Actual vs budgeted spend
- Cost per TB processed, per pipeline run
- Identify optimization opportunities
- Vendor contract renewal timeline

**Vendor escalation path:**
1. Technical support (standard ticket)
2. Account manager (business impact)
3. Executive escalation (contract-level)

**See `references/vendor_tools.md` for vendor evaluation, cost optimization, and tool selection.**

## When to Load References

- **Platform operations** → `references/platform_operations.md`
- **Team leadership** → `references/team_leadership.md`
- **Operational processes** → `references/operational_processes.md`
- **Vendor & tools** → `references/vendor_tools.md`
