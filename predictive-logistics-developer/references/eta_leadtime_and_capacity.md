# ETA, lead time, and capacity

## Lead time and ETA modeling

### Problem variants

| Variant | Target | Features |
|---|---|---|
| Lane lead time | Days/hours order-to-receipt | Mode, carrier, distance, season |
| Transit time | Hub-to-hub duration | Network path, congestion index |
| ETA (execution) | Remaining time to delivery | GPS/telematics (via geospatial peer), last scan |
| Dock appointment | Yard-to-unload delay | Appointment rules, peak hours |

### Modeling approach

1. **Define event timestamps** — order release, pickup, hub arrival, out-for-delivery, delivery
2. **Align labels** to information available at prediction time (no future scans)
3. Predict **distribution**—quantiles or survival time—for promise-date engines
4. Calibrate **by lane and carrier**; avoid global averages on heterogeneous networks

### External and operational signals

| Signal | Source | Caution |
|---|---|---|
| Weather | External API | Location and time alignment |
| Port / rail congestion | Indices, news | Sparse; validate lift |
| Carrier performance | Historical OTIF by lane | Regime change after network redesign |
| Facility throughput | WMS/TMS events | Define measurement window |
| Telematics | Fleet platform | Feature engineering via `geospatial-telematics-developer` |

## Capacity and congestion

| Asset | Predicted quantity | Use |
|---|---|---|
| DC dock | Queue hours, unload delay | Labor and appointment planning |
| Yard | Trailer dwell distribution | Drayage scheduling |
| Lane | Volume vs capacity index | Tendering, mode shift |
| Linehaul | Utilization forecast | Procurement of capacity |

Build **congestion indices** from rolling dwell times, backlog depth, and scheduled vs actual appointments—not only static nameplate capacity.

## Route and network flow (model-integration)

- Forecast **origin-destination volumes** and **mode mix** for planning horizons
- Provide **uncertainty** for robust planning inputs
- Do **not** implement VRP, time windows, or driver scheduling—hand to OR skill with forecasted OD matrix

## Cold chain transit

- Add **temperature compliance risk** features (lane history, season, equipment type)
- Extend lead-time variance for **refrigerated lanes** with higher disruption rates
- Separate **spoilage clock** from transit clock for perishables

## Evaluation specifics

| Metric | Application |
|---|---|
| MAE / RMSE on hours | Operational scheduling |
| Quantile coverage | Promise dates (P90 reliability) |
| Bias by lane | Carrier scorecards |
| OTIF attribution | Decompose forecast error vs execution |

Penalize **late bias** differently from **early bias** when customer promise dates asymmetric.

## Production patterns

- **Batch refresh** for planning (daily/weekly lane tables)
- **Near-real-time** ETA updates for TMS dashboards with staleness bounds
- **Fallback** to historical lane median when feature pipeline fails
- Version **carrier network changes** explicitly in model registry
