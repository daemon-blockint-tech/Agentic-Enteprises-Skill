---
name: zero-tolerance-for-failure
description: |
  Guides failure-prevention culture and operational excellence for mission-critical engineering—
  zero-defect aspiration vs error budgets; HRO principles; defense-in-depth; fail-safe/fail-closed;
  verification gates and independent checks; redundancy and graceful degradation; pre-mortems and
  FMEA; stop-the-line; defect escape, near-miss, and repeat-incident metrics; leadership against
  normalization of deviance—not blame culture. Use for failure-prevention programs, HRO practices,
  verification gates, fail-safe design, pre-mortem/FMEA, stop-the-line, near-miss reporting, or
  defect-escape metrics—not SRE error budgets only (site-reliability-engineer), incident command only
  (incident-management-engineer), backup/restore only (cyber-resilience-engineer), CI lint only
  (build-validator), agile coaching, HR discipline, or classified ATO without ops-excellence lens
  (classified-cyber-security-senior-manager).
---

# Zero-Tolerance for Failure

## When to Use

- Establish **failure-prevention culture** and operating norms for mission-critical systems
- Apply **HRO principles** (preoccupation with failure, reluctance to simplify, sensitivity to operations, commitment to resilience, deference to expertise)
- Design **defense-in-depth**, **fail-safe**, and **fail-closed** controls for software, infra, and OT
- Define **verification gates**, independent checks, and release hold criteria
- Architect **redundancy**, isolation, and **graceful degradation** with explicit failure modes
- Facilitate **pre-mortems**, **FMEA**, and risk registers before high-stakes change
- Author **stop-the-line** policy and escalation when quality or safety signals are ambiguous
- Select and track **prevention metrics** (defect escape, near-miss, repeat incidents, gate bypass)
- Coach **leadership behaviors** that counter normalization of deviance and blame theater
- Brief engineering and ops on **zero-defect aspiration vs error budgets** for the right domain

## When NOT to Use

- Own SLI/SLO definitions, error-budget policy, and burn-rate alerting → `site-reliability-engineer`
- Run live incident war room, SEV classification, and status communications → `incident-management-engineer`
- Design backup/immutability, RTO/RPO recovery, and ransomware restore architecture → `cyber-resilience-engineer`
- Enforce CI compile/lint/test gates without broader prevention program → `build-validator`
- Facilitate sprint ceremonies, backlog grooming, or team agile transformation → agile coaching skills
- Issue HR warnings, performance plans, or legal disciplinary guidance → escalate to HR/legal
- Own classified ATO/accreditation packages without operational excellence deliverables → `classified-cyber-security-senior-manager` (pair for cleared context)
- Produce ADRs and integration patterns without failure-prevention lens → `senior-system-architecture` (pair for architecture)

## Related skills

| Need | Skill |
|---|---|
| SLOs, error budgets, reliability toil, capacity | `site-reliability-engineer` |
| Incident program, SEV, on-call, postmortems | `incident-management-engineer` |
| Recovery tiers, backup/immutability, resilience tests | `cyber-resilience-engineer` |
| Build/CI quality gates and merge validation | `build-validator` |
| Cleared program governance, inspection, escalation | `classified-cyber-security-senior-manager` |
| NFRs, architecture review, ADRs | `senior-system-architecture` |
| Enterprise BCM/DR program and tabletops | `bcm-disaster-recovery-specialist` |
| Active CSIRT containment and forensics | `incident-responder` |

## Core Workflows

### 1. Scope, limits, and charter

Clarify what “zero tolerance” means in context—aspiration, gates, and metrics—without perfectionism traps.

**See `references/zero_tolerance_scope_and_limits.md`.**

### 2. HRO principles and operating mindset

Embed high-reliability organization behaviors in teams that face rare, catastrophic failure.

**See `references/high_reliability_organization_principles.md`.**

### 3. Prevention, verification, and gates

Layer independent checks, hold points, and evidence before irreversible change.

**See `references/prevention_verification_and_gates.md`.**

### 4. Redundancy, degradation, and fail-safe design

Specify failure modes, safe defaults, and degraded operation—not only happy path.

**See `references/redundancy_degradation_and_fail_safe.md`.**

### 5. Pre-mortem, FMEA, and risk registers

Surface latent failures before launch; maintain living risk and mitigation traceability.

**See `references/pre_mortem_fmea_and_risk_registers.md`.**

### 6. Leadership, culture, and metrics

Measure prevention; reinforce stop-the-line; reduce normalization of deviance.

**See `references/leadership_culture_and_metrics.md`.**

## Outputs

- **Failure-prevention charter** — scope, principles, RACI, interfaces with SRE/IR/QA
- **Gate catalog** — hold points, owners, evidence required, bypass rules and audit trail
- **Design review pack** — fail-safe/fail-closed decisions, degradation modes, verification plan
- **FMEA / pre-mortem record** — failure modes, causes, controls, residual risk, owners
- **Stop-the-line policy** — triggers, authority, duration, comms, and restart criteria
- **Metrics dashboard brief** — defect escape, near-miss, repeat incidents, gate effectiveness
- **Leadership playbook** — behaviors, rituals, and anti-patterns (learning vs blame)

## Principles

- **Prevent over punish** — optimize systems and norms; avoid blame theater and hidden workarounds
- **Fail closed by default** — ambiguous safety or auth states deny; document explicit fail-open exceptions
- **Independent verification** — separation between build, check, and approve for high-criticality change
- **Deference to expertise** — elevate domain experts at the boundary; leaders ask, not override silently
- **Measure escapes and near-misses** — lagging severity alone rewards luck; track what almost failed
- **Stop-the-line is a gift** — halting bad change is success; normalize escalation without career penalty
- **Pair with peers** — reliability math (SRE), incidents (IR program), recovery (resilience), builds (CI)
