# Sensor fusion scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Architecture capture](#architecture-capture)
3. [Sensor inventory template](#sensor-inventory-template)
4. [Latency and compute budget](#latency-and-compute-budget)
5. [What good looks like](#what-good-looks-like)

## Role boundary

| Sensor fusion engineer owns | Others own |
|---|---|
| Multi-sensor world model, tracks, state estimation interfaces | Full autonomy behavior, ROE, geofence, mission abort (`tactical-ai-autonomy-developer`) |
| Calibration/sync/TF for perception sensors | MCU drivers, RTOS, ISR timing (`embedded-real-time-software-engineer`) |
| Association, gating, MOT, filter/graph architecture | PLC/DCS plant logic, historians (`control-software-developer`) |
| Fusion metrics, bag replay, scenario regression | HIL security bench, bus injection (`hardware-in-the-loop-security-tester`) |
| Uncertainty outputs to planning/control | Adversarial ML on detectors unless fusion robustness (`ai-adversarial-robustness-engineer`) |

## Architecture capture

Document before detailed design:

| Dimension | Questions |
|---|---|
| **Platform** | Ground robot, UAS, marine, automotive—operating domain and dynamics |
| **Sensors** | Modalities, models, FOV, range, update rate, failure modes |
| **Outputs** | Tracks, occupancy, ego state, landmarks—for which consumers |
| **Safety** | Which estimates are safety-critical; required integrity/availability |
| **Compute** | Edge SoC vs distributed; GPU/DSA use; hard real-time partitions |
| **Middleware** | ROS2-style topics, lifecycle, recording—pattern level only |
| **Ground truth** | RTK, motion-capture, labeled logs—for calibration and metrics |

## Sensor inventory template

| Sensor | Rate (Hz) | Latency (ms) | Frame | Noise / clutter model | Degraded behavior |
|---|---|---|---|---|---|
| LiDAR | | | | | |
| Camera | | | | | |
| Radar | | | | | |
| IMU | | | | | |
| GNSS | | | | | |
| Wheel/leg odometry | | | | | |

Include **detection pipeline** ownership (learned detector vs geometric) and where fusion attaches (detections vs features vs tracks).

## Latency and compute budget

Chain end-to-end:

```
capture → driver → preprocess → detect → associate → filter → publish
```

For each stage record: typical, p95, max; drop policy when over budget; whether to **hold** last estimate or **coast** tracks.

| Budget item | Typical target (tune per program) |
|---|---|
| Sensor to detection | Platform-specific |
| Detection to track update | ≤ 1–2 sensor periods for tracking |
| Track to planner interface | Contract with planning team |
| Total perception latency | Document vs control loop period |

## What good looks like

- Clear fusion boundary vs autonomy behavior and embedded firmware
- Sensor table with rates, frames, and explicit drop/degrade rules
- Latency budget with measured p95, not only nominal rates
- Downstream contracts: message types, uncertainty fields, max age of data
- Open risks: uncalibrated extrinsics, unsynced cameras, untested GNSS denial
