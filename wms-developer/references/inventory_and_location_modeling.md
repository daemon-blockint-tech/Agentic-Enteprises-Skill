# Inventory and location modeling

## Table of contents

1. [SKU and unit of measure](#sku-and-unit-of-measure)
2. [Location hierarchy](#location-hierarchy)
3. [Inventory dimensions](#inventory-dimensions)
4. [Allocation and ATP](#allocation-and-atp)
5. [Holds and quarantine](#holds-and-quarantine)
6. [Slotting and replenishment](#slotting-and-replenishment)
7. [Common pitfalls](#common-pitfalls)

## SKU and unit of measure

- Define **base UOM** (each) and **handling UOM** (case, pallet) with conversion factors
- Capture **catch weight**, **variable weight**, and **nested pack** hierarchies where needed
- Track **attributes**: lot, serial, expiry, country of origin, temperature zone, hazmat class
- Enforce **receipt validation**—weight/tolerance, shelf-life minimum on inbound

## Location hierarchy

Typical levels (adjust to product):

| Level | Purpose |
|---|---|
| **Site / warehouse** | Legal and operational boundary |
| **Zone** | Pick, reserve, staging, QA, returns |
| **Aisle / bay** | Travel path grouping |
| **Location / bin** | Addressable storage unit |
| **Pick face** | Active pick slot tied to replenishment |

Rules:

- **Unique location IDs**; avoid reusing IDs across sites without namespace prefix
- Mark locations **pickable**, **replenishable**, **countable**, **shipping-staging** explicitly
- Support **virtual locations** for in-transit, VAS, and system buffers

## Inventory dimensions

Track quantity by:

- **SKU + location + LPN/container** (license plate number)
- **Status**—available, allocated, picked, on-hold, damaged
- **Lot/serial/expiry** when attribute-controlled

Maintain **transaction log** (immutable) separate from **balance snapshot** for audit and replay.

## Allocation and ATP

| Concept | Definition |
|---|---|
| **On-hand** | Physical quantity in location |
| **Allocated** | Reserved for orders or tasks |
| **Available** | On-hand minus holds minus allocations |
| **ATP** | Available promising to downstream systems (may include inbound ASNs) |

Allocation strategies (examples):

- **FIFO/FEFO** by expiry
- **Strict lot** for regulated or customer-specific orders
- **Zone-priority**—pick face first, then reserve
- **Substitution** rules with approval and audit

## Holds and quarantine

Hold types: QA, damage, recall, customs, client embargo. Holds must:

- Block allocation and pick
- Surface reason codes on RF
- Require **role-based release** with comment

## Slotting and replenishment

- **Slotting** moves fast movers to pick faces; slow movers to reserve
- **Min/max** and **demand-based replen** generate move tasks from reserve to active
- Measure **pick density** and **travel time** when changing slotting—coordinate with operations before mass moves

## Common pitfalls

- Mixing **ERP available** with **WMS available** without sync lag documentation
- Allowing **negative available** without controlled backorder rules
- **Splitting lots** across picks without capture at pack confirm
- **Oversized LPN** nesting causing pick-path dead ends
- Missing **UOM conversion** on case picks leading to short ships
