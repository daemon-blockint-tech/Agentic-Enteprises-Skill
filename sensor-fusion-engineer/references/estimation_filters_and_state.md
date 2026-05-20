# Estimation, filters, and state

## Table of contents

1. [State vector patterns](#state-vector-patterns)
2. [Process and measurement models](#process-and-measurement-models)
3. [Kalman-family filters](#kalman-family-filters)
4. [Factor graphs (high level)](#factor-graphs-high-level)
5. [Tuning and consistency](#tuning-and-consistency)

## State vector patterns

| Application | Typical state components |
|---|---|
| **Ego (IMU + GNSS)** | Position, velocity, attitude, IMU biases |
| **Object track (CV model)** | Position, velocity; optional acceleration |
| **Extended object** | Pose, size, shape parameters for LiDAR/radar |
| **Landmark / SLAM** | Landmark positions + ego pose in graph |

Keep state **minimal** for the motion model in use; avoid unobservable states without constraints.

## Process and measurement models

**Process model:** how state evolves between measurements (constant velocity, coordinated turn, IMU propagation).

**Measurement model:** \(h(x)\) mapping state to sensor space (range-bearing, pixel bbox, point cloud plane).

Document for each sensor:

- Expected **nonlinearity** (strong → UKF or iterative EKF)
- **Clutter** and false alarm rate (affects gating, not only R matrix)
- **Detection probability** \(P_d\) vs range/occlusion

## Kalman-family filters

| Filter | When to use | Caveat |
|---|---|---|
| **KF** | Linear Gaussian subsystems | Rare alone in robotics |
| **EKF** | Mild nonlinearity, fast updates | Jacobian quality, consistency |
| **UKF** | Strong nonlinearity in attitude/range | Cost vs EKF |
| **IMM** | Multiple motion models (stop/go) | Model set design, complexity |
| **Particle** | Multimodal, low-D | Curse of dimensionality |

**Update pattern:**

1. Predict with process noise Q (and IMU propagation if applicable)
2. Gate measurements (see association reference)
3. Update with innovation \(y = z - h(\hat{x})\)
4. Monitor innovation statistics

## Factor graphs (high level)

Use when **batch or sliding-window** smoothing helps:

- Visual–inertial odometry, LiDAR odometry + loop closure
- Offline calibration refinement
- Joint optimization of poses and landmarks

Concepts: nodes (variables), factors (constraints), sparse solvers, marginalization for real-time windows.

Do not duplicate a full SLAM product scope unless explicitly in charter—interface poses/tracks to mapping nodes.

## Tuning and consistency

| Knob | Effect |
|---|---|
| **Q** | Responsiveness vs smoothness; too low → lag, too high → noise |
| **R** | Trust in measurements; mis-set R → NEES failure |
| **Initial P** | Transient after track birth; avoid overconfident spawn |

**Consistency checks:**

- **NEES** (Normalized Estimation Error Squared) for Gaussian filters
- **NIS** per sensor stream
- Innovation whiteness (rough check in field)

If NEES ≫ dof: filter overconfident (inflate R, fix calibration). If NEES ≪ dof: over-inflated uncertainty or wrong model.
