# Delivery Charter

## Charter fields

| Field | Example |
|---|---|
| **Initiative ID** | CAP-2026-EU1-H2 |
| **Site** | Colo Frankfurt / owned Virginia |
| **Capacity increment** | 1.5 MW IT, 60 racks @ 25 kW |
| **Demand date** | Date engineering needs rack-ready |
| **Portfolio approval** | Steering date / capex slot |
| **Budget** | Capex envelope + contingency % |
| **Delivery DRI** | Capacity delivery manager |
| **Design DRI** | `data-center-design-execution-lead` |

## Scope boundaries

| In scope | Out of scope |
|---|---|
| Deliver contracted kW and rack positions | Workload migration planning (engineering) |
| Network meet-me to demarc | Application cutover |
| Commissioning and acceptance | Long-run PUE optimization program |
| DCIM points live | GPU procurement queue |

## Success criteria

- **Rack-ready** on or before demand date (or approved re-baseline)
- Acceptance tests passed; as-builts in DCIM
- Operations runbook handed to facilities
- No open red safety or compliance items

## Interfaces

| Stakeholder | Interface |
|---|---|
| Portfolio office | Funding, priority, slip tradeoffs |
| Design lead | IFC packages, RFIs, design changes |
| Utility / colo | Power energization, access |
| Network | Cross-connects, backbone aug |
| IT infrastructure | Rack install, cluster bootstrap |

## Change control

Capacity, date, or budget change → steering or portfolio lead approval; update master schedule within 2 business days.
