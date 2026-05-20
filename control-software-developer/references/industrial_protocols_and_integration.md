# Industrial protocols and integration

## Table of contents

1. [Protocol selection](#protocol-selection)
2. [OPC UA](#opc-ua)
3. [Modbus](#modbus)
4. [DNP3](#dnp3)
5. [MQTT and AMQP](#mqtt-and-amqp)
6. [Gateways and quality](#gateways-and-quality)
7. [Security interfaces](#security-interfaces)

## Protocol selection

| Need | Typical choice | Caveat |
|---|---|---|
| Plant-wide data model, rich typing | OPC UA | Server capacity, certificate lifecycle |
| Simple register access, legacy devices | Modbus TCP/RTU | No built-in discovery; endianness and mapping errors |
| Electric utility telemetry/control | DNP3 | Strict addressing and event buffering semantics |
| Cloud/IT analytics fan-out | MQTT / AMQP | Not a substitute for deterministic control paths |
| High-rate control I/O | Fieldbus/vendor I/O (document only) | Route deep fieldbus design to vendor docs + embedded peer if custom |

## OPC UA

- Define **namespace**, node IDs, and browse paths in a tag dictionary shared with HMI/historian
- Specify **subscription** rates, queue sizes, and discard policies for overload
- Plan **certificates**, trust lists, and renewal without breaking production clients
- Separate **read-only** analytics clients from **write-capable** operators; gate writes in server logic

## Modbus

- Document **register map** (function codes, scaling, signedness, word order)
- Handle **exception responses** and comm timeouts with explicit quality degradation
- Avoid using Modbus as sole SOE path—timestamps are often weak compared to native event systems
- Rate-limit concurrent masters to protect fragile serial devices

## DNP3

- Clarify **outstation vs master** roles, event classes, and unsolicited responses
- Plan buffer sizes for comm outages; define backfill behavior
- Align **time sync** strategy with SOE requirements
- Treat control commands with **select-before-operate** patterns where required

## MQTT and AMQP

| Pattern | Use |
|---|---|
| Sparkplug B / UDT-style topics | Normalized plant metrics to cloud with birth/death certificates |
| Command topics | Only with authentication, ACLs, and server-side validation—never direct unguarded writes |
| AMQP routing | Enterprise integration, work queues, audit-friendly consumers |

Document **at-least-once** semantics: idempotent consumers, dedup keys, and stale command rejection.

## Gateways and quality

- Place gateways at **zone boundaries** per OT architecture (coordinate with `scada-ics-cyber-security-specialist`)
- Propagate **quality flags** (good, uncertain, bad) through mappings—do not coerce bad to good
- Define **back-pressure**: when historian or cloud sinks lag, shed non-critical publishes first
- Maintain **mapping version** alongside logic version for rollback

## Security interfaces

This skill does not own OT hardening. When adding protocols, deliver to OT security:

- New listen ports, brokers, and certificate stores
- Write paths and authentication models
- Data exfiltration surfaces (cloud historians, remote vendors)

Route control testing of security features to `scada-ics-cyber-security-specialist` and bench security to `hardware-in-the-loop-security-tester` as appropriate.
