---
name: data-center-compute-supply-efficiency
description: |
  Guides data center compute supply and resource efficiency—capacity and utilization planning,
  kW-per-useful-compute metrics, stranded power and rack space, hardware refresh and decommission,
  power-aware placement, consolidation and right-sizing of physical hosts, GPU/CPU supply
  alignment with workload demand, and sustainability reporting (PUE, carbon intensity).
  Use when optimizing on-prem or colo compute footprint, forecasting server/GPU supply,
  reducing idle capacity, improving DC utilization, or balancing efficiency vs performance SLAs—not
  for greenfield facility design (data-center-design-execution-lead), K8s deploy/troubleshoot
  (cluster-deployment-engineer), cloud-only FinOps (infrastructure-engineer scope varies), or
  LLM token cost programs (ai-token-improvement-plan-engineer), or multi-site investment
  prioritization and steering (data-center-portfolio-planning-execution-lead), or MW/rack
  construction delivery (senior-data-center-capacity-delivery-manager). Compute accounting:
  compute-accounting-manager.
---

# Data Center Engineer — Resource Efficiency (Compute Supply)

## When to Use

- Measure and improve utilization of racks, kW, and compute (CPU/GPU/memory)
- Forecast compute supply: how many nodes/GPUs needed by quarter
- Find stranded capacity (power allocated but unused, empty U, low CPU%)
- Plan hardware refresh, standard builds, and end-of-life decommission
- Consolidate workloads to free racks or defer capex
- Set power caps and placement rules for efficiency without breaching SLAs
- Report efficiency KPIs to finance, sustainability, and engineering leadership
- Compare efficiency of keeping workloads on-prem vs shifting burst to cloud

## When NOT to Use

- New hall design, MEP, commissioning → `data-center-design-execution-lead`
- Helm, cluster upgrades, pod debug → `cluster-deployment-engineer`
- VPC, Terraform, managed cloud architecture → `infrastructure-engineer`
- AI inference token/cost roadmap → `ai-token-improvement-plan-engineer`
- AI production ops cadence → `ai-lead-ops`
- Multi-vendor DC construction program → `technical-program-manager`
- Multi-site DC roadmap and capex prioritization → `data-center-portfolio-planning-execution-lead`

## Related skills

| Need | Skill |
|---|---|
| Facility design and build | `data-center-design-execution-lead` |
| K8s scheduling and workloads on clusters | `cluster-deployment-engineer` |
| Hybrid cloud and virtualization | `infrastructure-engineer` |
| Large efficiency program coordination | `technical-program-manager` |
| Enterprise DC portfolio and steering | `data-center-portfolio-planning-execution-lead` |
| Rack-ready / MW delivery execution | `senior-data-center-capacity-delivery-manager` |
| On-site install, asset/serial capture | `field-services-engineer` |
| Executive/sustainability messaging | `communication-lead` |
| Compliance evidence for facilities | `compliance-engineer` |
| Compute capex, depreciation, cloud GL | `compute-accounting-manager` |

## Core Workflows

### 1. Baseline efficiency metrics

Establish dashboards for:

- **Facility:** PUE, total IT kW, cooling kW
- **Supply:** rack count, kW committed vs kW used, GPU/CPU inventory
- **Demand:** avg/peak utilization, useful work per kW (define numerator per org)
- **Waste:** idle hosts, powered empty U, oversubscribed cooling margin

**See `references/efficiency_metrics.md`.**

### 2. Compute supply planning

1. **Demand** — workload growth, new products, GPU training vs inference mix
2. **Supply** — on-hand, on-order, lead times, standard SKUs
3. **Gap** — quarter-by-quarter surplus or deficit
4. **Actions** — buy, refresh, cloud burst, or defer

**See `references/compute_capacity_supply.md`.**

### 3. Utilization and consolidation

- Inventory hosts below utilization threshold for 30+ days
- Plan migration windows; validate performance tests post-move
- Target: raise average utilization without violating HA or latency SLOs
- Virtualization or K8s density changes → coordinate with `cluster-deployment-engineer`

**See `references/utilization_optimization.md`.**

### 4. Power and thermal efficiency

- Align rack kW nameplate with actual draw; recover stranded breaker capacity
- Power capping policies (OS/firmware/IPMI) where SLA allows
- Match GPU trays to cooling class (air vs liquid)

**See `references/power_thermal_management.md`.**

### 5. Hardware lifecycle

| Stage | Efficiency focus |
|---|---|
| Standardize | Few SKUs → spare pool efficiency |
| Deploy | Fill racks to target kW; avoid one-off configs |
| Operate | Monitor age, warranty, power draw drift |
| Refresh | TCO: new gen perf per watt vs extend |
| Decommission | Power down, wipe, reclaim U and kW |

**See `references/hardware_lifecycle.md`.**

### 6. Reporting and targets

- Monthly: utilization, PUE trend, supply vs demand
- Quarterly: refresh plan, capex avoidance from consolidation
- Tie narratives to sustainability goals without greenwashing

**See `references/reporting_targets.md`.**

## Output standards

- Supply/demand table by quarter (nodes, kW, GPUs)
- Top 10 stranded assets with recommended action and risk
- Efficiency initiative backlog with estimated kW or capex saved
- Assumptions explicit (utilization window, SLA exclusions)

## When to load references

- **KPIs and formulas** → `references/efficiency_metrics.md`
- **Forecast and procurement** → `references/compute_capacity_supply.md`
- **Consolidation and right-size** → `references/utilization_optimization.md`
- **Power caps and cooling fit** → `references/power_thermal_management.md`
- **Refresh and decomm** → `references/hardware_lifecycle.md`
- **Dashboards and targets** → `references/reporting_targets.md`
