# Test bench and safety

## Table of contents

1. [Bench topology](#bench-topology)
2. [Safety interlocks](#safety-interlocks)
3. [Pre-test checklist](#pre-test-checklist)
4. [During test discipline](#during-test-discipline)
5. [Post-test and handoff](#post-test-and-handoff)

## Bench topology

Document a single-line diagram covering:

| Element | Record |
|---|---|
| **Target(s)** | ECU/PLC ID, part number, firmware/hash, security state |
| **Power** | Supply limits, inrush protection, remote enable, kill relay |
| **Plant / HIL** | Simulator model version, I/O mapping, actuator mock vs real |
| **Bus access** | CAN/LIN/Ethernet tap points, termination, galvanic isolation |
| **Gateways** | Diagnostic dongles, VCI, engineering laptops (isolated VLAN) |
| **Monitoring** | Logic analyzer, bus logger, power probe attachment points |
| **Clocks** | Time sync source (PTP/NTP/GPS) for correlated captures |

Prefer **isolated lab networks**; block paths to corporate or internet unless explicitly in scope.

## Safety interlocks

| Control | Purpose |
|---|---|
| **Hardware e-stop** | Cuts actuator power independent of software |
| **Software interlock** | HIL disables outputs when guard open or fault injected |
| **Torque/speed limits** | Cap dynamometer or motor drives during security runs |
| **Fire / ventilation** | Battery or HV bench rules per facility policy |
| **Two-person rule** | Required for first energization or new wiring |

Never bypass OEM safety mechanisms without written approval from product safety.

## Pre-test checklist

```
[ ] ROE and safety sign-off on file
[ ] Bench FMEA updated for this target and stimulus plan
[ ] E-stop tested; interlocks verified closed-loop
[ ] Firmware/calibration baseline captured and checksummed
[ ] Bus termination and ground reference verified
[ ] Emergency contacts posted; fire extinguisher rated for bench
[ ] Rollback plan: reflash, power cycle, config restore documented
```

## During test discipline

- Increase stimulus **gradually**; log each step with UTC timestamp and operator ID
- Pause on unexpected actuator motion, smoke, over-temperature, or loss of watchdog
- Use **named test cases** (IDs) tied to version-controlled stimulus files
- Avoid unbounded random fuzz on safety-related frames without rate limits and abort conditions

## Post-test and handoff

1. Return target to **approved baseline** (reflash or config restore)
2. Clear diagnostic sessions, temporary keys, and engineering unlocks
3. Archive traces with test case ID, operator, target hash, and tool versions
4. File **incident note** if any safety event occurred—even if no security finding
5. Brief firmware/vehicle security with raw evidence paths and reproduction package
