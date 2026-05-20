---
name: wms-developer
description: |
  Guides design, build, customization, and integration of warehouse management systems—receiving,
  putaway, inventory, allocation, picking (wave/batch/zone), packing, shipping, cycle counts;
  slotting; lot/serial/expiry; RF/mobile and barcode; WMS–ERP–TMS–OMS integration; EDI/API;
  WCS/automation handoffs; peak scaling; multi-warehouse and 3PL models.
  Use when the user mentions WMS developer, warehouse management system, pick path, wave planning,
  putaway, cycle count, WMS integration, RF scanning, slotting, 3PL WMS, fulfillment system,
  inventory allocation, or WMS customization—not supply chain strategy without WMS
  (supply-chain-manager), generic ERP consulting, logistics routing without WMS, OT/ICS plant
  (scada-ics-cyber-security-specialist, control-software-developer), analytics warehouse marts
  (data-warehouse-engineer), or generic app/platform work without warehouse domain
  (senior-software-engineer, platform-engineer).
---

# WMS Developer

## When to Use

- Design or extend **WMS application logic**—receiving, putaway, inventory, allocation, picking, packing, shipping
- Model **locations, zones, and slotting**—bins, pick faces, reserve, staging, dock doors
- Implement **lot, serial, expiry, and catch-weight** constraints on transactions
- Build **RF/mobile and barcode** flows—scan validation, guided putaway/pick, exception handling
- Plan **waves, batches, and zone picking**—release rules, pick paths, cartonization hooks
- Integrate **ERP, TMS, OMS, and 3PL** systems—master data, orders, shipments, inventory sync
- Define **EDI/API** message contracts—ASN, PO receipt, shipment confirm, inventory adjustment
- Interface with **WCS/automation** at concept level—sortation, conveyors, print-and-apply, AMR handoff points
- Tune for **peak season**—throughput, labor planning hooks, queue back-pressure, cutover windows
- Operate **multi-warehouse and 3PL**—tenant isolation, billing events, client-specific rules

## When NOT to Use

- Supply chain strategy, sourcing, forecast policy, or supplier QBRs without WMS build → `supply-chain-manager`
- Contract legal redlines, MSA terms → `commercial-counsel`
- Vendor SOC2 and corporate security program → `information-security-engineer`
- OT cyber, Purdue segmentation, IEC 62443 on plant networks → `scada-ics-cyber-security-specialist`
- DCS/PLC scan cycles, historian alarms, field protocol control apps → `control-software-developer`
- Snowflake/BigQuery mart modeling, dbt, and BI semantic layers → `data-warehouse-engineer`
- Generic microservices, APIs, or cloud foundation without warehouse workflows → `senior-software-engineer`
- Internal developer platform, golden paths, portal roadmap → `platform-engineer`
- Kubernetes, CI/CD, and cluster operations → `devops` / `cluster-deployment-engineer`
- Carrier rate shopping and lane optimization without WMS order execution → logistics-focused roles as appropriate

## Related skills

| Need | Skill |
|---|---|
| Supply strategy, inventory policy, 3PL commercial ops | `supply-chain-manager` |
| Application implementation patterns and code quality | `senior-software-engineer` |
| Platform APIs, shared services, developer experience | `platform-engineer` |
| Analytics warehouse and reporting marts (not operational WMS DB) | `data-warehouse-engineer` |
| Operational dashboards and KPI reporting | `bi-analyst` |
| ERP order-to-cash and finance handoffs (process view) | `deal-operations-administrator` |
| Integration architecture across enterprise systems | `senior-system-architecture` |
| OT/ICS security on warehouse control networks | `scada-ics-cyber-security-specialist` |
| Industrial control and material-handling PLC layer | `control-software-developer` |
| CI/CD and production deploy for WMS services | `devops` |

## Core Workflows

### 1. Scope and boundaries

Define WMS footprint, tenants, automation touchpoints, and handoffs.

**See `references/wms_developer_scope.md`.**

### 2. Inventory and locations

SKU attributes, UOM, location hierarchy, allocation rules, and holds.

**See `references/inventory_and_location_modeling.md`.**

### 3. Inbound and outbound

Receiving, putaway, order release, shipping, and exceptions.

**See `references/inbound_outbound_workflows.md`.**

### 4. Picking and fulfillment

Waves, batches, pick methods, packing, and cartonization.

**See `references/picking_waves_and_fulfillment.md`.**

### 5. Integrations

ERP, TMS, OMS, EDI, APIs, and event patterns.

**See `references/integrations_erp_tms_edi.md`.**

### 6. Customization, testing, and operations

Extensions, UAT, cutover, monitoring, and peak readiness.

**See `references/customization_testing_and_ops.md`.**

## Outputs

- **Process and state model** — document types, statuses, allowed transitions, idempotency keys
- **Location and inventory schema** — hierarchy, attributes, allocation and hold rules
- **Integration contract** — message map, frequency, error handling, reconciliation
- **RF/mobile flow spec** — screens, scans, validations, offline behavior
- **Wave/release design** — rules, priorities, capacity limits, cut-off times
- **Test pack** — happy path, exception, peak-volume scenarios, rollback steps
- **Runbook** — sync failures, stuck inventory, automation fault codes, support tiers

## Principles

- Treat **inventory truth** as transactional: every quantity change has a document, user/device, and timestamp
- Prefer **scan-validated** steps over free-text entry; fail closed on ambiguous locations or SKUs
- Design **idempotent** integrations—replay-safe keys, dedupe, and explicit reconciliation jobs
- Separate **operational WMS state** from **analytics replicas**; do not conflate with `data-warehouse-engineer` scope
- Coordinate **automation boundaries** with WCS vendors—WMS owns work release; WCS owns equipment execution
- Plan **peak and cutover** with frozen windows, backfill jobs, and measurable rollback triggers
