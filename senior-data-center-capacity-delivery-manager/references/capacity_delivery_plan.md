# Capacity Delivery Plan

## Milestone chain (typical)

| # | Milestone | Output |
|---|---|---|
| 1 | Design baseline / IFC | Frozen drawings, spec |
| 2 | Permits and utility | Energization date confirmed |
| 3 | Long-lead equipment | Switchgear, chillers, AHUs on site |
| 4 | Rough-in complete | MEP rough-in signed |
| 5 | Fit-out complete | Containment, PDUs, busway |
| 6 | MEP startup | Standalone testing |
| 7 | Integrated commissioning | IST scripts pass |
| 8 | **Rack-ready** | Power/network at rack; safe for install |
| 9 | **Workload-ready** | Compute/cabling; cluster accept |

Not every increment needs all steps (e.g. colo turn-key); tailor.

## Critical path

Identify longest pole:

- Utility feed and switchgear
- Cooling plant or colo build SLA
- Carrier fiber lead time
- Commissioning window and authority having jurisdiction

Update critical path when change orders land.

## Capacity burn-up

Track weekly:

| Week | Planned kW cumulative | Actual kW cumulative | Planned racks | Actual racks |
|---|---|---|---|---|

**At risk** when actual lags planned with no recovery plan in 2 weeks.

## Schedule integration

Single **master schedule** (not separate Gantt per vendor without links):

- Design releases
- Procurement
- Construction
- Network
- Commissioning
- IT install (dependency only)

## Demand date negotiation

If slip inevitable:

1. Quantify impact on product/engineering (GPU queue, colo contract)
2. Options: partial MW, phased rows, cloud burst bridge
3. Recommend to `data-center-portfolio-planning-execution-lead`
