# Routing, scheduling, and networks

## Table of contents

1. [Network flows and assignment](#network-flows-and-assignment)
2. [Vehicle routing (VRP)](#vehicle-routing-vrp)
3. [Scheduling](#scheduling)
4. [Resource allocation](#resource-allocation)
5. [Inventory and production planning](#inventory-and-production-planning)
6. [Method selection](#method-selection)

## Network flows and assignment

| Problem | Structure | Methods |
|---|---|---|
| Transportation | Bipartite supply/demand | LP, Hungarian (assignment) |
| Min-cost flow | Capacitated directed network | Network simplex, OR-Tools flow |
| Multi-commodity | Shared capacities | LP relaxation, MIP for integrality |
| Shortest path | One origin–destination | Dijkstra, A* with time windows |

**Check**: conservation of flow, capacity on arcs, cost sign convention.

## Vehicle routing (VRP)

| Variant | Extra structure |
|---|---|
| CVRP | Capacity per route |
| VRPTW | Time windows, service times |
| PDVRP | Pickup before delivery |
| Heterogeneous fleet | Multiple vehicle types/costs |
| Multi-depot | Depot choice per route |

**Exact MIP**: viable only for small instances; use for benchmarks.

**Metaheuristics / OR-Tools routing**: default for operational scale—document destroy/repair or search operators used.

**Output contract**: routes as ordered node lists, arrival times, load profiles, unassigned customers with reason codes.

## Scheduling

| Type | Decisions | Formulation notes |
|---|---|---|
| Job shop | Machine order per job | Disjunctive constraints; big-M or time-indexed |
| Flow shop | Same machine sequence | Simpler permutations |
| Parallel machines | Assign + order | Assignment + sequencing |
| Project scheduling | Precedence + resources | RCPSP; resource-constrained |
| Workforce | Shifts, skills, labor rules | Set covering/partitioning |

**Horizon discretization**: choose time buckets vs continuous—trade model size vs accuracy.

**Objective**: minimize makespan, tardiness Σ w_i T_i, or weighted completion.

## Resource allocation

- **Bipartite matching**: one-to-one assign with preferences/costs
- **Generalized assignment**: agents with capacity, tasks with demand—MIP
- **Fairness**: max-min or equity constraints—may need extra variables or multi-objective scalarization

Coordinate with **product SLOs**—explain trade-off between cost optimality and fairness.

## Inventory and production planning

| Model | Elements |
|---|---|
| Economic order quantity | Closed form; baseline only |
| Multi-period lot sizing | Setup binary, inventory balance, capacity |
| Capacitated production | Ramp limits, overtime variables |
| BOM explosion | Multi-level; link to `supply-chain-manager` for policy, OR for solve |

**Link periods**: inventory_t = inventory_{t-1} + production − demand.

## Method selection

| Scale / structure | Prefer |
|---|---|
| Pure network, continuous | LP / min-cost flow |
| Small combinatorial | MIP or CP |
| Large routing | Specialized VRP engine + local search |
| Large scheduling | CP (OR-Tools CP-SAT) or decomposition |
| Need proven gap | MIP with time limit; report gap |

Route **warehouse execution software** to `wms-developer`; OR may output **plans** (waves, routes) as inputs, not WMS code.
