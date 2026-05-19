# Vendor and invoice controls

## Table of contents

1. [Vendor types](#vendor-types)
2. [Three-way match](#three-way-match)
3. [Common issues](#common-issues)
4. [Controls](#controls)

## Vendor types

| Vendor | Accounting touchpoints |
|---|---|
| Hyperscaler (AWS, Azure, GCP) | AP, prepaid, usage accrual |
| Colocation | OpEx or lease; power pass-through |
| OEM / distributor (Dell, HPE) | Capex AP; asset creation |
| Maintenance / support | OpEx or prepaid |
| Network carriers | OpEx; may capitalize if part of build |

## Three-way match

For **hardware capex**:

1. **PO** — approved amount, capex project code
2. **Receipt** — serials, quantity, in-service trigger
3. **Invoice** — match to PO; capitalize to asset or inventory

For **cloud**:

- Match **enterprise agreement** or account master to invoice
- Validate **payer account** list vs approved subscriptions

## Common issues

| Issue | Resolution |
|---|---|
| Invoice in wrong entity | Rebill or intercompany recharge |
| Duplicate serial capitalized | Retire duplicate asset |
| Credits on separate line | Map to expense or prepaid reduction |
| Partial shipment | Accrue or capitalize only received units |
| Backdated colo rate change | Catch-up adjustment with memo |

## Controls

- **Segregation** — approver ≠ preparer for capex over threshold
- **Master data** — GL and cost center on PO required
- **Tag policy** — block close on untagged prod spend above limit (if automated)
- **Asset disposal** — dual approval before GL retirement
- **PBC retention** — invoices, capitalization memos, reconciliation sign-offs

Route **lease** classification and **sales/use tax** on equipment to tax/legal per policy.
