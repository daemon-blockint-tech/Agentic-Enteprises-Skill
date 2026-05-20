---
name: cloud-architect
description: |
  Guides cloud solution architecture—Well-Architected alignment, landing zone and org design,
  workload placement and service selection, network and security segmentation, hybrid and
  multi-region patterns, migration roadmaps (7Rs), cost architecture, and cloud ADRs with
  diagrams for stakeholder review.
  Use when choosing cloud platforms and reference architectures, designing account guardrails,
  comparing managed vs self-managed services, planning cloud migration or exit, or running
  cloud architecture review—not for hands-on resource configuration (cloud-engineer), Terraform
  module implementation (infrastructure-engineer), CI/CD delivery (devops), K8s cluster ops
  (cluster-deployment-engineer), IDP product strategy (platform-engineer), enterprise-wide
  non-cloud system ADRs (senior-system-architecture), or applied AI solution design
  (applied-ai-architect-commercial-enterprise).
---

# Cloud Architect

## When to Use

- Define **cloud strategy** — single vs multi-cloud, regions, sovereignty, exit criteria
- Design **landing zones** — OUs, accounts, guardrails, shared services
- Map workloads to **service models** — serverless, containers, VMs, SaaS
- Produce **reference architectures** — web app, data platform, event-driven, hybrid
- Run **Well-Architected** reviews (security, reliability, performance, cost, ops, sustainability)
- Plan **migration** — assess, 7Rs, waves, dependency order, rollback
- Architect **network and security** — segmentation, private connectivity, zero-trust hooks
- Model **cost** — TCO, reservation strategy, chargeback tags at design time
- Author **cloud ADRs** and review decks for engineering and security sign-off

## When NOT to Use

- Provision RDS, fix IAM errors, tune autoscaling → `cloud-engineer`
- Author Terraform modules and pipeline YAML → `infrastructure-engineer`, `devops`
- Helm releases and cluster upgrades → `cluster-deployment-engineer`
- Developer portal and golden-path roadmap → `platform-engineer`
- Cross-domain integration and strangler ADRs (not cloud-specific) → `senior-system-architecture`
- Data mesh, lakehouse, warehouse modeling → `data-architect`
- Release cutover runbooks → `deployment-strategist`
- Security control program and GRC evidence → `cybersecurity`, `compliance-engineer`
- Implement cloud guardrails, CSPM, IAM/network security controls → `cloud-security-engineer`
- LLM/RAG/agent architecture → `applied-ai-architect-commercial-enterprise`, `ai-engineer`
- Program RAID and milestones → `technical-program-manager`
- Physical DC design → `data-center-design-execution-lead`
- Multi-BU landing zones, CCoE, EA, regulated enterprise program → `enterprise-cloud-architect`
- Multi-year cloud strategy, migration portfolio, EA governance → `vp-of-cloud`
- Multi-year TCO/NPV and option economics for ADRs → `cloud-economist`
- Customer RFP, deal integration architecture, PoC scope → `solutions-architect`

## Related skills

| Need | Skill |
|---|---|
| VP cloud program and migration portfolio | `vp-of-cloud` |
| Enterprise-scale cloud governance | `enterprise-cloud-architect` |
| Implement cloud resources | `cloud-engineer` |
| IaC modules and delivery patterns | `infrastructure-engineer` |
| CI/CD and GitOps | `devops` |
| Kubernetes platform operations | `cluster-deployment-engineer` |
| Internal developer platform | `platform-engineer` |
| Enterprise system architecture | `senior-system-architecture` |
| Data platform architecture | `data-architect` |
| Cloud security guardrails and posture | `cloud-security-engineer` |
| Corporate security program and tooling | `information-security-engineer` |
| Cloud TCO and option economics | `cloud-economist` |
| FinOps accounting | `compute-accounting-manager` |
| Hybrid / DC connectivity | `data-center-design-execution-lead` |
| AI workload on cloud | `applied-ai-architect-commercial-enterprise` |
| Customer deal solution and RFP technical design | `solutions-architect` |

## Core Workflows

### 1. Architecture principles and NFRs

Pillars, constraints, quality attributes.

**See `references/cloud_architecture_principles.md`.**

### 2. Landing zone and organization

Accounts, guardrails, shared services.

**See `references/landing_zone_org_design.md`.**

### 3. Workload placement and services

Compute model and vendor selection.

**See `references/workload_placement_service_selection.md`.**

### 4. Network and security architecture

Segmentation, connectivity, controls.

**See `references/network_security_architecture.md`.**

### 5. Migration and hybrid

Roadmaps, hybrid patterns, exit.

**See `references/migration_and_hybrid.md`.**

### 6. Deliverables and review

Diagrams, ADRs, review checklist.

**See `references/architecture_deliverables.md`.**

## Outputs

- **Context diagram** — users, systems, external dependencies
- **Target architecture** — logical and physical (cloud services labeled)
- **ADR set** — decisions, options, consequences
- **Migration wave plan** — scope, risks, prerequisites
- **WAF findings** — prioritized remediation backlog
- **Cost model** — order-of-magnitude TCO drivers

## Principles

- **Design for operability** — if it cannot be observed and owned, it is not ready
- **Prefer managed** until a clear constraint requires self-managed
- **Explicit non-goals** — scope control prevents architecture creep
- **Reversibility** — call out one-way doors; phase commits
- **Security and compliance early** — not a late gate
