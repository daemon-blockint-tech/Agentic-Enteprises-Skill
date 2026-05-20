# Integrations: ERP, TMS, EDI, and APIs

## Table of contents

1. [Integration principles](#integration-principles)
2. [ERP patterns](#erp-patterns)
3. [OMS and e-commerce](#oms-and-e-commerce)
4. [TMS and carriers](#tms-and-carriers)
5. [EDI message map](#edi-message-map)
6. [API and events](#api-and-events)
7. [Reconciliation](#reconciliation)

## Integration principles

- Assign **system of record** per entity: items (usually ERP), warehouse inventory (WMS), shipment tracking (TMS/carrier)
- Use **idempotency keys** on every inbound message (`messageId`, `correlationId`)
- Prefer **async events** for high volume; **synchronous APIs** for low-latency lookups
- Log **payload hash, status, retry count**; never silently drop failures
- Schedule **reconciliation jobs** comparing WMS vs ERP quantities and open orders

## ERP patterns

| Entity | Typical direction | Notes |
|---|---|---|
| **Item master** | ERP → WMS | UOM, attributes, hazmat, shelf life |
| **PO / ASN** | ERP → WMS | Expected receipts; close on receive confirm |
| **Sales orders** | ERP/OMS → WMS | Allocate in WMS; status back on ship |
| **Inventory adjustments** | WMS → ERP | Cycle count, scrap, shrink with reason codes |
| **Receipts / shipments** | WMS → ERP | Financial and available-to-promise updates |

Handle **partial receipts**, **over-receipts**, and **closed PO line** rejects explicitly.

## OMS and e-commerce

- **Order import** on create or release from hold
- **Cancel/split** propagation before pick starts
- **Inventory feed**—ATP or available quantity snapshots with latency SLA
- **Ship confirm + tracking** to OMS for customer notifications

## TMS and carriers

- **Rate shop** optional at pack; store selected service level
- **Label generation**—ZPL/PDF to print server; capture tracking number
- **Manifest** close-out; PRO/BOL for LTL
- **Tracking events** inbound to OMS (delivered, exception)

WMS owns **carton content**; TMS owns **carrier contract** unless tightly coupled module.

## EDI message map

Common retail/wholesale EDI (illustrative):

| EDI | Purpose | Direction |
|---|---|---|
| **850** | Purchase order | Inbound to shipper systems |
| **856** | ASN / ship notice | Outbound after ship |
| **940** | Warehouse shipping order | To 3PL WMS |
| **945** | Warehouse shipping advice | From 3PL WMS |
| **997** | Functional ack | Both |

Map segments to **canonical internal models** before WMS tables—avoid EDI-shaped tables in core schema.

## API and events

Patterns:

- **REST/JSON** for real-time order and inventory queries
- **Webhooks** for ship confirm, receipt complete
- **Message bus** (Kafka/SQS) for peak absorption with consumer groups per site

Version APIs; support **backward-compatible** fields; document **error codes** for ops.

## Reconciliation

Daily (or hourly) jobs:

- Compare **on-hand by SKU** WMS vs ERP within tolerance
- List **open orders** stuck in allocated/picked
- Flag **unposted shipments** and **orphan LPNs**
- Produce **operator work queue** with drill-down links

Escalate persistent drift to integration owner—not ad-hoc SQL in production without change control.
