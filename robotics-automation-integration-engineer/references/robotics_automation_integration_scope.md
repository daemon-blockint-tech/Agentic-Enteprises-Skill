# Robotics and automation integration scope

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Roles and RACI](#roles-and-raci)
6. [Handoffs](#handoffs)

## Purpose

Define **robotics and factory automation integration** boundaries—connecting robots, AMRs, PLCs, peripherals, vision, and enterprise systems into runnable production cells.

This skill covers **integration design, commissioning, and acceptance**—not autonomy research, WMS product logic, or OT security program ownership.

## Terminology

| Term | Meaning |
|---|---|
| Cell | Bounded automation unit—robot(s), conveyor, vision, safety fence, control panel |
| Cobot | Collaborative robot—often speed/force limited; shared workspace safeguards |
| AMR / AGV | Autonomous or guided mobile robot for material transport |
| STO | Safe torque off—drive power removal on safety demand |
| FAT / SAT | Factory / site acceptance test—integration verification before and after install |
| Handshake | Discrete signals or messages sequencing two subsystems (e.g., robot ↔ PLC) |
| GSD / EDS | Device description files for Profinet / EtherNet/IP configuration |
| MES / WMS / ERP | Manufacturing execution, warehouse, enterprise resource planning interfaces |

## In scope

| Area | Examples |
|---|---|
| Cell integration | Multi-device sequencing, mode management, fault aggregation |
| Robot OEM interfaces | Ethernet/IP adapter, Profinet device, vendor SDK/RPC at integration tier |
| AMR fleet hooks | Mission dispatch, station arrive/leave, traffic zones, charging docks |
| PLC/PC interfaces | I/O mapping, fieldbus devices, HMI tags for cell status |
| Safety integration | E-stop chains, light curtains, STO wiring concepts, reset permissives |
| Fieldbuses | Profinet, EtherNet/IP, EtherCAT, Modbus TCP/RTU device integration |
| Peripherals | Conveyors, vision triggers, printers, grippers, tool changers |
| Enterprise edges | Order release, completion, traceability IDs at cell boundary |
| Commissioning | I/O check, dry cycle, FAT/SAT scripts, as-built docs |
| ROS/ROS2 bridges | Topic/service bridges to PLC or MES where explicitly required |

## Out of scope

| Topic | Route to |
|---|---|
| PLC/DCS control application logic, PID, historian alarms | `control-software-developer` |
| MCU firmware, RTOS, bare-metal drivers | `embedded-real-time-software-engineer` |
| OT segmentation, IEC 62443, ICS monitoring | `scada-ics-cyber-security-specialist` |
| WMS waves, slotting, inventory rules | `wms-developer` |
| Autonomy stack, SLAM, mission planning AI | `tactical-ai-autonomy-developer` |
| Physics simulation, digital twin fidelity | `simulation-software-engineer` |
| HIL security exploitation on benches | `hardware-in-the-loop-security-tester` |
| Sensor fusion algorithms (non-factory) | `sensor-fusion-engineer` |
| SIL calculation, certified risk assessment | Site process safety / engineering |

## Roles and RACI

| Activity | Integration engineer | Controls engineer | Safety engineer | Operations |
|---|---|---|---|---|
| I/O and protocol map | R/A | C | I | I |
| Cell sequence design | R/A | C | C | I |
| Safety device integration | C | C | R/A | I |
| Robot program structure | C | I | I | I |
| FAT/SAT execution | R | C | C | A |
| MES/WMS interface spec | R/A | I | I | C |
| Live bypass of guards | I | I | R/A | A |

*R = responsible, A = accountable, C = consulted, I = informed*

## Handoffs

- **To `control-software-developer`** — scan-cycle logic, alarm models, historian tags beyond cell I/O
- **To `embedded-real-time-software-engineer`** — custom boards, firmware on microcontrollers in tooling
- **To `scada-ics-cyber-security-specialist`** — VLAN design, remote access policy, monitoring agents on OT networks
- **To `wms-developer`** — inventory transactions, pick/put rules, RF workflows behind AMR missions
- **From mechanical/electrical** — layout drawings, device bills of material, safety circuit schematics for review
