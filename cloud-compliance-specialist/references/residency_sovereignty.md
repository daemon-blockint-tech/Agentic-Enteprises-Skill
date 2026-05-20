# Residency and sovereignty

## Table of contents

1. [Technical documentation](#technical-documentation)
2. [Region and replication](#region-and-replication)
3. [Cross-border transfers](#cross-border-transfers)
4. [Subprocessors in cloud](#subprocessors-in-cloud)

## Technical documentation

Provide engineers and assessors **factual** diagrams (not legal opinions):

- Primary **region** per workload and data store
- **DR/backup** regions and replication direction
- **CDN/edge** locations if customer data cached
- **Logging** and support personnel access regions (provider docs)

Update when architecture changes (`cloud-architect` sign-off).

## Region and replication

Controls to verify:

- **Resource policies** restricting regions (SCPs, org policies, policy assignments)
- **Default region** in IaC and CI
- **RDS/GCS/SQL** cross-region replica documented
- **S3/GCS/Blob** replication rules and destination buckets
- **KMS keys** regional and not unintentionally multi-region where prohibited

Evidence: Config rules “approved regions only”; export of resource inventory by region.

## Cross-border transfers

Document **technical paths** when data may leave jurisdiction:

- Replication to DR region in another country
- Global services (support, logging aggregation) per provider data processing terms
- Third-party SaaS integrated with cloud data

Legal mechanism (SCCs, adequacy) → legal/commercial; engineering documents **what flows where**.

## Subprocessors in cloud

Maintain table:

| Subprocessor | Service used | Data processed | Region | Contract ref |
|---|---|---|---|---|
| Hyperscaler | IaaS/PaaS | Per scope | Listed regions | BAA/DPA |
| Observability SaaS | APM | Logs may contain PII | US/EU | DPA |

Refresh when enabling new cloud marketplace integrations or regions.
