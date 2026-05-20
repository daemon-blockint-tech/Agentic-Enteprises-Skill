# Interrupts, drivers, and HAL

## Table of contents

1. [ISR design rules](#isr-design-rules)
2. [Deferred work patterns](#deferred-work-patterns)
3. [Driver architecture](#driver-architecture)
4. [HAL layering](#hal-layering)
5. [DMA and buses](#dma-and-buses)

## ISR design rules

- **Minimize latency**: clear flags, capture timestamps, enqueue pointer—return
- **No blocking**: no printf, malloc, mutex lock (unless documented ISR-safe API)
- **Re-entrancy**: same IRQ can nest on some cores—use per-channel state or disable briefly
- **Shared IRQ lines**: demux in ISR; defer demuxed handling per device
- **Measure**: GPIO toggle or trace marker for IRQ duration histogram

Document per-IRQ **maximum time** and **stack use** if nested.

## Deferred work patterns

| Pattern | Best for |
|---|---|
| RTOS semaphore/queue FromISR | Task wakes to process batch |
| Bottom-half / work queue | Linux-style; Zephyr `k_work` |
| Dedicated high-priority task | Polling ring fed by ISR |
| Zero-copy ring buffer | Streaming sensors, comm stacks |

Choose one pattern per peripheral class; avoid mixing without state diagram.

## Driver architecture

Typical layers:

```
Application / middleware
        ↓
Driver API (init, read, write, ioctl, async callback)
        ↓
HAL (register macros, clock enable, pin mux)
        ↓
Hardware
```

Driver state machine:

| State | Allowed ops |
|---|---|
| UNINIT | init only |
| READY | start transfer |
| BUSY | poll or callback in flight |
| ERROR | recovery path defined |

Return **typed errors** (timeout, NACK, CRC, bus fault); implement bounded retry.

## HAL layering

- **HAL**: chip-specific registers; no business logic
- **PAL** (optional): board pin mapping, external transceiver enable
- **Mock HAL**: host unit tests for logic above register layer
- **Compile-time** vs runtime configuration—prefer static tables for cert-friendly builds

Keep register access in one module; forbid scatter `#define` magic across app code.

## DMA and buses

| Concern | Practice |
|---|---|
| Buffer alignment | Meet peripheral and cache line rules |
| Cache coherency | Invalidate/clean on Cortex-A class; know MPU attributes |
| Linked descriptors | Pre-build rings; reload in completion ISR |
| CAN/Ethernet/SPI | Separate TX/RX paths; bound queue depth |
| Bus arbitration | Document blocking when DMA and CPU share bus |

For multi-master buses (CAN, I2C), serialize access with mutex at driver layer; never from ISR except ISR-safe lock.
