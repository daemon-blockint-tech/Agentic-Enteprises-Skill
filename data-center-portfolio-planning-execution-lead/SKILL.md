---
name: data-center-portfolio-planning-execution-lead
description: |
  Guides enterprise data center portfolio planning and execution—multi-site capacity roadmaps,
  investment prioritization (build, expand, refresh, exit, colo vs owned), portfolio RAID and
  dependency management across DC programs, stage-gate governance, capex/opex alignment, regional
  and resiliency strategy, and steering-committee reporting.
  Use when prioritizing several DC initiatives, harmonizing site plans over 3–5 years, tracking a
  portfolio of hall builds and refreshes, or aligning facilities/IT/finance on DC investments—not
  for a single hall MEP design (data-center-design-execution-lead), host-level utilization
  (data-center-compute-supply-efficiency), generic software programs (technical-program-manager),
  or cloud IaC (infrastructure-engineer). For executing approved MW/rack delivery on schedule,
  use senior-data-center-capacity-delivery-manager.
---

# Data Center Portfolio Planning & Execution Lead

## When to Use

- Build or refresh a **multi-site** data center capacity roadmap (3–5+ years)
- Prioritize competing DC investments under a fixed capex envelope
- Run **portfolio governance**: stage gates, RAID, dependencies between DC projects
- Align regional strategy (latency, sovereignty, DR, cloud burst)
- Consolidate business cases from site leads into one portfolio narrative
- Track execution across concurrent builds, expansions, refreshes, and exits
- Prepare steering or board-level DC portfolio status
- Decide build vs colo vs extend vs cloud at **portfolio** level

## When NOT to Use

- Single facility design, MEP, commissioning → `data-center-design-execution-lead`
- Server/GPU utilization, consolidation, refresh tactics → `data-center-compute-supply-efficiency`
- Multi-team **software** program (no DC portfolio) → `technical-program-manager`
- Corporate strategy, operating model, issue trees → `business-consultant`
- Terraform, VPC, K8s foundation → `infrastructure-engineer`
- K8s cluster operations → `cluster-deployment-engineer`
- Launch messaging only → `communication-lead`
- MW/rack delivery program and readiness gates → `senior-data-center-capacity-delivery-manager`

## Related skills

| Need | Skill |
|---|---|
| Infrastructure capex policy and capitalization | `director-infrastructure-capex-accounting` |
| One site design and build execution | `data-center-design-execution-lead` |
| Compute supply and efficiency | `data-center-compute-supply-efficiency` |
| Cross-functional software delivery program | `technical-program-manager` |
| Investment narrative and options | `business-consultant` |
| Hybrid cloud technical patterns | `infrastructure-engineer` |
| Compliance evidence for facilities | `compliance-engineer` |
| Executive updates | `communication-lead` |
| Capacity delivery execution | `senior-data-center-capacity-delivery-manager` |

## Core Workflows

### 1. Portfolio charter and scope

Define:

- **Sites in scope** — owned, colo, edge, planned
- **Horizon** — planning years and refresh cycles
- **Constraints** — capex ceiling, power at utility, sustainability targets
- **Decision rights** — steering, stage gates, who owns site DRIs

**See `references/portfolio_charter.md`.**

### 2. Capacity and demand rollup

1. Aggregate demand by region (kW, racks, GPUs) from engineering and product
2. Map to **supply** per site (committed, available, planned)
3. Expose **gaps** by quarter and region
4. Flag single points of failure (one site, one carrier, one cooling plant)

**See `references/capacity_roadmap.md`.**

### 3. Investment prioritization

Score initiatives: strategic fit, risk reduction, NPV/TCO, dependency unlock, time criticality.

Output: ranked backlog, **funded / deferred / kill**, and tradeoff narrative.

**See `references/investment_prioritization.md`.**

### 4. Execution governance

- **Stage gates** — concept → approved → execute → operate
- **Portfolio RAID** — risks that span sites (power, lead time, vendor)
- **Dependency map** — e.g. network build before hall acceptance
- Integrate site-level status from `data-center-design-execution-lead` DRIs

**See `references/execution_governance.md`.**

### 5. Hybrid and exit strategy

- Portfolio rules for cloud burst vs committed metal
- Site exit or consolidation when utilization and TCO favor move
- Contract and migration dependencies

**See `references/hybrid_exit_strategy.md`.**

### 6. Steering reporting

Monthly/quarterly: portfolio health (RAG), spend vs plan, milestone slip, top risks, decisions needed.

**See `references/steering_reporting.md`.**

## Output standards

- One-page portfolio summary + detailed initiative register
- Roadmap by region (kW/racks/GPUs) with assumptions stated
- Prioritization scorecard with explicit tradeoffs
- Decision log for steering (what was decided, what was deferred)
- No duplicate site engineering detail — link to site workstreams

## When to load references

- **Charter and roles** → `references/portfolio_charter.md`
- **Multi-site roadmap** → `references/capacity_roadmap.md`
- **Scoring and funding** → `references/investment_prioritization.md`
- **Gates, RAID, dependencies** → `references/execution_governance.md`
- **Cloud, colo, exit** → `references/hybrid_exit_strategy.md`
- **Steering pack** → `references/steering_reporting.md`
