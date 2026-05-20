# TCO and build vs buy

## Table of contents

1. [TCO components](#tco-components)
2. [Cloud vs on-prem](#cloud-vs-on-prem)
3. [Managed vs self-managed](#managed-vs-self-managed)
4. [NPV checklist](#npv-checklist)

## TCO components

Include all material costs over horizon (typically 3–5 years):

| Category | Cloud | On-prem / colo |
|---|---|---|
| Compute/storage/network | Metered services | Hardware, power, rack, network |
| Operations labor | Lower if managed PaaS | Higher FTE for stack |
| Software licenses | Often embedded | DB, OS, virtualization |
| Migration | One-time | Refresh cycles |
| Downtime risk | SLA credits (partial) | Impairment, redundancy capex |
| Exit | Egress, data transfer | Decommission, resale |

Do not compare **invoice line** to **depreciation only**.

## Cloud vs on-prem

When cloud TCO wins (often):

- Variable or uncertain demand
- Short horizon or experimental workload
- Need global regions quickly
- Want to avoid hardware refresh cycle

When on-prem/colo may win:

- Stable 24/7 high utilization for years
- Very high scale with efficient operations team
- Strict data gravity with cheap local power
- Existing sunk hardware

Build **crossover chart**: cumulative cost vs time; note breakeven year.

## Managed vs self-managed

Economic trade-off:

| Factor | Managed (RDS, GKE control plane) | Self-managed (EC2 + OSS) |
|---|---|---|
| Labor | Lower | Higher |
| Unit price | Higher meter | Lower meter + labor |
| Risk | Provider patches | Your patch debt |
| Scale elasticity | Fast | Slower |

Model **FTE hours × rate** explicitly for self-managed options.

## NPV checklist

1. Define **discount rate** (WACC or finance-provided)
2. Cash flows by year (CapEx, OpEx, migration)
3. Terminal value or explicit end-of-horizon exit cost
4. **Sensitivity** on utilization and growth ±20%
5. Document **non-monetary** factors separately (agility, compliance) — do not hide in fudge factors

Legal/regulatory constraints are inputs, not overridden by NPV alone.
