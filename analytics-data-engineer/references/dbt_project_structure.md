# dbt Project Structure

## Layering

| Layer | Prefix | Purpose |
|---|---|---|
| **Sources** | `source()` | Raw landing; minimal logic |
| **Staging** | `stg_` | Clean, rename, type, dedupe keys |
| **Intermediate** | `int_` | Business logic joins; not exposed to BI |
| **Marts** | `fct_`, `dim_`, `mart_` | Analytics-ready; documented grain |

Rule: **BI tools only query marts** (and approved exposures), not staging.

## Naming

- `{entity}` singular for dimensions, events plural for facts where clear
- Suffix role: `_daily`, `_hourly` for snapshots of grain
- Avoid environment names in model names

## Materializations (defaults)

| Layer | Default | Notes |
|---|---|---|
| Staging | view or ephemeral | Cheap rebuild |
| Intermediate | view or table | Table if expensive |
| Marts | table or incremental | Incremental for large facts |

Override in `dbt_project.yml` by folder.

## Packages and macros

- Centralize **surrogate keys**, **timezone**, **currency** in macros
- Pin package versions in `packages.yml`

## Environments

| Target | Use |
|---|---|
| dev | Personal schema or prefix |
| ci | Ephemeral PR schema |
| prod | Stable schemas; no full-refresh without approval |

## Anti-patterns

- Business logic in staging
- Circular dependencies between intermediates
- `select *` in production models
