# Simulation, testing, and validation

## Table of contents

1. [Test pyramid](#test-pyramid)
2. [SIL and HIL concepts](#sil-and-hil-concepts)
3. [Scenario design](#scenario-design)
4. [Metrics and gates](#metrics-and-gates)
5. [Sim-to-real](#sim-to-real)
6. [Field testing](#field-testing)

## Test pyramid

| Layer | Focus |
|---|---|
| **Unit** | Geometry, rules engine, message parsers, BT nodes |
| **Component** | Perception on recorded bags; planner on synthetic worlds |
| **Integration** | Full PPC chain in SIL with mocked sensors |
| **HIL** | Real autopilot/compute with simulated or injected I/O |
| **Field** | Limited envelopes; incremental ODD expansion |

Autonomy releases should not skip layers without documented risk acceptance.

## SIL and HIL concepts

| Term | Meaning for autonomy |
|---|---|
| **SIL** | Software-in-the-loop: plant model + autonomy stack on workstation or rack |
| **HIL** | Hardware-in-the-loop: real edge computer and I/O; plant simulated or partial |
| **Replay** | Log playback through perception/planner for regression |
| **Monte Carlo** | Parameter sweeps on wind, delay, sensor dropout |

Distinguish **functional HIL** (autonomy integration) from **security HIL** (`hardware-in-the-loop-security-tester`).

## Scenario design

Structure scenarios with IDs:

| Field | Example |
|---|---|
| **ID** | `SCN-RTL-014` |
| **ODD slice** | GPS-denied, 10 m/s wind |
| **Injections** | Camera dropout at T+30s |
| **Success** | RTL within 60s, geofence never breached |
| **Artifacts** | Bag file hash, config version |

Cover: nominal mission, edge ODD, single-fault, common double-faults, operator abort, rules trip.

## Metrics and gates

| Category | Examples |
|---|---|
| **Safety** | Geofence violations (must be 0), abort latency, false override rate |
| **Performance** | Track error, time-to-goal, fuel/battery use |
| **Robustness** | Success rate across scenario suite version |
| **Latency** | p95 stage timings on target hardware |
| **Logging** | 100% abort/rule events have correlated trace |

Pre-register **pass/fail** before running campaigns; version the scenario suite.

## Sim-to-real

Document gaps explicitly:

| Gap | Mitigation |
|---|---|
| **Sensor noise** | Domain randomization; fine-tune on field bags |
| **Dynamics** | Identify plant model error; limit speed in early field |
| **Latency** | Inject delays in SIL; measure on HIL |
| **Comms** | Drop/jam models before field |

Require **field scenarios** for any behavior not bounded by sim evidence.

## Field testing

| Practice | Rationale |
|---|---|
| **Phased ODD** | Expand only after gates pass |
| **Range safety** | Separate from software skill—follow local procedures |
| **Logging** | Full autonomy trace on every sortie used for release |
| **Rollback** | Known-good config on vehicle before trial |
| **After-action** | Diff logs vs expected; file issues against scenario IDs |

Never use production customer environments for unapproved autonomy experiments.
