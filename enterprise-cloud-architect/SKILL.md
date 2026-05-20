---
name: enterprise-cloud-architect
description: |
  Guides enterprise-scale cloud architecture—multi-BU landing zones and federation, cloud Center
  of Excellence governance, enterprise agreement and commit strategy, org-wide FinOps and
  chargeback, regulated-workload patterns (residency, segmentation), hybrid integration with
  identity and ERP, and architecture review board standards for large organizations.
  Use when designing cloud at hundreds of accounts, steering CCoE policy, EA/MACC optimization,
  sovereign or regulated cloud placement, or executive cloud governance—not for single-product
  cloud designs (cloud-architect), hands-on service config (cloud-engineer), SOC 2 evidence
  automation (compliance-engineer), general cross-domain ADRs (senior-system-architecture), or
  enterprise AI copilot architecture (applied-ai-architect-commercial-enterprise), or VP-level
  cloud program portfolio and board narratives (vp-of-cloud).
---

# Enterprise Cloud Architect

## When to Use

- Design **multi-BU landing zone** programs — OUs, account vending, inherited guardrails
- Stand up or refresh **Cloud Center of Excellence** — standards, ARB, exception process
- Plan **enterprise agreement** strategy — commits, true-ups, multi-year cloud economics
- Define **org-wide FinOps** — allocation, showback/chargeback, EA utilization
- Place **regulated workloads** — residency, encryption, logging, isolation patterns
- Architect **hybrid at scale** — identity federation, DC portfolio, carrier diversity
- Harmonize **multi-cloud** posture — primary vs secondary, exit and portability
- Prepare **steering and board** materials — risk, cost, migration portfolio
- Publish **enterprise reference architectures** and mandatory controls catalog

## When NOT to Use

- Single application or single-account target architecture → `cloud-architect`
- Configure RDS, IAM errors, autoscaling tuning → `cloud-engineer`
- Terraform module factory → `infrastructure-engineer`
- CI/CD and GitOps delivery → `devops`
- SOC 2 / ISO control evidence packs → `compliance-engineer`
- Cloud-specific attestations, residency proof, CSPM evidence → `cloud-compliance-specialist`
- IdP/KMS/SIEM program ownership → `information-security-engineer`
- IAM entitlement design, access reviews, federation, SoD → `iam-specialist`
- Non-cloud integration ADRs → `senior-system-architecture`
- DC facility design → `data-center-design-execution-lead`
- Multi-site DC capex portfolio → `data-center-portfolio-planning-execution-lead`
- LLM/RAG enterprise copilot design → `applied-ai-architect-commercial-enterprise`
- Strategy issue trees without cloud delivery → `business-consultant`
- Program RAID for mixed software programs → `technical-program-manager`
- Infrastructure org strategy, capex envelope, executive narratives → `vp-of-infrastructure`
- Cloud program strategy, migration portfolio funding, cloud SteerCo → `vp-of-cloud`
- Customer RFP, partner solution design, PoC scoping → `solutions-architect`

## Related skills

| Need | Skill |
|---|---|
| VP cloud program and executive cloud narrative | `vp-of-cloud` |
| Product/line-of-business cloud design | `cloud-architect` |
| Cloud resource implementation | `cloud-engineer` |
| IaC modules and pipelines | `infrastructure-engineer`, `devops` |
| Enterprise system architecture | `senior-system-architecture` |
| Compliance evidence | `compliance-engineer` |
| Cloud framework evidence and assessor packages | `cloud-compliance-specialist` |
| Security architecture | `information-security-engineer`, `cybersecurity` |
| Identity governance, federation, PAM, cloud IAM standards | `iam-specialist` |
| DC portfolio and hybrid capacity | `data-center-portfolio-planning-execution-lead` |
| FinOps analysis and optimization | `finops-analyst` |
| EA/commit economic modeling and NPV | `cloud-economist` |
| Compute accounting and invoices | `compute-accounting-manager` |
| Customer deal solution and RFP technical design | `solutions-architect` |
| Enterprise AI on cloud | `applied-ai-architect-commercial-enterprise` |
| AI governance | `ai-risk-governance` |
| Large transformation program | `technical-program-manager` |
| VP infrastructure leadership | `vp-of-infrastructure` |

## Core Workflows

### 1. Enterprise governance and CCoE

Standards, ARB, federation model.

**See `references/enterprise_cloud_governance.md`.**

### 2. Landing zone at scale

Multi-account hierarchy and vending.

**See `references/landing_zone_at_scale.md`.**

### 3. Enterprise agreements and FinOps

EA, commits, allocation.

**See `references/enterprise_agreements_finops.md`.**

### 4. Regulated enterprise patterns

Residency, controls, isolation.

**See `references/regulated_enterprise_patterns.md`.**

### 5. Hybrid and enterprise integration

Identity, ERP, DC linkage.

**See `references/hybrid_enterprise_integration.md`.**

### 6. Executive deliverables

Steering packs, standards catalog.

**See `references/enterprise_architecture_deliverables.md`.**

## Outputs

- **Enterprise cloud strategy** — principles, scope, multi-year themes
- **Landing zone blueprint** — OU map, guardrails, shared services
- **Standards catalog** — mandatory, recommended, deprecated patterns
- **ARB decision log** — exceptions with expiry and owners
- **FinOps model** — allocation keys, EA coverage plan
- **Migration portfolio** — waves, dependencies, risk tier

## Principles

- **Federation over central bottlenecks** — standards with self-service account vending
- **Policy as code** — guardrails enforced; exceptions time-boxed
- **One financial truth** — billing, tags, and GL alignment with finance
- **Regulatory fit by design** — not retrofit after launch
- **Prefer cloud-architect** for team-level designs inside the enterprise frame
