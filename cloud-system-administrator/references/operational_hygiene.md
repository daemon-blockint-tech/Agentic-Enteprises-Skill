# Operational hygiene

## Table of contents

1. [Cost cleanup](#cost-cleanup)
2. [Quotas and limits](#quotas-and-limits)
3. [DNS and certificates](#dns-and-certificates)
4. [Tagging compliance](#tagging-compliance)

## Cost cleanup

Monthly hygiene (non-prod aggressive, prod cautious):

| Resource | Action |
|---|---|
| Stopped instances >30d | Terminate after owner notice |
| Unattached EBS/disks | Snapshot then delete |
| Old snapshots | Lifecycle or manual per policy |
| Unused elastic IPs | Release |
| Orphaned load balancers | Verify targets empty |

Report **estimated savings**; finance visibility via tags — `compute-accounting-manager` for GL not cleanup execution.

## Quotas and limits

- Monitor **quota utilization** dashboards
- Open provider case **before** hard block at 80% on critical quotas
- Document approved increase and valid until date
- After increase, verify workload success

## DNS and certificates

- Track **cert expiry** 30/14/7 days alerts
- Renew via automation first; manual DNS validation runbook as backup
- **Route53/Cloud DNS** record changes via change ticket
- Validate **propagation** after TTL

## Tagging compliance

- Report untagged resources to owners
- Enforce via policy where org mandates — remediation SLA
- Required tags: owner, environment, cost center (per `enterprise-cloud-architect` or local standard)

Do not delete untagged prod resources without owner escalation path.
