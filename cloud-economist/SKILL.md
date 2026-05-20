---
name: cloud-economist
description: |
  Guides cloud economics—TCO and NPV for cloud vs on-prem or SaaS, pricing-model trade-offs
  (on-demand, commitments, spot), commitment portfolio economics, marginal cost and elasticity,
  regional and service cost comparisons, migration and architecture option business cases, and
  CFO-ready economic narratives tied to growth drivers.
  Use when building cloud business cases, comparing architectural cost options, sizing EA or
  commit programs economically, modeling 3–5 year spend scenarios, or explaining margin impact
  of cloud choices—not for monthly bill optimization (finops-analyst), GL close (compute-accounting-manager),
  hands-on tagging/rightsizing (finops-analyst), technical reference architecture (cloud-architect),
  or general non-cloud strategy consulting (business-consultant).
---

# Cloud Economist

## When to Use

- Build **TCO/NPV** for cloud migration, repatriation, or hybrid
- Compare **economic options** — serverless vs containers vs VMs, managed vs self-run, regions
- Model **commitment portfolio** — coverage mix, term, break-even, flexibility value
- Analyze **marginal cost** of scale (next 10k users, new region, new product line)
- Quantify **elasticity** — cost at p50 vs p99 load; burst vs steady-state economics
- Prepare **EA or commit negotiation** inputs (volume curves, alternative structures)
- Run **sensitivity analysis** — usage growth, price changes, discount tiers, FX
- Link cloud spend to **gross margin** and unit economics for product/finance
- Evaluate **multi-cloud** cost of redundancy vs lock-in risk (economic framing)
- Support **cloud-architect** and **enterprise-cloud-architect** ADRs with cost models

## When NOT to Use

- CUR analysis, idle resource cleanup, monthly budgets → `finops-analyst`
- GL mapping, amortization, fixed assets → `compute-accounting-manager`
- VPC design, landing zones, migration waves (technical) → `cloud-architect`
- Org CCoE and EA program design → `enterprise-cloud-architect`
- Cloud program portfolio, migration funding, executive EA sign-off → `vp-of-cloud`
- Issue trees and operating model (non-cloud-specific) → `business-consultant`
- Rack/GPU supply TCO in data centers → `data-center-compute-supply-efficiency`
- Implement infra or purchase commits → `cloud-engineer`, `finops-analyst`
- Deal-level sizing, RFP cost framing, build-vs-buy for a customer → `solutions-architect`

## Related skills

| Need | Skill |
|---|---|
| VP cloud spend envelope and EA commercial frame | `vp-of-cloud` |
| Operational FinOps and dashboards | `finops-analyst` |
| Accounting and ledger | `compute-accounting-manager` |
| Cloud architecture and WAF cost pillar | `cloud-architect` |
| Enterprise EA and org FinOps | `enterprise-cloud-architect` |
| Strategy consulting (general) | `business-consultant` |
| Business model research | `business-model-researcher` |
| Data platform TCO | `data-architect` |
| AI/token cost programs | `ai-token-improvement-plan-engineer` |
| Supply chain hardware TCO | `supply-chain-manager` |
| Customer deal cost framing and option comparison | `solutions-architect` |

## Core Workflows

### 1. Scope and economic lens

Boundaries vs FinOps, architect, finance.

**See `references/cloud_economist_scope.md`.**

### 2. TCO and build vs buy

Cloud vs on-prem vs SaaS; NPV framework.

**See `references/tco_build_vs_buy.md`.**

### 3. Commitment portfolio economics

RI/SP/CUD/EA economic trade-offs.

**See `references/commitment_portfolio_economics.md`.**

### 4. Marginal cost and elasticity

Scale economics and demand shapes.

**See `references/marginal_cost_and_elasticity.md`.**

### 5. Scenario and sensitivity modeling

What-if and risk ranges.

**See `references/scenario_sensitivity_modeling.md`.**

### 6. Executive economic briefings

CFO and board narratives.

**See `references/executive_economic_briefings.md`.**

## Outputs

- **Economic model** — assumptions, 3–5 year cash flows, NPV/IRR where applicable
- **Option comparison table** — cost, flexibility, risk, break-even
- **Commitment recommendation memo** — coverage, term, $ at risk, exit cost
- **Sensitivity chart** — drivers ranked by impact on spend or margin
- **One-pager for ADR** — recommended option with economic rationale
- **Negotiation brief** — volume forecast, walk-away, alternative structures

## Principles

- **Explicit assumptions** — growth, utilization, discount, labor, egress
- **Compare options at equal SLO** — do not trade reliability without pricing risk
- **Time value matters** — NPV for multi-year commits and migrations
- **Flexibility has value** — price the option to scale down or pivot
- **Hand off execution** — economist models; `finops-analyst` operationalizes
