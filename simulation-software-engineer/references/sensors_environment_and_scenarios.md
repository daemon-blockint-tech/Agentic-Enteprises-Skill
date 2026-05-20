# Sensors, environment, and scenarios

## Table of contents

1. [Purpose](#purpose)
2. [Truth vs sensor vs consumer](#truth-vs-sensor-vs-consumer)
3. [Sensor modeling patterns](#sensor-modeling-patterns)
4. [Environment modeling](#environment-modeling)
5. [Actors and traffic](#actors-and-traffic)
6. [Scenario runner design](#scenario-runner-design)
7. [Scenario DSL and parameters](#scenario-dsl-and-parameters)
8. [Synthetic data and labels](#synthetic-data-and-labels)
9. [Checklist](#checklist)

## Purpose

Guide **sensor pipelines**, **environment/world state**, and **scenario runners** so simulations produce decision-grade outputs with explicit contracts for SIL, replay, and validation.

## Truth vs sensor vs consumer

| Layer | Contents | Consumers |
|---|---|---|
| Ground truth | True poses, velocities, classifications (oracle) | Metrics, label generation, debug |
| Sensor observation | Truth + noise, latency, dropout, distortion | Perception stacks, SIL software |
| Recorded log | Serialized observations + timestamps | Replay, regression, twin sync |

**Rule:** Never score perception against truth without documenting **which sensor model** was used; fusion teams need `sensor-fusion-engineer` for estimator design.

## Sensor modeling patterns

| Sensor | Minimal (F0) | Representative (F1) | Validated (F2+) |
|---|---|---|---|
| IMU | Biased rates/accel at fixed rate | Noise density, bias random walk, misalignment | Temperature model from bench |
| GNSS | Position fix at rate | Multipath stub, outage profiles, HDOP-like scalar | Urban canyon maps (generic) |
| Camera | Pinhole + fixed delay | Rolling shutter, distortion, exposure, motion blur | Calibration from target rigs |
| LiDAR | Range rays on primitives | Beam divergence, reflectivity, multipath stub | Hardware-specific noise models |
| Radar | Range/range-rate points | CFAR-like false alarms, angular error | Scenario-calibrated clutter |

**Timing model (always specify):**

- Capture time vs publish time vs host receive time
- Jitter distribution and **worst-case latency** for real-time SIL
- Frame drops and out-of-order delivery for robustness tests

## Environment modeling

| Element | Options | Validation hook |
|---|---|---|
| Terrain / map | Heightfield, meshes, tiles | Compare elevation profiles to survey data |
| Lighting | Sun angle, overcast, artificial | Camera exposure metrics on reference scenes |
| Weather | Rain/fog visibility models | Range error vs recorded LiDAR/radar |
| Static world | Buildings, vegetation proxies | Collision mesh vs visual mesh alignment |
| Dynamic world | Moving obstacles, doors, lifts | Event timing in DE schedules |

Keep **collision geometry** separate from **visual meshes**; document simplifications.

## Actors and traffic

- **Behavior layers:** kinematic paths, rule-based, learned policies (black-box OK if versioned).
- **Interaction:** right-of-way, spawn/despawn rules, density controls.
- **Determinism:** seeded traffic flows for regression; separate streams from environment RNG.

For training sims (generic, NDA-safe), avoid **identifying** real locations or classified tactics—use abstract maps and nominal parameters.

## Scenario runner design

Core responsibilities:

1. **Load** world + robot/platform + parameter set + seed
2. **Initialize** state and RNG streams
3. **Step** or **run** until termination conditions
4. **Record** agreed topics (truth, sensors, commands, metrics)
5. **Score** pass/fail and emit artifacts for CI

**Runner API surface (conceptual):**

```
run(scenario_id, params, seed) -> RunResult(metrics, logs, exit_reason)
replay(log_uri, options) -> RunResult
sweep(matrix) -> SweepReport
```

## Scenario DSL and parameters

| Feature | Purpose |
|---|---|
| Parameter schema | Typed overrides (weather, spawn counts, sensor faults) |
| Initial conditions | Pose, velocity, mode, fuel/energy if relevant |
| Termination | Time, goal reached, failure conditions, max cost |
| Fault injection | Sensor bias step, dropout window, actuator lag |
| Tags | `regression`, `nightly`, `hil_smoke`, `monte_carlo` |

Version **scenario packs** with the sim binary and asset manifest (hash pins).

## Synthetic data and labels

- Auto-label from truth for ML pipelines; document **label delay** if sensor-time labels differ.
- Publish **calibration metadata** (intrinsics/extrinsics) alongside synthetic sets.
- For domain randomization, track **parameter ranges** and **coverage** across sweeps.

## Checklist

- [ ] Truth/sensor/consumer boundaries documented
- [ ] Per-sensor timing, noise, and failure modes specified
- [ ] Environment collision vs visual meshes aligned or gap listed
- [ ] Scenario schema versioned; seeds and tags required
- [ ] Recording format supports deterministic replay
- [ ] Handoff notes for fusion/autonomy peers on interfaces
