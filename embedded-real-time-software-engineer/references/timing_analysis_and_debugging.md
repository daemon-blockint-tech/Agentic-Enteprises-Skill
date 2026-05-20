# Timing analysis and debugging

## Table of contents

1. [Measurement first](#measurement-first)
2. [WCET concepts](#wcet-concepts)
3. [Jitter and latency chains](#jitter-and-latency-chains)
4. [Debug and trace](#debug-and-trace)
5. [Field diagnostics](#field-diagnostics)

## Measurement first

Before optimizing:

| Technique | Captures |
|---|---|
| GPIO scope marker | ISR/task segment duration |
| Cycle counter (DWT) | Fine-grained on Cortex-M |
| RTOS trace (SystemView, etc.) | Context switches, blocking |
| Logic analyzer | Bus timing, handshake gaps |
| SWO/ITM | printf-free logging |

Record **configuration**: clock, cache state, compiler flags, build ID.

## WCET concepts

**WCET** = worst-case execution time under stated assumptions.

Build argument from:

1. **Path analysis** — longest path through code; no "typical" paths for hard deadlines
2. **Hardware effects** — wait states, flash prefetch, cache misses, bus contention
3. **Blocking** — mutex wait, DMA completion, interrupt preemption stack
4. **Tool support** — aiT, measurement + margin, hybrid when available

Document **assumptions** and **residual risk** when WCET is estimated not proven.

| Evidence level | Description |
|---|---|
| Measured peak | Stress test + margin |
| Analytical | Tool or manual bound |
| Unknown | Must not claim hard guarantee |

## Jitter and latency chains

For chain \(A \rightarrow B \rightarrow C\):

- Budget **per segment** including queueing delay
- Account for **tick granularity** if RTOS delays wake
- Include **interrupt storms** and **lower-priority task** blocking windows
- Report **p99 vs max**—hard RT needs max unless statistical argument accepted by safety process

## Debug and trace

| Tool | Use |
|---|---|
| JTAG/SWD | Breakpoints, memory, flash programming |
| ETM/ETB trace | Instruction flow, crash post-mortem |
| SWD multi-drop | Complex boards—verify topology |
| Logic analyzer | Protocol decode, timing violations |
| Core dump | RAM/registers to flash/ UART on fault |

**Production constraints**: disable invasive debug in release; gate semihosting; protect keys.

## Field diagnostics

- Structured **fault records** (reason, PC, LR, stack, version, uptime)
- **Assert policy**: development verbose; release minimal codes
- **Counters** for restarts, watchdog events, stack high-water
- **Safe logging** rate-limited; circular buffer flush on fault
- Correlate with **build fingerprint** and **config CRC**

Pair with `hardware-in-the-loop-security-tester` when reproducing issues requires bench stimulus—not for everyday bring-up.
