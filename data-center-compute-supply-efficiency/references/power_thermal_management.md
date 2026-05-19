# Power and Thermal Management

## Power hierarchy

```
Utility → UPS/PDU → Rack PDU → Server PSU → Components
```

Efficiency work focuses on **matching IT load to committed capacity** and **perf per watt**.

## Stranded power recovery

1. Measure actual draw per rack (not nameplate alone)
2. Compare to breaker / colo contract kW
3. Identify racks below policy (e.g. < 40% of committed)
4. Options:
   - Add workloads (consolidation)
   - Lower committed allocation with colo (contract change)
   - Rebalance across rows

## Power capping

| Mechanism | Use when |
|---|---|
| OS/firmware power limits | Batch acceptable; save kW |
| GPU power limit | Training not latency-critical |
| Dynamic voltage/frequency | General compute |

Document **SLA exclusions** where caps are forbidden.

## Thermal and density

| Workload | Cooling consideration |
|---|---|
| Air-cooled GPU (≤700W class) | CFM per rack, hot aisle containment |
| Liquid direct-to-chip | Manifold, leak detection, maintenance |
| High-density CPU | Per-U kW limits |

Mismatch → throttling, reduced useful work per kW.

## Coordination with facility

- **Cooling setpoints** — don't lower PUE on paper while IT throttles
- **Row balance** — avoid hot spots from uneven load
- **New density** → `data-center-design-execution-lead` if beyond existing class

## Tariff and carbon (optional)

- Time-of-use: shift batch to off-peak
- **Carbon intensity** by grid hour — report separately from PUE
- On-site renewables or PPAs — sustainability narrative
