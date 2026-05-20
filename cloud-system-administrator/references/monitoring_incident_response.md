# Monitoring and incident response

## Table of contents

1. [Alert triage](#alert-triage)
2. [Runbook execution](#runbook-execution)
3. [Incident timeline](#incident-timeline)
4. [Vendor outages](#vendor-outages)

## Alert triage

First 15 minutes:

1. **Acknowledge** page; open incident channel/ticket
2. **Scope** — one resource, one region, one account, or provider-wide?
3. **Impact** — prod vs non-prod; customer-facing?
4. **Recent changes** — deploy, IAM, network, maintenance?
5. **Dashboards** — CPU, errors, saturation, quota metrics

Severity mapping follows org **SEV definitions** — `incident-management-engineer`.

## Runbook execution

Runbook sections:

- **Symptoms** — alert names, typical causes
- **Diagnosis** — commands/console paths (read-only first)
- **Mitigation** — rollback, failover, scale up, disable feature flag (app team)
- **Escalation** — when to page cloud-engineer or vendor support
- **Verification** — all-clear checks

Update runbook after every significant incident.

## Incident timeline

Log entries:

- Detection time (alert)
- Actions with timestamps
- Hypothesis changes
- Resolution and customer impact end
- Follow-up tickets (root cause fix)

Blameless postmortem if SEV threshold met — process from incident program.

## Vendor outages

Cloud status page check:

- Confirm **regional** issue vs local misconfig
- Enable **communication** template if customer impact
- Avoid destructive changes during provider incident unless runbook says failover
- Open **support case** if single-tenant anomaly
