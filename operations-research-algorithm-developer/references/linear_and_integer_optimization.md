# Linear and integer optimization

## Table of contents

1. [Model families](#model-families)
2. [LP workflow](#lp-workflow)
3. [MIP workflow](#mip-workflow)
4. [Formulation patterns](#formulation-patterns)
5. [Big-M discipline](#big-m-discipline)
6. [Valid inequalities and tightening](#valid-inequalities-and-tightening)
7. [Decomposition (conceptual)](#decomposition-conceptual)
8. [QP and conic notes](#qp-and-conic-notes)

## Model families

| Family | Variables | Typical use |
|---|---|---|
| LP | Continuous | Flows, blending, transport (fractional splits) |
| MIP | Integer/binary | Fixed costs, setup, yes/no assignments |
| QP | Continuous (+ quadratic) | Portfolio variance, distance squared (careful) |
| MILP | Mixed | Industry standard for planning |

## LP workflow

1. Build sparse constraint matrix or algebraic model
2. Check feasibility with Phase I or solver presolve
3. Solve; read duals only when **sure** model is pure LP (no degeneracy caveats documented)
4. Sensitivity: allow objective/rhs ranges where solver supports it
5. Report objective, dual summary (optional), binding constraints

## MIP workflow

1. Start from **LP relaxation**—bound quality predicts difficulty
2. Set **time limit** and **MIP gap** upfront; align with business SLO
3. Enable **presolve**, **cuts**, and **heuristics** (solver defaults often good)
4. Track **incumbent** improvement curve for tuning
5. If gap stalls—tighten formulation before raising time limit indefinitely

## Formulation patterns

| Pattern | Formulation sketch |
|---|---|
| Fixed charge | y_j ∈ {0,1}, x_j ≤ M y_j |
| Either-or | x ≤ M y, x ≥ m y (or SOS1) |
| Minimum batch | Σ x_i ≥ L y, x_i ≤ U y |
| Logical | Linearize with standard AND/OR templates |
| Piecewise linear | SOS2 or multiple binary segments |

Prefer **SOS and indicator constraints** when solver supports them—often numerically stabler than naive big-M.

## Big-M discipline

1. Derive M from **physical or logical bounds**, not 1e6 habit
2. Use **tightest valid M per constraint**, not one global constant
3. Test relaxation value—if binaries fractional at root, M likely loose
4. Consider **indicator constraints** (Gurobi/CPLEX) or OR-Tools literals

## Valid inequalities and tightening

| Technique | When |
|---|---|
| Cover inequalities | Knapsack-like rows |
| Clique cuts | Conflict graphs (scheduling, coloring) |
| Symmetry breaking | Identical machines/vehicles |
| Variable fixing | Dominated assignments from preprocessing |
| Bounds strengthening | Update LB/UB on variables from constraints |

Document any **manual cuts** so maintenance engineers understand binding logic.

## Decomposition (conceptual)

| Method | Idea | When |
|---|---|---|
| Benders | Master complicates, sub checks feasibility/cost | Large-scale facility, stochastic |
| Lagrangian | Relax coupling; dualize complicating constraints | Network + complicating side constraints |
| Column generation | Generate variables on the fly | Cutting stock, crew pairing |
| Dantzig-Wolfe | Block structure with master prices | Same family as column gen |

Prototype on small instances before committing to custom decomposition code.

## QP and conic notes

- Confirm **convexity** for global QP optimum
- Distance objectives often linearized for MILP (Manhattan) or handled in routing engines
- Second-order cone useful for robust norms—use when solver license includes conic
