# SQL Optimization & Query Tuning

## Execution Plans

Capture and read execution plans per platform:

| Platform | Command | Key fields to inspect |
|---|---|---|
| Snowflake | `EXPLAIN USING JSON` | `partitions_scanned`, `bytes_scanned`, `operator_statistics` |
| BigQuery | `EXPLAIN` or Query Plan in UI | `rows read`, `slot time`, `stages`, `shuffle` |
| Databricks | `EXPLAIN EXTENDED` or Spark UI | `Scan parquet`, `Exchange`, `SortMergeJoin` vs `BroadcastHashJoin` |
| Redshift | `EXPLAIN` or SVL_QUERY_REPORT | `XN Seq Scan` vs `XN Bitmap Scan`, `DS_DIST_NONE` vs `DS_DIST_ALL_NONE` |

## Common Anti-Patterns & Fixes

| Anti-Pattern | Fix | Platform Notes |
|---|---|---|
| `SELECT *` in production | Project only needed columns | All — reduces IO significantly |
| Functions on indexed columns (`WHERE UPPER(email) = ...`) | Use case-insensitive collation or computed column | BigQuery: `COLLATE`; Snowflake: `COLLATE` |
| Filtering on a non-partitioned date column | Partition by date; use `WHERE event_date >= '2024-01-01'` | Redshift: `SORTKEY`; BigQuery: partition by `DATE` |
| Many-to-many join without aggregation | Add bridge table or pre-aggregate | All |
| Correlated subquery in SELECT | Rewrite as JOIN or use `LATERAL` / `CROSS APPLY` | Databricks/Redshift prefer JOIN |
| Casting inside a JOIN predicate | Cast once in a CTE or materialized stage | All — prevents index usage |

## Partitioning & Clustering

| Platform | Partitioning | Clustering / Sorting |
|---|---|---|
| Snowflake | Micro-partitions (automatic) | `CLUSTER BY (col1, col2)` |
| BigQuery | `PARTITION BY DATE(timestamp)` | `CLUSTER BY customer_id` |
| Databricks | `PARTITIONED BY (date_col)` | `ZORDER BY (col)` via OPTIMIZE |
| Redshift | `DISTSTYLE KEY DISTKEY(col)` + `SORTKEY(col)` | Compound or interleaved SORTKEY |

## Materialization Patterns

- **Materialized View**: Platform-native auto-refresh (limited flexibility)
- **Manual Summary Table**: Full control; refresh via MERGE or INSERT OVERWRITE
- **Pre-join**: Flatten star schema into wide table for specific dashboards

Use manual summary tables when:
- Refresh logic is complex (e.g., SCD type 2 dimensions)
- You need incremental refreshes with custom business rules
- Platform MV limitations prevent required joins

## Cost Optimization

| Technique | When |
|---|---|
| Short-circuit with partitions | Always filter on partition key first |
| Avoid cross-joins | Cartesian products explode cost; verify with row counts |
| Cache repeated CTEs | Materialize intermediate results in temp tables |
| Limit large sorts | Use approximate algorithms (`APPROX_COUNT_DISTINCT`, HyperLogLog) |
