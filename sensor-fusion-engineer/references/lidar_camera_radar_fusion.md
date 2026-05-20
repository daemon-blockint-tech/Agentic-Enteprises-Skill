# LiDAR, camera, radar, IMU, and GNSS fusion

## Table of contents

1. [Fusion taxonomy](#fusion-taxonomy)
2. [Modality strengths](#modality-strengths)
3. [Integration patterns](#integration-patterns)
4. [Degraded modes](#degraded-modes)
5. [Common failure modes](#common-failure-modes)

## Fusion taxonomy

| Stage | What is fused | Pros | Cons |
|---|---|---|---|
| **Early (data-level)** | Raw or preprocessed signals | Rich correlation | Alignment, sync, compute heavy |
| **Middle (feature-level)** | Embeddings, voxels, depth | Balance | Pipeline coupling |
| **Late (decision-level)** | Detections or tracks | Modular sensors | Double counting, timing |
| **Track-to-track** | Independent trackers merged | Sensor autonomy | Association at track level |

Choose based on **sync quality**, **calibration stability**, and **team ownership** per sensor stack.

## Modality strengths

| Sensor | Strong for | Weak for |
|---|---|---|
| **LiDAR** | Range, geometry, night | Weather, long range cost, reflectivity |
| **Camera** | Class, texture, color | Range, glare, night without IR |
| **Radar** | Range-rate, weather | Azimuth resolution, clutter |
| **IMU** | High-rate attitude, short-term motion | Drift without aiding |
| **GNSS** | Global position (open sky) | Multipath, denial, latency |

## Integration patterns

### LiDAR + camera

- Project LiDAR points to image for **semantic labeling** or **frustum filtering**
- **Lift** 2D detections with depth from LiDAR/radar/stereo
- **BEV fusion** networks (concept)—shared grid in bird's-eye view
- Validate **time offset** between rolling shutter and spinning LiDAR

### Radar + camera / LiDAR

- Radar **range-rate** anchors velocity; camera/LiDAR refine lateral position
- Guard against **radar multipath** ghosts in association gates
- Doppler ambiguity policies at high speed

### IMU + GNSS (+ wheel)

- **INS/GNSS EKF** for ego; wheel odometry as pseudo-measurement
- **GNSS denial:** switch covariances, use vision/LiDAR odometry constraints
- Document **lever arms** and **antenna phase center**

### Multi-LiDAR / multi-camera

- Unified frame via extrinsics; **overlap FOV** for redundancy
- Per-sensor health flags before fusion weighting

## Degraded modes

| Loss | Mitigation |
|---|---|
| Camera washout / night | Rely on LiDAR/radar; widen gates cautiously |
| LiDAR rain/fog | Radar + IMU; reduce trust in geometry |
| Radar clutter | Raise birth threshold; map-based masking if available |
| GNSS outage | Visual/LiDAR odometry; inflate position uncertainty |
| IMU bias jump | Re-init biases; detect saturation |

Publish **degradation enum** to autonomy stack (`tactical-ai-autonomy-developer`) for behavior changes.

## Common failure modes

- **Stale TF** or wrong extrinsic after shock/vibration
- **Clock skew** causing systematic association bias
- **Overconfident** fusion when one sensor is miscalibrated
- **ID switches** at occlusions—fix association before tuning Q/R
- **Double counting** same object from radar + camera late fusion
- **Latency mismatch**—planner uses old tracks marked as fresh
