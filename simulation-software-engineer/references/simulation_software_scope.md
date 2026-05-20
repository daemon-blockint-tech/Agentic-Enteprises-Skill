# Simulation software scope

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Simulation paradigms](#simulation-paradigms)
6. [Domain patterns](#domain-patterns)
7. [Fidelity tiers](#fidelity-tiers)
8. [Roles and RACI](#roles-and-raci)
9. [Handoffs](#handoffs)

## Purpose

Define **simulation software engineering** boundaries—designing and building executable models of systems, environments, and sensors for verification, training, exploration, and digital-twin operation.

This skill covers **architecture, modeling, execution, validation, and integration patterns**—not live product autonomy delivery, formal certification claims, or security-focused HIL exploitation.

## Terminology

| Term | Meaning |
|---|---|
| DE | Discrete-event simulation—event queue, state jumps at event times |
| CT | Continuous-time simulation—numerical integration of ODEs/DAEs |
| Hybrid | Coupled DE schedulers with CT physics integrators |
| SIL | Software-in-the-loop—plant/world model with software under test |
| HIL | Hardware-in-the-loop—real hardware interfaced to simulated plant/environment |
| Digital twin | Live or periodic sync between operational asset and simulation state |
| Scenario runner | Engine that loads parameterized worlds, runs episodes, scores outcomes |
| Ground truth | True simulated state before sensor corruption |
| Fidelity | Level of physical/detail fidelity chosen for a given decision |
| Deterministic replay | Bit- or tolerance-bounded reproduction of a prior run from logs + seeds |

## In scope

| Area | Examples |
|---|---|
| Architecture | DE vs CT vs hybrid; module boundaries; plugin/world composition |
| Physics/kinematics | Rigid body, wheeled/tracked vehicles, simplified aero, constraints, contact |
| Sensors | Camera/LiDAR/radar/IMU/GNSS models; noise, latency, dropout, calibration errors |
| Environment | Terrain, weather, lighting, traffic, actors, procedural or map-based worlds |
| Execution | Real-time, scaled-time, as-fast-as-possible; scheduling and back-pressure |
| Determinism | Seeds, ordering, FP policy, record/playback, regression baselines |
| Validation | Compare to logs/flight/bench data; metrics; calibration parameters |
| Sweeps | Monte Carlo, parameter grids, sensitivity, coverage reporting |
| Integration | SIL/HIL interfaces, clocks, I/O maps, twin sync (concept level) |
| Distributed sim | Federation, time management, bandwidth budgets (high level) |
| Pipelines | Game-engine or middleware sim stacks when rigor requirements are met |

## Out of scope

| Topic | Route to |
|---|---|
| Sensor fusion / estimation product algorithms | `sensor-fusion-engineer` |
| Autonomy stack delivery (perception/planning product) | `tactical-ai-autonomy-developer` |
| MCU firmware, ISR/RTOS, chip drivers | `embedded-real-time-software-engineer` |
| DCS/PLC plant control, OPC historian apps | `control-software-developer` |
| Formal proof, certified code, assurance cases | `software-assurance-formal-methods-specialist` |
| HIL security testing, bus fault injection for security | `hardware-in-the-loop-security-tester` |
| Server/UI load testing without sim architecture | `performance-engineer` |
| Pure game content/graphics without sim contracts | Game/graphics skills as appropriate |
| Legal export-control or contractor-specific data | Compliance / legal review; keep artifacts generic |

## Simulation paradigms

| Paradigm | Best for | Watch-outs |
|---|---|---|
| Discrete-event | Logistics, networks, protocol timing, queueing, mission timelines | State explosion; inconsistent time if mixed carelessly with CT |
| Continuous-time | Vehicles, mechanisms, control plants, smooth physics | Stiff systems; step-size vs stability; real-time overrun |
| Hybrid | Robotics with contact + discrete mode switches; avionics schedules + physics | Clock coupling; event detection; cross-domain bugs |
| Agent-based | Crowds, traffic micro-behavior, synthetic populations | Calibration to macro data; validation discipline |
| Monte Carlo / ensembles | Uncertainty quantification, reliability, coverage | Cost; clear parameter priors; reproducible sampling |

**Decision rule:** Pick the **coarsest paradigm that answers the decision**; add fidelity only when metrics fail without it.

## Domain patterns

| Domain | Typical sim stack elements | Notes |
|---|---|---|
| Robotics / autonomy | World + robot dynamics + sensor models + scenario runner | Keep truth vs sensor vs estimator separate |
| Aerospace / defense training | Mission timeline + platform kinematics + env/sensors (generic) | NDA-safe scenarios; no controlled performance data |
| Automotive | Vehicle dynamics + traffic actors + sensor pipelines | Often SIL for ECU stacks; log replay common |
| Manufacturing | Discrete flows + equipment state machines + throughput metrics | DE-first; integrate MES-like event feeds |
| Game-engine pipelines | Rendering + physics + scripted scenarios | Add determinism/replay/validation contracts explicitly |

## Fidelity tiers

| Tier | Intent | Examples |
|---|---|---|
| F0 — Functional | Correct interfaces and timing stubs | Constant-rate sensors, kinematic motion |
| F1 — Representative | Shape of dynamics and noise reasonable | Lumped masses, simplified aero, basic sensor noise |
| F2 — Validated | Parameters tuned to measured data | Calibrated IMU bias, camera distortion from bench |
| F3 — High | Expensive; decision-critical only | CFD-informed tables, high-res terrain, full sensor physics |

Document **tier per subsystem** and **upgrade triggers** (which metric failed at lower tier).

## Roles and RACI

| Activity | Simulation software engineer | Controls / embedded | Fusion / autonomy | V&V / test | Security HIL |
|---|---|---|---|---|---|
| Sim architecture | A | C | C | C | I |
| Physics/sensor models | A | C | C | C | I |
| Scenario runner design | A | I | C | C | I |
| SIL interface spec | A | C | C | A | I |
| HIL engineering interface | A | C | I | C | C |
| HIL security assessment | I | I | I | C | A |
| Formal assurance | I | I | I | C | I |

## Handoffs

- **To `sensor-fusion-engineer`:** Provide sensor outputs, timestamps, and ground truth; receive estimator requirements and failure modes to model.
- **To `tactical-ai-autonomy-developer`:** Deliver sim APIs, scenario catalogs, and regression baselines; receive stack interfaces and release gates.
- **To `embedded-real-time-software-engineer`:** Align clock domains, I/O rates, and WCET assumptions for HIL targets.
- **To `control-software-developer`:** Exchange plant models and scan-cycle semantics when simulating industrial controllers.
- **To `hardware-in-the-loop-security-tester`:** Separate engineering HIL I/O maps from security test plans and authorized injection.
- **To `software-assurance-formal-methods-specialist`:** Provide model assumptions and environment contracts; do not claim proofs from sim alone.
