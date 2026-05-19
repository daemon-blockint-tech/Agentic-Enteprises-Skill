# Enterprise Architecture Patterns

## Data Mesh

**Core principles (Zhamak Dehghani):**
- Domain-oriented decentralized data ownership
- Data as a product (with SLAs, documentation, discoverability)
- Self-serve data infrastructure as a platform
- Federated computational governance

**When to adopt:**
- Large organization (>500 data consumers)
- Multiple domains with distinct data needs
- Pain points with centralized data team bottleneck

**When NOT to adopt:**
- Small organization (<50 data consumers)
- Limited platform engineering capacity
- Strong need for centralized compliance control

**Implementation phases:**
1. Identify domains and domain data product owners
2. Build self-serve infrastructure platform (data catalog, pipeline templates, access control)
3. Define federated governance standards (schema registries, quality SLAs)
4. Gradually migrate domain by domain

## Data Lakehouse

**Combines data lake flexibility + warehouse reliability:**
- Open table formats: Delta Lake, Apache Iceberg, Apache Hudi
- ACID transactions on object storage
- Schema evolution and time travel
- Unified batch + streaming

**Architecture layers:**

```
┌─────────────────────────────────────┐
│  Consumption (BI, ML, Analytics)   │
├─────────────────────────────────────┤
│  Semantic/Gold (curated, modeled)   │
├─────────────────────────────────────┤
│  Refined/Silver (cleaned, joined)   │
├─────────────────────────────────────┤
│  Raw/Bronze (ingested as-is)        │
├─────────────────────────────────────┤
│  Ingestion (batch + streaming)       │
└─────────────────────────────────────┘
```

**Medallion architecture guidelines:**
- Bronze: Append-only, schema on read, keep raw for 30-90 days
- Silver: Deduplicated, typed, domain-partitioned
- Gold: Business-aggregated, star schema, optimized for query

## Domain-Driven Design (DDD) for Data

**Bounded contexts map to data domains:**
- Each domain owns its data models, pipelines, and quality SLAs
- Shared kernels for cross-domain concepts (customer, product)
- Anti-corruption layer when integrating legacy systems

**Ubiquitous language:**
- Maintain a business glossary per domain
- Map terms to logical model entities
- Resolve conflicts at enterprise level (e.g., "customer" in Sales vs Support)

## Event-Driven Architecture

**Patterns:**
- **Event sourcing**: Store state changes as events; reconstruct state
- **CQRS**: Separate read and write models
- **Change Data Capture (CDC)**: Database → event stream → consumers

**When to use:**
- Microservices needing data synchronization
- Real-time analytics requirements
- Audit trails and compliance needs

## Reference Architectures

### Modern Data Platform (Simplified)

```
Sources → Ingestion → Storage → Processing → Serving → Consumption

Sources:     Apps, APIs, DBs, IoT, SaaS
Ingestion:   Kafka, Fivetran, Airbyte, Debezium
Storage:     S3/ADLS/GCS (lake) + Warehouse (Snowflake/BQ)
Processing:  Spark, dbt, Flink, Airflow
Serving:     Semantic layer (Cube, dbt metrics), Feature store
Consumption: BI (Looker, Tableau), Notebooks, Apps
```

### Hybrid Cloud
- Sensitive data on-premise (HIPAA, financial)
- Analytics in cloud (scalability, ML services)
- Use private connectivity (Direct Connect, ExpressRoute)
