---
name: supply-chain-manager
description: |
  Guides supply chain management—sourcing and supplier qualification, procurement and PO governance,
  demand forecasting and inventory policy, logistics and fulfillment (3PL, Incoterms, lead times),
  supplier scorecards, cost and TCO analysis, supply risk and continuity, and SCM KPI dashboards.
  Use when designing supply strategy, running RFQs, setting safety stock, resolving stockouts or
  excess inventory, improving OTIF, dual-sourcing critical parts, or building supplier business
  reviews—not for contract legal redlines (commercial-counsel), vendor security assessments
  (information-security-engineer), DC construction delivery programs (senior-data-center-capacity-delivery-manager),
  compute GL and invoice reconciliation (compute-accounting-manager), SaaS quote-to-order
  (deal-operations-administrator), or enterprise strategy cases (business-consultant).
---

# Supply Chain Manager

## When to Use

- Define **supply chain operating model** — make vs buy, single vs multi-source, regional strategy
- Run **sourcing** — RFQ/RFP, supplier qualification, should-cost, award recommendation
- Set **inventory policy** — safety stock, reorder points, ABC/XYZ, slow-mover disposition
- Align **demand forecast** with sales, ops, and finance horizons
- Manage **logistics** — 3PL selection, lanes, Incoterms, customs, lead-time buffers
- Build **supplier scorecards** — quality, delivery, cost, responsiveness
- Mitigate **supply risk** — sole source, geopolitical, concentration, continuity plans
- Resolve **exceptions** — stockouts, late POs, quality holds, invoice/PO mismatches (ops view)
- Prepare **QBR materials** with strategic suppliers

## When NOT to Use

- MSA, liability, indemnity redlines → `commercial-counsel`
- Vendor SOC2, access, security questionnaire → `information-security-engineer`
- DC MW/rack construction critical path → `senior-data-center-capacity-delivery-manager`
- Server/GPU utilization and stranded kW → `data-center-compute-supply-efficiency`
- Capex accounting, depreciation, cloud CUR to GL → `compute-accounting-manager`
- CRM quote, order form, billing handoff → `deal-operations-administrator`
- Customer support and subscription ops → `customer-ops-specialist`
- AI model vendor bake-offs → `ai-lead-ops`
- Issue-tree strategy without supply execution → `business-consultant`
- Multi-team software integration TPM → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| Commercial contract terms | `commercial-counsel` |
| Supplier security review | `information-security-engineer` |
| DC capacity vendor delivery | `senior-data-center-capacity-delivery-manager` |
| Compute hardware forecast | `data-center-compute-supply-efficiency` |
| Hardware/cloud invoice accounting | `compute-accounting-manager` |
| Order-to-cash operations | `deal-operations-administrator` |
| BI and operational dashboards | `bi-analyst` |
| Large cross-functional program | `technical-program-manager` |
| Strategy and operating model | `business-consultant` |

## Core Workflows

### 1. Strategy and operating model

Scope, KPIs, governance.

**See `references/supply_chain_strategy_framing.md`.**

### 2. Sourcing and suppliers

RFQ, qualification, scorecards.

**See `references/sourcing_supplier_management.md`.**

### 3. Inventory and demand

Forecast, policies, exceptions.

**See `references/inventory_demand_planning.md`.**

### 4. Logistics and fulfillment

3PL, lanes, lead times.

**See `references/logistics_fulfillment.md`.**

### 5. Risk and resilience

Continuity, dual source, buffers.

**See `references/supply_risk_resilience.md`.**

### 6. Cost and performance

TCO, OTIF, dashboards.

**See `references/cost_and_performance_metrics.md`.**

## Outputs

- **Supply plan** — demand, supply, gap by period
- **Sourcing recommendation** — award matrix with risks
- **Inventory policy sheet** — SKU rules and parameters
- **Supplier scorecard** — quarterly metrics and actions
- **Risk register** — sole source, lead time, mitigation owner
- **Executive summary** — cost, service, risk trade-offs

## Principles

- **Service level before lowest unit price** — total cost includes stockout and expedite
- **Forecast is a process** — bias and error tracked, not a one-time spreadsheet
- **Contracts follow commercial counsel** — SCM owns business terms input, not legal sign-off
- **Measure what suppliers control** — clear OTIF and quality definitions
- **Resilience has a price** — document buffer and dual-source cost for leadership
