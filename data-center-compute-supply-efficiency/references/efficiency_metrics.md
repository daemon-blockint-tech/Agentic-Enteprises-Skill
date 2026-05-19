# Efficiency Metrics

## Facility layer

| Metric | Definition | Notes |
|---|---|---|
| **PUE** | Total facility power / IT equipment power | Industry benchmark ~1.2–1.5; site-specific |
| **WUE** | Water / IT kW | Relevant for liquid cooling sites |
| **kW committed** | Breaker or contract allocation per rack/row | May exceed actual draw |
| **kW actual** | Measured IT load | PDU, intelligent rack PDU, DCIM |

## Compute supply layer

| Metric | Definition |
|---|---|
| **Rack utilization** | Occupied U / total U |
| **kW utilization** | Actual IT kW / committed kW |
| **Host count** | Physical servers, GPU nodes, blades |
| **GPU/CPU inventory** | Units by SKU and generation |
| **Stranded kW** | Committed − used, above policy threshold |
| **Stranded U** | Empty rack space with power still reserved |

## Demand / usefulness layer

Define **useful work** per organization—examples:

- vCPU-hours consumed (virtualization)
- GPU-hours scheduled (training/inference)
- Completed batch jobs per kW
- Inference requests per watt (requires app telemetry)

| Metric | Purpose |
|---|---|
| **CPU avg / p95 utilization** | Host or cluster |
| **GPU SM / memory utilization** | Accelerator efficiency |
| **Idle host %** | Below threshold N days |
| **Oversized host %** | Peak < X% of capacity |

## Derived efficiency KPIs

- **kW per useful GPU-hour** — lower is better (same SLA)
- **Servers per rack at target kW** — density efficiency
- **Capex per unit useful capacity** — supply efficiency
- **Refresh gain** — perf/watt delta gen-over-gen

## Data sources

- DCIM, PDU, environmental sensors
- vCenter, hypervisor, bare-metal inventory
- Kubernetes metrics (node allocatable vs requests) — coordinate with cluster team
- CMDB / asset tags (owner, environment, criticality)
- Cloud billing for hybrid comparison (not primary for this skill)

## Anti-patterns

- Optimizing average CPU% alone while latency SLOs fail
- Ignoring **committed** kW when colo charges by allocation
- Mixing dev idle hosts with production peaks in one average
