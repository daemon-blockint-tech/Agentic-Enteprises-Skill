# Problem formulation and data

## Table of contents

1. [Formulation checklist](#formulation-checklist)
2. [Notation template](#notation-template)
3. [Hard vs soft constraints](#hard-vs-soft-constraints)
4. [Data preparation](#data-preparation)
5. [Validation rules](#validation-rules)
6. [Uncertainty hooks](#uncertainty-hooks)
7. [Common formulation errors](#common-formulation-errors)

## Formulation checklist

1. **Decision variables**—what is chosen (assign, route, schedule, produce)?
2. **State**—what is known vs decided each period?
3. **Objective**—single scalar; document weights for multi-criteria cases
4. **Constraints**—capacity, precedence, compatibility, time windows, minimum service
5. **Parameters**—demand, costs, travel times, capacities, yields (with units)
6. **Feasibility policy**—allow slack? penalty costs? reject infeasible inputs?
7. **Optimality target**—prove optimal, or accept gap/time limit?

## Notation template

Document before implementation:

```
Sets:    I (items), J (locations), T (periods), K (vehicles)
Params:  d_i (demand), c_ij (cost), Q_k (capacity), [τ_ij] (time)
Vars:    x_ij ∈ {0,1} (assign i→j), y_kt ≥ 0 (inventory)
Objective: min Σ c_ij x_ij + holding costs
s.t.     Σ_j x_ij = 1          ∀i   (each item assigned once)
         Σ_i d_i x_ij ≤ Q_j    ∀j   (capacity)
         ...
```

Keep **indices consistent** across data files, code, and reports.

## Hard vs soft constraints

| Type | Modeling pattern | When to use |
|---|---|---|
| Hard | Must hold; infeasible if violated | Safety, physical limits, regulations |
| Soft | Slack variable + penalty in objective | Preferences, target service levels |
| Elastic | Tiered penalties | Overtime, lateness bands |

Penalize slack in **objective units comparable to primary cost**—document penalty calibration.

## Data preparation

| Step | Action |
|---|---|
| Extract | Pull parameters from warehouse, ERP, GIS, or manual scenario files |
| Normalize | Consistent units (hours vs minutes, $ vs cents) |
| Index | Map business keys to model indices; keep bidirectional lookup tables |
| Aggregate | Roll up SKUs/locations when model size requires it—document loss |
| Impute | Only with explicit rules; flag imputed fields for sensitivity |
| Version | Tag scenario_id, effective_date, model_version on every solve |

## Validation rules

Run before every solve:

- **Dimensional analysis**—cost = rate × quantity; time matrices symmetric if required
- **Bounds**—capacities ≥ 0; demands non-negative unless returns modeled
- **Coverage**—every demand node has supply or penalty; every job has eligible resources
- **Graph checks**—no disconnected required arcs; unreachable customers flagged
- **Feasibility screen**—total demand ≤ total capacity (necessary, not sufficient)

## Uncertainty hooks

| Approach | Use when |
|---|---|
| Deterministic scenarios | Few discrete futures; solve each; compare |
| Stochastic programming | Here-and-now vs recourse; small scenario trees |
| Robust optimization | Uncertainty sets; protect worst-case within budget |
| Simulation outer loop | Complex dynamics; OR model inner step |

Route full **sim platform builds** to `simulation-software-engineer`; keep OR-level scenario loops lightweight.

## Common formulation errors

| Error | Symptom | Fix |
|---|---|---|
| Big-M too loose | Weak LP, slow MIP | Tighten M from problem structure |
| Strict inequality | Solver rejects or wrong | Use ≤ with ε or integer time grids |
| Double counting | Objective too low | Trace units through constraint blocks |
| Nonlinearity hidden | Local solver failure | Explicit linearization or conic/QP form |
| Missing coupling | Silly “optimal” plans | Link periods, routes, and inventory |
