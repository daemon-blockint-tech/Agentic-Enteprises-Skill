# Cost classification (capex vs OpEx)

## Table of contents

1. [Decision framework](#decision-framework)
2. [Common categories](#common-categories)
3. [Documentation](#documentation)

## Decision framework

| Question | Capex (capitalize) | OpEx (expense) |
|---|---|---|
| Useful life | >1 year, identifiable asset | Consumed in period |
| Ownership risk | Company controls economic benefit | Pay-as-you-go service |
| Nature | Physical server/GPU, long-term license prepay for asset | Cloud usage fees, support without asset |
| Project vs BAU | Qualifying build / implementation (policy) | Maintenance, monitoring, small tools |

**Cloud usage** (compute hours, storage GB-month) → typically **OpEx COGS or hosting expense**.

**Purchased servers/GPUs** for owned or colo deploy → typically **capex** → fixed asset.

**Implementation labor** — follow company policy (capitalize eligible costs vs expense).

## Common categories

| Item | Typical treatment | Notes |
|---|---|---|
| AWS/Azure/GCP on-demand usage | OpEx | Map by tag to COGS vs R&D |
| RI / Savings Plan upfront or commitment | Prepaid asset → amortize | Match benefit period |
| Server, GPU, storage array | Capex | Serial, in-service date |
| Colo monthly MRC | OpEx or lease (ASC 842) | Legal determines lease classification |
| Cables, rails, minor parts under threshold | OpEx | De minimis policy |
| Software subscription (SaaS) | OpEx | Unless capitalized software policy applies |
| Freight, installation for capital equipment | Capitalize as part of asset | If policy requires |
| Spare parts inventory | Inventory or OpEx | Per policy |

## Documentation

Capitalization memo should include:

- Description and business purpose
- Invoice or PO reference
- In-service date and location (site/account)
- Useful life and depreciation method
- Policy paragraph or precedent
- Approver (controller or delegate)
