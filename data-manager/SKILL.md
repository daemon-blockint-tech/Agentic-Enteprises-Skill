---
name: data-manager
description: |
  Guides data management across program/product management, governance operations, and data operations/reliability.
  Covers data roadmaps, stakeholder coordination, metadata stewardship, lifecycle management, monitoring,
  incident response, capacity planning, and SLA frameworks.
  Use when managing data teams, defining data product roadmaps, running governance programs,
  handling data incidents, or establishing operational cadences for data infrastructure.
---

# Data Manager

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

**See `references/program_management.md` for roadmap templates, stakeholder matrices, and prioritization frameworks.**

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

**See `references/governance_operations.md` for stewardship models, access review templates, and lifecycle policies.**

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

**See `references/data_operations.md` for runbooks, backup strategies, and capacity planning.**

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

**See `references/metrics_framework.md` for SLA templates, scorecard examples, and team productivity metrics.**

## When to Load References

- **Program management** → `references/program_management.md`
- **Governance operations** → `references/governance_operations.md`
- **Data operations** → `references/data_operations.md`
- **Metrics & SLAs** → `references/metrics_framework.md`
