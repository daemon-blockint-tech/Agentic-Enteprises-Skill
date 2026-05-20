# DCS, PLC, and RTU architecture

## Table of contents

1. [Platform classes](#platform-classes)
2. [Logic partitioning](#logic-partitioning)
3. [Redundancy and failover](#redundancy-and-failover)
4. [Engineering workflow](#engineering-workflow)
5. [RTU and remote sites](#rtu-and-remote-sites)
6. [Soft-PLC and PC control](#soft-plc-and-pc-control)

## Platform classes

| Class | Strengths | Typical application layer |
|---|---|---|
| DCS | Integrated IO, advanced control libraries, uniform HMI | Continuous process, complex regulatory control |
| PLC | Rugged, discrete/batch, vendor ecosystems | Machines, utilities, distributed skids |
| RTU | Telemetry-focused, comms-efficient remote sites | Pipelines, wells, substations (with DNP3) |
| Soft-PLC / PC | Flexibility, IT-like tooling | Hybrid lines, retrofit, analytics-adjacent control |

## Logic partitioning

| Rule | Rationale |
|---|---|
| One clear owner per interlock | Avoid split logic across controllers without documented interface |
| Minimize cross-controller writes in fast loops | Latency and fault modes multiply |
| Group by unit/area | Align downloads with operations outages |
| Isolate experimental logic | Staging CPU or simulation partition before merge |

Document **interface tags** between controllers: direction, rate, fail-safe values, and timeout behavior.

## Redundancy and failover

- Clarify **1oo2**, hot-standby, or vendor-specific redundancy for CPUs and networks
- Define **bump-less transfer** expectations for outputs and integrators
- Plan **I/O redundancy** vs **controller redundancy** separately
- Test failover with **loaded comms** and maintenance activities—not idle benches only

## Engineering workflow

| Artifact | Content |
|---|---|
| Tag dictionary | Name, engineering units, limits, alarm classes, access level |
| Logic modules | Areas, programs, routines; version and author metadata |
| Download package | Target controller, checksum, prerequisites, rollback image |
| Simulation hook | MIL/SIL mapping of tags to model I/O |

Enforce **check-in/out** or vendor equivalent; align with site change management.

## RTU and remote sites

- Prefer **exception-based reporting** for WAN links; define offline store-and-forward
- Separate **monitoring** from **control** paths where security architecture requires
- Document **latency-sensitive** controls that must not run across high-latency links
- Plan battery/ power fail behavior for comms equipment affecting control visibility

## Soft-PLC and PC control

- Match **IEC 61131** language choices to maintainer skills (LD/FBD/ST/SFC)
- Define runtime **startup order**: comms before outputs enabled, safe defaults on boot
- Coordinate with `embedded-real-time-software-engineer` when custom I/O or kernel drivers are in scope
- Avoid mixing IT patch cadence with OT validation windows without explicit risk acceptance
