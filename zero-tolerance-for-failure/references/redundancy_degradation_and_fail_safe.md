# Redundancy, degradation, and fail-safe design

## Table of contents

1. [Failure mode thinking](#failure-mode-thinking)
2. [Fail-safe vs fail-closed vs fail-open](#fail-safe-vs-fail-closed-vs-fail-open)
3. [Redundancy patterns](#redundancy-patterns)
4. [Graceful degradation](#graceful-degradation)
5. [OT and classified considerations](#ot-and-classified-considerations)
6. [Design review prompts](#design-review-prompts)

## Failure mode thinking

For each component, document:

| Question | Output |
|---|---|
| What can fail? | Failure mode list |
| How does it fail? | Safe vs unsafe failure states |
| What is detected? | Monitoring, health checks, watchdogs |
| What is the response? | Failover, degrade, halt, manual procedure |
| What is the blast radius? | Users, data, safety, compliance |

Use **FMEA** (`references/pre_mortem_fmea_and_risk_registers.md`) for structured scoring on high-criticality systems.

## Fail-safe vs fail-closed vs fail-open

| Posture | When to use | Examples |
|---|---|---|
| **Fail-closed** | Default deny when uncertain | AuthZ, firewall on auth failure, payment holds |
| **Fail-safe** | Move to physically or logically safe state | OT interlock engages; drain connections |
| **Fail-open** | Availability over immediate security—**requires explicit approval** | Rare; document compensating controls |

**Default:** Prefer **fail-closed** for security and integrity; **fail-safe** for safety; document any fail-open with risk owner and monitoring.

## Redundancy patterns

| Pattern | Benefit | Caveat |
|---|---|---|
| **N+1 capacity** | Survive single node loss | Correlated failures (AZ, firmware) |
| **Active/active** | Low failover time | Split-brain needs fencing |
| **Active/passive** | Simpler consistency | Failover untested = unknown RTO |
| **Geographic redundancy** | Regional disaster | Data residency, replication lag |
| **Diverse implementations** | Common-mode bug resistance | Cost and complexity |

Redundancy without **tested failover** is wishful thinking—schedule exercises; pair `cyber-resilience-engineer` for recovery proof.

## Graceful degradation

Define **degraded modes** explicitly:

| Mode | Capability retained | Disabled or limited | User/comms expectation |
|---|---|---|---|
| **Full** | All features | — | Normal |
| **Degraded** | Core path only | Non-critical features | Banner / status |
| **Read-only** | Query, no mutation | Writes | Clear messaging |
| **Maintenance** | None or admin only | Public API | Planned window |

Requirements:

- **Deterministic defaults** — feature flags and config default to safer mode
- **Backpressure** — shed load before unbounded queue growth
- **Cascading failure containment** — timeouts, bulkheads, circuit breakers
- **Observability** — metric per degradation mode; alert on unintended entry

## OT and classified considerations

| Domain | Extra design rules |
|---|---|
| **OT** | Manual override visible and logged; no silent remote setpoint change |
| **Classified** | Redundant paths meet accreditation; no cross-domain leakage on failover |
| **Dual-use cloud** | Sovereignty and key custody on failover—`classified-cyber-security-senior-manager` |

## Design review prompts

- [ ] Unsafe failure states identified and eliminated where possible
- [ ] Fail-closed/default-deny documented for auth and data paths
- [ ] Degraded modes defined with monitoring and runbooks
- [ ] Redundancy tested in last 12 months (or justified exception)
- [ ] Single points of failure listed with accepted risk owner
- [ ] Rollback/automation path exists for deploy-induced failure

Capture decisions in ADR or architecture pack—pair `senior-system-architecture` for NFR traceability.
