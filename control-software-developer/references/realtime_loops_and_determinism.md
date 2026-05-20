# Real-time loops and determinism

## Table of contents

1. [Scan-cycle model](#scan-cycle-model)
2. [Control loop patterns](#control-loop-patterns)
3. [Jitter and overrun](#jitter-and-overrun)
4. [I/O synchronization](#io-synchronization)
5. [Soft-PLC and PC-based control](#soft-plc-and-pc-based-control)
6. [Evidence and measurement](#evidence-and-measurement)

## Scan-cycle model

| Concept | Guidance |
|---|---|
| Cycle time | Choose from process dynamics (fast loops vs slow sequences); document minimum stable period |
| Task order | Define deterministic order: inputs → logic → outputs; avoid hidden reorder across vendors |
| Fast vs slow tasks | Partition high-rate loops from slow sequences; avoid starving fast tasks |
| Redundancy | Clarify primary/standby execution, bump-less transfer, and I/O failover semantics |

## Control loop patterns

| Pattern | Notes |
|---|---|
| PID / regulatory | Anti-windup, bumpless transfer, mode tracking (auto/manual/cascade) |
| Cascade / ratio | Subordinate limits, saturation handling, explicit mode per layer |
| Sequences | Step timers, permissives, abort paths, hold/resume, interlock precedence |
| Interlocks | Hard vs soft; never implement SIS functions in BPCS without explicit boundary |
| State machines | Explicit states, illegal transition handling, logging on transitions |

## Jitter and overrun

| Signal | Action |
|---|---|
| Cycle overrun | Define shed policy: skip non-critical work, alarm, safe output hold |
| Jitter budget | Allocate % of cycle to I/O, logic, comms; measure before tuning gains |
| Watchdog | Align software watchdog with hardware/OS watchdog where present |
| Timestamping | Use consistent clock source for SOE; document leap/smear behavior at integration |

## I/O synchronization

- Map physical I/O refresh to scan boundaries; document one-scan delay where unavoidable
- For networked I/O, include transport latency in control design (do not assume wire-speed)
- For buffered inputs, define validity windows and stale-data handling
- Document bad-quality I/O behavior: last-good-value vs fail-safe vs forced safe state per tag class

## Soft-PLC and PC-based control

| Topic | Guidance |
|---|---|
| Runtime isolation | Prefer dedicated industrial PCs or RT hypervisor partitions for determinism |
| OS jitter | Measure under load; avoid best-effort scheduling for fast loops |
| NIC offload | Document interrupt load from high-rate protocols |
| Storage | Separate config/logs from control runtime disk; plan wear and corruption recovery |

## Evidence and measurement

Produce a **timing budget table**: cycle time, measured worst case, overrun policy, and test method (logic analyzer, vendor diagnostics, built-in profilers).

For disputes between teams, prefer **measured traces** over nominal vendor marketing cycle times.
