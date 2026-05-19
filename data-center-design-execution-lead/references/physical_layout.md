# Physical layout

## Table of contents

1. [Rack standards](#rack-standards)
2. [Aisle and containment](#aisle-and-containment)
3. [Labeling](#labeling)

## Rack standards

- **42U** common; confirm depth (800–1200 mm) for GPU and cable bend radius
- **Weight:** populate bottom-heavy; check floor point loads vs slab rating
- **PDU placement:** vertical PDUs vs rack PDUs; leave service space
- **Spares:** 1–2 racks per hall for break/fix and staging

## Aisle and containment

| Pattern | When |
|---|---|
| Hot aisle / cold aisle | Default air-cooled |
| Cold aisle containment | Higher density, stable intake temp |
| Hot aisle containment | Exhaust to return plenum |
| Liquid (CDU in row) | GPU blocks, rear-door HX |

Minimum aisle width per fire code and cabinet door swing; keep escape paths clear.

Cable management: separate fiber and copper trays; maintain bend radius; color code A/B paths.

## Labeling

Standardize before install:

- Rack: `DC-HALL-ROW-RU` (e.g. `DC1-A04-R12`)
- Ports: TIA-606 style; match DCIM and switch config
- Power: PDU circuit → rack feed documented in as-built

As-built drawings updated within 30 days of substantial completion.
