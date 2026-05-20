# Power, boot, and deployment

## Table of contents

1. [Reset and boot chain](#reset-and-boot-chain)
2. [Clocks and power modes](#clocks-and-power-modes)
3. [Low-power design](#low-power-design)
4. [RTOS tickless and wake](#rtos-tickless-and-wake)
5. [Update and deployment](#update-and-deployment)
6. [Manufacturing hooks](#manufacturing-hooks)

## Reset and boot chain

Document sequence:

| Stage | Responsibility |
|---|---|
| ROM bootloader | Trust anchor, minimal validation |
| Secondary loader | Image select, crypto verify if required |
| Application | Hardware init order, RTOS start |
| Late init | Network, filesystem, non-RT services |

Rules:

- **Init order** respects dependencies (clocks → pins → peripherals → tasks)
- **Fail closed** on verify errors; defined recovery (retry bank, service mode)
- **Boot time budget** for products with fast wake requirements

## Clocks and power modes

| Mode | Typical use |
|---|---|
| Run | Full performance |
| Sleep | CPU stopped, peripherals on |
| Stop/Standby | RAM retention tradeoffs |
| Deep sleep | Wake from RTC/GPIO only |

For each mode list: **wake sources**, **RAM retained**, **peripheral state**, **transition time**, **RTOS compatibility**.

## Low-power design

- Gate clocks to unused blocks; disable peripherals explicitly
- Choose **polling vs interrupt** for rare events—energy vs latency
- Batch sensor samples; align radio TX with wake windows
- Avoid **busy-wait** except documented short spins
- Profile **energy per use-case** not just average current

## RTOS tickless and wake

- Tickless idle reduces timer interrupts but adds **wake latency**
- Verify **timeout accuracy** for protocol stacks after tickless
- Document **maximum idle duration** before missed deadlines
- Test wake from **every** IRQ path used in production

## Update and deployment

| Topic | Considerations |
|---|---|
| Dual bank | A/B swap, power-loss safe commit |
| Delta vs full | Flash wear, rollback |
| Signing | Key storage, secure element, anti-rollback counters |
| Config | Separate NV params; migration version |
| Downtime | Background download vs service window |

Coordinate with security peers for **trust model**; implement firmware-side state machine only.

## Manufacturing hooks

- **Test firmware** or BIST modes behind GPIO/straps
- **JTAG lock** policy documented
- **Serial number** / calibration storage layout
- **EOL tests**: RAM march, flash CRC, communication loopback
- **Provisioning** keys in HSM/OTP—never log secrets

Use `build-validator` for release readiness across firmware + CI + ops when scope exceeds implementation.
