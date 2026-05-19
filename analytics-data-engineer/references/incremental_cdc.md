# Incremental and CDC

## When to incremental

| Signal | Approach |
|---|---|
| Large fact table | `incremental` materialization |
| Append-only events | Timestamp watermark |
| CDC from OLTP | Merge on primary key |
| Small dimension | Full refresh acceptable |

## Strategies

| Strategy | dbt pattern | Risk |
|---|---|---|
| **Append** | `insert_overwrite` / append new partitions | Duplicates if rerun wrong |
| **Merge** | `unique_key` + merge | Requires reliable key |
| **Delete+insert** | Partition replace | Window must be correct |
| **Snapshot** | `dbt snapshot` | Storage growth |

## Watermarks

- Use `updated_at` with lookback buffer (e.g. 3 days) for late updates
- Document lookback in model description
- Full-refresh job on schedule for small tables only

## CDC sources

- Fivetran/Airbyte/DMS — trust ` _fivetran_synced` or equivalent
- Deletions: soft-delete flag in staging; filter in mart

## Backfill playbook

1. Pause downstream dashboards or warn BI
2. Run full-refresh in maintenance window
3. Validate row counts and key uniqueness tests
4. Reconcile sample metrics with `bi-analyst`

## Full refresh guardrails

- Require PR label and approver for prod full-refresh on large models
- Use `--select model+` carefully in CI
