---
name: control-software-developer
description: |
  Guides industrial control application software—real-time loops and application layers above field
  devices; DCS/PLC/RTU integration; OPC UA, Modbus, DNP3, MQTT/AMQP; historian and alarm/event
  pipelines; HMI/SCADA server-side logic (not graphics-only); soft-PLC/PC control; deterministic scan
  cycles; MIL/SIL (high level); versioned OT deploy; coordination with OT security/safety without
  owning plant ops. Use for control logic, PLC/DCS apps, protocol integration, historian/alarms, SCADA
  server logic, scan-cycle determinism, MIL/SIL planning, OT software deployment—not OT cyber only
  (scada-ics-cyber-security-specialist), MCU firmware only (embedded-real-time-software-engineer),
  HIL security bench (hardware-in-the-loop-security-tester), enterprise web/backend
  (senior-software-engineer), tiering without control depth (mission-critical), HRO only
  (zero-tolerance-for-failure).
---

# Control Software Developer

## When to Use

- Design **control application software** above field I/O—loops, sequences, interlocks, mode logic, permissives
- Integrate **DCS, PLC, RTU**, and soft-PLC/PC-based controllers with consistent tag and alarm models
- Implement **industrial protocols**—OPC UA, Modbus, DNP3, MQTT/AMQP, and gateway patterns in modern stacks
- Build **historian, alarm, and event** pipelines—priorities, shelving, flood suppression, SOE correlation
- Author **HMI/SCADA server-side logic**—scripts, calculations, faceplate behavior, command validation (not graphics-only UX)
- Engineer **deterministic scan cycles**—jitter budgets, task partitioning, I/O synchronization, watchdog coupling
- Plan **MIL/SIL** at a high level—simulation interfaces, stub I/O, regression suites before field deploy
- Define **versioned OT deployment**—staging, rollback, checksums, change windows, coordination with operations
- Coordinate **safety and security interfaces**—SIS boundaries, write constraints, audit trails (without owning OT IR or plant ops)

## When NOT to Use

- **OT cyber program**, Purdue segmentation, IEC 62443 gap assessment, passive ICS monitoring → `scada-ics-cyber-security-specialist`
- **Bare-metal MCU firmware**, ISR/RTOS on chip, WCET on MCU, driver bring-up without plant application layer → `embedded-real-time-software-engineer` (unless implementing control stack on that target)
- **HIL security bench**, bus fault injection, authorized exploitation on hardware rigs → `hardware-in-the-loop-security-tester`
- **Generic backend**, APIs, microservices, or cloud SaaS without control-cycle constraints → `senior-software-engineer`
- **Criticality tiering**, RTO/RPO, enterprise redundancy patterns without control logic → `mission-critical`
- **HRO culture**, stop-the-line, defect-escape metrics without implementation → `zero-tolerance-for-failure`
- **Process safety engineering** (SIL calculation, LOPA) or legal certification claims → site process safety / engineering
- **HMI graphics-only** UX, branding, or visual design systems → design/frontend skills as appropriate

## Related skills

| Need | Skill |
|---|---|
| OT/ICS security, segmentation, monitoring, hardening roadmaps | `scada-ics-cyber-security-specialist` |
| MCU/RTOS firmware, drivers, WCET on embedded targets | `embedded-real-time-software-engineer` |
| HIL security assessment, bus injection on benches | `hardware-in-the-loop-security-tester` |
| Mission-critical tiering, availability objectives | `mission-critical` |
| Failure-prevention culture, verification gates, FMEA mindset | `zero-tolerance-for-failure` |
| Enterprise backend and cloud services | `senior-software-engineer` |
| SRE SLOs and service reliability (IT/cloud) | `site-reliability-engineer` |
| BCM/DR program and crisis continuity | `bcm-disaster-recovery-specialist` |

## Core Workflows

### 1. Scope and role boundaries

Define control-application boundaries, safety interfaces, and handoffs with operations, OT security, and embedded teams.

**See `references/control_software_scope.md`.**

### 2. Real-time loops and determinism

Design scan cycles, loop execution order, jitter acceptance, and synchronization with I/O and higher-level applications.

**See `references/realtime_loops_and_determinism.md`.**

### 3. Industrial protocols and integration

Select protocol stacks, address mapping, quality flags, gateway placement, and back-pressure for historians and cloud bridges.

**See `references/industrial_protocols_and_integration.md`.**

### 4. DCS / PLC / RTU architecture

Partition logic across controllers, redundancy, download semantics, and engineering workstation workflows.

**See `references/dcs_plc_rtu_architecture.md`.**

### 5. Historians, alarms, and HMI logic

Model alarms, events, shelving, historian compression, and server-side HMI/SCADA behavior.

**See `references/historians_alarms_and_hmi_logic.md`.**

### 6. Deployment, testing, and safety coordination

Plan FAT/SAT hooks, MIL/SIL staging, versioned deploy, rollback, and coordination with OT security without unsafe live changes.

**See `references/deployment_testing_and_safety.md`.**

## Outputs

- **Control application design** — loops, sequences, modes, interlocks, tag dictionary, execution order
- **Integration specification** — protocol roles, endpoints, scan rates, exception handling, gateway map
- **Scan-cycle and timing budget** — cycle time, task split, I/O latency, watchdog and overrun handling
- **Alarm and event model** — priorities, classes, shelving rules, flood logic, SOE requirements
- **Historian pipeline design** — sampling, compression, retention, archival handoff
- **HMI/SCADA logic spec** — server scripts, validations, command gating (not screen mockups alone)
- **Deploy and rollback runbook** — versions, checksums, staging path, verification steps, operations sign-off
- **MIL/SIL test outline** — stubs, scenarios, acceptance criteria (high level; not safety certification)
- **Handoff notes for OT security** — attack surfaces introduced by new integrations (for `scada-ics-cyber-security-specialist`)

## Principles

- **Respect scan-cycle determinism** — document cycle time, execution order, and overrun behavior before optimizing
- **Keep safety systems separate** — do not merge SIS/BPCS logic; enforce write constraints and proven separation
- **Never instruct unsafe live-plant changes** — require operations authorization for downloads affecting running process
- **Prefer simulation before field** — MIL/SIL and staged controllers before production OT networks
- **Version everything** — logic, configs, HMI server scripts, and protocol maps with traceable deploy artifacts
- **Coordinate, do not own OT security or plant ops** — frame risks and interfaces; route hardening and operations decisions to peers
- **Separate graphics from control logic** — HMI pixels are not a substitute for documented server-side behavior and alarms

## When to load references

| Topic | Reference |
|---|---|
| Role scope, terminology, RACI | `references/control_software_scope.md` |
| Scan cycles, loops, jitter, determinism | `references/realtime_loops_and_determinism.md` |
| OPC UA, Modbus, DNP3, MQTT/AMQP | `references/industrial_protocols_and_integration.md` |
| DCS, PLC, RTU, soft-PLC patterns | `references/dcs_plc_rtu_architecture.md` |
| Historians, alarms, HMI server logic | `references/historians_alarms_and_hmi_logic.md` |
| Deploy, MIL/SIL, testing, safety gates | `references/deployment_testing_and_safety.md` |
