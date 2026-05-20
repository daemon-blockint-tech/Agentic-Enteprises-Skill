# Cost and operations

## Table of contents

1. [Tagging and chargeback](#tagging-and-chargeback)
2. [Rightsizing and commitments](#rightsizing-and-commitments)
3. [Quotas and limits](#quotas-and-limits)
4. [Troubleshooting](#troubleshooting)

## Tagging and chargeback

Required tags (enforce via policy):

- `environment`, `owner`, `cost-center`, `service`, `data-classification`

Use **Cost Explorer**, **Billing budgets**, **alerts** at 80/100% threshold.

Finance close and capex accounting → `compute-accounting-manager`.

## Rightsizing and commitments

- Review **idle** resources monthly: unattached volumes, old snapshots, oversized instances
- **Reserved instances / CUD / savings plans** after 30-day stable baseline
- **Spot/preemptible** for fault-tolerant batch only
- Serverless: tune memory and timeout to actual use

## Quotas and limits

- Request **quota increases** before launch spikes
- Watch API **rate limits** — exponential backoff in apps
- Service-specific limits (Lambda concurrency, EIP count) in design checklist

## Troubleshooting

| Symptom | Checks |
|---|---|
| Access denied | IAM policy, SCP, resource policy, session context |
| Timeout to service | SG/firewall, NACL, route table, PrivateLink DNS |
| Throttling | Quota, TPS, burst limits |
| Unexpected bill | New region, NAT GW hours, cross-AZ traffic, public egress |
| DB connection fail | SG, subnet group, credential rotation, max connections |

Capture **CloudTrail / Audit Logs / Activity Log** correlation ID for incidents.

Hand off application bugs to `senior-software-engineer`; cluster issues to `cluster-deployment-engineer`.
