# Degraded modes and fail-safe

## Table of contents

1. [Failure taxonomy](#failure-taxonomy)
2. [Mode state machine](#mode-state-machine)
3. [Detection and hysteresis](#detection-and-hysteresis)
4. [Safe outcomes](#safe-outcomes)
5. [Recovery](#recovery)
6. [Testing degraded paths](#testing-degraded-paths)

## Failure taxonomy

| Domain | Examples | Typical autonomy response |
|---|---|---|
| **Sensor** | Camera blur, lidar dropout, IMU bias spike | Reduce speed; switch sensor; hold |
| **Estimation** | SLAM divergence, GPS jam | Dead-reckon window then RTL |
| **Planning** | No feasible path, solver timeout | Hover/hold; request human |
| **Comms** | Link loss, high latency | Pre-planned BLOS behavior |
| **Compute** | Thermal throttle, process crash | Watchdog → safe mode |
| **Power** | Low battery | Forced RTB or land |

Map each to **detected by**, **debounce**, **mode transition**, **logged code**.

## Mode state machine

Example modes (rename per program):

```
INIT → STANDBY → ARMED → AUTONOMOUS ⇄ ASSISTED
                    ↓         ↓
                 DEGRADED ←──┘
                    ↓
              SAFE_HOLD / RTL / LAND / ABORT
```

Rules:

- **Single writer** for mode authority (avoid races between planner and UI)
- **Explicit transitions** only; no silent skip of DEGRADED
- **Entry actions** (e.g., clear integrators, announce to operator)

## Detection and hysteresis

| Pitfall | Mitigation |
|---|---|
| Flapping on threshold | Enter/exit thresholds; minimum dwell time |
| Stale data treated fresh | Timestamp + max age per input |
| Cascading faults | Priority table: abort > RTL > degrade > nominal |

Publish **health bitmap** or structured diagnostics for HITL displays.

## Safe outcomes

| Outcome | When appropriate |
|---|---|
| **Hold position** | Short planner fault; protected airspace |
| **RTL** | Navigation uncertainty; comms loss with home known |
| **Land in place** | RTL not viable; energy critical |
| **Manual passthrough** | Operator takeover available |
| **Terminate mission segment** | Task-only abort; vehicle still controllable |

Fail-safe defaults should be **conservative** when uncertainty is high—prefer smaller ODD over aggressive continuation.

## Recovery

| Question | Policy |
|---|---|
| **Auto-recover to AUTONOMOUS?** | Only if fault cleared N seconds + self-test pass |
| **Human ack required?** | After ABORT or rules violation |
| **Partial perception** | Define minimum sensor set per mode |

Log **recovery attempts** and reasons for denial.

## Testing degraded paths

- Inject faults in SIL/HIL per scenario ID
- Verify **no geofence violation** during degradation
- Measure **time in each mode** on field logs
- Regression: any change to detection thresholds reruns fault suite

Coordinate with `embedded-real-time-software-engineer` on watchdog and `control-software-developer` on actuator interlocks where platforms overlap.
