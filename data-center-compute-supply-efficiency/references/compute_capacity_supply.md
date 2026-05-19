# Compute Capacity and Supply Planning

## Supply chain view

```
Demand forecast → Required capacity → Supply plan → Deploy → Measure → Adjust
```

## Demand inputs

| Source | Horizon |
|---|---|
| Product roadmaps (new GPU workloads) | 6–18 mo |
| Engineering growth (headcount, env count) | 3–12 mo |
| Contractual SLAs (reserved capacity) | Fixed |
| Seasonality (batch, year-end jobs) | Recurring |
| Cloud burst policy | Elastic overflow |

## Supply inputs

| Source | Lead time |
|---|---|
| On-hand inventory | Immediate |
| PO in flight | Weeks–months |
| Vendor allocation (GPU) | Highly variable |
| Refresh pool (returns from decomm) | After wipe/QA |
| Colo additional kW / racks | Months (facility) |

## Standard builds

Reduce supply fragmentation:

- **2–4 server SKUs** (general, storage, GPU tier)
- Document: CPU, RAM, NIC, GPU, PSU kW, form factor
- Spare parts aligned to SKUs

## Forecast template (quarterly)

| Quarter | Demand (nodes/GPUs/kW) | Supply on hand | Gap | Action |
|---|---|---|---|---|
| Q1 | | | | Buy / refresh / cloud / defer |
| Q2 | | | | |
| Q3 | | | | |
| Q4 | | | | |

## GPU / accelerator supply

- Separate **training** (burst, high power) vs **inference** (steady, latency-sensitive)
- Track **allocation queue** — projects waiting for GPUs
- Model: `effective GPUs = physical × utilization × scheduling efficiency`

## Capex vs efficiency tradeoffs

| Decision | Efficiency angle |
|---|---|
| Buy now vs cloud burst | Avoid powered idle metal |
| Higher density GPU rack | Needs cooling class match |
| Extend warranty vs refresh | Perf/watt and power draw |
| Buy fewer larger nodes vs many small | Utilization and failure blast radius |

## Handoffs

- **New kW or halls** → `data-center-design-execution-lead`
- **Workload placement on K8s** → `cluster-deployment-engineer`
- **Hybrid cloud capacity** → `infrastructure-engineer`
