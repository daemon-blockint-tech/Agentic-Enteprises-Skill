# Inbound and outbound workflows

## Table of contents

1. [Inbound overview](#inbound-overview)
2. [Receiving and putaway](#receiving-and-putaway)
3. [Outbound overview](#outbound-overview)
4. [Order release and shipping](#order-release-and-shipping)
5. [Returns and VAS](#returns-and-vas)
6. [Exceptions](#exceptions)

## Inbound overview

Standard flow:

```
ASN/PO ──► Check-in ──► Receive ──► QA (optional) ──► Putaway ──► Available inventory
```

**ASN** (advance ship notice) pre-populates expected lines; receiving matches **PO line, qty, lot**.

## Receiving and putaway

| Step | Behavior |
|---|---|
| **Check-in** | Appointment, door assignment, unload start time |
| **Receive** | Scan PO/ASN, SKU, qty, lot/serial; capture over/short/damage |
| **LPN creation** | Assign pallet/case license plate for traceability |
| **Putaway** | System-directed or user-selected; scan location confirm |
| **Cross-dock** | Skip reserve—direct to outbound staging when rules match |

Putaway strategies:

- **Directed**—system proposes location by velocity, zone, weight, hazmat
- **User override**—allowed with reason code and supervisor PIN if configured
- **Consolidation**—merge partial LPNs when rules permit

## Outbound overview

```
Order download ──► Allocate ──► Release (wave) ──► Pick ──► Pack ──► Ship confirm
```

Support **B2B** (pallet/case) and **B2C** (each pick) on same platform with different document types.

## Order release and shipping

- **Allocation** reserves inventory; failed lines → backorder, substitute, or cancel rules
- **Wave release** creates pick tasks by priority, carrier cut-off, route, or zone
- **Pack** verifies contents (scan-to-carton), weight, dims, SSCC labels
- **Ship confirm** posts to ERP/OMS; generates **ASN 856**, **BOL**, tracking

Carrier integration (with TMS):

- Rate shop optional at pack; **label print** at pack station
- **Manifest close** triggers billing and tracking email events

## Returns and VAS

**Returns (RMA)**:

- Inspect grade A/B/scrap; restock, refurb, or destroy paths
- Quarantine until disposition

**Value-added services (VAS)**:

- Kitting, labeling, gift wrap, embroidery—model as **work orders** consuming components

## Exceptions

| Exception | Handling |
|---|---|
| Short receive | Close line partial; notify buyer; adjust ASN |
| Damaged receive | Hold location; photo reference; supplier claim hook |
| Pick short | Re-allocate, cancel line, or split shipment |
| Mis-ship | Reverse ship confirm; inventory adjustment with approval |
| Label failure | Reprint with new tracking; audit sequence |

Document every exception with **user, timestamp, reason code**, and link to source order/LPN.
