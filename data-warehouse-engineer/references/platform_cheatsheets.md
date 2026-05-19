# Platform Cheatsheets

## Data Type Mapping

| Concept | Snowflake | BigQuery | Databricks | Redshift |
|---|---|---|---|---|
| Timestamp | `TIMESTAMP_NTZ` / `TIMESTAMP_LTZ` | `TIMESTAMP` | `TIMESTAMP` / `TIMESTAMP_NTZ` | `TIMESTAMP` |
| Auto-increment | `SEQUENCE` or `IDENTITY` | Not native; use `GENERATE_UUID()` | `GENERATED ALWAYS AS IDENTITY` | `IDENTITY(1,1)` |
| Variant/JSON | `VARIANT` | `JSON` / `STRUCT` / `ARRAY` | `VARIANT` (Spark) | `SUPER` (RA3) |
| Decimal | `NUMBER(38,0)` | `NUMERIC` / `BIGNUMERIC` | `DECIMAL(38,0)` | `DECIMAL(38,0)` |
| Large text | `VARCHAR(16777216)` | `STRING` | `STRING` | `VARCHAR(MAX)` |

## Query Syntax Differences

| Task | Snowflake | BigQuery | Databricks | Redshift |
|---|---|---|---|---|
| Limit rows | `LIMIT n` | `LIMIT n` | `LIMIT n` | `LIMIT n` |
| Sample | `SAMPLE (n)` | `TABLESAMPLE SYSTEM (n PERCENT)` | `TABLESAMPLE (n PERCENT)` | Not native |
| Current timestamp | `CURRENT_TIMESTAMP()` | `CURRENT_TIMESTAMP()` | `current_timestamp()` | `GETDATE()` / `SYSDATE` |
| Date diff | `DATEDIFF(day, start, end)` | `DATE_DIFF(end, start, DAY)` | `datediff(day, start, end)` | `DATEDIFF(day, start, end)` |
| Cast | `::TYPE` or `CAST(x AS TYPE)` | `CAST(x AS TYPE)` | `CAST(x AS TYPE)` | `CAST(x AS TYPE)` |
| String concat | `\|\|` | `\|\|` or `CONCAT` | `\|\|` or `CONCAT` | `\|\|` or `CONCAT` |
| Qualify | `QUALIFY ROW_NUMBER() ...` | `QUALIFY` supported | `QUALIFY` supported | Not native; use CTE + WHERE |
| Time travel | `AT ({ TIMESTAMP => ... })` | `SYSTEM_TIME AS OF` | Not native (use Delta time travel `VERSION AS OF`) | Not native |

## Loading Data

| Platform | Bulk Load Command | File Formats |
|---|---|---|
| Snowflake | `COPY INTO table FROM @stage` | CSV, JSON, Parquet, Avro, ORC |
| BigQuery | `LOAD DATA INTO table FROM FILES` or `bq load` | CSV, JSON, Parquet, Avro |
| Databricks | `COPY INTO` or Auto Loader | CSV, JSON, Parquet, Delta |
| Redshift | `COPY table FROM 's3://bucket/file'` | CSV, JSON, Parquet, Avro, ORC |

## Cost Gotchas

| Platform | Watch Out For |
|---|---|
| Snowflake | Warehouse auto-resume; idle timeouts; compute cost per second |
| BigQuery | On-demand pricing per bytes scanned; use `INFORMATION_SCHEMA.JOBS` to audit |
| Databricks | DBU consumption; auto-scaling clusters can spike; photon vs non-photon |
| Redshift | Concurrency scaling charges; RA3 vs DC2 node types; spectrum external queries |

## Security

| Platform | Role-Based Access | Column-Level | Row-Level |
|---|---|---|---|
| Snowflake | `GRANT` on roles | Dynamic Data Masking | Row Access Policies |
| BigQuery | IAM + Dataset ACL | Policy Tags / Column ACL | Row-level security views |
| Databricks | Unity Catalog | Unity Catalog column masks | Row filters in Unity Catalog |
| Redshift | `GRANT` + role hierarchy | Not native (use views) | `RLS POLICY` (Redshift RLS) |

## Useful System Tables

| Platform | Query History | Table Sizes | Users/Roles |
|---|---|---|---|
| Snowflake | `SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY` | `SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS` | `SNOWFLAKE.ACCOUNT_USAGE.USERS` |
| BigQuery | `INFORMATION_SCHEMA.JOBS` | `__TABLES__` / `INFORMATION_SCHEMA.TABLE_STORAGE` | `INFORMATION_SCHEMA.OBJECT_PRIVILEGES` |
| Databricks | `system.information_schema` + Spark UI | `DESCRIBE HISTORY` / `OPTIMIZE` | Unity Catalog `information_schema` |
| Redshift | `STL_QUERY` / `STV_INFLIGHT` | `SVV_TABLE_INFO` | `PG_USER` / `SVV_ROLE_GRANTS` |
