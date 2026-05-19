---
name: compute-accounting-manager
description: |
  Guides accounting for compute infrastructure—cloud COGS and prepaid commitments, capex vs OpEx
  for servers/GPUs, depreciation and asset disposal, colo and hardware accruals, GL mapping from
  usage and invoices (CUR, billing exports), chargeback/showback to products, and month-end
  reconciliation of compute spend to the ledger.
  Use when classifying compute costs, capitalizing hardware, amortizing RIs/Savings Plans, building
  allocation models, fixed-asset register for compute, or closing compute-related accounts—not for
  ASC 606 revenue recognition (senior-revenue-accountant), engineering utilization optimization
  (data-center-compute-supply-efficiency), cloud architecture (infrastructure-engineer), deal desk
  order forms (deal-operations-administrator), commercial contract negotiation (commercial-counsel),
  or capex policy and board-level infrastructure asset governance (director-infrastructure-capex-accounting).
---

# Compute Accounting Manager

## When to Use

- Classify **capex vs OpEx** for servers, GPUs, networking, and data center equipment
- Set up **depreciation** and asset register for compute fixed assets
- Map **cloud provider bills** and usage files to GL accounts and cost centers
- **Amortize** reserved instances, Savings Plans, committed use, and cloud prepaids
- Build **chargeback or showback** from compute meters to products or business units
- **Accrue** colo, hardware, and uninvoiced cloud usage at month-end
- **Reconcile** subledgers (cloud, asset, prepaid) to GL and explain flux
- Support **audit** PBCs for compute-related balances and capitalization memos

## When NOT to Use

- SaaS revenue recognition, deferred revenue, ARR → `senior-revenue-accountant`
- Rack utilization, stranded kW, refresh planning → `data-center-compute-supply-efficiency`
- Terraform, VPC, K8s platform design → `infrastructure-engineer`
- Order form, CRM-to-billing operational handoff → `deal-operations-administrator`
- MSA/contract redlines → `commercial-counsel`
- BI dashboards without ledger tie-out → `bi-analyst`

## Related skills

| Need | Skill |
|---|---|
| Revenue and ASC 606 | `senior-revenue-accountant` |
| DC utilization and supply planning | `data-center-compute-supply-efficiency` |
| Capacity delivery and rack-ready | `senior-data-center-capacity-delivery-manager` |
| On-site asset install and serials | `field-services-engineer` |
| Cloud platform and networking | `infrastructure-engineer` |
| Deal desk and billing ops | `deal-operations-administrator` |
| SOX control evidence | `compliance-engineer` |
| Business requirements for finance systems | `business-analyst` |
| Capex policy, WIP/CIP, audit steering | `director-infrastructure-capex-accounting` |

## Core Workflows

### 1. Cost classification (capex vs OpEx)

Policy, thresholds, useful life, project vs BAU.

**See `references/cost_classification_capex_opex.md`.**

### 2. Cloud cost to GL

CUR/billing mapping, credits, prepaid amortization.

**See `references/cloud_cost_gl_mapping.md`.**

### 3. Fixed assets and depreciation

Asset register, additions, disposals, impairments.

**See `references/fixed_asset_compute.md`.**

### 4. Chargeback and showback

Allocation keys, internal rates, stakeholder reporting.

**See `references/chargeback_showback.md`.**

### 5. Month-end close

Reconciliations, accruals, flux commentary.

**See `references/month_end_reconciliation.md`.**

### 6. Vendor and invoice controls

Colo, OEM, distributor; three-way match and accruals.

**See `references/vendor_invoice_controls.md`.**

## Outputs

- **Capitalization memo** — facts, policy cite, asset life, in-service date
- **Account mapping table** — service/SKU/tag → GL, department, product
- **Amortization schedule** — prepaid cloud or capitalized implementation
- **Reconciliation workbook** — subledger to GL, reconciling items
- **Flux narrative** — drivers for MoM compute COGS or prepaid movement
- **Chargeback statement** — units, rate, allocated amount by consumer

## Principles

- **Substance over label** — classify by nature (asset vs period cost), not vendor line names alone
- **Single source of meters** — align FinOps dashboards to the same tags used in GL allocation
- **Document judgments** — capitalization, useful life changes, and material estimates
- **Not tax or legal advice** — escalate ASC 842 leases, transfer pricing, and tax treatment to qualified advisors
- **Coordinate with engineering** — in-service dates and decommissions must match asset records
