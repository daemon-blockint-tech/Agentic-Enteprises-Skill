# Storage and data services

## Table of contents

1. [Object storage](#object-storage)
2. [Block and file](#block-and-file)
3. [Managed databases](#managed-databases)
4. [Caches and messaging](#caches-and-messaging)

## Object storage

S3 / GCS / Blob:

- **Block public access** by default; bucket policies deny `Principal: *`
- **Versioning** for prod buckets with lifecycle to IA/Glacier
- **Encryption** SSE-KMS or CMEK; document key rotation
- **Lifecycle rules** — expire incomplete multipart uploads
- **Cross-region replication** only when RPO requires; cost impact

## Block and file

EBS / Persistent Disk / Managed Disks:

- Match **IOPS/throughput** to workload; monitor burst credits
- **Snapshots** automated; test restore quarterly
- Shared file: EFS, Filestore, Azure Files — security group / firewall scope

## Managed databases

RDS / Cloud SQL / Azure Database:

- **Multi-AZ** for prod; read replicas for read scale
- **Parameter groups** reviewed; no open `0.0.0.0/0` security groups
- **Private subnet** + security group source = app tier only
- **Backups** retention meets RPO; PITR enabled where supported
- Major version upgrades — maintenance window + rollback plan

Data modeling and warehouse design → `data-warehouse-engineer`.

## Caches and messaging

ElastiCache / Memorystore / Azure Cache; SQS/SNS/Pub/Sub/Event Hub:

- **Auth** via IAM or SAS; TLS in transit
- Queue **visibility timeout** and DLQ configured
- Topic **fan-out** subscriptions documented
