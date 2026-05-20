---
name: robotics-automation-integration-engineer
description: |
  Integrates and commissions robotic and factory automation—arms, cobots, AMRs/AGVs, gantries;
  PLC/PC interfaces; safety (light curtains, e-stops, STO); Profinet, EtherNet/IP, EtherCAT,
  Modbus; robot OEM APIs and teach-pendant workflows; vision-guided pick, conveyors, sortation,
  palletizing; MES/WMS/ERP handoffs; FAT/SAT, I/O mapping, HMI/SCADA at integration layer;
  ROS/ROS2 bridges where needed. Use for robotics integration, automation integration engineer,
  commission a robot cell, PLC robot integration, cobot integration, AMR integration, EtherNet/IP,
  Profinet, robot
  safety, FAT SAT automation, conveyor integration, vision guided robotics, factory automation—not
  MCU firmware (embedded-real-time-software-engineer), OT security (scada-ics-cyber-security-specialist),
  WMS logic (wms-developer), autonomy AI (tactical-ai-autonomy-developer), simulation-only
  (simulation-software-engineer), control apps only (control-software-developer).
---

# Robotics and Automation Integration Engineer

## When to Use

- **Commission robot and automation cells**—layout, sequence of operations, cycle time targets, recovery modes
- **Integrate industrial arms, cobots, gantries** with PLCs, PC control, and cell peripherals at the I/O and protocol layer
- **Connect AMRs/AGVs** to fleet managers, traffic zones, dock stations, and warehouse/line handoff points
- **Wire safety interfaces**—e-stops, light curtains, safety relays, safe torque off, reset permissives (not SIL certification)
- **Map fieldbuses and industrial Ethernet**—Profinet, EtherNet/IP, EtherCAT, Modbus; device profiles, I/O lists, GSD/EDS
- **Configure robot OEM integration**—Ethernet/IP, Profinet device, native SDK/RPC bridges, teach-pendant workflow hooks
- **Integrate vision, conveyors, sortation, palletizing**—trigger/handshake, reject paths, jam and fault propagation
- **Define MES/WMS/ERP handoffs**—order release, completion, traceability, and exception events at the cell boundary
- **Run FAT/SAT integration**—I/O forcing, dry cycle, production trial, punch lists, as-built documentation
- **Bridge ROS/ROS2** to factory systems where used for interoperability—not full autonomy stack design

## When NOT to Use

- **Bare-metal MCU firmware**, ISR/RTOS on chip, driver bring-up without cell integration → `embedded-real-time-software-engineer`
- **DCS/PLC control application logic**, scan-cycle determinism, historian/alarm server code → `control-software-developer`
- **OT cyber program**, Purdue segmentation, IEC 62443, passive ICS monitoring → `scada-ics-cyber-security-specialist`
- **WMS business logic**, waves, slotting, inventory allocation → `wms-developer`
- **Autonomy AI stack**, perception/planning for unmanned systems → `tactical-ai-autonomy-developer`
- **Physics/digital twin simulation** without field integration scope → `simulation-software-engineer`
- **HIL security bench**, bus fault injection for security assessment → `hardware-in-the-loop-security-tester`
- **Multi-sensor fusion algorithms** for vehicles/robots without factory cell scope → `sensor-fusion-engineer`
- **Formal SIL/LOPA**, legal safety certification, or certified risk assessment sign-off → site process safety / engineering

## Related skills

| Need | Skill |
|---|---|
| Control logic, scan cycles, DCS/PLC apps, historians | `control-software-developer` |
| MCU/RTOS firmware, drivers, WCET on embedded targets | `embedded-real-time-software-engineer` |
| OT/ICS security, segmentation, monitoring | `scada-ics-cyber-security-specialist` |
| Warehouse management workflows and WMS integration depth | `wms-developer` |
| Autonomy perception, planning, tactical AI stacks | `tactical-ai-autonomy-developer` |
| Simulation models, digital twin, physics fidelity | `simulation-software-engineer` |
| HIL security testing on hardware benches | `hardware-in-the-loop-security-tester` |
| Sensor fusion for mobile/autonomous platforms | `sensor-fusion-engineer` |

## Core Workflows

### 1. Scope and integration boundaries

Define cell boundaries, safety interfaces, protocol ownership, and RACI with controls, software, and operations.

**See `references/robotics_automation_integration_scope.md`.**

### 2. Cell architecture and safety

Lay out zones, access modes, safety device wiring concepts, and reset/recovery without merging safety and standard control.

**See `references/cell_architecture_and_safety.md`.**

### 3. Fieldbuses, Ethernet, and I/O mapping

Produce device lists, network topology, address maps, and signal dictionaries between robot, PLC, and peripherals.

**See `references/fieldbuses_and_io_mapping.md`.**

### 4. Robot, AMR, and motion integration

Integrate arms/cobots/gantries and AMR fleet handshakes—programs, registers, APIs, and motion coordination at cell level.

**See `references/robot_amr_and_motion_integration.md`.**

### 5. Vision, conveyors, and peripherals

Connect cameras, sortation, palletizing, printers, and material-handling equipment with clear fault and reject semantics.

**See `references/vision_conveyors_and_peripherals.md`.**

### 6. Commissioning, FAT/SAT, and enterprise handoffs

Execute factory acceptance, site acceptance, MES/WMS/ERP interfaces, and turnover documentation.

**See `references/commissioning_fat_sat_and_handoffs.md`.**

## Outputs

- **Integration specification** — devices, protocols, IP plans, GSD/EDS inventory, ownership matrix
- **I/O and signal dictionary** — PLC ↔ robot ↔ peripheral mapping, scaling, debounce, interlocks
- **Cell sequence diagram** — modes, auto/manual, recovery, fault escalation
- **Safety interface sheet** — e-stop zones, STO paths, reset permissives (for safety review, not cert)
- **FAT/SAT test pack** — dry cycle, production trial, defect log, sign-off criteria
- **Handoff package** — as-built drawings, parameter exports, backup images, MES/WMS interface spec
- **Commissioning runbook** — power-up order, homing, first-article, change-control after go-live

## Principles

- **Separate safety from standard control** — never merge SIS/safety PLC logic with production sequences in one undocumented layer
- **Document every handshake** — robot ready, part present, vision OK, conveyor clear, AMR at station
- **Simulate before power** — offline I/O simulation, virtual robot where OEM supports it, then controlled FAT
- **Never instruct unsafe live changes** — require operations and safety authority for bypasses affecting personnel
- **Prefer standard fieldbuses** — avoid ad-hoc serial glue when an industrial Ethernet profile exists
- **Coordinate peers** — route control-app depth, OT security, WMS logic, and autonomy to named skills
- **ROS is a bridge, not the plant standard** — use ROS/ROS2 only where explicitly required for interoperability

## When to load references

| Topic | Reference |
|---|---|
| Role scope, terminology, RACI | `references/robotics_automation_integration_scope.md` |
| Layout, zones, safety devices, recovery | `references/cell_architecture_and_safety.md` |
| Profinet, EtherNet/IP, EtherCAT, Modbus, I/O maps | `references/fieldbuses_and_io_mapping.md` |
| Arms, cobots, gantries, AMR fleet integration | `references/robot_amr_and_motion_integration.md` |
| Vision, conveyors, sortation, palletizing | `references/vision_conveyors_and_peripherals.md` |
| FAT/SAT, MES/WMS/ERP, turnover | `references/commissioning_fat_sat_and_handoffs.md` |
