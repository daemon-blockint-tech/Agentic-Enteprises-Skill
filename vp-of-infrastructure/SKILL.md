---
name: vp-of-infrastructure
description: |
  Guides VP-level infrastructure leadership—org strategy and operating model, multi-year cloud,
  data center, and platform portfolio, capex and opex governance, org-wide reliability and security
  posture, hyperscaler/colo/vendor and enterprise agreement strategy, build-vs-buy and multi-year
  roadmaps, and board/CFO/CTO executive narratives.
  Use when setting infrastructure direction, designing infra org and decision rights, prioritizing
  portfolio investments, steering vendor or EA strategy, preparing executive or board updates, or
  adjudicating cross-functional trade-offs—not for Terraform/K8s implementation (infrastructure-engineer),
  cloud program leadership—migration portfolio, CCoE, EA at cloud scope (vp-of-cloud),
  landing zone or CCoE design (enterprise-cloud-architect), SLI/SLO operations (site-reliability-engineer),
  monthly CUR FinOps (finops-analyst), TCO/NPV modeling (cloud-economist), or GL close/capex accounting
  policy (director-infrastructure-capex-accounting, compute-accounting-manager).
---

# VP of Infrastructure

## When to Use

- Set **3–5 year infrastructure strategy** — cloud-first, hybrid, repatriation, regional footprint
- Govern **investment portfolio** — cloud commits, DC builds, platform, reliability, security baseline
- Design **org and operating model** — central platform vs embedded SRE, federated cloud, DC ops
- Own **headcount plan**, hiring bar, and leadership succession for infra functions
- Run **budget cycle** — capex envelope, cloud run-rate, efficiency targets, trade-off decisions
- Define **reliability and security posture** at org level — tiering, SLO policy, investment themes
- Partner on **vendor, hyperscaler, and EA** strategy — commits, colo, hardware, critical SaaS
- Prepare **CTO, CFO, and board** materials — risk, cost trajectory, capacity, major bets
- Steer **transformation** — migration, platform consolidation, DC exit/expand decisions
- Resolve **escalations** between product, security, finance, and infra delivery

## When NOT to Use

- Terraform modules, VPC, K8s manifests → `infrastructure-engineer`, `cloud-engineer`
- Cloud program strategy, migration portfolio, CCoE charter, cloud SteerCo → `vp-of-cloud`
- Landing zones, CCoE standards, EA technical design → `enterprise-cloud-architect`, `cloud-architect`
- SLI/SLO implementation, PRRs, burn-rate alerts → `site-reliability-engineer`
- Access tickets, patching, restores → `cloud-system-administrator`
- Cloud control implementation and CSPM tuning → `cloud-security-engineer`
- CUR rightsizing, monthly FinOps dashboards → `finops-analyst`
- TCO/NPV models and commit economics → `cloud-economist`
- MW/rack delivery execution → `senior-data-center-capacity-delivery-manager`
- Rack utilization and GPU supply efficiency → `data-center-compute-supply-efficiency`
- Capex capitalization policy and audit steering → `director-infrastructure-capex-accounting`
- Month-end cloud GL and amortization → `compute-accounting-manager`
- Software program milestones and RAID → `technical-program-manager`
- Issue trees and generic operating model → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| VP cloud program (strategy, migration, EA, CCoE) | `vp-of-cloud` |
| Enterprise cloud governance and CCoE | `enterprise-cloud-architect` |
| Product/line cloud architecture | `cloud-architect` |
| Hands-on cloud, IaC, and platform build | `infrastructure-engineer`, `cloud-engineer` |
| SRE and SLO operations | `site-reliability-engineer` |
| Cloud day-2 operations | `cloud-system-administrator` |
| Cloud security architecture and controls | `cloud-security-engineer` |
| FinOps operations | `finops-analyst` |
| Cloud economics and business cases | `cloud-economist` |
| DC portfolio planning | `data-center-portfolio-planning-execution-lead` |
| DC capacity delivery | `senior-data-center-capacity-delivery-manager` |
| Compute utilization and refresh | `data-center-compute-supply-efficiency` |
| Infrastructure capex accounting | `director-infrastructure-capex-accounting` |
| Operational compute accounting | `compute-accounting-manager` |
| Cross-team program delivery | `technical-program-manager` |
| Security and compliance partnership | `information-security-engineer`, `cloud-compliance-specialist` |
| BCM/DRP posture, tier-0 recovery investment, exercise outcomes | `bcm-disaster-recovery-specialist` |
| Executive messaging | `communication-lead` |

## Core Workflows

### 1. Scope and executive lens

Boundaries vs architects, operators, finance, and TPM.

**See `references/vp_infrastructure_scope.md`.**

### 2. Infrastructure portfolio strategy

Prioritize cloud, DC, platform, reliability, and transformation bets.

**See `references/infrastructure_portfolio_strategy.md`.**

### 3. Capex and OpEx governance

Envelope, targets, and trade-offs with finance.

**See `references/capex_opex_governance.md`.**

### 4. Reliability and security posture

Org-tiering, SLO policy, and investment themes with security partners.

**See `references/reliability_security_posture.md`.**

### 5. Vendor, EA, and supply

Hyperscaler, colo, hardware, and critical SaaS commercial strategy.

**See `references/vendor_ea_and_supply.md`.**

### 6. Executive infrastructure briefings

SteerCo, QBR, board packs, and investment asks.

**See `references/executive_infrastructure_briefings.md`.**

## Outputs

- **Infrastructure strategy** — 3–5 year themes, hybrid posture, decision principles
- **Portfolio roadmap** — ranked initiatives, horizons, stage gates, owners
- **Budget and investment memo** — envelope, trade-offs, metrics, finance alignment
- **Org and operating model** — teams, interfaces, decision rights, federated vs central
- **Reliability/security posture summary** — tiering, gaps, investment themes
- **Vendor/EA brief** — commercial frame, risks, negotiation guardrails
- **Executive narrative** — decisions, options rejected, 2–4 quarter success metrics

## Principles

- **Portfolio over projects** — fund outcomes and capacity, not every request
- **Explicit trade-offs** — reliability, cost, speed, and risk on one page
- **Delegate execution** — VP sets direction; specialists implement
- **One financial truth** — align with FinOps, FP&A, and accounting partners
- **Measure in quarters** — tie bets to leading indicators, not activity
