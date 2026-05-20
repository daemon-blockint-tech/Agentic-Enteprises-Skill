---
name: predictive-logistics-developer
description: |
  Build and operate predictive models for logistics networks—demand forecasting at SKU/location/lane
  granularity; inventory positioning and safety stock optimization interfaces; ETA and lead-time
  prediction; capacity and congestion signals; route and network flow forecasting at model-integration
  level; cold chain and perishables; promotion and seasonality; model monitoring, drift, and
  backtesting against operational KPIs (fill rate, OTIF, WMAPE/MAPE). Use for predictive logistics,
  demand forecasting logistics, ETA prediction, inventory positioning, safety stock optimization,
  OTIF forecast, lane demand, WMAPE, logistics ML, capacity forecasting logistics, or cold chain
  forecast—not pure OR/MIP without logistics domain (operations-research-algorithm-developer), supply
  chain strategy only (supply-chain-manager), WMS feature dev (wms-developer), fleet telematics
  ingestion (geospatial-telematics-developer), generic ML without logistics (data-scientist), or EDI
  document mapping (edi-engineer).
---

# Predictive Logistics Developer

## When to Use

- Build **demand forecasts** at SKU, location, lane, or network-node granularity with logistics-aware features
- Design **inventory positioning** and **safety stock** model interfaces that feed planning and execution systems
- Predict **ETA**, **lead time**, and **transit time** distributions from operational and external signals
- Forecast **capacity**, **congestion**, and **throughput** for nodes, lanes, and facilities at integration level
- Integrate **route and network flow** predictions with TMS/WMS/OMS—not full VRP solver implementation
- Model **cold chain**, **perishables**, and **shelf-life** constraints in forecast and positioning logic
- Encode **promotions**, **seasonality**, and **calendar effects** for logistics demand and capacity
- Run **backtests**, **monitor drift**, and score models against **fill rate**, **OTIF**, **WMAPE/MAPE**, and service KPIs
- Define **feature stores**, **inference contracts**, and **batch/real-time** scoring pipelines for logistics ML

## When NOT to Use

- **Pure OR/MIP** formulation and solver implementation without logistics prediction scope → `operations-research-algorithm-developer`
- **Supply chain strategy**, RFQ, supplier scorecards, or inventory policy governance without ML build → `supply-chain-manager`
- **WMS workflows**—waves, pick paths, RF scanning, slotting application logic → `wms-developer`
- **Fleet telematics ingestion**, map matching, or geospatial pipeline engineering → `geospatial-telematics-developer`
- **Generic ML** experimentation, causal inference, or MLOps without logistics domain framing → `data-scientist`
- **EDI/X12** mapping, AS2, or partner document translation → `edi-engineer`
- **Warehouse dimensional modeling** or dbt mart design without prediction modeling → `analytics-data-engineer`

## Related skills

| Need | Skill |
|---|---|
| LP/MIP, VRP, scheduling optimization | `operations-research-algorithm-developer` |
| SCM strategy, forecast process, supplier QBRs | `supply-chain-manager` |
| WMS application and ERP/WMS integration | `wms-developer` |
| GPS/telematics streams and spatial ETL | `geospatial-telematics-developer` |
| Partner EDI and order/shipment documents | `edi-engineer` |
| General ML, A/B tests, MLOps patterns | `data-scientist` |
| BI dashboards and KPI storytelling | `bi-analyst` |
| Feature pipelines and warehouse modeling | `analytics-data-engineer` |

## Core Workflows

### 1. Scope and problem framing

Clarify horizon, granularity, decision consumer, and operational KPI contract.

**See `references/predictive_logistics_scope.md`.**

### 2. Demand forecasting and features

Build SKU/location/lane demand models with logistics calendars, promotions, and hierarchy reconciliation.

**See `references/demand_forecasting_and_features.md`.**

### 3. Inventory and network positioning

Connect forecasts to positioning, safety stock interfaces, and multi-echelon handoffs.

**See `references/inventory_and_network_positioning.md`.**

### 4. ETA, lead time, and capacity

Model transit times, node congestion, and capacity signals for planning and execution.

**See `references/eta_leadtime_and_capacity.md`.**

### 5. Evaluation and monitoring

Backtest against operational KPIs; track drift, bias, and forecast value.

**See `references/model_evaluation_and_monitoring.md`.**

### 6. Operations integration

Wire scores to OMS/TMS/WMS, planning cycles, and human-in-the-loop overrides.

**See `references/integration_with_operations.md`.**

## Outputs

- **Problem brief** — granularity, horizon, consumers, KPI targets, and non-goals
- **Feature catalog** — definitions, freshness SLAs, leakage checks, and hierarchy keys
- **Model card** — training window, metrics (WMAPE/MAPE, bias), segments, and known failure modes
- **Backtest report** — rolling-origin results tied to fill rate, OTIF, or inventory service proxies
- **Inference contract** — schema, latency, batch cadence, fallback rules, and version pins
- **Monitoring runbook** — drift thresholds, retrain triggers, and escalation to planning ops

## Principles

- **Optimize for operational KPIs**, not only statistical accuracy — tie WMAPE to service and inventory outcomes
- **Respect logistics calendars** — lead times, cutoffs, carrier schedules, and promotion lift are first-class features
- **Prevent leakage** — exclude post-decision signals; align train labels to information available at forecast origin
- **Reconcile hierarchies** — bottom-up vs top-down consistency for SKU × location × lane stacks
- **Separate prediction from optimization** — deliver distributions and interfaces; route MIP/VRP to OR peers
- **Monitor in production** — drift, bias by lane/node, and forecast value beat one-time offline accuracy
- **Document override paths** — planners and TMS rules may supersede scores; model serving must degrade safely

## When to load references

| Topic | Reference |
|---|---|
| Role scope, boundaries, RACI | `references/predictive_logistics_scope.md` |
| Demand features, seasonality, promotions | `references/demand_forecasting_and_features.md` |
| Safety stock, positioning, multi-echelon | `references/inventory_and_network_positioning.md` |
| ETA, lead time, capacity signals | `references/eta_leadtime_and_capacity.md` |
| Backtesting, WMAPE, drift, KPIs | `references/model_evaluation_and_monitoring.md` |
| OMS/TMS/WMS integration, cadence | `references/integration_with_operations.md` |
