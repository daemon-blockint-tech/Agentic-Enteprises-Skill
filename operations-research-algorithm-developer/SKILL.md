---
name: operations-research-algorithm-developer
description: |
  Formulate and implement operations research optimization models—LP, MIP/QP, constraint programming,
  network flows, assignment, VRP, scheduling, resource allocation, inventory/production planning;
  heuristics and metaheuristics; sensitivity and infeasibility diagnosis; solver integration
  (OR-Tools, Gurobi, CPLEX, HiGHS, PuLP, Pyomo); production OR APIs (timeouts, warm starts).
  Use for operations research, OR engineer, optimization model, linear programming, mixed integer
  programming, MIP, VRP, vehicle routing, scheduling optimization, OR-Tools, Gurobi, constraint
  programming, resource allocation optimization, infeasible model, metaheuristic—not ML prediction
  (data-scientist), SCM strategy without optimization math (supply-chain-manager), WMS features
  (wms-developer), simulation platforms (simulation-software-engineer), generic backend
  (senior-software-engineer), dbt/warehouse (analytics-data-engineer).
---

# Operations Research Algorithm Developer

## When to Use

- Frame a **decision problem** as an optimization model—objectives, decisions, constraints, parameters, uncertainty
- Build **LP, MIP, QP, or constraint programming** formulations for planning and allocation
- Model **network flows**, **assignment**, **routing (VRP)**, **scheduling**, and **resource allocation**
- Design **inventory and production planning** models (lot sizing, capacity, multi-period)
- Select **exact vs heuristic** methods—branch-and-bound, column generation, decomposition, metaheuristics
- Run **sensitivity analysis**, **infeasibility diagnosis**, and **benchmarking** (optimality gap, runtime)
- Integrate **solvers** conceptually—OR-Tools, Gurobi, CPLEX, HiGHS, PuLP, Pyomo—and production patterns
- Prepare **input data**, validate units, and enforce **constraint modeling discipline**
- **Productionize** OR services—APIs, timeouts, warm starts, incremental solves, solution pools

## When NOT to Use

- **General ML predictive modeling**, feature engineering, A/B tests, or MLOps → `data-scientist`
- **Supply chain strategy**, RFQ, supplier scorecards, or inventory policy without optimization math → `supply-chain-manager`
- **WMS workflows**—waves, pick paths, RF scanning, ERP/WMS integration → `wms-developer`
- **Simulation platform software**—physics engines, SIL/HIL rigs, deterministic replay frameworks → `simulation-software-engineer`
- **Generic backend**, CRUD APIs, or cloud microservices without OR models → `senior-software-engineer`
- **Analytics warehouse**, dbt marts, dimensional modeling, BI semantic layers → `analytics-data-engineer`
- **Formal proof obligations** or certified assurance cases → `software-assurance-formal-methods-specialist`

## Related skills

| Need | Skill |
|---|---|
| ML prediction, experimentation, MLOps | `data-scientist` |
| SCM sourcing, forecast process, supplier QBRs | `supply-chain-manager` |
| Warehouse management application logic | `wms-developer` |
| DES/physics sim platforms, digital twins | `simulation-software-engineer` |
| Enterprise application and API engineering | `senior-software-engineer` |
| dbt, warehouse modeling, BI pipelines | `analytics-data-engineer` |
| Executive dashboards and KPI storytelling | `bi-analyst` |
| Service SLOs and production incident response | `site-reliability-engineer` |

## Core Workflows

### 1. Scope and problem class

Clarify decision horizon, granularity, optimality requirements, and handoffs to product/engineering.

**See `references/or_algorithm_developer_scope.md`.**

### 2. Formulation and data

Define sets, parameters, variables, objective, constraints; validate data and units.

**See `references/problem_formulation_and_data.md`.**

### 3. Linear and integer optimization

LP/MIP/QP structure, big-M discipline, tightening, decomposition hooks.

**See `references/linear_and_integer_optimization.md`.**

### 4. Routing, scheduling, and networks

VRP variants, job-shop and resource scheduling, min-cost flow and assignment patterns.

**See `references/routing_scheduling_and_networks.md`.**

### 5. Heuristics and metaheuristics

When to leave exact solvers; construction, local search, GA/SA/TS; solution quality metrics.

**See `references/heuristics_and_metaheuristics.md`.**

### 6. Solver integration and production

Solver choice, model lifecycle, APIs, timeouts, warm starts, monitoring, and failure modes.

**See `references/solver_integration_and_production.md`.**

## Outputs

- **Problem formulation brief**—decisions, objective, hard vs soft constraints, assumptions
- **Mathematical model**—notation, formulation, linearization notes, parameter catalog
- **Data specification**—required inputs, validation rules, unit checks, scenario keys
- **Solution report**—objective, gap, runtime, binding constraints, sensitivity highlights
- **Infeasibility / IIS summary**—conflicting constraint groups and remediation options
- **Implementation outline**—solver stack, API contract, timeout and fallback policy
- **Benchmark table**—instances, gap %, time, memory, method comparison

## Principles

- **Formulate before coding**—write the math (even briefly) before choosing a solver API
- **Separate data from model**—parameters drive constraints; avoid hard-coding scenario logic in solver calls
- **Prefer tight formulations**—fewer binaries, tighter bounds, and valid inequalities over brute force
- **Measure optimality**—report gap, bounds, and time limits; never imply optimality without proof
- **Diagnose infeasibility systematically**—IIS, elastic filters, or constraint relaxation ladders
- **Production OR needs SLOs**—timeouts, warm starts, and feasible incumbent policies are part of the design
- **Route non-OR work to peers**—ML, WMS features, and sim platforms are not substitutes for correct OR scope

## When to load references

| Topic | Reference |
|---|---|
| Role scope, boundaries, RACI | `references/or_algorithm_developer_scope.md` |
| Sets, parameters, validation | `references/problem_formulation_and_data.md` |
| LP, MIP, QP, tightening | `references/linear_and_integer_optimization.md` |
| VRP, scheduling, networks | `references/routing_scheduling_and_networks.md` |
| Heuristics, metaheuristics | `references/heuristics_and_metaheuristics.md` |
| Solvers, APIs, production | `references/solver_integration_and_production.md` |
