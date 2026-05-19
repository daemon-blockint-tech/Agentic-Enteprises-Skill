# Platform & Technology Selection

## CAP Theorem for Data Systems

**In distributed systems, pick two:**
- **Consistency**: All nodes see the same data at the same time
- **Availability**: Every request receives a response
- **Partition tolerance**: System continues despite network failures

**Data system choices:**
| System | CAP Priority | Use Case |
|---|---|---|
| Traditional RDBMS | CP | Financial transactions, inventory |
| Distributed Warehouse | AP | Analytics, BI (eventual consistency acceptable) |
| Stream processing | AP | Real-time analytics, monitoring |
| Distributed ledger | CP | Audit trails, consensus |

## Platform Comparison Matrix

| Dimension | Snowflake | BigQuery | Databricks | Redshift | S3 + Athena |
|---|---|---|---|---|---|
| **Pricing model** | Compute + storage | On-demand / slots | DBU | Node-based | Storage + query |
| **Scaling** | Auto (elastic) | Serverless (auto) | Auto (clusters) | Manual / Concurrency | Query-level |
| **Best for** | Multi-cloud, SaaS | GCP-native, ad-hoc | ML + Spark + SQL | AWS-native, predictable | Cost exploration |
| **Semi-structured** | VARIANT (native) | JSON/ARRAY/STRUCT | Spark schemas | SUPER (RA3) | Schema on read |
| **Streaming** | Snowpipe | Streaming API | Delta Live Tables | Kinesis (external) | Kinesis + Athena |
| **ML integration** | Snowpark | BigQuery ML | Spark ML, MLflow | Redshift ML (SageMaker) | External (SageMaker) |
| **Data sharing** | Secure data sharing | Analytics Hub | Delta Sharing | Data sharing (limited) | S3 cross-account |
| **Vendor lock-in** | Medium | High (GCP) | Medium (Spark-based) | Medium (AWS) | Low (open formats) |

## TCO Considerations (3-Year)

**Cost components:**
1. Infrastructure (compute, storage, networking)
2. Licensing / subscription
3. Migration (data movement, schema conversion, testing)
4. Operations (monitoring, tuning, support)
5. Training (team upskilling)

**Cost optimization levers:**
- Reserved instances / committed use discounts for predictable workloads
- Separate dev/test environments (smaller or spot instances)
- Lifecycle policies: hot → warm → cold → archive
- Query optimization (see `data-warehouse-engineer` skill for SQL tuning)

## Vendor Evaluation Checklist

**Technical:**
- [ ] Supports required data types and formats
- [ ] Meets latency/throughput SLAs
- [ ] Integrates with existing toolchain
- [ ] Has required security certifications
- [ ] Provides adequate backup/DR capabilities

**Commercial:**
- [ ] Pricing model aligns with usage patterns
- [ ] Contract terms allow flexibility (scale up/down)
- [ ] Exit strategy defined (data portability, format)

**Organizational:**
- [ ] Team has skills or can acquire them
- [ ] Vendor support quality assessed
- [ ] Community/ecosystem maturity

## Hybrid & Multi-Cloud Strategies

**When to go multi-cloud:**
- Vendor redundancy requirements
- Best-of-breed services (e.g., BigQuery for analytics + Snowflake for sharing)
- M&A integration (inherited platforms)

**Challenges:**
- Data egress costs
- Cross-cloud identity management
- Operational complexity
- Consistent tooling across platforms

**Mitigation:**
- Use open table formats (Iceberg, Delta) for portability
- Centralize orchestration (Airflow, Dagster)
- Abstract storage (S3-compatible APIs)
