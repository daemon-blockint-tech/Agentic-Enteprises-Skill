# Data Modeling

## Conceptual Modeling

**Purpose:** Align business and technology on "what" data exists

**Techniques:**
- **Business capability mapping**: What does the business do? → What data does it need?
- **Domain storytelling**: Walk through user journeys; identify events and entities
- **Event storming**: Identify domain events, commands, aggregates

**Output:**
- Business glossary (terms, definitions, owners)
- High-level entity list
- Context map showing bounded contexts

## Logical Modeling

### ER Notation (Crow's Foot)
- Entity = rectangle
- Relationship = line with crow's foot (many) or single bar (one)
- Attribute = oval or listed inside entity

### Normalization Rules

| Normal Form | Rule | When to Stop |
|---|---|---|
| 1NF | Atomic values, no repeating groups | Always |
| 2NF | No partial dependencies (non-key depends on full key) | Composite keys only |
| 3NF | No transitive dependencies | Most OLTP; OLAP often denormalizes |
| BCNF | Every determinant is a candidate key | Academic rigor |

**Practical guidance:**
- Normalize to 3NF in logical model
- Denormalize in physical model for read performance
- Document every denormalization with justification

### Common Schema Patterns

**Star Schema**
- Central fact table + surrounding dimension tables
- Simple joins, fast aggregation
- Best for: BI, dashboards, ad-hoc analysis

**Snowflake Schema**
- Dimensions normalized into sub-dimensions
- Reduced redundancy, more complex joins
- Best for: complex hierarchies, storage optimization

**Data Vault 2.0**
- Hubs (business keys), Links (relationships), Satellites (attributes)
- Auditability, agility, parallel loading
- Best for: large enterprises, frequent source changes, compliance needs

**Anchor Modeling**
- Extreme normalization; every attribute is a separate table
- Highly flexible but complex queries
- Best for: domains with rapid schema evolution

### Key Design

| Key Type | Use Case | Example |
|---|---|---|
| Natural key | Stable business identifier | SSN (careful with PII) |
| Surrogate key | System-generated integer | `customer_id` auto-increment |
| UUID | Distributed systems, merge conflicts | `a1b2c3d4-...` |
| Composite key | Multi-entity relationships | `(order_id, line_number)` |

**Recommendation:** Use surrogate keys in physical tables; document natural key mapping.

## Physical Modeling

### Transformation from Logical to Physical

1. **Choose platform** (see `platform_selection.md`)
2. **Map data types** (platform-specific)
3. **Add technical columns**: `created_at`, `updated_at`, `loaded_by`, `batch_id`
4. **Design partitions**: Time-based for event data, hash-based for even distribution
5. **Add indexes**: Primary, foreign, covering indexes for common queries
6. **Apply compression**: Columnar for analytics, row for OLTP

### Partitioning Strategies

| Strategy | Best For | Platforms |
|---|---|---|
| Range (time) | Time-series, event data | All |
| List (category) | Discrete categories (region, status) | Most |
| Hash | Even distribution, no natural range | Databricks, Redshift |
| Composite | Large tables with multiple access patterns | BigQuery, Snowflake |

### Denormalization Techniques

| Technique | When | Trade-off |
|---|---|---|
| Pre-join | Repeated star schema queries | Storage for speed |
| Add redundant columns | Frequently accessed derived values | Update complexity |
| Materialized aggregates | Dashboard KPIs | Staleness vs freshness |
| JSON/Array columns | Semi-structured, variable schema | Query complexity |
