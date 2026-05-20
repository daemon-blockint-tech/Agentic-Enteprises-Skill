# Operations, monitoring, and escalation

## Table of contents

1. [Observability by tier](#observability-by-tier)
2. [Alerting philosophy](#alerting-philosophy)
3. [Escalation and command](#escalation-and-command)
4. [Runbooks and drills](#runbooks-and-drills)
5. [Regulatory and contractual operations](#regulatory-and-contractual-operations)
6. [Metrics for leadership](#metrics-for-leadership)

## Observability by tier

Tier 0/1 require **defense in depth** beyond default infra monitoring:

| Signal type | Tier 0/1 emphasis |
|---|---|
| **Synthetic journeys** | End-to-end probes on critical paths; multi-region |
| **RED/USE metrics** | Latency, errors, saturation on dependencies |
| **Integrity signals** | Reconciliation lag, audit failures, config drift |
| **Tracing** | Sampled distributed traces with retention for incidents |
| **Logs** | Structured, correlated IDs; tamper-aware storage for forensics |
| **Capacity** | Headroom alerts before exhaustion; queue depth |

Pair implementation detail with `site-reliability-engineer`; you define **what must exist per tier**.

## Alerting philosophy

| Principle | Application |
|---|---|
| **Page on user impact** | Not on single metric noise; use SLO burn where appropriate |
| **Page on integrity** | Data wrong > CPU high |
| **Severity maps to tier** | Same alert class may page faster for Tier 0 |
| **Runbook link required** | No alert without owner and first actions |
| **Escalation timers** | If unacked in N minutes, escalate tier |

**Anti-pattern:** hundreds of low-signal pages that train on-call to ignore Tier 0.

## Escalation and command

Define **escalation tree** per Tier 0/1 service:

| Level | Typical role | Trigger |
|---|---|---|
| **L1** | Primary on-call | Automated page, synthetic failure |
| **L2** | Service owner / tech lead | L1 not acked; complex mitigation |
| **L3** | Platform / architecture | Shared choke point, multi-service |
| **L4** | Executive / crisis cell | MTPD breach risk, safety, regulatory clock |

Distinguish **technical incident command** (`incident-responder`, `incident-management-engineer`) from **business crisis** (`bcm-disaster-recovery-specialist`).

Document **communication cadence** inputs (status, ETA, customer impact)—not full comms ownership.

## Runbooks and drills

| Artifact | Tier 0/1 standard |
|---|---|
| **Runbook** | Step-by-step; rollback; integrity checks; dependency bypass |
| **Dependency failure** | Per-upstream play (IdP down, DB read-only, region loss) |
| **Drill calendar** | Failover, restore, game day—linked to RTO proof |
| **Last drill date** | Visible on criticality register |

Failed drill = **open risk** until remediated or risk-accepted at sponsor level.

## Regulatory and contractual operations

Generic operational hooks (not legal advice):

| Driver | Operational implication |
|---|---|
| **Notification clocks** | Timer from detection; pre-drafted templates |
| **Evidence preservation** | Log retention, chain of custody handoff to IR |
| **Reporting** | Monthly availability/integrity attestation for Tier 0 |
| **Third-party SLAs** | Monitor vendor status; escalate before your MTPD |

Map clocks to **monitoring and paging**—“we would learn too late” is a design defect.

## Metrics for leadership

| Metric | Why it matters |
|---|---|
| **Tier 0/1 availability vs target** | Contract and safety narrative |
| **Integrity incidents / near-miss** | Corruption risk visibility |
| **RTO/RPO drill success rate** | Continuity credibility |
| **Change failure rate by tier** | Governance effectiveness |
| **Open choke-point mitigations** | Blast-radius debt |
| **Emergency change rate** | Process or architecture stress |

Present **one page** per quarter: tier summary, top risks, investment asks—pair financial BCM views when needed.
