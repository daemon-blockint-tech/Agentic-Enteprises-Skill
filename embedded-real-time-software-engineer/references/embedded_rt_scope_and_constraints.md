# Embedded RT scope and constraints

## Table of contents

1. [Role boundary](#role-boundary)
2. [Constraint capture](#constraint-capture)
3. [MCU selection tradeoffs](#mcu-selection-tradeoffs)
4. [Bare-metal vs RTOS](#bare-metal-vs-rtos)
5. [What good looks like](#what-good-looks-like)

## Role boundary

| Embedded RT engineer owns | Others own |
|---|---|
| Firmware architecture, scheduling, drivers/HAL, timing, memory policy | HIL security bench tests (`hardware-in-the-loop-security-tester`) |
| MCU bring-up, ISR design, RTOS integration (pattern level) | SCADA/ICS plant ops (`scada-ics-cyber-security-specialist`) |
| WCET reasoning, trace/debug strategy, power modes | Server/UI perf (`performance-engineer`) |
| MISRA-aware coding, safety-aware mitigations (no cert) | General backend (`senior-software-engineer`) |
| OTA/boot chain firmware concerns | Enterprise tiering only (`mission-critical`) |
| | FPGA/RTL implementation (`fpga`) |
| | Pre-merge cross-domain gates (`build-validator`) |

## Constraint capture

Document before design:

| Dimension | Questions |
|---|---|
| **Real-time class** | Hard (miss = hazard) vs soft (miss = degraded QoS) |
| **Deadlines** | End-to-end chains; which are externally visible |
| **Safety** | ASIL/IEC 62304 class intent—engineering mitigations only |
| **Resources** | Flash/RAM, core count, FPU, crypto accelerators |
| **Power** | Active/standby targets, battery vs mains, thermal |
| **Environment** | Temperature, EMI, vibration, supply brownout |
| **Lifecycle** | OTA, dual-bank, rollback, secure boot expectations |
| **Toolchain** | Compiler, RTOS license, static analysis, trace support |

## MCU selection tradeoffs

| Factor | Consider |
|---|---|
| **Compute headroom** | WCET margin at max clock; DSP/FPU needs |
| **Peripherals** | CAN-FD, Ethernet TSN, ADC resolution, crypto |
| **Memory** | SRAM for stacks/DMA; flash for A/B images |
| **Determinism** | Cache, MPU, dual-core interference |
| **Ecosystem** | BSP quality, long-term silicon support |
| **Safety lineage** | Safety manuals available vs generic MCUs |
| **Cost & supply** | Multi-source, obsolescence, lead time |

Produce a short **decision matrix** with scored options and explicit disqualifiers.

## Bare-metal vs RTOS

| Choose bare-metal when | Choose RTOS when |
|---|---|
| Few cooperative loops, simple superloop + ISRs | Many tasks, mixed periods, blocking I/O |
| Tightest IRQ latency, tiny footprint | Standard APIs, networking stacks, USB |
| Team can maintain custom scheduler | Need priority inheritance, timers, queues |
| | Third-party middleware expects RTOS |

At pattern level: FreeRTOS (wide BSP), Zephyr (device tree, networking)—compare tick rate, tickless idle, and driver model fit; do not prescribe vendor-specific APIs unless user context requires it.

## What good looks like

- Constraints written and signed by product/safety stakeholders where applicable
- Platform choice recorded with measurable timing and memory budgets
- Clear boundary: firmware engineering vs security bench vs enterprise tiering
- Open risks listed (unmeasured WCET, shared bus contention, heap use)
