# Fixed assets and depreciation

## Table of contents

1. [Asset register fields](#asset-register-fields)
2. [Lifecycle events](#lifecycle-events)
3. [Depreciation methods](#depreciation-methods)
4. [Disposal and impairment](#disposal-and-impairment)

## Asset register fields

Minimum fields per compute asset:

| Field | Example |
|---|---|
| Asset ID | FA-2024-00123 |
| Description | Dell R750, 2×GPU |
| Serial number | From `field-services-engineer` handoff |
| Category | Server, GPU, network, storage |
| In-service date | When placed in production use |
| Cost basis | Invoice + capitalized freight/install |
| Useful life | 3–5 years (policy) |
| Depreciation method | Straight-line |
| Location | Site, rack, account |
| GL accounts | Asset, accum depr, depr expense |
| Custodian / owner | Engineering or platform team |

## Lifecycle events

1. **Pending** — PO placed, not in service
2. **In service** — start depreciation
3. **Transfer** — site or cost center change; update tags and allocation
4. **Partial upgrade** — capitalize if new component meets threshold; else OpEx
5. **Retired** — stop depreciation; disposal workflow

Align **in-service** with engineering (not merely received at dock unless policy says otherwise).

## Depreciation methods

| Method | When used |
|---|---|
| Straight-line | Default for servers/GPU |
| Units of production | Rare; only if policy and reliable meter |
| Group depreciation | Policy permitting pooled assets |

Run **monthly depreciation** journal; tie subledger to GL.

## Disposal and impairment

**Disposal:**

- Remove cost and accumulated depreciation
- Record gain/loss on sale or scrap
- Retire serial from inventory/asset system

**Impairment indicators:**

- Long idle with no redeploy plan
- Obsolete generation (e.g., GPU end-of-life)
- Physical damage

Document **impairment test** per GAAP/IFRS policy; controller approval.
