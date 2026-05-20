# Database and data-path performance

## Table of contents

1. [Investigation flow](#investigation-flow)
2. [Query analysis](#query-analysis)
3. [Indexing and schema](#indexing-and-schema)
4. [Caching and denormalization](#caching-and-denormalization)
5. [Warehouse vs OLTP](#warehouse-vs-oltp)

## Investigation flow

1. Identify slow queries from **APM**, DB slow log, or `EXPLAIN`
2. Capture **plan**, row counts, buffer hits, execution time
3. Correlate with **traffic** — one query vs N+1 storm
4. Reproduce on **staging** with similar cardinality
5. Measure after fix under load test

## Query analysis

| Pattern | Fix direction |
|---|---|
| Full table scan | Index, rewrite filter, partition prune |
| N+1 ORM | Join, batch load, DataLoader pattern |
| Sort on large set | Index covering ORDER BY, limit early |
| Lock contention | Shorter tx, index order, avoid hot row updates |
| Pagination OFFSET | Keyset / cursor pagination |
| SELECT * | Project columns; reduce wire size |

Always compare **plans before/after**; watch plan regression on data growth.

## Indexing and schema

- Index **equality + range** columns in selective order
- Avoid over-indexing write-heavy tables
- Partial indexes for filtered subsets
- Consider **read replicas** for read-heavy, eventually-consistent OK paths

For warehouse-specific modeling and partition keys → `data-warehouse-engineer`.

## Caching and denormalization

| Layer | When |
|---|---|
| Application cache | Stable keys, TTL, invalidation story |
| CDN / edge | Public static or cacheable GET |
| DB query cache | Rare; prefer explicit app cache |
| Materialized view | Heavy aggregates, acceptable staleness |

Document **cache stampede** mitigation (single-flight, jittered TTL).

## Warehouse vs OLTP

| OLTP (this skill, app path) | Warehouse (`data-warehouse-engineer`) |
|---|---|
| Single-digit ms–low sec | Seconds–minutes acceptable |
| Row-level consistency | Batch/analytical |
| Index for point lookups | Partition, cluster, sort keys |

Route deep star-schema and ELT design to warehouse skill; stay on **app-issued SQL** and connection behavior here.
