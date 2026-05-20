# Vision, conveyors, and peripherals

## Table of contents

1. [Vision-guided robotics](#vision-guided-robotics)
2. [Conveyors and sortation](#conveyors-and-sortation)
3. [Palletizing and depalletizing](#palletizing-and-depalletizing)
4. [Grippers, tool changers, and utilities](#grippers-tool-changers-and-utilities)
5. [Fault propagation](#fault-propagation)

## Vision-guided robotics

| Integration element | Detail |
|---|---|
| Trigger | Hardware trigger (encoder, photo eye) vs. software trigger |
| Exposure / lighting | Stable during FAT; document maintenance for bulbs/lenses |
| Result handshake | Pass/fail, pose X/Y/Z/Rx/Ry/Rz, score threshold |
| Calibration | Hand-eye: robot frame ↔ camera frame; record procedure |
| Reject path | Failed parts routed without blocking line |
| Latency budget | Acquire + process + robot approach within takt |

Deliver **vision interface spec**: registers, strings, or fieldbus assembly layout; timeout and retry policy.

Algorithm development for detection → vision vendor or `tactical-ai-autonomy-developer` if ML-heavy; this skill wires results into the cell.

## Conveyors and sortation

| Device | Signals to map |
|---|---|
| Run / stop / jog | PLC outputs, local pendant |
| Photo eyes | Presence, jam, box gap |
| Encoders | Speed match, merge gaps |
| Diverts | Confirm position, failed divert alarm |
| Accumulation | Zero-pressure logic, release to robot pick |

**Jam logic:** stop upstream, notify robot hold, HMI prompt with physical location ID.

Sortation controls at WCS depth may involve `wms-developer` for destination rules; integration engineer defines **PLC ↔ sorter** handshake.

## Palletizing and depalletizing

- Layer patterns from robot or pallet software—version pattern IDs
- Slip sheet, tier sheet, stretch wrapper interlocks
- Height check and load stability sensors
- SKU change procedure: who loads pattern, verification first cycle

## Grippers, tool changers, and utilities

| Peripheral | Integration notes |
|---|---|
| Vacuum / pneumatic gripper | Pressure switch, blow-off timing |
| Tool changer | Lock confirm, tool ID feedback, crash if mismatch |
| Screw feeder | Ready, empty, fault; torque tool via robot |
| Label / inkjet printer | Print complete before release |
| Torque tools | OK/NOK to PLC and traceability record |

Map **analog thresholds** and debounce in signal dictionary (`fieldbuses_and_io_mapping.md`).

## Fault propagation

Define a **cell fault code list**:

| Code class | Example | Downstream action |
|---|---|---|
| Safety trip | Curtain broken | All motion stop, STO |
| Robot alarm | Overtravel | Hold conveyor, display on HMI |
| Vision fail | Low score | Reject, optional retry N times |
| Conveyor jam | PE blocked timeout | Stop upstream, call maintenance |
| AMR fault | Mission aborted | Release station lock, notify WMS |

Avoid duplicate alarms on every device—**root cause** at cell supervisor level where possible.
