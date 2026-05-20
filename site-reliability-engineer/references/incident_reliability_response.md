# Incident response (reliability lens)

## Table of contents

1. [During incident](#during-incident)
2. [SLO impact assessment](#slo-impact-assessment)
3. [Production readiness review](#production-readiness-review)
4. [Post-incident reliability actions](#post-incident-reliability-actions)

## During incident

SRE technical lead focus (process roles from `incident-management-engineer`):

1. Confirm **customer-facing SLI** movement (not only infra green)
2. Choose mitigation: rollback, scale, traffic shed, disable feature, failover
3. Estimate **error budget minutes** consumed in real time
4. Avoid destructive experiments unless runbook-approved
5. Capture **timeline** for postmortem (metrics screenshots, deploy IDs)

Escalate to `devops` for pipeline/artifact issues; `cloud-engineer` for net-new infra gaps.

## SLO impact assessment

After mitigation:

- Calculate bad events or downtime minutes in SLO window
- Update **budget remaining** dashboard
- Classify: transient spike vs sustained breach
- Decide if **policy actions** (freeze, review) trigger

## Production readiness review

Run PRR before launch or material architecture change.

| Area | Check |
|---|---|
| SLO | SLI defined, dashboards live, burn alerts configured |
| Capacity | Load test or model shows headroom at launch peak |
| Dependencies | Timeouts, retries, fallbacks documented |
| Deploy | Rollback tested; canary or flag path exists |
| Ops | Runbook, on-call rotation, escalation path |
| Data | Backup/restore tested if stateful |
| Security | Rate limits, authz paths reviewed with security |

Outcome: **Go**, **Go with conditions**, or **No-go** with required fixes.

## Post-incident reliability actions

Separate from IM postmortem process:

- **Reliability action items** — ranked by SLO impact and recurrence risk
- **Detection gaps** — why burn alert late or absent
- **Prevention** — automation, circuit breaker, capacity buffer
- **SLO revision** — only with data and stakeholder sign-off (rare)

Blameless tone; track completion in same system as engineering backlog.
