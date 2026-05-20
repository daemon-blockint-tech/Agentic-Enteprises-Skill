# Mapping and translation

## Table of contents

1. [Canonical model first](#canonical-model-first)
2. [Mapping layers](#mapping-layers)
3. [Segment and loop patterns](#segment-and-loop-patterns)
4. [Code lists and conversions](#code-lists-and-conversions)
5. [Dates, quantities, and UOM](#dates-quantities-and-uom)
6. [Allowances and charges](#allowances-and-charges)
7. [Direction-specific rules](#direction-specific-rules)
8. [Mapping specification template](#mapping-specification-template)

## Canonical model first

Define **canonical documents** independent of X12 or EDIFACT:

| Canonical | Core entities |
|---|---|
| **PurchaseOrder** | Header, parties, terms, lines (SKU, qty, UOM, price, dates) |
| **OrderAck** | PO ref, line status, promised qty/date, reject reasons |
| **Shipment** | PO refs, ship-from/to, packages, SSCC, line shipped qty |
| **Invoice** | PO/shipment refs, lines, taxes, allowances, remit-to |
| **InventorySnapshot** | Location, SKU, qty available, as-of datetime |

Use stable **business keys**: `partnerId`, `poNumber`, `lineNumber`, `sku`, `shipmentId`, `invoiceNumber`. Map EDI references (BEG03, RFF, REF) into named fields—not opaque segment dumps.

## Mapping layers

1. **Parse** — raw interchange → typed segment tree (validated syntax)
2. **Normalize** — trim, timezone, decimal scale, default missing optional segments per IG
3. **Transform** — segment tree ↔ canonical (rules engine or compiled maps)
4. **Enrich** — lookup SKU cross-ref, ship-to resolution, org hierarchy
5. **Publish** — canonical → ERP/WMS API or outbound generator

Keep layers **testable in isolation** with golden files per layer.

## Segment and loop patterns

**X12 loops** (examples):

- **PO1/N9/SCH** — line, reference, schedule
- **HL** hierarchy — shipment → order → pack → item (856)
- **IT1/TDS** — invoice lines and totals

**EDIFACT loops** — LIN, QTY, PRI, RFF, NAD, TDT, PAC segments grouped by message structure.

Rules:

- Document **loop entry/exit** conditions (e.g. HL03 code determines level)
- Handle **optional segments** with explicit defaults vs reject
- Support **repeating parties** (N1/N3/N4, NAD) via role codes (BT, ST, SF, BY)

## Code lists and conversions

Maintain **conversion tables** versioned per partner:

| Domain | X12 examples | EDIFACT examples |
|---|---|---|
| UOM | EA, CA, LB | PCE, KGM |
| Currency | USD in CUR | CUX |
| Transport | SCAC in TD5 | TDT + mode |
| Ack status | AK5, IK5 | ERC in CONTRL |

Never hardcode partner-specific qualifiers in shared maps—use **partner profile overlays**.

## Dates, quantities, and UOM

- Parse **CCYYMMDD** vs **YYMMDD** per IG; store UTC instants with source timezone metadata
- Quantities: respect **integer vs decimal** per UOM; reject ambiguous floats
- Catch-weight: separate **ordered vs shipped weight** fields in canonical model

## Allowances and charges

Map SAC, ALC, TAX segments into canonical **AllowanceCharge** lines with:

- Type (allowance vs charge)
- Basis (percent vs amount)
- Agency/qualifier codes
- Link to header vs line

Required for invoice match and deduction management.

## Direction-specific rules

| Direction | Extra concerns |
|---|---|
| **Inbound** | Duplicate PO detection, change orders (860), partial accepts |
| **Outbound** | Partner-specific mandatory segments, trailing segment limits |
| **Bidirectional** | Symmetric maps still need **separate** IG rules per direction |

## Mapping specification template

For each transaction set document:

```markdown
## 850 → PurchaseOrder (Partner: ACME, 5010)

### Header
| Canonical field | Segment | Element | Rule |
|---|---|---|---|
| poNumber | BEG | BEG03 | required |
| poDate | BEG | BEG05 | CCYYMMDD → date |

### Line loop PO1
| lineNumber | PO1 | PO101 | sequence |
| sku | PO1 | PO107 | via xref table partner_sku |

### Conditions
- If BEG02 = '00' then original PO; '05' replace — call change-order handler

### Samples
- inbound: samples/acme_850_001.x12 → expected: golden/acme_po_001.json
```

Store samples under version control; run in CI on map changes.
