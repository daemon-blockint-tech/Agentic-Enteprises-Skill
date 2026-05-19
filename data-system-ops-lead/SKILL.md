---
name: data-system-ops-lead
description: |
  Run data system operations and reliability engineering.
  Cover pipeline monitoring, incident response, SLA management, capacity planning,
  on-call runbooks, data quality alerting, and operational excellence.
  Triggers on "data pipeline monitoring", "incident response", "SLA management",
  "capacity planning", "on-call runbook", "data quality alerting", "operational excellence",
  "system reliability", "pipeline health check", or "data ops".
---

# Data System Operations Lead

## Overview

Run data system operations and reliability engineering. This skill covers pipeline monitoring,
incident response, SLA management, capacity planning, on-call runbooks, data quality alerting,
and operational excellence.

## Features

- Pipeline monitoring with alerting thresholds and dashboard design
- Incident response: severity classification, escalation paths, post-incident reviews
- SLA management with performance tracking and breach prevention
- Capacity planning: resource forecasting, scaling triggers, cost optimization
- On-call runbooks with step-by-step troubleshooting procedures
- Data quality alerting with anomaly detection and validation rules

## Usage

1. Identify the user's data ops need (monitoring, incident response, SLA, capacity, or runbooks)
2. Follow the corresponding workflow below
3. Produce structured outputs: monitoring dashboards, incident reports, SLA scorecards, or runbooks

## Examples

- **User**: "Set up pipeline monitoring"
  **Agent**: Runs Monitoring workflow, defines alert thresholds, creates dashboard with latency/throughput/error rate metrics

- **User**: "Handle a pipeline failure"
  **Agent**: Runs Incident Response workflow, classifies severity, executes runbook, produces post-incident report with root cause

- **User**: "Create an on-call runbook"
  **Agent**: Runs Runbook Creation workflow, documents troubleshooting steps, escalation paths, and verification checks

## When to Use

- Running daily data platform health checks, pipeline triage, and SLA enforcement
- Leading incident response, post-incident reviews, and on-call/shift handoffs
- Managing vendor escalations, cost reviews, and operational process design
- Coaching ops engineers on runbooks, capacity, and alert hygiene

## When NOT to Use

- Strategic data mesh/lakehouse architecture or governance policy → use `data-architect`
- Program roadmaps, quarterly planning, or governance committee operations → use `data-manager`
- Writing dimensional models or MERGE-based incremental ETL → use `data-warehouse-engineer`
- General cloud/Kubernetes infrastructure outside the data platform → use `infrastructure-engineer`
- Org-wide on-call program, SEV definitions, postmortem tooling → use `incident-management-engineer`

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
