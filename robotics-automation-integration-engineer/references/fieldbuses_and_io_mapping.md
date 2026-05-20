# Fieldbuses and I/O mapping

## Table of contents

1. [Protocol selection](#protocol-selection)
2. [Network topology](#network topology)
3. [Device configuration](#device-configuration)
4. [I/O mapping process](#io-mapping-process)
5. [Diagnostics and commissioning](#diagnostics-and-commissioning)

## Protocol selection

| Protocol | Typical use in robotics cells | Integration artifacts |
|---|---|---|
| Profinet | Siemens PLC, IO-Link masters, some robot adapters | GSDML, device names, I&M data |
| EtherNet/IP | Rockwell PLC, many U.S. robots and VFDs | EDS, RPI, connection sizes |
| EtherCAT | PC-based control, motion-heavy peripherals | ESI, distributed clock if used |
| Modbus TCP/RTU | Legacy VFDs, simple devices, gateways | Register map, endianness |
| OPC UA | MES, SCADA, cloud bridges (not fieldbus replacement) | NodeId map, security certs |

Prefer **one primary industrial Ethernet** per cell segment; use gateways deliberately with documented latency.

## Network topology

- **Cell switch** — managed switch with VLAN if OT policy requires; document port list
- **Robot controller** — often dual-port; avoid unintended loops; disable unused protocols
- **PLC / PC control** — scanner/adapter roles per vendor; fixed IP or DCP as policy dictates
- **AMR wireless** — separate from robot cable plant; coordinate handoff AP coverage with fleet vendor
- **Time sync** — IEEE 1588 only where required (vision sync, EtherCAT DC); otherwise document clock source

Deliver **one-line diagram**: IPs, device names, cable IDs, patch panel references.

## Device configuration

| Step | Action |
|---|---|
| 1 | Import GSD/EDS/ESI; verify firmware compatibility |
| 2 | Assign device names and IP (or DCP reservation) |
| 3 | Configure modules/slots to match physical IO |
| 4 | Set watchdog / connection parameters (RPI, cycle time) |
| 5 | Export project archive for version control |

Record **firmware versions** in as-built—robot, PLC, safety PLC, drives, camera.

## I/O mapping process

Build a **signal dictionary** (spreadsheet or DB) with columns:

| Column | Example |
|---|---|
| Signal ID | `CELL01_ROB_READY` |
| Source device | Robot controller DI map |
| Destination | PLC `%I0.0` or tag |
| Type | BOOL / INT / REAL |
| Direction | Robot → PLC |
| Description | Robot ready for cycle start |
| Safe state | FALSE on comm loss |
| Debounce | 50 ms |
| Interlock | Must be TRUE before `CONV_RUN` |

Group signals by **handshake phase**: power, enable, cycle, fault, maintenance.

## Diagnostics and commissioning

- Ping and name resolution check before download
- Bus diagnostics: lost frames, device not found, wrong module
- Force table for FAT—map forces to physical pins with sign-off
- Document **comm loss behavior**—hold last state vs. fail-safe per signal class
- Capture Wireshark only under OT security approval (`scada-ics-cyber-security-specialist`)

For control-scan logic inside PLC, hand detailed loop design to `control-software-developer`.
