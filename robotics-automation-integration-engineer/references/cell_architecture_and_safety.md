# Cell architecture and safety

## Table of contents

1. [Cell layout zones](#cell-layout-zones)
2. [Access modes](#access-modes)
3. [Safety device integration](#safety-device-integration)
4. [Reset and recovery](#reset-and-recovery)
5. [Documentation for safety review](#documentation-for-safety-review)

## Cell layout zones

| Zone | Typical contents | Integration notes |
|---|---|---|
| Robot work envelope | Arm, gripper, fixtures | Clear interference volumes; teach limits vs. hard limits |
| Operator load/unload | Manual stations, light curtains | Muting rules documented; never software-only |
| Conveyor path | Belts, transfers, accumulation | Jam sensors, photo eyes, encoder feedback to PLC |
| AMR approach | Dock, V-marker, RFID | Approach speed, station ID, handshake before robot move |
| Maintenance | Service positions, lockout points | LOTO alignment with control power segmentation |

Produce a **zone diagram** linking physical areas to safety inputs and control permissives.

## Access modes

| Mode | Control behavior | Integration checks |
|---|---|---|
| Production auto | Full sequence | All safety devices closed; no teach pendant override |
| Manual / teach | Reduced speed, jog | Key switch or mode selector; cobot reduced mode enforced |
| Setup | Step, dry cycle | Light curtain muted only per approved procedure |
| Fault | Hold, safe state | STO where required; clear fault taxonomy |
| Maintenance | LOTO | Control power off; verify stored energy (grippers, springs) |

Document **mode entry/exit conditions** and which subsystems must agree (PLC, robot controller, AMR fleet).

## Safety device integration

| Device | Typical integration | Caution |
|---|---|---|
| E-stop (category per design) | Hardwired chain to safety relay / safety PLC | Do not route only through standard PLC without analysis |
| Light curtain | OSSD to safety inputs; muting via safety module | Muting timers and conditions are safety-engineered |
| Area scanner | Zone sets for speed limit or stop | Field validation after layout changes |
| Door interlock | Trapped key or solenoid lock | Run mode only when closed and locked |
| STO | Drive-specific safe stop | Confirm robot vendor STO vs. category stop |
| Pressure mats / edges | Optional perimeter | Test edge cases at door transitions |

**Integration engineer delivers:** device list, wiring interface sheet, signal names, expected safe state on trip—not SIL proof.

## Reset and recovery

1. **Identify trip cause** — safety vs. process fault vs. robot alarm
2. **Clear hazard** — personnel out, tooling safe, AMR path clear
3. **Safety reset** — twist reset, OSSD clear, safety PLC acknowledge per design
4. **Control reset** — PLC fault ack, robot alarm reset, vision re-arm
5. **Homing / re-sync** — axis home, tool frame verify, conveyor clear
6. **Production resume** — first-cycle slow speed if policy requires

Define **forbidden auto-restart** conditions (e-stop pressed, gate open, vision fail).

## Documentation for safety review

Provide to site safety / integrator:

- Safety IO list with device tag, function, and normal state
- Sequence diagram showing safety permissives gating motion
- Muting matrix (if any)—sensor, condition, max duration, operator presence
- STO and stop category mapping per axis/drive
- Known limitations (e.g., cobot hand-guiding only in teach mode)

Do not claim compliance with ISO 10218, ISO 3691-4, or local regulations without qualified review.
