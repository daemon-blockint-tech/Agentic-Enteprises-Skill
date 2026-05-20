# Multi-sensor association and tracking

## Table of contents

1. [Data association](#data-association)
2. [Gating](#gating)
3. [Assignment algorithms](#assignment-algorithms)
4. [Track lifecycle](#track-lifecycle)
5. [MOT metrics](#mot-metrics)

## Data association

**Problem:** match measurements (detections, clusters, radar returns) to existing tracks or new births.

| Association style | Description |
|---|---|
| **Nearest neighbor** | Simple; fails in clutter |
| **Global nearest neighbor** | One-to-one per scan |
| **JPDA** | Probabilistic weights on multiple hypotheses (concept) |
| **MHT** | Maintain hypothesis tree; deferred decisions |

For multi-sensor fusion, clarify **association level**:

- Per-sensor then fuse tracks (track-to-track)
- Fuse detections in common frame then associate (early fusion)
- Hybrid: camera 2D → 3D lift then LiDAR association

## Gating

Reject unlikely pairs before assignment.

| Gate type | Domain |
|---|---|
| **Mahalanobis** | State space with innovation covariance |
| **Euclidean / IoU** | Image boxes, BEV distance |
| **Gate on velocity** | Kinematic feasibility |
| **Sensor-specific** | Radar range-rate, LiDAR height band |

Document **gate thresholds** per class and range; tune with labeled data where possible.

**Clutter:** uniform or Poisson clutter models inform expected false associations; adjust birth threshold.

## Assignment algorithms

| Algorithm | Complexity | Notes |
|---|---|---|
| **Hungarian (Munkres)** | \(O(n^3)\) | Standard for rectangular cost matrices |
| **Greedy** | Lower | Acceptable when gates are tight |
| **Auction / JV** | Variants | Large sparse problems |

**Cost matrix** examples: negative log likelihood, Mahalanobis distance, weighted sum of position + appearance (high level).

## Track lifecycle

| State | Entry | Exit |
|---|---|---|
| **Tentative** | First detection(s) | Confirmed after M hits / N scans |
| **Confirmed** | Promotion | Coast → delete on miss |
| **Coasted** | Missed detections | Reacquire or terminate |
| **Merged/split** | Proximity events | Policy to avoid ID swap |

Rules to specify:

- **M-of-N** confirmation for radar/low \(P_d\) sensors
- **Coast limit** (time and distance) before delete
- **Duplicate track** suppression when two tracks lock same object
- **Track quality score** for downstream (planner consumes only Q > τ)

## MOT metrics

| Metric | Meaning |
|---|---|
| **MOTA** | Overall accuracy (misses, FP, mismatches) |
| **MOTP** | Localization precision |
| **IDF1 / ID switches** | Identity consistency |
| **HOTA** | Unified det + assoc (modern benchmark) |
| **Fragmentation** | Track breaks per object |

Report **per scenario class** (urban, highway, pedestrian-heavy) not only aggregate.

Pair with **fusion latency** and **track age** at handoff to planning.
