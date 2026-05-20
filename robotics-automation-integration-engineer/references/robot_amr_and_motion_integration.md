# Robot, AMR, and motion integration

## Table of contents

1. [Industrial robot integration](#industrial-robot-integration)
2. [Cobot specifics](#cobot-specifics)
3. [Gantry and external axes](#gantry-and-external-axes)
4. [AMR and AGV fleet integration](#amr-and-agv-fleet-integration)
5. [Coordination and collision avoidance](#coordination-and-collision-avoidance)
6. [ROS and ROS2 bridges](#ros-and-ros2-bridges)

## Industrial robot integration

| Layer | Integration focus |
|---|---|
| Electrical | STO, brake release, cabinet interlocks |
| Fieldbus | Adapter device, implicit/explicit messaging |
| Discrete I/O | Cycle start, busy, complete, fault, gripper OK |
| Program interface | Main job selection, subprograms, data registers |
| TCP / frames | Tool and user frames verified against mechanical CAD |

**Teach pendant workflow (integration level):** document job numbers, data registries used for PLC handshake, and who may alter paths after FAT sign-off.

Avoid deep motion tuning in this skill—focus on **interfaces and commissioning**.

## Cobot specifics

- Confirm **reduced mode** when persons in shared space
- Speed/separation monitoring if used—sensor placement per integrator
- Hand-guiding only in authorized modes
- Application standards (ISO 10218-2, TS 15066) referenced by safety team—not certified here

## Gantry and external axes

- Synchronize robot kinematics with linear/rotary external axes
- Shared estop and enable chain across drives
- Homing order documented (gantry first vs. robot first)
- Soft limits in both robot and motion controller—must agree

## AMR and AGV fleet integration

| Handshake | Typical signals / messages |
|---|---|
| Mission request | WMS/MES → fleet manager → AMR |
| Station approach | Zone clear, door open, floor marker |
| Docked / arrived | PLC permissive to robot or conveyor |
| Load/unload complete | Weight or presence verify |
| Depart | Clear station, close door, release zone |

Document **station IDs**, **traffic rules**, and **fire/evacuation** behavior with fleet vendor.

Warehouse rule depth → `wms-developer`; cell I/O here.

## Coordination and collision avoidance

- **Interlocks** — robot cannot enter volume while AMR present
- **Mutual exclusion zones** — PLC bits or fleet API locks
- **Predictable idle positions** — robot park point when AMR docks
- **Single source of truth** for “cell clear” before motion enable

Use **sequence charts** for multi-device cycles; avoid hidden race conditions in parallel threads.

## ROS and ROS2 bridges

Use only when required (research cells, mixed-vendor glue):

| Pattern | When |
|---|---|
| `rosbridge` / OPC UA shim | Lab or pilot lines |
| Custom node publishing PLC tags | Prototype—harden before production |
| Fleet ROS API | Some AMR vendors expose ROS topics |

Production lines should prefer **industrial Ethernet + PLC** over ROS for determinism and supportability.

Autonomy algorithms → `tactical-ai-autonomy-developer`; physics models → `simulation-software-engineer`.
