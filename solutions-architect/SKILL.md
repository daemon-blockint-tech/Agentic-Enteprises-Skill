---
name: solutions-architect
description: |
  Guides customer-facing and internal technical solution design—discovery and requirements,
  integration and reference architecture, security/compliance fit, sizing and cost framing,
  RFP/RFI responses, PoC scoping, build-vs-buy, and handoff to delivery.
  Use when scoping a customer or partner solution, designing integration architecture for a
  deal, drafting RFP/RFI technical responses, planning a proof-of-concept, framing security
  and compliance fit, or preparing solution decks for stakeholders—not for org-wide landing
  zones and Well-Architected programs (cloud-architect, enterprise-cloud-architect), internal
  product ADRs and C4 (senior-system-architecture), production Terraform/IaC (infrastructure-engineer),
  hands-on cloud resource config (cloud-engineer), live PoC execution and competitive demos
  (sales-engineer), business strategy without technical design (business-consultant), contract
  redlines (commercial-counsel), or deep FinOps/GL (finops-analyst, compute-accounting-manager).
---

# Solutions Architect

## When to Use

- Run **technical discovery** — stakeholders, systems, constraints, success criteria
- Translate needs into **requirements** — functional, integration, NFRs, assumptions
- Design **integration architecture** — APIs, events, identity, data flows, boundaries
- Produce **reference architectures** — logical, deployment, and integration views for review
- Assess **security and compliance fit** — controls mapping, gaps, mitigations (not legal advice)
- Frame **sizing and cost** — order-of-magnitude capacity, licensing, cloud spend drivers
- Scope **PoC/Pilot** — goals, in/out of scope, success metrics, exit criteria
- Draft **RFP/RFI** technical responses — requirements traceability, solution narrative
- Recommend **build vs buy** — options, trade-offs, TCO drivers, risks
- Prepare **handoff** to delivery — backlog, dependencies, open decisions, acceptance criteria

## When NOT to Use

- Org landing zones, CCoE, enterprise EA programs → `enterprise-cloud-architect`
- Single-product internal ADRs, C4, engineering standards → `senior-system-architecture`
- Well-Architected cloud platform design (non-deal) → `cloud-architect`
- Production Terraform modules, CI/CD, K8s build → `infrastructure-engineer`, `devops`
- Configure RDS, IAM errors, autoscaling tuning → `cloud-engineer`
- Build and demo the PoC in customer environment → `sales-engineer`
- Issue trees, operating model, steerCo without technical design → `business-consultant`
- MSA/SaaS redlines and legal risk → `commercial-counsel`
- SOC 2 evidence packs and control narratives → `compliance-engineer`
- Implement cloud guardrails and CSPM → `cloud-security-engineer`
- Multi-year NPV/EA economics deep dive → `cloud-economist`
- Program RAID, milestones, steering cadence → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| Cloud platform and migration architecture | `cloud-architect` |
| Enterprise cloud governance at scale | `enterprise-cloud-architect` |
| Internal system ADRs and architecture review | `senior-system-architecture` |
| IaC modules and delivery implementation | `infrastructure-engineer` |
| Cloud service configuration and ops | `cloud-engineer` |
| Pre-sales PoC execution and battlecards | `sales-engineer` |
| Business case and strategy (non-technical) | `business-consultant` |
| Cloud security controls and architecture review | `cloud-security-engineer` |
| TCO/NPV and economic option modeling | `cloud-economist` |
| Multi-team delivery and launch readiness | `technical-program-manager` |
| FinOps dashboards and rightsizing | `finops-analyst` |

## Core Workflows

### 1. Scope and engagement framing

Role boundaries, inputs, outputs, stakeholders.

**See `references/solutions_architect_scope.md`.**

### 2. Discovery and requirements

Interviews, current state, requirements pack, assumptions.

**See `references/discovery_and_requirements.md`.**

### 3. Integration and reference architecture

Context, integration patterns, reference diagrams, interfaces.

**See `references/integration_and_reference_architecture.md`.**

### 4. Security and compliance fit

Threat framing, control mapping, gaps, customer questionnaires.

**See `references/security_compliance_fit.md`.**

### 5. Sizing, cost, and options

Capacity, cost drivers, build-vs-buy, option comparison.

**See `references/sizing_cost_and_options.md`.**

### 6. RFP, PoC, and handoff

RFP structure, PoC charter, delivery handoff package.

**See `references/rfp_poc_and_handoff.md`.**

## Outputs

- **Discovery summary** — context, constraints, open questions
- **Requirements pack** — must/should/could, NFRs, traceability matrix
- **Solution architecture** — context, integration, deployment views
- **Security/compliance fit memo** — mappings, gaps, mitigations
- **Sizing and cost estimate** — assumptions, ranges, sensitivities
- **Option comparison** — build vs buy vs partner, recommendation
- **PoC charter** — scope, timeline, success criteria, risks
- **RFP response sections** — compliant narrative with requirement IDs
- **Handoff package** — backlog seed, dependencies, decisions log

## Principles

- **Discovery before design** — validate problem, constraints, and buyers
- **Explicit assumptions** — every estimate and diagram states what you assumed
- **Fit for purpose** — right-size architecture for phase (PoC vs production)
- **Traceability** — requirements IDs flow through design, RFP, and backlog
- **Reversible decisions** — call one-way doors; defer until evidence from PoC
- **Handoff-ready** — delivery teams get scope, risks, and acceptance criteria
