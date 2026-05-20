---
name: finops-analyst
description: |
  Guides FinOps analysis on AWS, GCP, and Azure—cost visibility and allocation, tagging and
  showback/chargeback models, rightsizing and waste removal, RI/Savings Plan/CUD recommendations,
  budgets and forecasts, anomaly detection, unit economics (cost per service/customer), and
  FinOps cadence with engineering accountability.
  Use when optimizing cloud spend, analyzing CUR/billing exports, building cost dashboards,
  explaining bill spikes, or improving allocation—not for GL mapping, capex, depreciation, or
  month-end ledger close (compute-accounting-manager), enterprise EA negotiation (enterprise-cloud-architect),
  hands-on resource provisioning (cloud-engineer), or hardware supply efficiency (data-center-compute-supply-efficiency).
---

# FinOps Analyst

## When to Use

- Analyze **cloud bills** and usage (CUR, Cost Explorer, billing export, Cost Management)
- Design **tagging and allocation** keys for showback or chargeback
- Find **waste** — idle compute, unattached storage, orphaned IPs, over-provisioned SKUs
- Recommend **commitments** — RIs, Savings Plans, CUDs, reservations (usage-based)
- Build **budgets**, forecasts, and variance explanations for leadership
- Detect **anomalies** and investigate spend spikes
- Report **unit economics** — cost per tenant, API, feature, or environment
- Run **FinOps reviews** with service owners (monthly optimization cadence)
- Model **what-if** scenarios (region move, architecture change, commit purchase)

## When NOT to Use

- Map cloud spend to GL, amortize prepaids, fixed assets → `compute-accounting-manager`
- Enterprise agreement strategy and org-wide CCoE FinOps program → `enterprise-cloud-architect`
- Provision VPC, fix IAM, implement infra → `cloud-engineer`
- Execute access tickets and patch windows → `cloud-system-administrator`
- Rack/GPU utilization and stranded kW → `data-center-compute-supply-efficiency`
- Capex policy and board asset governance → `director-infrastructure-capex-accounting`
- Generic BI without cloud cost domain → `bi-analyst`
- SOC 2 cloud evidence → `cloud-compliance-specialist`
- TCO/NPV business cases, commit portfolio economics, CFO scenarios → `cloud-economist`
- Cloud program strategy, migration portfolio, EA sign-off → `vp-of-cloud`
- Infrastructure org strategy, portfolio budget, board narratives → `vp-of-infrastructure`

## Related skills

| Need | Skill |
|---|---|
| VP cloud envelope and executive FinOps accountability | `vp-of-cloud` |
| TCO, NPV, migration and commit business cases | `cloud-economist` |
| Ledger, capex/OpEx, month-end close | `compute-accounting-manager` |
| Enterprise EA and org chargeback model | `enterprise-cloud-architect` |
| Tag enforcement and cost runbooks in ops | `cloud-engineer` |
| Hygiene execution (delete idle resources) | `cloud-system-administrator` |
| K8s cluster cost and rightsizing | `cluster-deployment-engineer` |
| LLM/token cost programs | `ai-token-improvement-plan-engineer` |
| AI ops cost and capacity | `ai-lead-ops` |
| Well-Architected cost pillar at design | `cloud-architect` |
| Business requirements for finance tools | `business-analyst` |
| VP infrastructure leadership | `vp-of-infrastructure` |

## Core Workflows

### 1. Scope and FinOps principles

Inform, optimize, operate; boundaries with accounting.

**See `references/finops_scope_and_principles.md`.**

### 2. Cost visibility and allocation

Tags, CUR, dashboards, allocation rules.

**See `references/cost_visibility_allocation.md`.**

### 3. Optimization and rightsizing

Waste, SKUs, commitments, engineering tickets.

**See `references/optimization_rightsizing.md`.**

### 4. Budgeting and forecasting

Budgets, forecasts, anomalies.

**See `references/budgeting_forecasting.md`.**

### 5. Unit economics and reporting

Cost per unit, executive narratives.

**See `references/unit_economics_reporting.md`.**

### 6. FinOps governance

Policies, RACI, review cadence.

**See `references/finops_governance.md`.**

## Outputs

- **Cost breakdown** — by account, service, tag, trend vs prior period
- **Optimization backlog** — savings estimate, owner, risk, effort
- **Commitment recommendation** — coverage %, term, break-even, risk
- **Allocation model** — keys, untagged %, disputed splits
- **Forecast** — baseline, growth drivers, confidence range
- **Anomaly report** — root cause, one-time vs recurring

## Principles

- **Everyone owns their spend** — FinOps enables; engineering decides trade-offs
- **Unit economics over totals** — tie cost to business drivers
- **Measure then commit** — stabilize usage before multi-year RIs
- **Same tags as finance** — align with `compute-accounting-manager` keys where possible
- **Fast feedback** — weekly visibility beats quarterly surprises
