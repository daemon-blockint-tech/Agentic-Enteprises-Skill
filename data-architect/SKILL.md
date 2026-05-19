---
name: data-architect
description: |
  Design data architecture at enterprise and solution levels.
  Cover data mesh, lakehouse, governance, domain-driven design, conceptual/logical/physical data modeling,
  platform selection, and compliance frameworks. Produce ADRs, data model diagrams, platform comparison
  matrices, and governance policy templates.
  Triggers on "design data platform", "choose data warehouse", "data mesh", "lakehouse architecture",
  "data governance", "data modeling", "platform selection", "data architecture decision",
  "compliance framework", or "data strategy". For applied AI solution architecture (RAG data plane,
  embeddings, vector stores in commercial or enterprise products), use
  applied-ai-architect-commercial-enterprise. For dbt analytics layers and mart delivery, use
  analytics-data-engineer—not data-architect.
---

# Data Architect

## Overview

Design data architecture at enterprise and solution levels. This skill covers data mesh, lakehouse,
governance, domain-driven design, conceptual/logical/physical data modeling, platform selection,
and compliance frameworks. Produce ADRs, data model diagrams, platform comparison matrices,
and governance policy templates.

## When to Use

- Choosing among warehouse, lake, lakehouse, mesh, or streaming-first patterns
- Creating conceptual, logical, or physical data models and ADRs
- Defining data governance, catalog, quality, and compliance frameworks
- Evaluating data platforms and long-term TCO or vendor trade-offs

## When NOT to Use

- Day-to-day pipeline on-call, SLA breaches, or shift handoffs → use `data-system-ops-lead`
- Single-platform SQL tuning or star-schema implementation detail → use `data-warehouse-engineer`
- dbt project implementation, mart tests, and analytics CI → use `analytics-data-engineer`
- Team roadmaps, sprint cadence, or governance operations execution → use `data-manager`
- OWL/RDF ontologies or knowledge-graph construction → use `ontology-engineer`
- Application integration patterns and non-data system ADRs → use `senior-system-architecture`
- LLM/RAG/copilot solution architecture and AI ADRs → use `applied-ai-architect-commercial-enterprise`

## Features

- Architecture decision framework with weighted criteria evaluation
- Progressive data modeling workflow (conceptual → logical → physical)
- Platform selection decision tree for warehouse/lake/lakehouse/mesh/streaming
- Governance pillar planning with tool recommendations
- ADR template generation and stakeholder review processes

## Usage

1. Identify the user's data architecture need (platform choice, modeling, governance, or decision framework)
2. Follow the corresponding workflow below
3. Produce structured outputs: ADRs, data model diagrams, platform comparison matrices, or governance policies

## Examples

- **User**: "Should we use a data lake or data warehouse for our analytics?"
  **Agent**: Runs Platform & Technology Selection workflow (Workflow 3), evaluates structured vs raw data needs, recommends warehouse/lake/lakehouse with trade-offs

- **User**: "We need to model our customer domain"
  **Agent**: Runs Data Modeling Workflow (Workflow 2), starts with conceptual model (entities, relationships), progresses to logical ER diagram, then physical DDL

- **User**: "How do we set up data governance for GDPR compliance?"
  **Agent**: Runs Governance & Compliance Planning (Workflow 4), maps GDPR requirements to governance pillars, recommends tools and controls

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

### 3. Platform & Technology Selection

**Decision tree:**

- Need structured analytics + BI at scale? → **Data Warehouse** (Snowflake, BigQuery, Redshift)
- Need raw data + ML + flexible schemas? → **Data Lake** (S3 + Athena/Spark)
- Need both with ACID guarantees? → **Lakehouse** (Databricks, Iceberg, Hudi)
- Need domain ownership + federated governance? → **Data Mesh** (multiple warehouses/lakes per domain)
- Need real-time + low latency? → **Streaming-first** (Kafka + Flink + materialized views)

### 4. Governance & Compliance Planning

**Governance pillars:**

| Pillar | Activities | Tools |
|---|---|---|
| Data Quality | Profiling, validation rules, anomaly detection | dbt tests, Great Expectations, Monte Carlo |
| Data Catalog | Metadata, lineage, discovery | DataHub, Collibra, Alation |
| Access Control | RBAC, ABAC, masking, encryption | Platform-native + Immuta/Okera |
| Master Data Management | Golden records, deduplication | Informatica, Reltio, custom MDM |
| Compliance | GDPR, CCPA, HIPAA, SOC 2 | Legal review + technical controls |
