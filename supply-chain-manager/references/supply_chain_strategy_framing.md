# Supply chain strategy framing

## Table of contents

1. [Operating model](#operating-model)
2. [Core KPIs](#core-kpis)
3. [Governance](#governance)
4. [Make vs buy](#make-vs-buy)

## Operating model

Clarify scope:

| Element | Decision |
|---|---|
| Planning horizon | S&OP monthly; tactical weekly |
| Regions | Local vs regional vs global sourcing |
| Fulfillment | In-house DC, 3PL, drop-ship, hybrid |
| Systems | ERP, WMS, TMS, PLM integration points |

Document **handoffs** to finance (forecast), legal (contracts), engineering (BOM).

## Core KPIs

| KPI | Definition hint |
|---|---|
| OTIF | On-time in-full to customer or internal request |
| Inventory turns | COGS / avg inventory |
| Days of supply | Inventory / avg daily demand |
| Supplier lead time | Order to receipt (actual vs quoted) |
| Cost variance | PO price vs standard / budget |
| Quality PPM | Defects per million (or return rate) |
| Forecast accuracy | MAPE or bias by SKU family |

Align targets with **service tier** (A/B/C SKUs).

## Governance

- **S&OP cadence** — demand, supply, inventory, gaps, decisions
- **Delegation of authority** — PO limits, sole-source approval
- **New supplier** — qualification checklist before first PO
- **Change control** — BOM revisions, ECO impact on open POs

## Make vs buy

Evaluate:

- Capital and capacity constraints
- IP and quality control needs
- Supplier market depth and geopolitical exposure
- Switching cost and ramp time

Strategic cases → input to `business-consultant`; legal structure → `commercial-counsel`.
