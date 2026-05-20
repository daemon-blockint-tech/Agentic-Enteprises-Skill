---
name: mission-critical
description: |
  Guides mission-critical system framing—tiering (mission-critical vs business-critical vs important),
  availability/integrity/continuity objectives, dependency and blast-radius mapping, architecture
  patterns (active-active, geo-redundancy, deterministic behavior), change/release governance,
  monitoring and escalation by criticality, and generic regulatory/contractual drivers (finance,
  healthcare, public safety, defense industrial base). Use when classifying criticality, setting
  RTO/RPO/MTPD and integrity targets, designing redundant architectures, mapping failure domains,
  governing Tier 0/1 releases, or ops escalation—not SRE error budgets only
  (site-reliability-engineer), HRO/prevention culture only (zero-tolerance-for-failure), incident
  command (incident-responder), recovery engineering only (cyber-resilience-engineer), enterprise
  security architecture only (enterprise-security-architect), ADRs without tiering
  (senior-system-architecture), or classified ATO only (classified-cyber-security-senior-manager).
---

# Mission-Critical Systems

## When to Use

- Classify **criticality tiers** (mission-critical, business-critical, important) with explicit impact criteria
- Set **availability, integrity, and continuity** objectives (uptime, RTO/RPO, MTPD, data loss tolerance)
- Map **dependencies**, failure domains, and **blast radius** for severe-impact services
- Select **architecture patterns**—active-active, geo-redundancy, quorum, deterministic execution, fail-safe defaults
- Define **change and release governance**—hold points, CAB tiers, emergency change, rollback criteria
- Tailor **monitoring, alerting, and escalation** to criticality (SLOs alone are insufficient for Tier 0)
- Align engineering with **contractual SLAs**, sector regulation, and continuity obligations (generic framing)
- Produce **criticality registers**, architecture decision records, and governance briefs for leadership

## When NOT to Use

- Own SLI/SLO definitions, error-budget policy, burn-rate alerting, and toil reduction → `site-reliability-engineer`
- Establish failure-prevention culture, HRO principles, stop-the-line, and defect-escape metrics → `zero-tolerance-for-failure`
- Run live incident war room, containment, and forensic preservation → `incident-responder`
- Design backup/immutability, ransomware recovery, and resilience test evidence → `cyber-resilience-engineer`
- Own enterprise BCM program, BIA facilitation, and regulatory BCM policy → `bcm-disaster-recovery-specialist`
- Enterprise security reference architecture and control frameworks without tiering lens → `enterprise-security-architect`
- Greenfield integration patterns and ADRs without criticality classification → `senior-system-architecture`
- Cleared program ATO, inspection, and personnel security without operational tiering → `classified-cyber-security-senior-manager`
- CI compile/lint gates without release governance for critical services → `build-validator`

## Related skills

| Need | Skill |
|---|---|
| SLOs, error budgets, reliability dashboards, capacity toil | `site-reliability-engineer` |
| HRO mindset, verification gates, fail-safe design, pre-mortem/FMEA | `zero-tolerance-for-failure` |
| RTO/RPO recovery architecture, immutability, attack playbooks | `cyber-resilience-engineer` |
| Enterprise BCM/DR program, tabletops, crisis comms | `bcm-disaster-recovery-specialist` |
| Active CSIRT response and containment | `incident-responder` |
| Incident program, SEV, on-call, postmortem process | `incident-management-engineer` |
| NFRs, architecture review, ADRs | `senior-system-architecture` |
| Security reference architecture, zero trust, governance | `enterprise-security-architect` |
| Cleared program governance and accreditation interfaces | `classified-cyber-security-senior-manager` |
| Cloud DR regions, landing zone, service placement | `cloud-engineer` |

## Core Workflows

### 1. Scope and criticality tiering

Define what “mission-critical” means in context; classify services and data; document drivers.

**See `references/mission_critical_scope_and_tiering.md`.**

### 2. Objectives: availability, integrity, continuity

Set measurable targets and exclusions; align tiers to RTO/RPO/MTPD and integrity classes.

**See `references/objectives_availability_integrity_continuity.md`.**

### 3. Architecture patterns for critical systems

Choose redundancy, partitioning, determinism, and degradation modes for Tier 0/1 workloads.

**See `references/architecture_patterns_for_critical_systems.md`.**

### 4. Dependencies and blast radius

Map upstream/downstream, shared fate, control planes, and containment boundaries.

**See `references/dependencies_and_blast_radius.md`.**

### 5. Change control and release governance

Tier releases, evidence gates, emergency change, and rollback for high-criticality paths.

**See `references/change_control_and_release_governance.md`.**

### 6. Operations, monitoring, and escalation

Observability depth, synthetic probes, runbooks, and escalation matched to impact.

**See `references/operations_monitoring_and_escalation.md`.**

## Outputs

- **Criticality register** — tier, owner, impact narrative, objectives, last review
- **Objectives sheet** — availability, integrity, RTO/RPO/MTPD per tier with measurement method
- **Dependency / blast-radius map** — failure domains, shared components, isolation notes
- **Architecture decision pack** — pattern choice, trade-offs, degradation and fail-safe behavior
- **Release governance matrix** — change type × tier → gates, approvers, evidence, rollback
- **Operations brief** — alert routes, escalation tree, runbook index, drill calendar hooks

## Principles

- **Tier before tooling** — criticality drives architecture and governance; do not retrofit labels after build
- **Integrity equals availability** — corruption or unauthorized change can be worse than downtime
- **Contain blast radius** — shared control planes and “single throat to choke” are Tier 0 risks
- **Govern change proportionally** — higher tier → more evidence, independence, and rollback discipline
- **Measure what customers and regulators care about** — pair SRE SLIs with tier-specific continuity proofs
- **Pair with peers** — reliability math (SRE), prevention culture (zero-tolerance), recovery (resilience), incidents (IR)
