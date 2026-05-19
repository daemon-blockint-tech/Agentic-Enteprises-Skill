---
name: senior-data-center-capacity-delivery-manager
description: |
  Guides delivery of data center capacity increments—MW/kW and rack-ready halls on schedule:
  capacity delivery plans, critical path (power, cooling, construction, network), vendor and
  contractor coordination, readiness gates, handoff to operations and compute install, and
  program RAID across concurrent capacity projects.
  Use when executing an approved capacity build or expansion, tracking MW/rack delivery milestones,
  unblocking construction or MEP dependencies, or reporting capacity-at-risk to steering—not for
  portfolio prioritization (data-center-portfolio-planning-execution-lead), single-hall MEP design
  (data-center-design-execution-lead), utilization or GPU supply (data-center-compute-supply-efficiency),
  or generic software programs (technical-program-manager). On-site rack-and-stack and smart-hands:
  field-services-engineer.
---

# Senior Data Center Capacity Delivery Manager

## When to Use

- Turn an **approved capacity initiative** into a dated delivery plan (kW/MW, racks, go-live)
- Run **critical path** across power, cooling, fit-out, network demarc, and acceptance tests
- Coordinate **vendors**: GC, MEP, colo, utility, carriers, commissioning agents
- Define **readiness gates**: construction complete → commissioned → rack-ready → workload-ready
- Track **capacity at risk** — slip vs demand date from engineering or portfolio
- Manage **RAID** and weekly status for capacity delivery programs
- Hand off to **facilities ops** and `cluster-deployment-engineer` when capacity is install-ready
- Support **multiple concurrent** hall or row expansions with dependency map

## When NOT to Use

- Multi-site capex prioritization and funding bands → `data-center-portfolio-planning-execution-lead`
- Detailed hall design, single-line diagrams, tier selection → `data-center-design-execution-lead`
- Host consolidation, GPU forecast, stranded kW optimization → `data-center-compute-supply-efficiency`
- Cross-team software integration program → `technical-program-manager`
- Terraform, cloud burst architecture → `infrastructure-engineer`

## Related skills

| Need | Skill |
|---|---|
| Portfolio roadmap and steering | `data-center-portfolio-planning-execution-lead` |
| MEP, layout, commissioning depth | `data-center-design-execution-lead` |
| Compute utilization and supply | `data-center-compute-supply-efficiency` |
| On-site install, cabling, acceptance | `field-services-engineer` |
| K8s on new capacity | `cluster-deployment-engineer` |
| Large mixed software+infra program | `technical-program-manager` |
| Physical security and compliance | `cybersecurity`, `compliance-engineer` |
| Exec status narrative | `communication-lead` |
| WIP/CIP and capex capitalization | `director-infrastructure-capex-accounting` |

## Core Workflows

### 1. Delivery charter

Scope: site, increment (e.g. 2 MW, 80 racks), demand date, budget envelope, DRIs.

**See `references/delivery_charter.md`.**

### 2. Capacity delivery plan

Milestones from design release through **rack-ready** and optional **workload-ready**.

**See `references/capacity_delivery_plan.md`.**

### 3. Workstream coordination

Power, cooling, construction, network, security, DCIM — integrated schedule.

**See `references/workstream_coordination.md`.**

### 4. Readiness gates

Objective criteria before declaring capacity available for install or production.

**See `references/readiness_gates.md`.**

### 5. Vendor and construction management

RFI/submittal cadence, site safety, change orders, acceptance.

**See `references/vendor_construction.md`.**

### 6. Reporting and escalation

Weekly RAG, MW/rack burn-up, top blockers, decisions for steering.

**See `references/reporting_escalation.md`.**

## Output standards

- Integrated master schedule with critical path identified
- Capacity burn-up: planned vs actual kW/racks by week
- RAID with owner and target date; escalate reds within 48h
- Readiness checklist signed by facilities and IT infrastructure
- Assumptions on utility lead times and colo lead times explicit

## When to load references

- **Charter** → `references/delivery_charter.md`
- **Schedule and milestones** → `references/capacity_delivery_plan.md`
- **Workstreams** → `references/workstream_coordination.md`
- **Gates** → `references/readiness_gates.md`
- **Site and vendors** → `references/vendor_construction.md`
- **Status pack** → `references/reporting_escalation.md`
