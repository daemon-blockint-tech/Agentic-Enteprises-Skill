---
name: sensor-fusion-engineer
description: |
  Guides multi-sensor perception fusion for autonomous and robotic systems—sensor models and noise;
  extrinsic/intrinsic calibration; time synchronization; coordinate frames and transforms; data
  association and gating; Kalman-family filters (EKF/UKF) and factor graphs at high level; track
  management (MOT); LiDAR–camera–radar–IMU–GNSS integration patterns; uncertainty representation;
  evaluation metrics (NEES, RMSE, track continuity); simulation and bag replay. Use when designing
  or debugging fusion stacks, calibration/sync, state estimation, multi-object tracking, sensor
  fusion architecture, fusion metrics, or rosbag/sim replay—not full autonomy behavior and mission
  rules (tactical-ai-autonomy-developer), MCU drivers/RTOS only (embedded-real-time-software-engineer),
  plant PLC/DCS control applications (control-software-developer), HIL security bench testing
  (hardware-in-the-loop-security-tester), or adversarial ML on models unless fusion-robustness focus
  (ai-adversarial-robustness-engineer).
---

# Sensor Fusion Engineer

## When to Use

- Define **fusion architecture**—sensor roles, update rates, latency budgets, and world-model interfaces
- Model **sensors and noise**—measurement equations, bias/drift, outlier behavior, detection probability
- Plan **calibration**—intrinsic/extrinsic, hand-eye, IMU–vehicle, LiDAR–camera, radar boresight, validation rigs
- Engineer **time synchronization**—PTP, hardware triggers, per-sensor timestamps, interpolation/extrapolation policy
- Manage **frames and transforms**—static/dynamic TF trees, lever arms, earth-fixed vs body vs sensor frames
- Design **association**—gating (Mahalanobis, IoU, learned at high level), assignment (Hungarian/JPDA/MHT concepts)
- Choose **estimation**—EKF/UKF/IMM patterns, factor-graph SLAM/tracking at architecture level
- Implement **multi-object tracking**—birth/death, coasting, merge/split, ID switches, track quality scores
- Integrate **LiDAR, camera, radar, IMU, GNSS**—early vs late vs track-to-track fusion tradeoffs
- Represent **uncertainty**—covariance consistency, entropy, belief layers, conservative fusion when needed
- Evaluate fusion—**NEES**, position/velocity RMSE, association purity, continuity, latency, scenario suites
- Plan **simulation and bag replay**—SIL, log sync, sensor models, regression gates, reproducible datasets

## When NOT to Use

- **Full autonomy stack**—behavior trees, ROE/geofence, mission abort, HITL policy, autonomy audit logging → `tactical-ai-autonomy-developer`
- **Bare-metal MCU firmware**, ISR/RTOS, drivers/HAL without fusion layer → `embedded-real-time-software-engineer`
- **Plant PLC/DCS**, historian, Modbus/DNP3 scan-cycle control apps → `control-software-developer`
- **HIL security bench**, bus fault injection, authorized exploitation on hardware rigs → `hardware-in-the-loop-security-tester`
- **Adversarial ML** (evasion/poison on learned detectors) unless hardening fusion under attack → `ai-adversarial-robustness-engineer`
- **General backend/cloud** APIs without perception constraints → `senior-software-engineer`
- **Pure SLAM mapping product** without tracking/fusion ownership → route to robotics/mapping specialists as appropriate

## Related skills

| Need | Skill |
|---|---|
| Tactical autonomy, behavior, safety rules, degraded modes | `tactical-ai-autonomy-developer` |
| MCU/RTOS, drivers, WCET, IRQ timing on chip | `embedded-real-time-software-engineer` |
| PLC/DCS, OT protocols, plant control applications | `control-software-developer` |
| HIL security assessment on benches | `hardware-in-the-loop-security-tester` |
| Adversarial robustness on ML perception | `ai-adversarial-robustness-engineer` |
| AI governance and model risk (policy) | `ai-risk-governance` |
| Enterprise backend and cloud services | `senior-software-engineer` |

## Core Workflows

### 1. Scope and fusion boundaries

Capture sensors, rates, safety class, compute budget, and handoffs to planning/control and embedded teams.

**See `references/sensor_fusion_scope.md`.**

### 2. Calibration, sync, and frames

Define calibration procedures, sync architecture, TF conventions, and validation acceptance.

**See `references/calibration_sync_and_frames.md`.**

### 3. Estimation, state, and uncertainty

Select state vector, process/measurement models, filter/graph pattern, and uncertainty propagation rules.

**See `references/estimation_filters_and_state.md`.**

### 4. Association and tracking

Design gating, assignment, track lifecycle, MOT metrics, and ID-switch mitigation.

**See `references/multi_sensor_association_tracking.md`.**

### 5. Multi-sensor fusion patterns

Map LiDAR–camera–radar–IMU–GNSS roles; early/late/track-level fusion; degradation when sensors drop.

**See `references/lidar_camera_radar_fusion.md`.**

### 6. Evaluation, simulation, and metrics

Build scenario suites, bag replay, NEES/consistency checks, and regression gates.

**See `references/evaluation_simulation_and_metrics.md`.**

## Outputs

- **Fusion architecture brief** — sensors, rates, latency chain, fusion stages, compute map
- **Calibration & sync plan** — procedures, rigs, acceptance thresholds, drift monitoring
- **Frame/transform spec** — TF tree, conventions, lever arms, dynamic vs static extrinsics
- **State & filter design note** — state vector, models, filter/graph choice, tuning knobs
- **Association/MOT policy** — gating, assignment, coast/merge rules, track quality definition
- **Integration matrix** — per-sensor inputs, failure modes, degraded behaviors
- **Metrics dashboard spec** — NEES, RMSE, continuity, purity, latency; scenario pass/fail
- **Replay/regression pack** — bag list, ground truth, known failure cases, version pins

## Principles

- **Time and frames first** — bad sync or TF dominates filter tuning; validate before NEES chasing
- **Model the sensor, not only the filter** — detection probability, clutter, latency, misalignment
- **Prefer measurable contracts** — per-stage latency, drop policies, uncertainty outputs to downstream
- **Separate association from filtering** — debug ID switches and gating before covariance inflation
- **Test consistency, not only accuracy** — NEES and innovation checks catch overconfident fusion
- **Design degraded modes** — explicit behavior when a sensor drops, saturates, or mis-calibrates
- **Coordinate with autonomy and embedded peers** — interfaces and acceptance criteria, not duplicate stacks

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries, architecture scope | `references/sensor_fusion_scope.md` |
| Calibration, PTP/sync, transforms | `references/calibration_sync_and_frames.md` |
| EKF/UKF, factor graphs, state vectors | `references/estimation_filters_and_state.md` |
| Gating, assignment, MOT lifecycle | `references/multi_sensor_association_tracking.md` |
| LiDAR/camera/radar/IMU/GNSS patterns | `references/lidar_camera_radar_fusion.md` |
| Metrics, bags, simulation, regression | `references/evaluation_simulation_and_metrics.md` |
