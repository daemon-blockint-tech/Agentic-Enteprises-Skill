# Analytics Modeling

## Grain first

Every mart answers: **one row = what?**

Document in model YAML:

```yaml
description: One row per order line per day (order_date)
```

Changing grain is a **breaking change** for BI.

## Patterns

| Pattern | When |
|---|---|
| **Star** | Facts + conformed dimensions |
| **Wide mart** | Self-serve BI; denormalized |
| **Bridge** | Many-to-many (campaign ↔ user) |
| **Activity schema** | Optional; event-centric products |

Coordinate star-schema depth with `data-warehouse-engineer` for platform-wide conformed dimensions.

## Facts

- Declarative measures; same grain
- Handle **late-arriving** dimensions in intermediate layer
- Surrogate keys stable across reloads

## Dimensions

- SCD2 via snapshots or `valid_from`/`valid_to` in intermediate
- Role-playing dates as separate keys in fact (order_date_key, ship_date_key)

## Intermediate layer role

- Complex joins and business rules here
- Keeps marts thin and testable
- Not exposed in catalog to general analysts

## Performance hints

- Pre-aggregate heavy metrics in `int_` or mart variants (`fct_orders_daily`)
- Align cluster/partition keys with filter columns — see `data-warehouse-engineer`
