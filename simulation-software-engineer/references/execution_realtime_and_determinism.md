# Execution, real-time, and determinism

## Table of contents

1. [Purpose](#purpose)
2. [Execution modes](#execution-modes)
3. [Scheduling and back-pressure](#scheduling-and-back-pressure)
4. [Determinism dimensions](#determinism-dimensions)
5. [Record and replay](#record-and-replay)
6. [Floating-point policy](#floating-point-policy)
7. [Regression and CI](#regression-and-ci)
8. [Distributed simulation (concept)](#distributed-simulation-concept)
9. [Checklist](#checklist)

## Purpose

Guide **how simulation runs execute**—real-time coupling, faster-than-real-time throughput, and **reproducible** record/replay for SIL, HIL, and Monte Carlo campaigns.

## Execution modes

| Mode | Wall-clock behavior | Typical use |
|---|---|---|
| As-fast-as-possible (AFAP) | No pacing; max throughput | Sweeps, Monte Carlo, nightly regression |
| Scaled real-time | Sim time × scale factor vs wall | Accelerated training, human monitoring |
| Hard real-time | Sim step aligned to wall clock | HIL, operator-in-the-loop, some SIL |
| Soft real-time | Best effort with overrun detection | Dev loops; not for safety claims |

**Document overrun policy:** skip frame, catch up, or **freeze** sim while controller continues (dangerous—justify explicitly).

## Scheduling and back-pressure

### Single-process loop

```
while running:
  wait_until(next_tick)           # if real-time
  integrate_physics(dt)
  update_environment()
  generate_sensor_observations()
  publish_to_sut()                # SIL/HIL boundary
  collect_commands()
  apply_actuation()
  log_frame()
```

### Multi-threaded pipelines

- Separate **physics**, **rendering**, **sensor raycast**, **I/O** threads with bounded queues.
- Define **drop policy** when queues fill (drop render vs drop sensor vs slow physics).
- Real-time HIL: prefer **bounded latency** over unbounded queues.

| Risk | Mitigation |
|---|---|
| Nondeterministic thread order | Single-writer event log; lock ordering; task graphs |
| Sensor backlog | Rate limit; coalesce; shed load with metrics |
| GPU async | Synchronize at frame boundary for replay builds |

## Determinism dimensions

| Dimension | Control |
|---|---|
| RNG seeds | Per-stream seeds logged at start |
| Event ordering | Tie-break rules in DE scheduler |
| Input ordering | Single ingress queue from hardware/network |
| Floating point | Compiler flags, fast-math off for replay builds |
| Asset versions | Hash-pinned meshes, maps, configs |
| Third-party engines | Pin build, solver iterations, thread count |

**Tolerance-based replay:** when bit-identical replay is infeasible, define **metric tolerances** (pose RMSE, sensor checksum buckets) and still log seeds and versions.

## Record and replay

### Minimum replay header

- `sim_version`, `scenario_id`, `params`, `seed_map`
- Asset manifest hashes
- Integrator and physics engine settings
- FP/compiler flags profile name

### Log contents (tiered)

| Tier | Fields |
|---|---|
| T0 | Commands, discrete mode changes, RNG seeds |
| T1 | + low-rate truth state, sensor outputs |
| T2 | + full internal diagnostics (large) |

**Replay modes:**

- **Open-loop:** feed recorded commands; compare outputs
- **Closed-loop:** re-run SUT with recorded exogenous disturbances only
- **Hybrid:** partial SIL with hardware replaced by recorded I/O

## Floating-point policy

- Maintain a **`deterministic` build profile** (no fast-math, fixed reduction order where needed).
- Document **known nondeterministic** ops (parallel reductions on GPU) and isolate them.
- For cross-platform replay, prefer **tolerance metrics** over bitwise identity.

## Regression and CI

| Gate | Intent |
|---|---|
| Smoke | Short scenario, strict time limit, seed fixed |
| Golden replay | Compare metrics to baseline within tolerance |
| Sensor snapshot | Hash selected topics after warm-up period |
| Performance budget | Wall time per scenario on reference hardware |

Fail CI on **silent metric drift**—require explicit baseline bumps with rationale.

## Distributed simulation (concept)

High-level only—detail belongs in program-specific designs:

- **Roles:** federate, orchestrator, physics owner, sensor service
- **Time management:** conservative vs optimistic synchronization
- **Bandwidth:** what state crosses the wire (poses vs full sensor blobs)
- **Failure:** partition handling, stale state, graceful degrade

Do not claim scalability numbers without measurement on target network.

## Checklist

- [ ] Execution mode and overrun policy documented
- [ ] Thread/queue diagram if multi-threaded
- [ ] Seed map and tie-break rules defined
- [ ] Replay header schema versioned
- [ ] Deterministic build profile named in CI
- [ ] Baseline metrics and tolerances stored per scenario
