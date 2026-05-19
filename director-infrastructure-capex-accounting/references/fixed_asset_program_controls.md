# Fixed-asset and prepaid program controls

## Table of contents

1. [Control objectives](#control-objectives)
2. [Key controls](#key-controls)
3. [Audit PBCs](#audit-pbcs)
4. [Subledger governance](#subledger-governance)

## Control objectives

- Valid capitalization (existence, ownership, correct period)
- Complete recording of disposals and transfers
- Accurate depreciation and amortization
- Restricted access to asset master and useful life changes

Partner with `compliance-engineer` for control documentation and evidence design.

## Key controls

| Control | Frequency |
|---|---|
| Capex PO approval over threshold | Per transaction |
| Capitalization memo for non-standard | Per asset |
| WIP aging review | Monthly |
| In-service approval (engineering + accounting) | Per project wave |
| Depreciation run review | Monthly |
| Asset disposal dual approval | Per event |
| Useful life change approval | Per change |
| Cloud prepaid reconciliation to vendor | Monthly |

Investigate **breaks** between CMDB/asset tag and fixed-asset register quarterly.

## Audit PBCs

Prepare rolling **PBC index**:

- Fixed-asset rollforward (cost, accum depr, additions, disposals)
- Top additions sample with invoices and memos
- Disposals and retirements
- Prepaid cloud rollforward
- WIP listing and aging
- Policy and exception log
- SOX walkthrough narratives

Assign DRI per section; `compute-accounting-manager` prepares detail, director reviews judgments.

## Subledger governance

- **Asset categories** and GL mapping — change control
- **Useful lives** — annual review with engineering obsolescence input
- **Project codes** — aligned to delivery programs; no orphan WIP
- **Segregation** — who can create assets vs post depreciation

Escalate ERP limitations (manual spreadsheets) with remediation roadmap to controller.
