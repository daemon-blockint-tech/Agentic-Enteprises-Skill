# WMS developer scope

## Table of contents

1. [Role definition](#role-definition)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [System landscape](#system-landscape)
5. [Operating models](#operating-models)
6. [Deliverable checklist](#deliverable-checklist)

## Role definition

A **WMS developer** designs and implements software that executes warehouse operations: receiving inventory, storing it, allocating it to demand, picking and packing orders, shipping, and maintaining accuracy through cycle counts and adjustments. The role spans configuration, customization, extension code, integration adapters, and operational runbooks—not executive supply chain strategy or plant-floor control engineering.

## In scope

| Area | Examples |
|---|---|
| **Inbound** | ASN/pre-receipt, dock check-in, receiving, QA holds, putaway tasks |
| **Inventory** | On-hand, available-to-promise, reservations, holds, lot/serial/expiry |
| **Outbound** | Order download, allocation, wave release, pick/pack/ship, manifest |
| **Locations** | Zones, aisles, bins, pick faces, staging, dock doors, virtual locations |
| **Execution UX** | RF/mobile screens, barcode symbologies, label print triggers |
| **Integrations** | ERP item/PO/SO sync, TMS ship confirm, OMS status, EDI 940/945/856 |
| **Automation interface** | Work release to WCS, container/LPN IDs, divert confirmations (concept) |
| **3PL / multi-site** | Client rules, billing capture events, site-specific parameters |
| **Performance** | Peak planning, batch sizing, queue tuning, archival strategy |

## Out of scope

- **Supply chain strategy** without WMS implementation—sourcing awards, safety stock policy workshops → `supply-chain-manager`
- **ERP functional consulting**—GL periods, revenue recognition, HR modules
- **Pure TMS routing**—carrier selection, rate engine, without WMS shipment execution
- **OT/ICS security and DCS logic**—PLC programs, Purdue zones → `scada-ics-cyber-security-specialist`, `control-software-developer`
- **Enterprise data warehouse**—dimensional models, dbt marts → `data-warehouse-engineer`
- **Generic cloud/K8s** without warehouse workflows → `platform-engineer`, `devops`

## System landscape

Typical integration map (logical):

```
OMS / e-commerce ──► WMS ◄──► ERP (items, PO, SO, finance)
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
          TMS        WCS/AMR      Label/print
       (labels,      (sort,        services
        tracking)     convey)      
```

**WMS** remains system of record for **warehouse inventory state** and **task execution** until ship confirm posts upstream.

## Operating models

| Model | Implications |
|---|---|
| **Owned DC** | Single tenant; simpler rules; shared master data with ERP |
| **Multi-DC network** | Site-specific rules; inter-facility transfers; network ATP views |
| **3PL** | Client isolation, billing events, SLA dashboards, branded documents |
| **Hybrid automation** | Manual + WCS zones; clear handoff IDs and fault escalation |

## Deliverable checklist

Before go-live, confirm:

- [ ] Document types and status transitions documented
- [ ] Location hierarchy and slotting rules signed off by operations
- [ ] Allocation and substitution rules tested with peak SKU mix
- [ ] RF flows UAT’d on target devices and Wi-Fi coverage
- [ ] Integration replay and reconciliation jobs defined
- [ ] Cycle count and adjustment audit trail verified
- [ ] Automation fault codes mapped to WMS exception tasks
- [ ] Cutover, rollback, and hypercare runbooks approved
