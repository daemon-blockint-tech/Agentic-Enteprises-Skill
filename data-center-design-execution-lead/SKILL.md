---
name: data-center-design-execution-lead
description: |
  Guides data center design and build execution—site and tier selection, capacity and density
  planning (kW/rack, floor loading), power and cooling architecture, physical layout and containment,
  network meet-me and carrier connectivity, standards alignment (TIA-942, Uptime tiers), contractor
  coordination, commissioning, and operational handoff (DCIM, monitoring).
  Use when planning a new or expanded colo/on-prem facility, reviewing MEP and rack layouts,
  sizing power/cooling for GPU or HPC density, running DC build phases, or accepting a hall from
  design—not for cloud VPC/IaC (infrastructure-engineer), K8s deploy (cluster-deployment-engineer),
  ADRs (senior-system-architecture), GRC-only (cybersecurity), compute utilization
  (data-center-compute-supply-efficiency), DC portfolio (data-center-portfolio-planning-execution-lead),
  or capacity delivery schedule (senior-data-center-capacity-delivery-manager).
---

# Data Center Design Execution Lead

## When to Use

- Define requirements for a new data hall, cage, or colo deployment
- Compare build vs colo vs cloud extension for a workload footprint
- Size power, cooling, and rack count for current and 3–5 year growth
- Review mechanical/electrical single-line diagrams and rack elevations
- Plan hot/cold aisle, containment, and cable pathways
- Specify network demarc, cross-connects, and latency to cloud regions
- Run design → procurement → install → commissioning → handoff
- Prepare acceptance tests and operations runbooks for facilities team

## When NOT to Use

- Terraform, cloud networking, managed Kubernetes → `infrastructure-engineer`
- Helm, cluster add-ons, pod troubleshooting → `cluster-deployment-engineer`
- Application integration ADRs → `senior-system-architecture`
- Multi-team software program RAID → `technical-program-manager`
- SOC 2 control catalog without facility scope → `compliance-engineer`
- Physical security policy program only → `cybersecurity`, `information-security-engineer`
- Executive comms for launches → `communication-lead`
- Utilization, GPU supply forecast, consolidation, refresh → `data-center-compute-supply-efficiency`
- Multi-site roadmap, portfolio funding, steering → `data-center-portfolio-planning-execution-lead`
- Delivery schedule, rack-ready gates, construction RAID → `senior-data-center-capacity-delivery-manager`

## Related skills

| Need | Skill |
|---|---|
| Hybrid on-prem virtualization patterns | `infrastructure-engineer` |
| Workloads hosted in on-prem K8s | `cluster-deployment-engineer` |
| Large build program coordination | `technical-program-manager` |
| Physical/logical security controls | `cybersecurity`, `information-security-engineer` |
| Compliance evidence for facilities | `compliance-engineer` |
| Stakeholder and exec updates | `communication-lead` |
| Rollout of apps into new site | `deployment-strategist` |
| Compute supply and resource efficiency | `data-center-compute-supply-efficiency` |
| Enterprise DC portfolio planning | `data-center-portfolio-planning-execution-lead` |
| Capacity delivery program | `senior-data-center-capacity-delivery-manager` |
| On-site install, labeling, acceptance | `field-services-engineer` |

## Core Workflows

### 1. Requirements and site strategy

Capture:

- Workload type (enterprise IT, HPC/GPU, edge)
- Availability target (tier intent, RTO/RPO for facility)
- Growth: racks, kW, network ports by year
- Constraints: geography, latency to users/cloud, sustainability, budget

Decide: **own build**, **colo cage**, or **cloud-only** with small edge.

**See `references/facility_requirements.md`.**

### 2. Power and cooling

- Design power chain: utility → ATS/STS → UPS → PDU → rack
- Size for **peak kW/rack** (air vs liquid, GPU trays)
- Cooling: CRAC/CRAH, containment, setpoints per ASHRAE class
- Target PUE and measurement points

**See `references/power_cooling.md`.**

### 3. Physical layout

- Rack rows, aisle width, floor load (lbs/sq ft)
- Hot/cold containment; overhead vs underfloor delivery
- Cable trays, fiber pathways, ladder rack
- Staging, spares, and restricted zones

**See `references/physical_layout.md`.**

### 4. Network and connectivity

- Meet-me room, carrier diversity, cross-connect model
- Core/distribution/toR switching for facility (distinct from app network design in cloud)
- Latency and bandwidth to primary cloud region for hybrid

**See `references/network_connectivity.md`.**

### 5. Execution and commissioning

| Phase | Deliverables |
|---|---|
| Design | BoM, drawings, capacity model sign-off |
| Procure | Long-lead gear tracked (switching, PDUs, genset) |
| Install | MEP fit-out, rack/stack, labeling standard |
| Commission | IST/FAT, red-tag clearance, integrated tests |
| Handoff | DCIM, monitoring, as-built, ops training |

**See `references/execution_commissioning.md`.**

### 6. Operations handoff

- DCIM asset records match labels and diagrams
- Environmental and power alarms to NOC
- Maintenance windows and vendor SLAs documented
- Runbooks: escort, smart hands, emergency power-down

**See `references/operations_handoff.md`.**

## Output standards

- Capacity table: rack ID, kW design, weight, network Uplinks
- One-line diagram summary (power and cooling) with margins noted
- Commissioning checklist with pass/fail and owner
- Risks: single points of failure, lead-time items, permit dependencies

## When to load references

- **Site, tier, capacity** → `references/facility_requirements.md`
- **Power, UPS, cooling, PUE** → `references/power_cooling.md`
- **Racks, aisles, containment** → `references/physical_layout.md`
- **Carriers, MMR, hybrid links** → `references/network_connectivity.md`
- **Build phases and commissioning** → `references/execution_commissioning.md`
- **DCIM and ops** → `references/operations_handoff.md`
