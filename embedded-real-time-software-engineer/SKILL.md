---
name: embedded-real-time-software-engineer
description: |
  Guides embedded real-time firmware—MCU tradeoffs, bare-metal vs RTOS (FreeRTOS/Zephyr patterns),
  task priorities/deadlines/jitter, ISR deferred work, stack/heap policy, WCET/timing analysis,
  concurrency and priority inversion, drivers/HAL, JTAG/SWD/trace, power modes, MISRA C awareness,
  safety-aware automotive/medical/industrial patterns without certification claims.
  Use for embedded firmware, RTOS scheduling, drivers/HAL, IRQ design, memory policy, WCET, bring-up,
  low-power—not HIL security (hardware-in-the-loop-security-tester), backend apps
  (senior-software-engineer), SCADA/OT (scada-ics-cyber-security-specialist), server perf
  (performance-engineer), RTL-only without firmware, CI gates (build-validator), tiering only
  (mission-critical).
---

# Embedded Real-Time Software Engineer

## When to Use

- Select or compare **MCUs/MPUs** for real-time, memory, peripheral, safety, and toolchain fit
- Choose **bare-metal vs RTOS** and define task model, priorities, periods, and deadlines
- Design **ISR → deferred work** paths (bottom halves, work queues, DMA completion chains)
- Set **memory policy**—static allocation, stack sizing, heap ban/limit, MPU regions where used
- Analyze **timing**—schedulability sketches, jitter budgets, measurement hooks, WCET reasoning
- Implement **concurrency**—mutex/Semaphore choice, priority inheritance, lock-free only with proof
- Layer **drivers and HAL**—register access, DMA, error recovery, test doubles for host tests
- Plan **bring-up and debug**—JTAG/SWD, trace, logic analyzer, assert/fault hooks, post-mortem dumps
- Design **power modes**—wake sources, clock gating, peripheral retention, RTOS tickless tradeoffs
- Apply **coding discipline**—MISRA C awareness, defensive checks, watchdog strategy, update strategy
- Frame **safety-aware** design for automotive/medical/industrial (hazards, FMEA hooks) without cert claims

## When NOT to Use

- **HIL security assessment**, bus fault injection, or bench penetration on real targets → `hardware-in-the-loop-security-tester`
- **General backend**, APIs, microservices, or cloud runtime without MCU constraints → `senior-software-engineer`
- **SCADA/ICS** plant operations, Purdue model, OT network monitoring → `scada-ics-cyber-security-specialist`
- **Service-level profiling**, load tests, p99 on servers or browsers → `performance-engineer`
- **FPGA/RTL-only** design, timing closure, synthesis—unless co-designing firmware for SoC/FPGA fabric
- **Pre-merge plan/design gates** across domains without embedded implementation → `build-validator`
- **Criticality tiering**, RTO/RPO, enterprise continuity without firmware architecture → `mission-critical`
- **Enterprise security program**, IAM, or SOC operations → `cybersecurity`, `information-security-engineer`
- **Production incident command** on live fleets → `incident-responder`

## Related skills

| Need | Skill |
|---|---|
| HIL security testing on benches, bus injection | `hardware-in-the-loop-security-tester` |
| OT/ICS plant and SCADA security operations | `scada-ics-cyber-security-specialist` |
| Application/backend implementation | `senior-software-engineer` |
| Server/UI performance profiling and load tests | `performance-engineer` |
| Pre-flight architecture/security/cost validation | `build-validator` |
| Mission-critical tiering, availability objectives | `mission-critical` |
| Failure-prevention culture, HRO gates, FMEA mindset | `zero-tolerance-for-failure` |
| Binary/firmware reverse engineering | `reverse-engineer` |
| CI pipelines and release automation | `devops` |

## Core Workflows

### 1. Scope, constraints, and platform choice

Capture hard real-time vs soft real-time, safety class, power budget, toolchain, and certification boundaries (inform only—do not claim compliance).

**See `references/embedded_rt_scope_and_constraints.md`.**

### 2. Scheduling, RTOS, and deadlines

Define tasks, priorities, periods, deadlines, synchronization, and jitter acceptance; sketch schedulability and worst-case paths.

**See `references/scheduling_rtos_and_deadlines.md`.**

### 3. Interrupts, drivers, and HAL

Partition ISR work, driver state machines, DMA paths, and hardware abstraction with testability.

**See `references/interrupts_drivers_and_hal.md`.**

### 4. Memory, concurrency, and safety-aware design

Stack/heap policy, MPU usage, locking rules, priority inversion mitigation, watchdogs, and hazard-aware patterns.

**See `references/memory_concurrency_and_safety.md`.**

### 5. Timing analysis and debugging

Measure latency, build WCET arguments, use trace and analyzers, capture field diagnostics.

**See `references/timing_analysis_and_debugging.md`.**

### 6. Power, boot, and deployment

Reset/boot chain, clock trees, low-power modes, OTA/update constraints, and manufacturing hooks.

**See `references/power_boot_and_deployment.md`.**

## Outputs

- **Platform decision record** — MCU, RTOS/bare-metal, memory map, toolchain, open risks
- **Task/scheduling table** — name, priority, period, WCET budget, shared resources, blocking rules
- **ISR/deferred-work map** — latency budget per IRQ, bottom-half mechanism, re-entrancy notes
- **Memory budget** — per-task stacks, globals, DMA buffers, heap policy (if any)
- **Driver/HAL interface sheet** — init/teardown, error codes, thread/ISR context rules
- **Timing evidence pack** — measurements, trace captures, WCET assumptions and gaps
- **Power mode matrix** — states, wake sources, peripheral retention, transition times
- **Review checklist** — MISRA-oriented items, watchdog, safe defaults, update/rollback hooks

## Principles

- **Measure timing; do not guess** — instrument before optimizing; document measurement setup
- **Keep ISRs minimal** — defer protocol and heavy work; respect IRQ latency budgets
- **Prefer static allocation** — prove stack depth; ban unbounded heap in safety paths
- **Make priority inversion visible** — inheritance, ceiling mutexes, or lock-free with formal sketch
- **Layer for testability** — HAL behind interfaces; host tests for logic; HIL for integration
- **Separate safety claims from engineering** — hazard IDs and mitigations yes; certification no
- **Pair with security and ops peers** — HIL security, mission-critical tiering, build validation as needed

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries, constraints, MCU tradeoffs | `references/embedded_rt_scope_and_constraints.md` |
| RTOS tasks, priorities, deadlines, jitter | `references/scheduling_rtos_and_deadlines.md` |
| ISRs, drivers, HAL, DMA | `references/interrupts_drivers_and_hal.md` |
| Memory, locks, safety-aware patterns | `references/memory_concurrency_and_safety.md` |
| WCET, measurement, debug/trace | `references/timing_analysis_and_debugging.md` |
| Boot, power, OTA, deployment | `references/power_boot_and_deployment.md` |
