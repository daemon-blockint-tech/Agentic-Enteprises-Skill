# Testing and Quality

## Test pyramid (analytics)

| Level | Examples |
|---|---|
| **Schema** | `unique`, `not_null`, `accepted_values` |
| **Relationships** | `relationships` to dimensions |
| **Business** | Custom SQL tests, singular tests |
| **Freshness** | `source freshness` on raw loads |
| **Volume** | Row count anomalies (optional package) |

## Severity

| Severity | On failure |
|---|---|
| **error** | Block merge / deploy |
| **warn** | Alert; investigate |

## Custom tests

Use for rules that are not single-column:

- Revenue = sum(line_amount)
- No orders with ship before order date
- Referential integrity across systems

## Contracts (optional)

- Define column types and constraints where warehouse supports
- Coordinate breaking contract changes with BI

## CI minimum bar

On every PR:

- `dbt parse` / `dbt compile`
- `dbt run --select state:modified+` (or slim CI)
- `dbt test --select state:modified+`

## Production monitoring

- Freshness SLA per critical source
- Test failures route to on-call per `data-system-ops-lead` runbook

## Anti-patterns

- Tests only on primary key
- No tests on business-critical measures
- Disabling tests to green CI
