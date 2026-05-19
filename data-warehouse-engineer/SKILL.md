---
name: data-warehouse-engineer
description: |
  Guides data warehouse engineering across Snowflake, BigQuery, Databricks, and Redshift.
  Covers SQL query optimization, dimensional data modeling (star/snowflake schemas, SCDs),
  and ETL pipeline design (incremental loads, CDC, idempotency, orchestration).
  Use when tuning slow queries, designing fact/dimension tables, building ETL pipelines,
  choosing a warehouse platform, or debugging data quality issues in warehouse workloads.
---

# Data Warehouse Engineer

## Core Workflows

### 1. Query Performance Diagnostics

**Step-by-step checklist (follow exactly):**

1. Identify the slow query and capture its execution plan
2. Check for full table scans; add partitioning or clustering if present
3. Verify join order: smallest/ most selective table first when possible
4. Look for selective predicates pushed to the partition/clustering key
5. Check for redundant aggregations or exploding joins (many-to-many without bridge)
6. Compare estimated vs actual rows; cardinality misestimates indicate stale stats
7. Consider materialized views or pre-aggregated summary tables for repeated patterns
8. Document the before/after execution time and cost

**See `references/sql_optimization.md` for platform-specific EXPLAIN syntax, partition strategies, and tuning patterns.**

### 2. Data Model Design

**Decision tree:**

- Need fast aggregations and simple joins? → **Star schema**
- Need normalized dimensions to reduce redundancy? → **Snowflake schema**
- Tracking historical changes in dimensions? → **Slowly Changing Dimension (SCD) type 2**
- Event-based data with high volume? → **Fact table with partitioning on event date**
- Need real-time-ish analytics? → **Streaming ingestion + micro-batch fact tables**

**See `references/data_modeling.md` for full SCD patterns, bridge tables, and degenerate dimensions.**

### 3. ETL Pipeline Design

**Essential properties every pipeline must satisfy:**

| Property | Pattern |
|---|---|
| Idempotency | MERGE / INSERT OVERWRITE with deterministic keys |
| Incrementality | `WHERE updated_at > (SELECT MAX(updated_at) FROM target)` |
| Atomicity | Wrap multi-step loads in a transaction or use staging → swap pattern |
| Observability | Row counts, null rates, freshness checks logged per run |
| Error handling | Dead-letter queue for bad records; fail loudly on schema drift |

**See `references/etl_patterns.md` for CDC patterns, orchestration templates (Airflow/dbt), and data quality checks.**

### 4. Platform Selection Quick Reference

| Need | Best Fit |
|---|---|
| Semi-structured JSON, auto-scaling | Snowflake |
| Tight GCP integration, nested/repeated fields | BigQuery |
| ML + Spark + SQL in one lakehouse | Databricks |
| AWS-native, predictable cost at scale | Redshift |

**See `references/platform_cheatsheets.md` for syntax differences, data types, and gotchas per platform.**

## When to Load References

- **SQL tuning details** → `references/sql_optimization.md`
- **Schema design details** → `references/data_modeling.md`
- **Pipeline patterns** → `references/etl_patterns.md`
- **Platform-specific syntax** → `references/platform_cheatsheets.md`
