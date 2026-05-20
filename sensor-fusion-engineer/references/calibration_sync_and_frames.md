# Calibration, synchronization, and frames

## Table of contents

1. [Calibration types](#calibration-types)
2. [Calibration workflow](#calibration-workflow)
3. [Time synchronization](#time-synchronization)
4. [Coordinate frames](#coordinate-frames)
5. [Validation checks](#validation-checks)

## Calibration types

| Type | What it fixes | Typical method |
|---|---|---|
| **Intrinsic (camera)** | Focal length, distortion | Checkerboard / target field |
| **Extrinsic (sensor–sensor)** | Relative pose | Target-based, hand-eye, SLAM-assisted |
| **IMU–vehicle** | Mount misalignment, biases | Static poses, maneuvers, Allan variance |
| **LiDAR–camera** | Projection alignment | Target corners, edge alignment metrics |
| **Radar boresight** | Azimuth/elevation offset | Corner reflectors, known geometry |
| **GNSS antenna lever arm** | Phase center vs body frame | Survey, CAD + fine tune |

Record **temperature** and **vibration** sensitivity where relevant; plan recalibration triggers.

## Calibration workflow

1. **Define acceptance metrics** — reprojection error (px), plane fit residual (m), yaw error (deg), velocity residual
2. **Collect calibration sequences** — coverage of FOV, range, motion excitation for IMU
3. **Estimate offline** — store parameters with version, date, rig ID, operator
4. **Validate on hold-out** — separate logs/scenes not used in solve
5. **Monitor in field** — online checks (reprojection drift, gravity direction, ground plane)

Maintain **calibration artifact store**: YAML/URDF snippets, not only binary blobs.

## Time synchronization

| Mechanism | Use when | Pitfalls |
|---|---|---|
| **PTP (IEEE 1588)** | Multi-sensor rig on Ethernet | Switch config, master clock choice |
| **Hardware trigger** | Cameras + LiDAR shutter alignment | Cable length, exposure rolling shutter |
| **Per-sensor timestamps** | Heterogeneous buses | Host receive time ≠ capture time |
| **Software sync** | Legacy or COTS sensors | Jitter, NTP unsuitable for fusion |

Policies to document:

- **Interpolation vs extrapolation** for measurements arriving between filter updates
- **Maximum time offset** before reject measurement
- **Out-of-order** message handling in replay vs live

## Coordinate frames

Standard conventions (adapt to program, document explicitly):

| Frame | Typical ID | Notes |
|---|---|---|
| World / map | `map`, `odom` | Fixed or drifting per odometry choice |
| Body | `base_link` | Vehicle centroid or IMU |
| Sensor | `lidar`, `camera_optical` | Optical vs ROS camera frame |
| Earth | ENU/NED | GNSS integration |

**TF tree rules:**

- Single authority for each transform; avoid duplicate publishers
- Static extrinsics in URDF; dynamic via state estimator where needed
- **Lever arms** from rotation center to each sensor phase center

## Validation checks

| Check | Pass indicator |
|---|---|
| Reprojection | Mean/max error below threshold across FOV |
| LiDAR–camera color/depth | Edge alignment on known objects |
| IMU gravity | Magnitude ~9.81 m/s² in static; axis consistent with vehicle |
| Round-trip | Transform A→B→A ≈ identity within tolerance |
| Sync | Residual motion when projecting LiDAR across camera exposure window |

Flag **rolling shutter** and **motion distortion** on cameras/LiDAR before blaming the filter.
