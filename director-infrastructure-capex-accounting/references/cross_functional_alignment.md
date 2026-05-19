# Cross-functional alignment

## Table of contents

1. [Stakeholder map](#stakeholder-map)
2. [Cadence](#cadence)
3. [Common conflicts](#common-conflicts)
4. [Handoffs](#handoffs)

## Stakeholder map

| Function | Need from accounting | Accounting need |
|---|---|---|
| DC / platform engineering | Clear capitalization rules | In-service dates, serials |
| Capacity delivery | WIP tied to milestones | Accurate project codes |
| Portfolio planning | Capex envelope truth | Classification consistency |
| FP&A | Forecast and bridge | Timely actuals and run-rate |
| Procurement | PO templates, capex flags | Invoices to correct project |
| Tax | Asset registers, credits | Treatment questions early |
| Treasury | Cash timing | Commitment visibility |
| Legal | Lease vs buy, contracts | ASC 842 inputs |
| Internal audit | Control narratives | Open issues closed |
| External audit | PBCs, judgments | Single DRI for infra capex |

## Cadence

| Meeting | Purpose |
|---|---|
| Monthly close sync | WIP, additions, issues with `compute-accounting-manager` |
| Quarterly capex review | Forecast vs actual with engineering and FP&A |
| Pre-board | Narrative and slides sign-off |
| Audit planning | Scoping infra capex risks annually |

## Common conflicts

| Conflict | Resolution |
|---|---|
| Engineering wants OpEx for speed | Policy exception or true OpEx if no future benefit |
| Early PO close vs not in service | Do not capitalize; keep in WIP or accrue |
| Cloud “all OpEx” culture | Prepaid/commitment policy enforced |
| Portfolio defers build but POs exist | Stop accruals; discuss cancel or hold WIP |
| Chargeback vs capex | Chargeback is allocation; does not change asset treatment |

## Handoffs

- **To `compute-accounting-manager`:** policy updates, approved memos, close calendar
- **From delivery programs:** milestone dates, acceptance packs
- **To `compliance-engineer`:** control changes after process updates
- **To `communication-lead`:** external messaging only through approved channels

Director escalates **material judgments** to controller/CFO; does not override GAAP without authority.
