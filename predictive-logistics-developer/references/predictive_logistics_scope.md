# Predictive logistics scope

## Purpose

Define **predictive modeling for logistics networks**—forecasting demand, transit and lead times, capacity stress, and inventory positioning inputs that drive planning and execution.

This skill covers **ML feature design, training, evaluation, monitoring, and integration contracts**—not supply chain strategy governance, WMS product features, pure optimization solvers, or telematics pipeline engineering.

## Terminology

| Term | Meaning |
|---|---|
| Granularity | Forecast unit—SKU, location, lane, node, week, day |
| Horizon | How far ahead the forecast must be accurate for the decision |
| OTIF | On-time in-full service metric—delivery promise vs actual |
| WMAPE | Weighted mean absolute percentage error—volume-weighted accuracy |
| Safety stock interface | Model output consumed by inventory policy engines (not policy sign-off) |
| Positioning | Where to hold inventory across echelons and nodes |
| Cold chain | Temperature-controlled lane with spoilage and compliance constraints |

## In scope

| Area | Examples |
|---|---|
| Demand forecasting | SKU × DC, lane demand, promotional lift, new-item ramps |
| Inventory inputs | Safety stock recommendations, positioning scores, service-level proxies |
| Transit prediction | ETA distributions, lead-time by lane/carrier/mode |
| Capacity signals | Yard dwell, dock throughput, lane congestion indices |
| Network flow (ML) | Predicted volumes between nodes for planning handoff—not VRP solving |
| Perishables | Shelf-life decay, spoilage risk features, FEFO-aware demand |
| Monitoring | Drift, bias by segment, backtests vs fill rate and OTIF |

## Out of scope

| Topic | Route to |
|---|---|
| MIP/VRP/scheduling solver models | `operations-research-algorithm-developer` |
| RFQ, supplier strategy, inventory policy governance | `supply-chain-manager` |
| WMS waves, pick paths, slotting UI | `wms-developer` |
| GPS ingestion, map matching, spatial databases | `geospatial-telematics-developer` |
| X12/EDIFACT mapping and AS2 | `edi-engineer` |
| Generic ML without logistics framing | `data-scientist` |

## Problem taxonomy

| Class | Typical output | Decision consumer |
|---|---|---|
| Demand | Point + interval forecast | S&OP, replenishment, procurement |
| Lead time / ETA | Distribution by lane | TMS, promise dates, planning |
| Capacity | Utilization or queue risk | Network planning, labor scheduling |
| Positioning | Stock targets by node | Inventory optimization interface |
| Perishables | Spoilage-adjusted demand | Cold chain ops, markdown triggers |

## Roles and RACI

| Activity | Predictive logistics dev | SCM / planning | Data eng | OR engineer | WMS/TMS eng |
|---|---|---|---|---|---|
| KPI and granularity definition | C | A | I | C | C |
| Feature pipeline and store | A | C | C | I | I |
| Model train/eval/monitor | A | C | C | I | I |
| Safety stock policy approval | I | A | I | C | I |
| Solver-based route plan | I | I | I | A | C |
| Score ingestion in WMS/TMS | C | I | C | I | A |

## Handoffs

- **To `operations-research-algorithm-developer`**: Provide forecast distributions and cost parameters; receive optimized plans—not embed solver logic in notebooks
- **To `supply-chain-manager`**: Translate model assumptions into policy and S&OP cadence; do not own supplier negotiations
- **To `wms-developer`**: Define inference APIs and event hooks; do not implement pick-path algorithms
- **To `geospatial-telematics-developer`**: Specify telematics features needed; do not own device ingestion
- **To `edi-engineer`**: Align shipment status fields used as features; do not own partner mappings
