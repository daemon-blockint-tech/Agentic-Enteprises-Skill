---
name: simulation-software-engineer
description: |
  Simulation systems: discrete-event and continuous-time physics/kinematics, sensor and environment
  models, digital twins, scenario runners, SIL/HIL interfaces, real-time and faster-than-real-time
  execution, deterministic replay, calibration/validation, Monte Carlo sweeps, distributed sim
  concepts. Robotics, training sim, automotive, manufacturing, game-engine pipelines (NDA-safe).
  Use for simulation software, build a simulator, discrete event simulation, physics simulation,
  digital twin, SIL, HIL, scenario runner, simulation framework, deterministic replay, Monte Carlo
  simulation, sensor model simulation, Simulink-style, real-time simulation—not game-only, fusion-only
  (sensor-fusion-engineer), autonomy stack (tactical-ai-autonomy-developer), MCU firmware
  (embedded-real-time-software-engineer), plant control (control-software-developer), formal proofs
  (software-assurance-formal-methods-specialist), HIL security (hardware-in-the-loop-security-tester),
  server perf only (performance-engineer).
---

# Simulation Software Engineer

## When to Use

- Choose **discrete-event vs continuous-time** (or hybrid) simulation architecture and time-stepping policy
- Build **physics and kinematics models**—rigid body, vehicle dynamics, simplified aerodynamics, constraints
- Model **sensors and environments**—noise, bias, latency, occlusion, weather, terrain, traffic, actors
- Design **digital twins** and **scenario runners**—parameterized worlds, replay, batch sweeps, regression suites
- Define **SIL/HIL interfaces**—stimulus injection, plant models, clock sync, I/O mapping, fault injection hooks (engineering, not security bench)
- Engineer **real-time vs faster-than-real-time** execution—scheduling, back-pressure, wall-clock coupling
- Implement **deterministic replay**—seed control, ordering, floating-point policy, record/playback contracts
- Run **calibration and validation** against logs, flight/field data, or bench measurements with explicit metrics
- Plan **Monte Carlo** and **parameter sweeps**—sampling design, coverage, aggregation, failure taxonomy
- Outline **distributed simulation**—federation concepts, time management, bandwidth/latency budgets (concept level)
- Integrate **game-engine or middleware pipelines** when simulation rigor (time, sensors, replay) is required

## When NOT to Use

- **Pure game development** without simulation rigor (determinism, validation, SIL/HIL, sensor truth models) → game/graphics skills as appropriate
- **Sensor fusion algorithms only**—Kalman/graph optimization, track association, estimator tuning without building the sim stack → `sensor-fusion-engineer`
- **Autonomy product stack**—perception/planning product code, fleet ops, tactical autonomy delivery → `tactical-ai-autonomy-developer`
- **Bare-metal MCU firmware**, ISR/RTOS on chip, driver bring-up → `embedded-real-time-software-engineer`
- **Industrial plant control applications**—DCS/PLC scan cycles, OPC UA to historians, BPCS logic → `control-software-developer`
- **Formal proof obligations**—theorem proving, certified code, assurance case ownership → `software-assurance-formal-methods-specialist`
- **HIL security testing**—authorized bus fault injection, exploit benches, penetration on hardware rigs → `hardware-in-the-loop-security-tester`
- **Service-level profiling**, load tests, p99 on servers or browsers without simulation architecture → `performance-engineer`

## Related skills

| Need | Skill |
|---|---|
| Sensor fusion, estimation, track logic | `sensor-fusion-engineer` |
| Autonomy product implementation and delivery | `tactical-ai-autonomy-developer` |
| MCU/RTOS firmware, drivers, WCET on embedded targets | `embedded-real-time-software-engineer` |
| DCS/PLC control applications and OT integration | `control-software-developer` |
| HIL security assessment, bus injection for security | `hardware-in-the-loop-security-tester` |
| Formal methods, proof, assurance cases | `software-assurance-formal-methods-specialist` |
| Server/UI performance profiling and load tests | `performance-engineer` |
| OT/ICS plant security and operations | `scada-ics-cyber-security-specialist` |
| Pre-flight architecture/security/cost validation | `build-validator` |

## Core Workflows

### 1. Scope, paradigms, and success criteria

Define simulation purpose (V&V, training, design exploration, digital twin), fidelity tiers, and measurable acceptance metrics.

**See `references/simulation_software_scope.md`.**

### 2. Time bases, physics, and numerical stability

Select DE/CT/hybrid time management, integrators, stiffness handling, and coordinate frames.

**See `references/modeling_time_and_physics.md`.**

### 3. Sensors, environment, and scenarios

Model sensing pipelines, world state, actors, and scenario DSL/runner contracts.

**See `references/sensors_environment_and_scenarios.md`.**

### 4. Execution, real-time, and determinism

Schedule sim loops, real-time coupling, record/playback, seeds, and reproducibility policies.

**See `references/execution_realtime_and_determinism.md`.**

### 5. Validation, calibration, and metrics

Compare sim to measured data; tune parameters; report uncertainty and regression gates.

**See `references/validation_calibration_and_metrics.md`.**

### 6. SIL/HIL, twins, and integration

Map software-in-the-loop and hardware-in-the-loop boundaries, clocks, I/O, and twin synchronization.

**See `references/integration_sil_hil_and_twins.md`.**

## Outputs

- **Simulation architecture brief** — paradigm (DE/CT/hybrid), time policy, modules, fidelity tiers, risks
- **Model catalog** — physics, sensors, environment, interfaces, units, assumptions, known gaps
- **Scenario specification** — parameters, initial conditions, termination, pass/fail metrics, seed policy
- **Determinism and replay contract** — what is logged, ordering rules, FP policy, version pins
- **SIL/HIL interface sheet** — signals, rates, latency, clock domains, fault injection points (engineering)
- **Validation report** — metrics vs ground truth, calibration parameters, residual analysis, regression suite
- **Sweep/Monte Carlo plan** — sampling design, coverage matrix, aggregation and failure taxonomy
- **Distributed sim concept note** — federation roles, time management, bandwidth budget (when applicable)

## Principles

- **Match fidelity to decision** — coarse models for exploration; high fidelity only where metrics demand it
- **Make time explicit** — document clocks, step sizes, event ordering, and real-time coupling assumptions
- **Separate truth, sensor, and estimator** — ground truth in sim ≠ sensor output ≠ fusion output
- **Invest in reproducibility** — seeds, deterministic builds, pinned assets, replay contracts before scaling sweeps
- **Validate against measurements** — calibration is incomplete without stated metrics and holdout data
- **Keep security and formal peers in lane** — route HIL security and proof obligations to named skills
- **Stay NDA-safe** — generic patterns only; no contractor names, controlled data, or export-sensitive payloads

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries, paradigms, domains | `references/simulation_software_scope.md` |
| DE/CT time, physics, integrators | `references/modeling_time_and_physics.md` |
| Sensors, environment, scenarios | `references/sensors_environment_and_scenarios.md` |
| Real-time, determinism, replay | `references/execution_realtime_and_determinism.md` |
| Calibration, validation, metrics | `references/validation_calibration_and_metrics.md` |
| SIL/HIL, digital twins, integration | `references/integration_sil_hil_and_twins.md` |
