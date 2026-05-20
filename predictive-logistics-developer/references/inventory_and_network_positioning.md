# Inventory and network positioning

## Purpose

Connect **demand and lead-time forecasts** to **inventory positioning** inputs—where to hold stock, how much buffer, and how echelons interact—without owning supply chain policy sign-off.

## Positioning problems

| Problem | Model role | Typical consumer |
|---|---|---|
| Safety stock | Forecast error × lead-time distribution | Inventory optimization / ERP |
| Reorder point | Demand over lead time + buffer | Replenishment engine |
| Multi-echelon positioning | Node-level demand + transit times | Network inventory tool |
| Lane pre-positioning | Lane demand + capacity risk | Transportation planning |
| Perishable positioning | Decay-adjusted demand | Cold chain ops |

## Safety stock interface design

Deliver to optimization engines:

- **Demand distribution** over risk period (not only point forecast)
- **Lead-time distribution** by lane/supplier (mean, variance, service level target)
- **Forecast error covariance** when systems support it; else segment-level scaling factors

Document:

- **Service level target** assumed (e.g., 95% cycle service vs fill rate)
- **Review period** and **protection interval** alignment
- **Override hooks** for planner buffers and commercial commitments

## Multi-echelon considerations

| Signal | Use |
|---|---|
| Upstream fill rate | Downstream starvation risk |
| Transit time variance | Buffer inflation on volatile lanes |
| Node capacity constraints | Cap inbound positioning recommendations |
| Substitution / alternate SKU | Redirect demand at forecast or policy layer |

Do not conflate **forecast** with **allocation solver**—pass inputs to OR or policy engines.

## Cold chain and perishables

- Model **remaining shelf life** at receipt and **FEFO** constraints as features
- Forecast **spoilage-adjusted demand**—discard unsellable inventory from sellable forecast
- Tie **markdown triggers** to spoilage risk thresholds separately from base demand
- Include **temperature excursion** flags as exogenous shocks when telemetry exists

## Network flow forecasting (integration level)

- Predict **volume between nodes** for S&OP and lane procurement
- Provide **confidence bands** for capacity planning—not detailed route sequences
- Hand off route optimization to `operations-research-algorithm-developer` with forecasted flows as parameters

## Validation tied to inventory KPIs

| KPI | How to link models |
|---|---|
| Fill rate | Backtest stockout probability vs recommended buffers |
| Days on hand | Compare implied inventory to actual after policy sim |
| Excess / obsolescence | Track over-forecast segments driving overstock |
| OTIF (inventory-caused) | Attribute misses to forecast vs execution |

## Handoffs

- **`supply-chain-manager`**: Approve service levels, ABC/XYZ policies, and S&OP targets
- **`operations-research-algorithm-developer`**: Multi-echelon optimization with distributional inputs
- **`wms-developer`**: Consume positioning targets in replenishment workflows
