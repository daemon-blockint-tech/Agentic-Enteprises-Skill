# Control software scope

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Safety and operational constraints](#safety-and-operational-constraints)
6. [Roles and RACI](#roles-and-raci)
7. [Handoffs](#handoffs)

## Purpose

Define **industrial control application software** boundaries—the logic and integration layers that execute control strategies, exchange process data, and drive HMI/SCADA behavior above field devices.

This skill covers **design, implementation patterns, integration, and deploy planning**—not live plant operation, OT security program ownership, or safety certification.

## Terminology

| Term | Meaning |
|---|---|
| BPCS | Basic process control system—regulatory and sequence control (non-SIS) |
| SIS | Safety instrumented system—separate from BPCS; highest change caution |
| DCS | Distributed control system—integrated controllers and engineering environment |
| PLC | Programmable logic controller—often ladder/ST/function blocks |
| RTU | Remote terminal unit—telemetry and control at remote sites |
| Soft-PLC | PC-based control runtime emulating PLC semantics (IEC 61131 environments) |
| Scan cycle | Periodic execution of control tasks and I/O refresh |
| Historian | Time-series archive of process values and metadata |
| SOE | Sequence of events—timestamped alarm/event ordering |
| MIL / SIL | Model-in-the-loop / software-in-the-loop simulation (high level here) |

## In scope

| Area | Examples |
|---|---|
| Control logic | PID, cascade, ratio, interlocks, sequences, state machines, mode management |
| Integration | OPC UA, Modbus, DNP3, MQTT/AMQP, protocol gateways, quality and timestamps |
| Architecture | Controller partitioning, redundancy, tag model, download areas |
| Data pipelines | Historian sampling, alarm routing, event correlation |
| HMI/SCADA logic | Server scripts, calculations, command validation, faceplate rules |
| Determinism | Scan rate, task order, I/O sync, overrun handling |
| Simulation | MIL/SIL interfaces, stub I/O, regression scenarios (not cert) |
| Deployment | Versioning, staging, rollback, FAT/SAT software hooks |

## Out of scope

| Topic | Route to |
|---|---|
| OT network segmentation, IEC 62443 program, passive monitoring | `scada-ics-cyber-security-specialist` |
| MCU ISR/RTOS, bare-metal drivers, chip WCET | `embedded-real-time-software-engineer` |
| HIL security bench, bus fault injection for security | `hardware-in-the-loop-security-tester` |
| Enterprise web/API backends | `senior-software-engineer` |
| Criticality tiering without control implementation | `mission-critical` |
| HRO culture and organizational prevention metrics | `zero-tolerance-for-failure` |
| SIL/LOPA and formal safety case | Site process safety / engineering |
| Graphics-only HMI design | UX/design skills as appropriate |
| Live CSIRT on OT networks | `incident-responder` + OT security peers |

## Safety and operational constraints

**Never instruct** the agent or operator to:

- Download logic to running production controllers without operations and change-control approval
- Modify SIS logic or bypass interlocks without documented process-safety authorization
- Change setpoints or outputs on live equipment from software examples without site runbooks
- Disable alarms, historians, or audit trails to “fix” performance without risk acceptance

**Prefer instead:**

- Staged controllers, simulation, and maintenance windows per site procedures
- Document tag impacts, rollback packages, and verification checklists before field deploy
- Explicit separation between BPCS application changes and SIS changes

## Roles and RACI

| Activity | Control software dev | Operations | OT security | Process safety | Vendor OEM |
|---|---|---|---|---|---|
| Application logic design | A | C | I | C | C |
| Protocol/integration design | A | I | C | I | C |
| Production download approval | C | A | I | C | C |
| OT hardening and monitoring | I | I | A | I | C |
| SIS logic changes | C | C | I | A | C |
| MIL/SIL test execution | A | C | I | C | C |

## Handoffs

| To skill | When |
|---|---|
| `scada-ics-cyber-security-specialist` | New remote access paths, OPC/MQTT exposure, zone impacts, monitoring use cases |
| `embedded-real-time-software-engineer` | Custom I/O modules, firmware on embedded targets running control runtime |
| `hardware-in-the-loop-security-tester` | Security validation on benches with real controllers and buses |
| `mission-critical` | Tiering, RTO/RPO, redundancy requirements spanning IT/OT |
| `zero-tolerance-for-failure` | Verification gates, pre-mortem, defect-escape prevention for control releases |
