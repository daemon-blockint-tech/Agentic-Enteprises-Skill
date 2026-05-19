# Capacity Roadmap (Multi-Site)

## Rollup structure

```
Enterprise demand (by region/workload class)
    → Site supply (current + planned)
    → Gap → Initiative (build / expand / cloud / efficiency)
```

## Demand inputs (aggregate)

| Input | Owner | Granularity |
|---|---|---|
| Compute growth (CPU/GPU) | Engineering | Region × quarter |
| Storage / network | Infrastructure | Region |
| Regulatory residency | Legal/compliance | Country/region |
| M&A or product launches | Product / corp dev | Event-driven |
| Efficiency reclaim | `data-center-compute-supply-efficiency` | kW freed |

## Supply per site

| Field | Example |
|---|---|
| Site ID | DC-EU-1 |
| Type | Owned / colo / edge |
| IT kW committed / used / planned | |
| Racks available | |
| GPU capacity | |
| Network egress to cloud regions | |
| Contract end / renewal | |

## Gap analysis

| Region | Quarter | Demand kW | Supply kW | Gap | Proposed initiative |
|---|---|---|---|---|---|
| | | | | | |

Flag:

- **Concentration risk** — >X% capacity in one metro
- **Lead time risk** — gap inside GPU or power lead time
- **Stranded investment** — built capacity with no demand forecast

## Roadmap views

1. **By region** — exec-friendly
2. **By initiative** — program office
3. **By capability** — GPU, general compute, storage-heavy

## Sync cadence

- Monthly: demand/supply refresh from site and engineering
- Quarterly: rebaseline roadmap and steering decisions
