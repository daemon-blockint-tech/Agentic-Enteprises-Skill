# Integration: SIL, HIL, and digital twins

## Table of contents

1. [Purpose](#purpose)
2. [SIL vs HIL vs twin](#sil-vs-hil-vs-twin)
3. [Interface architecture](#interface-architecture)
4. [Clocks and synchronization](#clocks-and-synchronization)
5. [I/O mapping and protocols](#io-mapping-and-protocols)
6. [Fault injection (engineering)](#fault-injection-engineering)
7. [Digital twin patterns](#digital-twin-patterns)
8. [Game-engine and middleware bridges](#game-engine-and-middleware-bridges)
9. [Security and safety boundaries](#security-and-safety-boundaries)
10. [Handoffs](#handoffs)
11. [Checklist](#checklist)

## Purpose

Guide **integration of simulation with software and hardware under test**—SIL/HIL boundaries, digital-twin synchronization, and middleware bridges—without owning security exploitation or formal assurance.

## SIL vs HIL vs twin

| Pattern | What is real | What is simulated | Typical goal |
|---|---|---|---|
| SIL | Software under test (SUT) | Plant, environment, sensors | Fast regression, CI |
| HIL | Hardware (ECU, actuator drivers, sensors) | Plant/environment remainder | Timing and I/O fidelity |
| Digital twin | Operational asset + services | Model updated from live data | Monitoring, prediction, training refresh |
| Operator-in-the-loop | Human + partial hardware | Environment/visuals | Training (generic scenarios) |

**MIL (model-in-the-loop):** often means controls model only—clarify whether “MIL” here excludes sensor rendering; align vocabulary with controls peers (`control-software-developer`).

## Interface architecture

```
+------------------+     observations      +------------------+
|  Sim world/plant | --------------------> |  SUT (SIL/HIL)   |
|  + sensor models |                       |  controllers/    |
+------------------+ <-------------------- |  perception stack|
        ^                  commands         +------------------+
        |                                            |
        +------------ optional twin ingest ----------+
```

**Contract elements:**

- Message types, rates, units, timestamps
- Semantic version of interface schema
- Error handling (stale data, NaN guards, safe defaults)

## Clocks and synchronization

| Domain | Practice |
|---|---|
| Sim time | Master for physics and sensor synthesis |
| SUT time | May use wall clock or stepped sync |
| HIL bridge | PLL-like alignment; measure round-trip latency |
| Logging | Single trace correlating sim tick, publish, HW IRQ |

**HIL overrun:** define whether sim **waits** for hardware, **freezes** plant, or **continues** open-loop—misconfiguration causes false pass.

## I/O mapping and protocols

Examples (generic):

- Analog/digital maps for actuator and sensor pins
- Ethernet/UDP CAN-FD bridges for automotive stacks
- Middleware (DDS, ROS-style, custom IPC) for robotics SIL

Document:

| Signal | Sim source | HW channel | Rate | Latency budget |
|---|---|---|---|---|

Prefer **recorded I/O playback** for bring-up before closed-loop HIL.

## Fault injection (engineering)

Engineering faults (for robustness testing):

- Sensor bias ramps, dropout, latency spikes
- Actuator saturation, delay, stuck values
- Environment parameter shocks (wind gust, friction change)

**Route security-focused bus manipulation and exploitation** to `hardware-in-the-loop-security-tester` with authorized rules of engagement.

## Digital twin patterns

| Pattern | Data flow | Sim role |
|---|---|---|
| Shadow | Live telemetry → compare to sim prediction | Drift detection |
| Scheduled refresh | Batch ingest → recalibrate parameters | Updated twin for planning |
| Interactive twin | Operator adjusts params → sim forecasts | Training / ops support |

**Requirements:**

- Identity mapping (asset ID, frame, time)
- **Freshness SLAs** and stale-state handling
- Versioned twin model matching field software baselines

Do not ingest **non-public or export-controlled** telemetry into shared repos—use sanitized synthetic or approved stores.

## Game-engine and middleware bridges

When using game engines or visual pipelines:

- Pin **physics substep**, collision meshes, and rendering decoupling
- Export **deterministic sensor topics** even if visuals are nondeterministic
- Provide **headless** mode for CI

For Simulink-style or block-diagram tools:

- Export **FMU/co-sim** boundaries with clear step negotiation
- Document algebraic loops and solver settings in the twin manifest

## Security and safety boundaries

- **Do not** instruct disabling interlocks or safety monitors in real systems from sim examples.
- **Do not** blend security attack scenarios with safety validation without explicit program separation.
- Formal claims require `software-assurance-formal-methods-specialist`—sim evidence alone is insufficient.

## Handoffs

| Peer | Deliverable |
|---|---|
| `embedded-real-time-software-engineer` | WCET assumptions, IRQ-safe I/O patterns for HIL targets |
| `control-software-developer` | Plant model exchange, scan-cycle semantics |
| `tactical-ai-autonomy-developer` | SIL APIs, scenario catalogs, release gates |
| `sensor-fusion-engineer` | Observation formats, truth for metric computation |
| `hardware-in-the-loop-security-tester` | Separate security test plan; engineering I/O map only |
| `performance-engineer` | Server-side load only if sim services are deployed as microservices |

## Checklist

- [ ] SIL/HIL boundary diagram and schema versioned
- [ ] Clock owner and overrun policy documented
- [ ] I/O map with rates and latency budgets complete
- [ ] Engineering fault catalog separated from security tests
- [ ] Twin freshness and model version policy defined
- [ ] NDA/export-safe data handling stated for live feeds
