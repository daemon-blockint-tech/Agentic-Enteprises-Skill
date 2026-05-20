# Objectives: availability, integrity, continuity

## Table of contents

1. [Objective families](#objective-families)
2. [Availability targets](#availability-targets)
3. [Integrity and authenticity](#integrity-and-authenticity)
4. [Continuity: RTO, RPO, MTPD](#continuity-rto-rpo-mtpd)
5. [Measurement and exclusions](#measurement-and-exclusions)
6. [Tier-to-objective mapping](#tier-to-objective-mapping)

## Objective families

Mission-critical engineering treats three families as **co-equal**:

| Family | Protects against | Example metrics |
|---|---|---|
| **Availability** | User-visible outage or unresponsive dependency | Uptime %, successful transaction rate, probe success |
| **Integrity** | Wrong, corrupted, or unauthorized data/state | Reconciliation breaks, audit failures, unsafe commands |
| **Continuity** | Cannot restore within required time | RTO achieved, RPO met, MTPD not breached |

Pair **SRE SLIs** (`site-reliability-engineer`) with **tier-specific continuity proofs**—error budgets alone do not satisfy Tier 0 obligations.

## Availability targets

Define per **user journey** or **control loop**, not per server:

- **Target** — e.g., 99.95% monthly for Tier 1 payment initiation (illustrative; set per contract)
- **Window** — calendar month vs rolling 28d; align with SLA text
- **Scope** — regions, channels, customer segments included
- **Dependencies** — explicit upstream exclusions (identity, network) documented

**Degraded modes:** specify **minimum viable function** when full feature set is unavailable (read-only, queue-and-replay, manual fallback).

## Integrity and authenticity

For Tier 0/1, specify:

| Control theme | Engineering ask |
|---|---|
| **Correctness** | Idempotency, exactly-once semantics, reconciliation jobs |
| **Tamper evidence** | Immutable logs, WORM, hash chains where warranted |
| **Authorization** | Fail-closed authZ; break-glass audited (`zero-tolerance-for-failure`) |
| **Dual control** | Four-eyes for irreversible or high-value state changes |
| **Determinism** | Bounded behavior under overload; no unbounded retries on shared resources |

**Integrity SLO examples:** max undetected ledger divergence duration; max time to detect unauthorized config drift.

## Continuity: RTO, RPO, MTPD

| Term | Definition | Owner interface |
|---|---|---|
| **RTO** | Max acceptable time to restore **service function** | Engineering + ops; validated by drill |
| **RPO** | Max acceptable **data loss** window | Backup/replication design; pair `cyber-resilience-engineer` |
| **MTPD** | Max tolerable **business disruption** before unacceptable impact | BCM input (`bcm-disaster-recovery-specialist`) |

Document **RTA** (actual recovery in tests) vs **RTO** (target)—gaps drive backlog.

## Measurement and exclusions

| Practice | Guidance |
|---|---|
| **Synthetic probes** | Black-box journeys for Tier 0/1; not only infra metrics |
| **Real user monitoring** | Sample critical paths; protect PII |
| **Exclusions** | Maintenance windows, force majeure—pre-approved and rare for Tier 0 |
| **Composite health** | Do not green dashboards when integrity checks fail |

Report **budget burn** (SRE) and **continuity margin** (time to MTPD breach) on one leadership slide for Tier 0/1.

## Tier-to-objective mapping

Illustrative defaults—**replace with org standards**:

| Tier | Availability (indicative) | Integrity | Continuity |
|---|---|---|---|
| **0** | Highest contractual + safety case | Formal integrity class; continuous verification | RTO/RPO in minutes–hours; MTPD from BCM |
| **1** | Contractual SLA + executive reporting | Reconciliation + change audit | RTO hours; tested quarterly |
| **2** | Internal SLO | Standard change + backup | RTO ≤ 1 business day |
| **3** | Best-effort SLO | Standard controls | Standard backup |

Every Tier 0/1 row links to **last successful drill date** and **open gap** count.
