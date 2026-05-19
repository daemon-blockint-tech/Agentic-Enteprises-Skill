# Governance Operations

## Data Stewardship Models

### Centralized Stewardship
- One team owns all metadata and quality
- Best for: Small orgs, strong governance need
- Risk: Bottleneck, limited domain expertise

### Federated Stewardship
- Domain owners are stewards for their data
- Central team sets standards and tooling
- Best for: Data mesh, large enterprises
- Risk: Inconsistent quality across domains

### Hybrid Stewardship
- Central stewards for shared/reference data
- Domain stewards for domain-specific data
- Best for: Most medium-to-large orgs

## Metadata Management

### Required Metadata Fields

| Field | Purpose | Example |
|---|---|---|
| Owner | Who is responsible | `data-team@company.com` |
| Description | What is this data | `Customer orders from Shopify` |
| Update frequency | How often refreshed | `Hourly` |
| Source system | Origin | `shopify_orders` |
| PII classification | Sensitivity | `Contains email, phone` |
| Retention period | How long kept | `7 years` |
| Quality SLA | Expected accuracy | `99.5%` |
| Downstream consumers | Who depends on this | `revenue_dashboard`, `rfm_model` |

### Catalog Enrichment Workflow

1. Auto-ingest technical metadata (schemas, types, stats)
2. Assign owners (auto-detect from query patterns or manual)
3. Tag with business glossary terms
4. Document descriptions and use cases
5. Validate completeness quarterly

## Access Review Process

### Quarterly Access Review

**Step-by-step:**
1. Export current access matrix (roles, users, tables)
2. Notify owners: "Review access by [date]"
3. Owners confirm or revoke per user
4. Security team audits high-risk access (PII, admin)
5. Apply changes and log in audit trail
6. Report completion to compliance

**Access review template:**

| User | Role | Resources | Last access | Owner decision | Action |
|---|---|---|---|---|---|
| alice@co.com | Analyst | `f_orders`, `d_customer` | 2 days ago | Retain | None |
| bob@co.com | Ex-employee | `f_orders` | 90 days ago | Revoke | Remove access |

## Data Lifecycle Management

### Lifecycle Stages

| Stage | Criteria | Action | Owner |
|---|---|---|---|
| Active | Accessed within 30 days | Keep in hot storage | Auto |
| Warm | Accessed 30-90 days ago | Move to warm tier | Operations |
| Cold | Accessed 90-365 days ago | Compress, move to cold | Operations |
| Archive | >1 year, compliance required | Glacier/deep archive | Operations |
| Delete | Retention expired + no legal hold | Secure deletion | Governance |

### Retention Policy Enforcement

**Automation rules:**
- Partitioned tables: Drop partitions older than retention
- Object storage: Lifecycle policies (S3/GCS)
- Logs: Aggregate then delete raw after 90 days
- PII: Anonymize after consent withdrawal or expiration

**Legal hold override:**
- Legal team can flag datasets for indefinite retention
- Hold metadata stored in catalog
- Notify operations before any deletion

## Governance Committee

### Charter Template

**Purpose:** Oversight of data policies, standards, and issue resolution

**Members:**
- Chair: CDO or VP Data
- Members: Data engineering lead, analytics lead, legal, security, business domain reps
- Observer: Compliance officer

**Meeting cadence:** Monthly
**Quorum:** 50% of voting members

### Agenda Template

```
1. Action items from last meeting (5 min)
2. Policy proposals (20 min)
   - New data classification scheme
   - Access policy update
3. Quality scorecard review (15 min)
   - Trending issues
   - Remediation status
4. Incident review (15 min)
   - Recent data breaches/quality failures
5. New business (5 min)
```

## Policy Documentation

### Required Policies

| Policy | Content | Review Frequency |
|---|---|---|
| Data classification | Public, internal, confidential, restricted | Annual |
| Access control | RBAC, approval workflows, recertification | Annual |
| Data retention | Per data class, legal requirements | Annual |
| Data quality | SLA definitions, measurement, escalation | Quarterly |
| Incident response | Severity, notification, remediation | Annual |
| Vendor data sharing | DPA requirements, approved vendors | Annual |

**Policy template structure:**
```markdown
# [Policy Name]

## Purpose
Why this policy exists

## Scope
Who and what it applies to

## Policy Statement
The rule

## Roles & Responsibilities
Who does what

## Enforcement
Consequences of violation

## Exceptions
How to request exceptions

## Review
When and how policy is reviewed
```
