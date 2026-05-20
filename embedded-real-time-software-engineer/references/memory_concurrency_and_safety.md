# Memory, concurrency, and safety

## Table of contents

1. [Memory policy](#memory-policy)
2. [Stack and heap](#stack-and-heap)
3. [MPU and protection](#mpu-and-protection)
4. [Concurrency hazards](#concurrency-hazards)
5. [Safety-aware practices](#safety-aware-practices)
6. [MISRA C awareness](#misra-c-awareness)

## Memory policy

Default posture for hard real-time / safety paths:

- **Static allocation** for all runtime objects
- **No malloc** in control loops; if heap exists, isolate to init phase or non-RT tasks
- **Const data** in flash; avoid RAM duplication
- **DMA buffers** statically placed with correct section attributes
- **Zero-init** assumptions documented for BSS

## Stack and heap

| Activity | Method |
|---|---|
| Stack sizing | Worst-case call tree + ISR nesting + margin (25–100% per policy) |
| Stack check | Canary, MPU guard region, or RTOS watermark high-water |
| Heap | If used: pool allocator, fixed block sizes, failure hooks |
| Fragmentation | Avoid; measure peak if unavoidable |

Run **stack profiling** under stress tests before release; record high-water per task.

## MPU and protection

When MPU/MMU available:

- Separate **privileged** drivers from **application** tasks
- Read-only code; no execute from RAM unless required and audited
- Guard regions below stacks
- Peripheral registers accessible only from driver task/ISR context

Document **fault handler** behavior: log, safe state, reset tier.

## Concurrency hazards

| Hazard | Mitigation |
|---|---|
| Priority inversion | Priority inheritance, ceiling mutex, shorten critical sections |
| Deadlock | Lock ordering table; try-lock only with timeout policy |
| Race on flags | Atomic ops or IRQ disable window with bounded time |
| Lost wake | Verify queue depth; use overwrite policy consciously |
| ABA (lock-free) | Hazard pointers or generation counters—justify formally |

Use **lock-free** only with memory ordering diagram and review; prefer mutex with bounded hold time.

## Safety-aware practices

Without claiming certification:

- Map functions to **hazards** (unintended motion, energy release, data corruption)
- Define **safe states** on fault: de-energize, limp mode, last-known-good output
- **Watchdog** hierarchy: task pet, logical flow checks, external windowed WDT
- **Input validation** at boundaries; range checks before actuation
- **Diversity** or monitor tasks for critical outputs where standard requires
- **Change impact**: every patch traces to hazard analysis ID when in regulated program

Escalate formal safety case work to qualified safety engineers; provide evidence packs they request.

## MISRA C awareness

High-level discipline (not a full rules audit):

- No implicit conversions that widen signedness risk
- Explicit widths (`uint32_t`); avoid plain `int` for hardware
- Check every return value; no empty `default` in switch
- Limit function complexity; single exit where team standard requires
- Restrict function-like macros and pointer arithmetic
- Use `const` and `static` to enforce linkage intent
- Pair with static analysis tool in CI when available

Document **deviations** with rationale in project matrix.
