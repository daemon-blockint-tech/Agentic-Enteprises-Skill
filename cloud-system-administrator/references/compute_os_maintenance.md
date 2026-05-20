# Compute and OS maintenance

## Table of contents

1. [Patching](#patching)
2. [Instance operations](#instance-operations)
3. [Storage operations](#storage-operations)
4. [Managed services ops](#managed-services-ops)

## Patching

VM and instance group patching:

1. **Scan** — missing critical patches report
2. **Schedule** — maintenance window; notify app owners
3. **Snapshot** — before major patch waves on prod
4. **Apply** — rolling update for ASG/MIG/VMSS; drain where required
5. **Verify** — health checks green; rollback AMI if failed

Document **reboot required** kernel patches separately.

## Instance operations

Common tasks:

- Resize instance type (stop/start or live resize if supported)
- Replace failed instance from launch template
- Attach/detach **EBS/disk** — verify AZ match
- User-data debug — only in non-prod; no secret exposure in console

## Storage operations

- Expand volumes — grow partition/OS after cloud resize
- Delete **unattached volumes** per hygiene policy (snapshot first if uncertain)
- S3 lifecycle — verify transitions; no accidental prod bucket delete

## Managed services ops

| Service | Ops tasks |
|---|---|
| RDS/Cloud SQL | Reboot, parameter apply pending reboot, storage autoscale check |
| ElastiCache | Failover test, maintenance window apply |
| Lambda | Not OS patch — config/version updates via change ticket |

Deep RDS performance tuning → DBA/app team; connectivity → network runbook.
