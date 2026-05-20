# Cost visibility and allocation

## Table of contents

1. [Data sources](#data-sources)
2. [Tagging standard](#tagging-standard)
3. [Allocation methods](#allocation-methods)
4. [Untagged spend](#untagged-spend)

## Data sources

| Provider | Primary exports |
|---|---|
| AWS | Cost Explorer, CUR (Athena/QuickSight), Budgets |
| GCP | Billing export to BigQuery, budgets |
| Azure | Cost Management + exports, budgets |

Use **daily granularity** for ops; **monthly** for leadership. Include credits, refunds, and tax lines explicitly.

## Tagging standard

Minimum tags (enforce via policy — `cloud-security-engineer` / `cloud-engineer`):

| Tag | Purpose |
|---|---|
| `environment` | prod / staging / dev / sandbox |
| `owner` | team or email alias |
| `cost-center` | finance code |
| `service` | product or microservice |
| `application` | optional grouping |

**Activate** cost allocation tags in billing console. Report **untagged %** weekly.

## Allocation methods

| Method | When |
|---|---|
| Direct | Resource has tags → 100% to tag value |
| Proportional | Shared cluster — split by CPU/memory, requests, or revenue |
| Fixed split | Known static % across BUs (document annually) |
| Showback | Inform only; no internal invoice |
| Chargeback | Internal billing with agreed rates |

Document **method per shared platform** (EKS, data lake, NAT gateway).

## Untagged spend

1. Rank by **$ untagged** descending
2. Identify resource type (often EC2, RDS, S3 without owner)
3. Open ticket to owner with **deadline** to tag or decommission
4. Escalate repeat offenders to engineering management
5. Apply **default allocation** only as temporary with expiry

Target: <5% untagged spend at steady state (org-specific goal).
