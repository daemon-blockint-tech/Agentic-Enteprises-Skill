# Inventory and demand planning

## Table of contents

1. [Forecasting](#forecasting)
2. [ABC and segmentation](#abc-and-segmentation)
3. [Inventory policies](#inventory-policies)
4. [Exception management](#exception-management)

## Forecasting

Inputs:

- Sales pipeline and bookings (lag adjusted)
- Historical shipment/consumption
- Promotions, seasonality, product lifecycle
- Engineering **BOM** and build plan for hardware

Reconcile **top-down** finance target vs **bottom-up** SKU forecast.

Track **bias** (over-forecast wastes cash; under-forecast causes stockout).

## ABC and segmentation

| Class | Typical rule | Policy |
|---|---|---|
| A | High value or critical | Tight control, frequent review |
| B | Medium | Standard reorder |
| C | Low | Min/max or MRO bulk buy |
| X/Y/Z | Demand variability | Higher safety stock for Z |

## Inventory policies

| Policy | Use |
|---|---|
| Reorder point + EOQ | Steady demand, known lead time |
| Min/max | C items, spare parts |
| MRP | Dependent demand from BOM |
| VMI / consignment | Shift holding cost to supplier (contract terms) |

**Safety stock** = f(service level, lead-time variability, demand variability).

Document assumptions; refresh when lead time shifts.

## Exception management

| Signal | Action |
|---|---|
| Stockout imminent | Expedite, alternate SKU, customer comms |
| Excess / obsolete | Promote, rework, scrap with finance approval |
| Open PO past due | Supplier escalation, partial ship |
| Cycle count variance | Root cause, adjust records, CAPA |

Hardware forecast alignment → `data-center-compute-supply-efficiency` for compute nodes.
