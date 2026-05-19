# ETL Pipeline Patterns

## Incremental Load Strategies

### 1. Timestamp-Based
```sql
INSERT INTO target
SELECT * FROM source
WHERE updated_at > (SELECT MAX(updated_at) FROM target);
```
- **Pros**: Simple, widely supported
- **Cons**: Misses hard deletes; clock skew risk

### 2. Change Data Capture (CDC)

| Method | Trigger | Best For |
|---|---|---|
| Debezium / Fivetran | Database binlog / WAL | Real-time, low-latency |
| Audit columns (`created_at`, `updated_at`) | Application writes | Simple implementations |
| Hash/compare (`MD5` of row) | Scheduled batch | Detecting any change including deletes |
| DELETE + full INSERT | Scheduled batch | Small tables (<10M rows) |

### CDC with Hash (Delete Detection)
```sql
-- Stage current source hash
CREATE TEMP TABLE staging AS
SELECT pk, MD5(CONCAT(col1, col2, col3)) AS row_hash FROM source;

-- Find deletes
SELECT pk FROM target_hash LEFT JOIN staging USING(pk) WHERE staging.pk IS NULL;

-- Find inserts/updates
SELECT s.pk, s.row_hash FROM staging s
LEFT JOIN target_hash t ON s.pk = t.pk
WHERE t.pk IS NULL OR s.row_hash != t.row_hash;
```

### 3. Streaming Ingestion
- Kafka → Snowpipe / BigQuery Streaming API / Delta Live Tables
- Use for: event data, clickstreams, IoT telemetry

## Idempotency Patterns

| Pattern | SQL Example |
|---|---|
| INSERT OVERWRITE | `INSERT OVERWRITE TABLE target PARTITION (dt) SELECT ...` |
| MERGE / UPSERT | `MERGE INTO target USING source ON target.pk = source.pk WHEN MATCHED UPDATE ... WHEN NOT MATCHED INSERT ...` |
| Delete + Insert (transactional) | `BEGIN; DELETE FROM target WHERE dt = '2024-01-01'; INSERT INTO target ...; COMMIT;` |
| Staging + Swap | Load into `target_staging`, then `ALTER TABLE target SWAP WITH target_staging` (Snowflake) |

## Orchestration & Scheduling

### dbt Patterns
- `{{ config(materialized='incremental', unique_key='order_id') }}`
- Use `is_incremental()` macro to branch logic
- Tests: `not_null`, `unique`, `accepted_values`, `relationships`

### Airflow Patterns
- One DAG per source system or business domain
- Use `TaskFlow` API for simple pipelines
- Sensor tasks to wait for upstream data readiness
- `on_failure_callback` to alert Slack/PagerDuty

## Data Quality Checks

| Check | Implementation |
|---|---|
| Row count sanity | `ABS(source_count - target_count) / source_count < 0.01` |
| Null rate | `COUNT(*) FILTER (WHERE col IS NULL) / COUNT(*) < threshold` |
| Freshness | `MAX(event_time) > NOW() - INTERVAL '1 hour'` |
| Referential integrity | Left join fact to dim; flag orphans |
| Distribution skew | `MAX(bucket_count) / AVG(bucket_count) < 10` |
| Duplicate keys | `SELECT key, COUNT(*) FROM table GROUP BY key HAVING COUNT(*) > 1` |

## Error Handling

- **Schema drift**: Versioned schemas; fail pipeline on unexpected column additions
- **Bad records**: Dead-letter queue table with `reject_reason`, `raw_payload`, `loaded_at`
- **Partial failures**: Transaction wrap or staging table with rollback capability
- **Retries**: Exponential backoff for transient API/database errors

## Backfilling

- Always backfill with the same idempotent logic as incremental loads
- Use `BETWEEN` date ranges in small chunks to avoid resource exhaustion
- For large backfills: disable indexes/constraints, load, rebuild
