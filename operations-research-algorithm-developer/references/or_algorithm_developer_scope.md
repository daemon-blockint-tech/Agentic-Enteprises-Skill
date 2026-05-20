# OR algorithm developer scope

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Problem taxonomy](#problem-taxonomy)
6. [Roles and RACI](#roles-and-raci)
7. [Handoffs](#handoffs)

## Purpose

Define **operations research and optimization engineering**—formulating decision problems, implementing solver-backed models, and delivering production-grade optimization services.

This skill covers **mathematical modeling, algorithm selection, solver integration, and OR-specific production patterns**—not general software platforms, ML prediction pipelines, or warehouse/ERP product features.

## Terminology

| Term | Meaning |
|---|---|
| LP | Linear program—all objective and constraints linear in continuous variables |
| MIP | Mixed-integer program—some variables integer or binary |
| QP | Quadratic program—quadratic objective and/or constraints (often convex) |
| CP | Constraint programming—combinatorial search with global constraints |
| VRP | Vehicle routing problem—routes, capacity, time windows, pickups/deliveries |
| IIS | Irreducible infeasible subset—minimal conflicting constraint set |
| Incumbent | Best feasible solution found so far during search |
| MIP gap | (best bound − incumbent) / \|incumbent\| when minimizing |
| Warm start | Reuse prior solution or basis when re-solving perturbed model |

## In scope

| Area | Examples |
|---|---|
| Formulation | Objectives, hard/soft constraints, multi-objective scalarization, robust/stochastic hooks |
| Model classes | LP, MIP, QP, min-cost flow, assignment, VRP, scheduling, lot sizing |
| Algorithms | Simplex, interior point, branch-and-bound, cutting planes, column generation, Benders |
| Heuristics | Greedy construction, local search, large neighborhood search, GA/SA/TS when justified |
| OR simulation | Queueing networks, discrete-event at planning level, Monte Carlo over scenarios |
| Analysis | Sensitivity, shadow prices (where valid), IIS, benchmarking, gap reporting |
| Solvers | OR-Tools, Gurobi, CPLEX, HiGHS, PuLP, Pyomo (conceptual integration patterns) |
| Production | Optimization APIs, timeouts, incremental solve, logging, model versioning |

## Out of scope

| Topic | Route to |
|---|---|
| Predictive ML, deep learning, MLOps | `data-scientist` |
| SCM strategy, RFQ, supplier management without OR model | `supply-chain-manager` |
| WMS pick/wave/RF workflows | `wms-developer` |
| Physics/DES simulation platforms, SIL/HIL software | `simulation-software-engineer` |
| Generic CRUD backends and SaaS features | `senior-software-engineer` |
| Snowflake/dbt/BI mart design | `analytics-data-engineer` |
| Formal verification and proof obligations | `software-assurance-formal-methods-specialist` |

## Problem taxonomy

| Class | Typical decisions | Common methods |
|---|---|---|
| Allocation | Who gets what, when | LP, MIP, assignment |
| Routing | Sequences, tours, visits | VRP heuristics, MIP (small), OR-Tools routing |
| Scheduling | Start times, machines, jobs | CP, MIP, disjunctive formulations |
| Network | Flows, capacities, costs | LP, min-cost flow |
| Inventory / production | Lots, periods, setup | MIP, lot-sizing templates |
| Staffing | Shifts, coverage, skills | MIP, set partitioning |

## Roles and RACI

| Activity | OR engineer | Product / PM | Data eng | SWE platform | Domain SME |
|---|---|---|---|---|---|
| Problem framing | A | C | I | I | C |
| Formulation & prototype | A | I | C | I | C |
| Data pipeline for parameters | C | I | A | C | C |
| Production API & deploy | C | I | C | A | I |
| Solver licensing & capacity | C | I | I | A | I |
| Accept solution quality SLOs | C | A | I | C | C |

## Handoffs

- **To `data-scientist`** when the core task is prediction/forecast accuracy without explicit optimization over decisions
- **To `supply-chain-manager`** when deliverable is operating model, policy, or supplier process—not solver-backed plan
- **To `simulation-software-engineer`** when building a reusable simulator runtime (time stepping, sensors, replay)
- **To `senior-software-engineer`** when work is primarily application logic without OR formulation ownership
- **From `analytics-data-engineer`** when curated tables and metrics feed parameters; OR owns model and solve
