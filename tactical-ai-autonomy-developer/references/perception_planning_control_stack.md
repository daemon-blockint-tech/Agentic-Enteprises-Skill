# Perception–planning–control stack

## Table of contents

1. [Pipeline overview](#pipeline-overview)
2. [Perception and fusion](#perception-and-fusion)
3. [Planning and behavior](#planning-and-behavior)
4. [Control and actuation interface](#control-and-actuation-interface)
5. [Learned vs symbolic split](#learned-vs-symbolic-split)
6. [Middleware patterns](#middleware-patterns)
7. [Timing and interfaces](#timing-and-interfaces)

## Pipeline overview

Typical sense-to-act chain (names vary by program):

```
Sensors → calibration/sync → perception → world model → planner/behavior → trajectory/setpoints → control → actuators
                ↑_____________________ safety / rules monitor _____________________↑
```

Assign **owner**, **rate (Hz)**, **max latency (ms)**, and **failure output** per block.

## Perception and fusion

| Concern | Practice |
|---|---|
| **Time sync** | PTP/NTP or hardware sync; per-sensor latency compensation |
| **Calibration** | Intrinsics/extrinsics versioning; field drift checks |
| **Fusion** | Track-level vs grid-level; explicit uncertainty (covariance, confidence) |
| **Outputs** | Stable object IDs, class, velocity, prediction horizon for planner |
| **Degradation** | Single-sensor fallback paths; mark `quality` flags downstream |

Avoid over-specifying vendor SDKs; define **interface contracts** (message fields, frames, timestamps).

## Planning and behavior

| Representation | Use when |
|---|---|
| **Finite state machine** | Few modes, strict sequencing, cert-friendly clarity |
| **Behavior tree** | Reactive tactics, parallel branches, easy abort subtrees |
| **Search / optimization** | Known dynamics, constraint-heavy paths (short horizon) |
| **Learned policy** | High-DOF dynamics with verified safety wrapper |
| **Hybrid** | Learned proposals + symbolic validator (common for tactical edge) |

Document **mode graph**: manual, assisted, autonomous, emergency, mission abort.

## Control and actuation interface

- Planner outputs: waypoints, splines, velocity commands, or low-level setpoints—match actuator controller expectations
- Respect **rate limits**, **saturation**, and **interlocks** from control/embedded peers
- Never bypass hardware estops or mechanical limits in software design docs

## Learned vs symbolic split

| Layer | Symbolic | Learned |
|---|---|---|
| **Perception** | Rules for invalid readings | Detectors, classifiers, trackers |
| **Planning** | Geofences, no-go, COLREGS-style hooks | Local policy, cost maps |
| **Safety** | Hard constraints, veto layer | Anomaly scores (advisory only unless proven) |

**Golden rule:** learned components propose; **safety layer disposes** (allow/deny/clamp/abort).

## Middleware patterns

ROS2-style concepts at high level (implementation-agnostic):

| Pattern | Purpose |
|---|---|
| **Pub/sub topics** | Sensor streams, state estimates, debug viz |
| **Services** | Infrequent config, mission upload, health checks |
| **Actions** | Long-running behaviors with cancel/preempt |
| **Lifecycle nodes** | Ordered bring-up/shutdown; safe inactive states |
| **QoS** | Best-effort sensors vs reliable commands—match semantics |

Name **critical topics** (commands, mode, abort) vs **best-effort** (debug).

## Timing and interfaces

| Artifact | Content |
|---|---|
| **Interface IDL/table** | Fields, units, frame IDs, max age of data |
| **Timing budget table** | Per-stage ms; sum ≤ chain deadline |
| **Stale data policy** | Hold, replan, or degrade when `age > threshold` |
| **Versioning** | Schema version in header; reject incompatible pairs |

Measure on hardware-in-the-loop or instrumented field rigs—not desktop-only profiling for release claims.
