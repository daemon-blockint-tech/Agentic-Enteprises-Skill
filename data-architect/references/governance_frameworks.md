# Governance & Compliance Frameworks

## Data Quality Framework

**Dimensions:**

| Dimension | Definition | Measurement |
|---|---|---|
| Completeness | Required fields are populated | `% non-null for mandatory columns` |
| Uniqueness | No unintended duplicates | `COUNT(DISTINCT key) / COUNT(*)` |
| Validity | Values conform to business rules | Regex, range checks, referential integrity |
| Timeliness | Data is fresh enough for use | `MAX(updated_at)` vs SLA threshold |
| Consistency | Same data means same thing everywhere | Cross-system reconciliation |
| Accuracy | Values reflect real-world truth | Sampling, source system validation |

**Implementation tiers:**
1. **Reactive**: Fix issues after they cause problems
2. **Proactive**: dbt tests, Great Expectations, data contracts
3. **Predictive**: Anomaly detection (Monte Carlo, Bigeye, Anomalo)

## Data Catalog & Lineage

**Capabilities:**
- **Discovery**: Search datasets by name, description, tags, owner
- **Metadata**: Schema, descriptions, data types, update frequency
- **Lineage**: Upstream sources → transformations → downstream consumers
- **Impact analysis**: What breaks if I change this column?

**Tools comparison:**

| Tool | Open Source | Best For | Limitations |
|---|---|---|---|
| DataHub | Yes | Modern stack, integrations | Setup complexity |
| Apache Atlas | Yes | Hadoop ecosystem | Dated UI, limited cloud-native |
| Collibra | No | Enterprise governance | Cost, heavyweight |
| Alation | No | Self-service catalog | Cost, limited lineage depth |
| Amundsen (Lyft) | Yes | Discovery-focused | Limited governance features |

**Lineage implementation approaches:**
1. **Query log parsing**: Parse SQL to build lineage (automated, incomplete)
2. **Orchestrator integration**: Airflow/Dagster task dependencies
3. **Manual annotation**: Human-curated for critical pipelines

## Master Data Management (MDM)

**When to implement MDM:**
- Same entity exists in 3+ systems with conflicting data
- Customer 360 initiatives failing due to fragmented data
- Compliance requires single source of truth

**Patterns:**
- **Registry**: Match IDs across systems, no central storage
- **Consolidation**: Extract, match, merge into golden record database
- **Coexistence**: Hybrid; updates flow back to source systems
- **Transaction hub**: Central system becomes system of record

**Matching techniques:**
- Deterministic: Exact match on email, phone, SSN
- Probabilistic: Fuzzy matching (Levenshtein, Jaro-Winkler)
- ML-based: Classification models for entity resolution

## Access Control Architecture

**Layered approach:**

```
Network → Identity → Role → Policy → Data

Network: VPC, private links, IP allowlists
Identity: SSO, MFA, service accounts
Role: RBAC groups (analyst, engineer, admin)
Policy: Row-level, column-level, masking
Data: Encryption at rest, in transit
```

**Row-level security (RLS) patterns:**
- Filter predicates in views
- Platform-native RLS policies
- Application-level enforcement (last resort)

## Compliance Frameworks

### GDPR (EU)
**Key requirements for data architecture:**
- Data minimization: Collect only what's necessary
- Purpose limitation: Define and enforce use cases
- Right to erasure: Technical capability to delete across systems
- Data portability: Export in machine-readable format
- Privacy by design: Pseudonymization, encryption

### CCPA/CPRA (California)
**Key requirements:**
- Consumer rights: Know, delete, opt-out of sale
- Data inventory: Map personal information flows
- Service provider contracts: Ensure downstream compliance

### HIPAA (Healthcare)
**Key requirements:**
- PHI identification and access logging
- Encryption (at rest, in transit)
- Audit trails (who accessed what, when)
- Minimum necessary access principle

### SOC 2
**Trust services criteria:**
- Security: Access controls, encryption
- Availability: Monitoring, incident response
- Processing integrity: Data validation, error handling
- Confidentiality: Classification, retention
- Privacy: Consent, collection limitations

## Data Retention & Lifecycle

**Policy template:**

| Data Class | Retention | Action After | Storage Tier |
|---|---|---|---|
| Raw transactional | 90 days | Archive to cold | Hot → Cold |
| Aggregated analytics | 7 years | Archive | Warm → Cold |
| PII (with consent) | Until consent withdrawn | Anonymize or delete | Hot |
| Audit logs | 7 years | None (compliance) | Cold |
| Dev/test data | 30 days | Delete | Hot |

**Technical implementation:**
- Partitioning by date enables efficient deletion/archival
- Object storage lifecycle policies (S3 Glacier, GCS Nearline)
- Legal holds override automatic deletion
