# Heuristics and metaheuristics

## Table of contents

1. [When to use heuristics](#when-to-use-heuristics)
2. [Construction heuristics](#construction-heuristics)
3. [Local search](#local-search)
4. [Large neighborhood search](#large-neighborhood-search)
5. [Metaheuristics](#metaheuristics)
6. [Hybrid with exact methods](#hybrid-with-exact-methods)
7. [Quality measurement](#quality-measurement)
8. [OR-level simulation](#or-level-simulation)

## When to use heuristics

| Signal | Action |
|---|---|
| MIP gap flat after reasonable time | Switch or seed metaheuristic |
| Problem NP-hard at operational scale | Plan heuristic from start |
| Real-time re-optimization (< seconds) | Incumbent-first; partial solve |
| Need diverse solutions | Solution pool + perturbation |

Always retain **benchmark instances** where exact or strong bounds exist.

## Construction heuristics

| Pattern | Use |
|---|---|
| Nearest neighbor / greedy | Fast VRP or assignment start |
| Clarke-Wright savings | VRP routes |
| Earliest due date | Scheduling seed |
| Regret-k insertion | Richer VRP/insertion |

Document **determinism** (tie-breaking) for reproducible tests.

## Local search

| Move | Problem |
|---|---|
| 2-opt / 3-opt | TSP, route improvement |
| Swap / relocate | VRP, assignment |
| Shift one job | Scheduling |
| Or-opt chains | Route refinement |

**First improvement vs best improvement**—trade runtime vs quality.

## Large neighborhood search

1. Destroy part of solution (random, related, worst)
2. Repair with exact subroutine (MIP/CP) or greedy
3. Accept if better (or simulated annealing rule)

Strong for **VRP and scheduling** at scale when paired with OR-Tools or custom repair MIPs.

## Metaheuristics

| Method | Behavior | Notes |
|---|---|---|
| Genetic algorithm | Population, crossover, mutation | Encode feasibility carefully |
| Simulated annealing | Accept worse with cooling | Tune temperature schedule |
| Tabu search | Memory of recent moves | Aspiration criteria |
| GRASP | Randomized greedy + local search | Multiple iterations |

Avoid **tuning folklore** without validation on held-out instances.

## Hybrid with exact methods

| Pattern | Description |
|---|---|
| Matheuristic | Fix subset of integers; solve sub-MIP |
| Column generation + pricing heuristic | When exact pricing too slow |
| Branch-and-price with heuristic columns | Practical large instances |
| Warm start MIP | Inject heuristic incumbent |

Report **gap vs branch-and-bound bound** when available.

## Quality measurement

| Metric | Definition |
|---|---|
| Optimality gap | (UB − LB) / \|UB\| |
| Runtime | Wall clock to incumbent and to stop |
| Stability | Variance over seeds on same instance |
| Feasibility rate | % inputs where feasible solution returned |

Publish **Pareto** runtime vs quality curves when choosing production defaults.

## OR-level simulation

Use for:

- **Queueing**—M/M/c, G/G/1 approximations; staffing sensitivity
- **Discrete-event** lightweight models—verify plan under stochastic arrivals (not full sim platform)
- **Monte Carlo** over demand/cost scenarios when closed form unavailable

Do not conflate with **`simulation-software-engineer`** (runtime, sensors, replay engines).
