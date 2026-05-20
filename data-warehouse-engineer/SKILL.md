---
name: data-warehouse-engineer
description: |
  Design and implement data warehouses.
  Cover star/snowflake schemas, dimensional modeling, SQL optimization, ETL/ELT patterns,
  partitioning strategies, and warehouse-specific features (Snowflake, BigQuery, Redshift).
  Triggers on "design star schema", "optimize SQL query", "build ETL pipeline",
  "warehouse partitioning", "dimensional modeling", "data warehouse design",
  "query performance tuning", or "warehouse migration".
  For dbt project structure, staging/mart layers, incremental models, and analytics CI, use
  analytics-data-engineer—not data-warehouse-engineer alone. OLTP app latency and load testing:
  performance-engineer.
---

# Data Warehouse Engineer

## Overview

Design and implement data warehouses. This skill covers star/snowflake schemas, dimensional modeling,
SQL optimization, ETL/ELT patterns, partitioning strategies, and warehouse-specific features
(Snowflake, BigQuery, Redshift).

## Features

- Dimensional modeling: star schema, snowflake schema, fact/dimension table design
- SQL optimization: query tuning, indexing, materialized views, partition pruning
- ETL/ELT patterns: incremental loads, CDC, data quality checks, error handling
- Partitioning strategies: range, list, hash, and composite partitioning
- Warehouse-specific features: Snowflake clustering, BigQuery partitioning, Redshift sort keys

## Usage

1. Identify the user's warehouse need (schema design, SQL optimization, ETL, or partitioning)
2. Follow the corresponding workflow below
3. Produce structured outputs: ER diagrams, optimized SQL queries, ETL pipeline designs, or partitioning plans

## Examples

- **User**: "Design a star schema for sales"
  **Agent**: Runs Dimensional Modeling workflow, identifies fact table (sales), dimension tables (date, product, customer, region), creates ER diagram

- **User**: "Optimize a slow query"
  **Agent**: Runs SQL Optimization workflow, analyzes execution plan, recommends indexes, rewrites query with CTEs

- **User**: "Set up incremental loads"
  **Agent**: Runs ETL/ELT workflow, designs CDC pattern, implements watermark-based extraction, adds data quality checks

## When to Use

- Diagnosing slow warehouse SQL and improving partition, cluster, or join plans
- Designing star/snowflake schemas, SCDs, and fact/dimension tables
- Building idempotent, incremental, or CDC ETL with observability and quality checks
- Comparing Snowflake, BigQuery, Databricks, or Redshift syntax and trade-offs

## When NOT to Use

- Enterprise-wide data mesh, governance pillars, or compliance program design → use `data-architect`
- BI dashboard layout, chart selection, or stakeholder-facing metrics → use `bi-analyst`
- dbt layers, mart tests, exposures, and analytics engineering workflows → use `analytics-data-engineer`
- ML feature stores, model serving, or experiment analysis → use `data-scientist`
- On-call leadership for the full data platform org → use `data-system-ops-lead`
- Application runtime profiling, API load tests, OLTP latency SLOs → use `performance-engineer`

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

### 2. Data Model Design

**Decision tree:**

- Need fast aggregations and simple joins? → **Star schema**
- Need normalized dimensions to reduce redundancy? → **Snowflake schema**
- Tracking historical changes in dimensions? → **Slowly Changing Dimension (SCD) type 2**
- Event-based data with high volume? → **Fact table with partitioning on event date**
- Need real-time-ish analytics? → **Streaming ingestion + micro-batch fact tables**

### 3. ETL Pipeline Design

**Essential properties every pipeline must satisfy:**

| Property | Pattern |
|---|---|
| Idempotency | MERGE / INSERT OVERWRITE with deterministic keys |
| Incrementality | `WHERE updated_at > (SELECT MAX(updated_at) FROM target)` |
| Atomicity | Wrap multi-step loads in a transaction or use staging → swap pattern |
| Observability | Row counts, null rates, freshness checks logged per run |
| Error handling | Dead-letter queue for bad records; fail loudly on schema drift |

### 4. Platform Selection Quick Reference

| Need | Best Fit |
|---|---|
| Semi-structured JSON, auto-scaling | Snowflake |
| Tight GCP integration, nested/repeated fields | BigQuery |
| ML + Spark + SQL in one lakehouse | Databricks |
| AWS-native, predictable cost at scale | Redshift |
