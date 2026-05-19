---
name: data-architect
description: |
  Guides data architecture decisions at enterprise and solution levels.
  Covers data mesh, lakehouse, governance, domain-driven design, conceptual/logical/physical data modeling,
  platform selection, and compliance frameworks.
  Use when designing data platforms, choosing between lake/warehouse/mesh, defining governance policies,
  creating data models, or making technology selection decisions for data infrastructure.
---

# Data Architect

## Core Workflows

### 1. Architecture Decision Framework

**Use this 5-step process for any major data architecture decision:**

1. **Define the decision context**
   - Business drivers (scale, latency, cost, compliance)
   - Constraints (budget, timeline, existing tech, team skills)
   - Stakeholders (data engineers, analysts, product, legal)

2. **Identify alternatives**
   - At least 3 options (do nothing, minimal change, transformative)
   - Include cloud-native, hybrid, and open-source alternatives

3. **Evaluate against criteria**
   | Criterion | Weight | Score 1-5 each option |
   |---|---|---|
   | Scalability | High |  |
   | Cost (TCO 3yr) | High |  |
   | Time to value | Medium |  |
   | Operational complexity | Medium |  |
   | Team fit | Medium |  |
   | Vendor lock-in risk | Low |  |

4. **Assess risks & mitigation**
   - Migration risk, talent risk, operational risk
   - POC plan for the top 2 options

5. **Document the decision**
   - ADR (Architecture Decision Record) with context, decision, consequences
   - Share with stakeholders; revisit quarterly

**See `references/enterprise_architecture.md` for data mesh, lakehouse, and domain-driven design patterns.**

### 2. Data Modeling Workflow

**Progressive refinement from business to implementation:**

| Stage | Output | Audience | Key Activities |
|---|---|---|---|
| Conceptual | Entity list, relationships, business glossary | Business stakeholders | Workshops, domain events |
| Logical | Normalized ER diagram, attributes, keys | Data analysts, architects | Identify entities, resolve many-to-many |
| Physical | DB-specific DDL, partitions, indexes | Engineers | Platform optimization, denormalization |

**Key principles:**
- Start with the business question, not the technology
- Use surrogate keys in physical model; natural keys in logical
- Denormalize only when you have a performance requirement

**See `references/data_modeling.md` for ER notation, normalization rules, and schema patterns.**

### 3. Platform & Technology Selection

**Decision tree:**

- Need structured analytics + BI at scale? → **Data Warehouse** (Snowflake, BigQuery, Redshift)
- Need raw data + ML + flexible schemas? → **Data Lake** (S3 + Athena/Spark)
- Need both with ACID guarantees? → **Lakehouse** (Databricks, Iceberg, Hudi)
- Need domain ownership + federated governance? → **Data Mesh** (multiple warehouses/lakes per domain)
- Need real-time + low latency? → **Streaming-first** (Kafka + Flink + materialized views)

**See `references/platform_selection.md` for CAP theorem trade-offs, TCO comparisons, and vendor evaluation.**

### 4. Governance & Compliance Planning

**Governance pillars:**

| Pillar | Activities | Tools |
|---|---|---|
| Data Quality | Profiling, validation rules, anomaly detection | dbt tests, Great Expectations, Monte Carlo |
| Data Catalog | Metadata, lineage, discovery | DataHub, Collibra, Alation |
| Access Control | RBAC, ABAC, masking, encryption | Platform-native + Immuta/Okera |
| Master Data Management | Golden records, deduplication | Informatica, Reltio, custom MDM |
| Compliance | GDPR, CCPA, HIPAA, SOC 2 | Legal review + technical controls |

**See `references/governance_frameworks.md` for implementation patterns, policy templates, and compliance checklists.**

## When to Load References

- **Enterprise patterns** → `references/enterprise_architecture.md`
- **Data modeling deep-dive** → `references/data_modeling.md`
- **Platform comparison** → `references/platform_selection.md`
- **Governance & compliance** → `references/governance_frameworks.md`
