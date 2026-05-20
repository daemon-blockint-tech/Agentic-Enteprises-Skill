---
name: senior-system-architecture
description: |
  Guides senior system and solution architecture—cross-service boundaries, integration patterns,
  non-functional requirements (scale, reliability, security, cost), ADRs, C4-style modeling,
  architecture review, build-vs-buy, and phased migration (strangler, dual-write).
  Use when designing multi-service systems, evaluating platform or vendor choices, writing or
  reviewing architecture decision records, defining standards and principles, or assessing
  technical risk across domains—not for single-service RFCs and module design
  (senior-software-engineer), data platform or mesh decisions (data-architect), cloud landing zone,
  Well-Architected, and migration architecture (cloud-architect), cloud/IaC implementation
  (infrastructure-engineer, cloud-engineer), internal developer platform product (platform-engineer),
  or program tracking (technical-program-manager). For business strategy and cases, use
  business-consultant; for applied AI (RAG, agents, copilots), use applied-ai-architect-commercial-enterprise.
---

# Senior System Architecture

## When to Use

- Define or review cross-service/system boundaries and contracts
- Compare architectural options with explicit trade-offs and NFR impact
- Author or review ADRs for decisions that are hard to reverse
- Run architecture review before major launches or vendor commitments
- Plan migration off legacy systems (strangler, parallel run, cutover)
- Establish architecture principles, standards, and exception process

## When NOT to Use

- Single-team service RFC and implementation slices → `senior-software-engineer`
- Lakehouse, mesh, or enterprise data modeling → `data-architect`
- VPC, Kubernetes, Terraform, or CI/CD build → `infrastructure-engineer`, `devops`
- IDP, golden paths, Backstage → `platform-engineer`
- Milestones, RAID, steering status → `technical-program-manager`
- Release cutover tactics only → `deployment-strategist`
- Security control catalog and enterprise GRC → `cybersecurity`
- LLM/RAG system design → `ai-engineer`
- Business strategy, issue trees, steerCo cases → `business-consultant`
- Applied AI / LLM solution architecture → `applied-ai-architect-commercial-enterprise`
- Customer-facing solution design, RFP/RFI, PoC scope, deal integration → `solutions-architect`

## Related skills

| Need | Skill |
|---|---|
| Service-level RFC and code review | `senior-software-engineer` |
| Data domain and governance architecture | `data-architect` |
| Cloud solution and migration architecture | `cloud-architect` |
| Enterprise cloud governance and landing zones | `enterprise-cloud-architect` |
| Cloud/network/IaC delivery | `infrastructure-engineer`, `cloud-engineer` |
| Platform-as-product and golden paths | `platform-engineer` |
| Multi-team launch coordination | `technical-program-manager` |
| Rollout and rollback planning | `deployment-strategist` |
| Security architecture and controls | `cybersecurity`, `information-security-engineer` |
| Requirements and business constraints | `business-analyst` |
| Strategy, business case, operating model | `business-consultant` |
| AI/LLM solution patterns | `ai-engineer` |
| Commercial/enterprise applied AI architecture | `applied-ai-architect-commercial-enterprise` |
| Customer deal solution, RFP, PoC handoff | `solutions-architect` |

## Core Workflows

### 1. Frame the decision

Capture before drawing boxes:

- Business outcome and measurable success criteria
- Constraints: budget, timeline, compliance, existing estate
- Non-goals (explicit scope cuts)
- Stakeholders and decision owner
- Reversibility: one-way door vs two-way door

**One-way doors** require ADR + architecture review. **Two-way doors** can stay in team RFC.

### 2. Model the system (C4-lite)

Minimum views for reviewers:

1. **Context** — actors, external systems, trust zones
2. **Containers** — deployable units, data stores, queues, who owns each
3. **Critical path** — sequence diagram for highest-risk flows only

Label every arrow: sync/async, protocol, auth model, and failure behavior.

**See `references/integration_patterns.md`.**

### 3. Define NFRs and quality attributes

For each capability, specify targets (not vague "high availability"):

| Attribute | Example target | Verification |
|---|---|---|
| Availability | 99.9% monthly | SLO, error budget |
| Latency | p99 < 300ms read | Load test + prod SLO |
| Throughput | 5k RPS peak | Capacity model |
| Durability | RPO 1h, RTO 4h | DR drill |
| Security | mTLS east-west, OIDC | Threat model link |
| Cost | <$X / 1M requests | FinOps estimate |

**See `references/nfr_quality_attributes.md`.**

### 4. Evaluate options

Present at least two viable options plus "do nothing / minimal change":

| Criterion | Weight | Option A | Option B |
|---|---|---|---|
| Time to value | | | |
| Operational burden | | | |
| Scalability headroom | | | |
| Team skill fit | | | |
| Vendor lock-in | | | |
| Security/compliance fit | | | |

Recommend one; document rejected options and why.

**See `references/adr_template.md`.**

### 5. Architecture review

Before build or contract signature:

1. Problem and constraints restated in one paragraph
2. Diagrams current; contracts versioned (OpenAPI, event schema)
3. Failure modes: partial outage, dependency down, poison messages
4. Data: ownership, retention, PII, migration path
5. Observability: golden signals per container
6. Security: authz boundaries, secrets, blast radius
7. Rollout and rollback linked to `deployment-strategist` if multi-phase

**See `references/architecture_review.md`.**

### 6. Evolution and migration

For legacy replacement:

1. Identify **capability slices** that can move independently
2. Prefer **strangler** over big-bang when risk is high
3. Define **parity criteria** before cutover
4. Plan **dual-write / dual-read** duration and reconciliation
5. Deprecate old path with telemetry proving zero traffic

**See `references/migration_evolution.md`.**

## When to load references

- **ADR format and bar** → `references/adr_template.md`
- **Review checklist** → `references/architecture_review.md`
- **Sync, events, sagas, APIs** → `references/integration_patterns.md`
- **SLOs, capacity, DR, cost** → `references/nfr_quality_attributes.md`
- **Strangler and cutover** → `references/migration_evolution.md`
