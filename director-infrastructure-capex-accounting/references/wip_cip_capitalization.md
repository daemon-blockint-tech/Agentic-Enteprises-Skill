# WIP/CIP and project capitalization

## Table of contents

1. [Project types](#project-types)
2. [WIP lifecycle](#wip-lifecycle)
3. [In-service criteria](#in-service-criteria)
4. [Closeout and reconciliation](#closeout-and-reconciliation)

## Project types

| Type | WIP account | Capitalize to |
|---|---|---|
| New hall / build-out | CIP — construction | Building / leasehold improvement or pooled DC asset |
| Rack wave / server fleet | CIP — equipment | Server/GPU fixed-asset categories |
| Network refresh | CIP — network | Network asset class |
| Cloud commitment prepay | Prepaid asset | Amortize per cloud policy |

Separate **project codes** in ERP tied to `senior-data-center-capacity-delivery-manager` milestones.

## WIP lifecycle

1. **Budget approved** — FP&A project ID; capex in forecast
2. **Commitment** — PO issued; optional commitment accounting
3. **Spend accumulation** — invoices and accruals to WIP
4. **Substantially complete** — engineering sign-off
5. **In service** — transfer WIP → fixed asset; start depreciation
6. **Close project** — zero WIP balance; post-mortem variance

Monthly **WIP aging** review: flag projects open > policy threshold.

## In-service criteria

Require documented evidence:

| Asset | In-service trigger |
|---|---|
| Server/GPU | Production workload or approved soak complete |
| Storage/network | Carrying production traffic |
| DC fit-out | Certificate of occupancy or agreed partial occupancy |
| Cloud RI/SP | Commitment start date per contract |

**Not sufficient alone:** goods received, rack mounted without power-on, or PO closed.

Coordinate with `field-services-engineer` acceptance records for serials and dates.

## Closeout and reconciliation

At project close:

- [ ] All invoices booked to WIP or corrected
- [ ] Accruals reversed or converted
- [ ] Asset register populated with serials and locations
- [ ] Depreciation run scheduled from in-service month
- [ ] Forecast updated (capex → depreciation run-rate)

Capitalize **only** eligible costs; reclassify ineligible spend to OpEx with memo.
