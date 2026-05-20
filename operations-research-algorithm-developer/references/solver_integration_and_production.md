# Solver integration and production

## Table of contents

1. [Solver landscape](#solver-landscape)
2. [Selection criteria](#selection-criteria)
3. [Model lifecycle](#model-lifecycle)
4. [API and service patterns](#api-and-service-patterns)
5. [Timeouts and fallbacks](#timeouts-and-fallbacks)
6. [Warm starts and incremental solve](#warm-starts-and-incremental-solve)
7. [Infeasibility diagnosis](#infeasibility-diagnosis)
8. [Sensitivity and reporting](#sensitivity-and-reporting)
9. [Observability](#observability)
10. [Licensing and deployment](#licensing-and-deployment)

## Solver landscape

| Stack | Strengths | Typical interface |
|---|---|---|
| OR-Tools | Routing, CP-SAT, free tier | Python, C++ |
| Gurobi | Fast MIP/LP, tuning | Python, PuLP, Pyomo |
| CPLEX | Enterprise MIP, CP | Same |
| HiGHS | Open-source LP/MIP | PuLP, Pyomo |
| PuLP | Modeling → multiple backends | Python |
| Pyomo | Algebraic modeling, decomposition hooks | Python |

Treat solver choice as **non-functional requirement**—license, support, and performance on *your* model class.

## Selection criteria

| Criterion | Question |
|---|---|
| Problem fit | Routing native? CP? Conic? |
| Scale | Variables, constraints, binary count |
| Gap SLO | Need proven optimal or 1% gap in 60s? |
| License | Cloud, container, academic, core count |
| Team skill | Existing Pyomo vs raw API |
| Determinism | Same seed → same incumbent? |

## Model lifecycle

1. **Version** formulation (git tag) separate from code
2. **Serialize** instance files (JSON, LP, MPS) for reproducibility
3. **CI**: small golden instances—objective within tolerance, feasible
4. **Staging**: full-size nightly with time limits
5. **Production**: pinned solver version; monitor regressions

## API and service patterns

| Pattern | Use |
|---|---|
| Sync solve | Interactive planning UI (< few minutes) |
| Async job | Large MIP; poll status; store incumbent |
| Batch | Overnight scenario packs |
| Incremental | Real-time dispatch with warm start |

**Response payload**: status, objective, gap, runtime, solution, dual summary (optional), warnings, model_version.

Validate inputs **before** solver call—return 400 with structured errors, not opaque solver crashes.

## Timeouts and fallbacks

| Policy | Behavior |
|---|---|
| Time limit | Return best incumbent + gap |
| No incumbent | Return infeasible or “no solution” with diagnostics |
| Degraded mode | Heuristic-only path if MIP exceeds budget |
| Previous plan | Serve last feasible if new solve fails (document staleness) |

Never block HTTP workers unbounded—thread pool or job queue for long solves.

## Warm starts and incremental solve

- **MIP start**: inject prior x values; verify feasibility
- **LP basis** (advanced): speed re-solve after small rhs changes
- **Rolling horizon**: fix early periods, optimize tail
- **Real-time**: limit changed variables; short time limit

Log whether warm start **improved time to first incumbent**.

## Infeasibility diagnosis

| Step | Tool / action |
|---|---|
| 1 | Presolve infeasible → check data validation |
| 2 | IIS (Gurobi/CPLEX) → minimal conflict set |
| 3 | Elastic mode / slack on constraint groups | Rank relaxations |
| 4 | Manual bisect | Disable constraint families |

Deliver **business-readable conflict**—e.g., “capacity week 12 + minimum service” not only row IDs.

## Sensitivity and reporting

- **Objective coefficients**: allowable increase/decrease (LP)
- **RHS shadow prices**: interpret only for valid LP segments
- **Scenario compare**: side-by-side objectives and key decisions
- **Benchmark table**: method, gap, time, nodes (MIP)

## Observability

| Metric | Purpose |
|---|---|
| solve_duration_ms | SLO tracking |
| mip_gap | Quality |
| incumbent_found | Reliability |
| infeasible_count | Data/model health |
| solver_status | Failure taxonomy |

Alert on **gap regression** or **infeasibility spike** after deploy.

## Licensing and deployment

- Run license server or cloud token per vendor docs
- Pin **solver version** in container images
- Isolate **CPU and memory** limits for solve workers
- Do not embed license secrets in repos—use env/secret store

Coordinate with **`senior-software-engineer`** for service mesh, auth, and deployment; OR owns model correctness and solve SLOs.
