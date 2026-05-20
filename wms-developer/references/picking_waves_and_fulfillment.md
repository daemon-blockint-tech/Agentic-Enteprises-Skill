# Picking, waves, and fulfillment

## Table of contents

1. [Pick methods](#pick-methods)
2. [Wave planning](#wave-planning)
3. [Batch and cluster picking](#batch-and-cluster-picking)
4. [Zone and sortation](#zone-and-sortation)
5. [Packing and cartonization](#packing-and-cartonization)
6. [Labor and productivity](#labor-and-productivity)

## Pick methods

| Method | When to use |
|---|---|
| **Discrete order pick** | Low volume, heavy items, strict order integrity |
| **Batch pick** | Many small orders sharing SKUs; sort after pick |
| **Cluster pick** | Cart with multiple order totes; scan sort at pick |
| **Zone pick** | Large building; pass container between zones |
| **Pick-to-light / voice** | High-density pick faces; integrate via WCS/vendor APIs |

Pick path optimization:

- Sequence by **location pick path** (serpentine aisle order)
- Respect **weight/volume** limits per container
- Split **hazmat** and **temperature** zones

## Wave planning

**Wave** = batch of demand released together for picking.

Release criteria examples:

- Carrier **cut-off time**
- **Priority** or service level (same-day vs standard)
- **Route/stop** for retail distribution
- **Single-SKU** waves for promotional spikes

Wave lifecycle:

```
Build pool ──► Allocate ──► Release tasks ──► Pick in progress ──► Complete / close
```

Controls:

- **Max lines / units / orders** per wave
- **Labor capacity** caps by zone
- **Frozen wave** during count or system maintenance

## Batch and cluster picking

- **Batch**: one picker, one SKU, many orders—**sortation** required post-pick
- **Cluster**: multi-order cart; scan **tote + SKU** to confirm placement
- Validate **no SKU commingling** without scan at sort station

## Zone and sortation

- **Pick-and-pass**: container moves zone to zone; each zone picks its lines
- **Put-wall / sort wall**: batch pick to wall slots by order
- **WCS divert**: WMS sends **container ID + destination**; WCS confirms divert scan

At concept level: WMS publishes **work units**; automation confirms **completion events**—never assume silent success.

## Packing and cartonization

- **Scan-to-pack**—each item scanned into carton; short pack blocks close
- **Cartonization rules**—choose box size by dims/weight; minimize void fill
- **Insert rules**—pack slips, marketing, hazmat docs per order profile
- **Multi-carton orders**—parent shipment ID links cartons

## Labor and productivity

Metrics (operational, not HR payroll):

- Lines/units per hour by zone
- Travel time estimates vs actual (if captured)
- Exception rate (shorts, mis-scans)

Use metrics to tune **wave size** and **slotting** before peak season.
