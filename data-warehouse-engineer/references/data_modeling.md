# Data Modeling

## Dimensional Modeling

### Star Schema
- One central fact table surrounded by denormalized dimension tables
- Best for: query simplicity, fast aggregations, BI tool compatibility

### Snowflake Schema
- Dimensions normalized into sub-dimensions
- Best for: reducing storage redundancy, complex hierarchies
- Trade-off: more joins, slightly slower queries

## Fact Table Design

| Property | Guidance |
|---|---|
| Grain | One row per business event (e.g., one order line item) |
| Degenerate dimensions | Store dimension-like attributes directly (order_number, transaction_id) |
| Foreign keys | Surrogate integer keys (not natural keys) for stability |
| Partition key | Event date or ingestion date for time-series data |
| Measures | Additive (sales_amount), semi-additive (balance), non-additive (unit_price) |

## Dimension Table Patterns

### Slowly Changing Dimension (SCD)

| Type | Behavior | Implementation |
|---|---|---|
| Type 0 | Fixed, never changes | Static reference data |
| Type 1 | Overwrite in place | Simple UPDATE; loses history |
| Type 2 | Track history with effective dates | Add `valid_from`, `valid_to`, `is_current` columns |
| Type 3 | Track limited history (previous + current) | Add `previous_value` column |
| Type 4 | Mini-dimension for high-change attributes | Separate table for volatile attributes |

**SCD Type 2 SQL Template:**

```sql
-- Close existing row
UPDATE dim_customer
SET valid_to = CURRENT_DATE, is_current = FALSE
WHERE customer_id = :id AND is_current = TRUE;

-- Insert new current row
INSERT INTO dim_customer (customer_id, name, region, valid_from, valid_to, is_current)
VALUES (:id, :name, :region, CURRENT_DATE, '9999-12-31', TRUE);
```

### Junk Dimensions
Combine low-cardinality flags into a single dimension to reduce fact table width.

### Bridge Tables
Use for many-to-many relationships (e.g., patient → multiple diagnoses).

## Naming Conventions

| Object | Convention | Example |
|---|---|---|
| Fact tables | `f_<event>` | `f_order_line` |
| Dimension tables | `d_<entity>` | `d_customer` |
| Date dimension | `d_date` | Standard calendar |
| Aggregate tables | `agg_<grain>_<metric>` | `agg_daily_revenue` |
| Staging tables | `stg_<source>_<entity>` | `stg_shopify_orders` |

## Data Vault (Alternative)
Use when:
- Source systems change frequently
- Need full auditability and traceability
- Agility > query performance (sacrifice some speed for flexibility)

Components: Hubs (business keys), Links (relationships), Satellites (attributes).
