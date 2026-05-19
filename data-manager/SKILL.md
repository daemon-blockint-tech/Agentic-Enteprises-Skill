---
name: data-manager
description: |
  Manage data programs, governance operations, and data reliability.
  Cover data roadmaps, stakeholder coordination, metadata stewardship, lifecycle management, monitoring,
  incident response, capacity planning, and SLA frameworks.
  Triggers on "manage data team", "data roadmap", "governance review", "data incident",
  "SLA framework", "data ops", "stewardship", "data product delivery", or "data KPIs".
  Human annotation/labeling platform PM: product-management-human-data-platform.
---

# Data Manager

## Overview

Manage data programs, governance operations, and data reliability. This skill covers data roadmaps,
stakeholder coordination, metadata stewardship, lifecycle management, monitoring, incident response,
capacity planning, and SLA frameworks.

## Features

- Data roadmap planning with stakeholder alignment and delivery cadence
- Governance operations: stewardship, access reviews, lifecycle enforcement
- Data ops monitoring with incident response and escalation paths
- Team KPI/SLA scorecards and operational metrics
- Cross-functional coordination across engineers, analysts, scientists, and legal

## Usage

1. Identify the user's data management need (roadmap, governance, ops, or coordination)
2. Follow the corresponding workflow below
3. Produce structured outputs: roadmaps, governance policies, incident reports, or KPI dashboards

## Examples

- **User**: "Create a data team roadmap"
  **Agent**: Runs Program Management workflow, produces quarterly roadmap with initiatives, dependencies, and stakeholder sign-offs

- **User**: "Set up data governance"
  **Agent**: Runs Governance Operations workflow, defines stewardship roles, access review cadence, and lifecycle policies

- **User**: "Handle a data incident"
  **Agent**: Runs Data Ops workflow, triages severity, executes runbook, produces post-incident report with action items

## When to Use

- Own the data roadmap, stakeholder reviews, and data product delivery cadence
- Run governance operations (stewardship, access reviews, lifecycle enforcement)
- Establish data ops monitoring, incident response, and team KPI/SLA scorecards
- Coordinate engineers, analysts, scientists, and legal on cross-functional data work

## When NOT to Use

- Deep platform architecture ADRs or ontology design → use `data-architect` or `ontology-engineer`
- Hands-on warehouse SQL optimization or SCD modeling → use `data-warehouse-engineer`
- ML experimentation, model evaluation, or MLOps deployment → use `data-scientist`
- Cloud VPC, Kubernetes, or IaC provisioning → use `infrastructure-engineer`
- Company-wide multi-team technical programs (non-data) → use `technical-program-manager`

## Core Workflows

### 1. Data Program & Product Management

**Responsibilities:**
- Own the data roadmap aligned to business outcomes
- Translate stakeholder needs into data product requirements
- Coordinate cross-functional data work (engineers, analysts, scientists, legal)

**Operational cadence:**

| Meeting | Frequency | Attendees | Purpose |
|---|---|---|---|
| Data Leadership Sync | Weekly | Data leads, PMs | Blockers, priorities, resource allocation |
| Stakeholder Reviews | Bi-weekly | Business sponsors | Roadmap alignment, value demonstration |
| Sprint Planning | Bi-weekly | Engineering team | Commitments, estimation, dependencies |
| Retrospectives | Monthly | Full data team | Process improvements, team health |

**Data product delivery checklist:**
1. Define the business question and success criteria
2. Identify data sources and validate availability/quality
3. Design the data model (see `data-architect` skill)
4. Build with observability (logging, lineage, tests)
5. Validate with stakeholders before GA
6. Document and train consumers
7. Monitor usage and iterate

### 2. Governance Operations Execution

**Core activities:**

| Activity | Frequency | Owner | Output |
|---|---|---|---|
| Metadata stewardship | Continuous | Data stewards | Enriched catalog, documented lineage |
| Access reviews | Quarterly | Security + owners | Approved access matrix |
| Data lifecycle enforcement | Monthly | Operations | Archived/deleted per retention policy |
| Quality SLA review | Monthly | Governance lead | Quality scorecard, remediation plan |
| Policy compliance audit | Quarterly | Audit/compliance | Gap report, remediation tickets |

**Escalation paths:**
- Data incident → On-call engineer → Team lead → Director
- Quality breach → Data steward → Governance committee → CDO
- Access violation → Security team → Legal (if PII exposure)

### 3. Data Operations & Reliability

**Monitoring stack:**

| Layer | Metrics | Alert Threshold |
|---|---|---|
| Infrastructure | CPU, memory, disk, network | >80% for 5 min |
| Database | Connections, lock waits, replication lag | Replication lag >30s |
| Pipelines | Success rate, duration, row counts | <95% success rate |
| Data quality | Null rate, freshness, duplicates | SLA breach |
| Cost | Daily spend vs budget | >110% of daily budget |

**Incident response phases:**
1. **Detect**: Alert fires or user reports issue
2. **Triage**: Assess severity (P1-P4), assign owner
3. **Mitigate**: Stop bleeding (rollback, redirect traffic)
4. **Resolve**: Root cause fix deployed
5. **Review**: Post-mortem within 48 hours for P1-P2

### 4. Metrics & SLA Framework

**Data team KPIs:**

| Category | Metric | Target | Measurement |
|---|---|---|---|
| Reliability | Pipeline success rate | >99% | Airflow/Dagster logs |
| Quality | Data quality score | >95% | dbt tests + Great Expectations |
| Freshness | Data latency (source → warehouse) | <4 hours | Pipeline metadata |
| Cost | Cost per TB processed | Trend down | Cloud billing |
| Productivity | Time from request to production | <2 weeks | Jira/Asana cycle time |
| Adoption | Active data consumers | Grow 10% QoQ | BI tool usage logs |

**SLA tiers:**

| Tier | Description | RTO | RPO | Example |
|---|---|---|---|---|
| Tier 1 | Business-critical dashboards | 1 hour | 0 | Revenue reporting |
| Tier 2 | Operational analytics | 4 hours | 4 hours | Marketing attribution |
| Tier 3 | Research/exploratory | 24 hours | 24 hours | Ad-hoc analysis |
