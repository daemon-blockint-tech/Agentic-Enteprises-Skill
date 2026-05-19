# Hardware Lifecycle

## Stages

| Stage | Efficiency goals |
|---|---|
| **Standardize** | Few SKUs; predictable kW per unit |
| **Procure** | Align to forecast; avoid speculative GPU hoard |
| **Receive** | Asset tag, kW nameplate in CMDB |
| **Deploy** | Fill to target rack kW; cable once |
| **Operate** | Monitor age, drift, firmware power profiles |
| **Refresh** | Improve perf/watt; reduce node count |
| **Decommission** | Power off, wipe, reclaim U and kW |

## Refresh decision matrix

| Factor | Refresh favor | Extend favor |
|---|---|---|
| Perf/watt gain | Large (new GPU gen) | Marginal |
| Power per unit | New unit uses less kW for same work | — |
| Warranty / failure rate | High RMA | Stable |
| Software support | EOL OS/driver | Supported |
| Utilization | Can't consolidate further | Still headroom |

## Decommission checklist

- [ ] Workloads migrated or retired
- [ ] Data destroyed per policy
- [ ] Licenses reclaimed
- [ ] Removed from monitoring and CMDB
- [ ] Powered off; PDU port documented free
- [ ] Spares or resale disposition
- [ ] kW and U added back to supply pool

## Spares and inventory

- Spares are **insurance**, not efficiency — cap % of fleet
- Rotate spares through test lab to avoid stale firmware

## GPU-specific

- Track **firmware, driver, and CUDA** stacks per generation
- Pool allocation: shared vs dedicated per team
- End-of-life: resale market, donation policy, destruction certs

## E-waste and compliance

- Vendor takeback or certified recycler
- Chain of custody for storage media
- Environmental reporting → `compliance-engineer` if regulated
