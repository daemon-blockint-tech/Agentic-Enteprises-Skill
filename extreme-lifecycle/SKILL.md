---
name: extreme-lifecycle
description: |
  Guides end-to-end lifecycle governance for mission-critical, high-assurance, or zero-failure-
  tolerance systems—concept through retirement: phases, gates, evidence, traceability, obsolescence,
  tech refresh, configuration baselines, NDA-safe regulated/classified patterns, assurance/DevSecOps/
  ATO interfaces, decommissioning and data disposition. Use for extreme lifecycle, system lifecycle,
  mission-critical lifecycle, lifecycle gates, sustainment, tech refresh, obsolescence management,
  decommissioning, configuration baseline, lifecycle evidence, end-to-end lifecycle, or retire a
  system—not TPM-only (technical-program-manager), HRO-only (zero-tolerance-for-failure), tiering-only
  (mission-critical), classified pipeline-only (classified-software-devsecops-engineer), formal
  proofs (software-assurance-formal-methods-specialist), compliance-only (compliance-engineer),
  CI-only (build-validator), infra portfolio-only (vp-of-infrastructure).
---

# Extreme Lifecycle

## When to Use

- Govern **end-to-end system lifecycle** from concept through disposal for high-assurance workloads
- Define **lifecycle phases**, entry/exit criteria, and **gate reviews** with required evidence
- Maintain **bidirectional traceability**—requirements, design, build, test, deploy, ops, and retire
- Control **configuration baselines**, approved changes, and tech refresh / obsolescence plans
- Plan **sustainment**—spares, vendor support, patch posture, and end-of-life transitions
- Interface with **assurance, DevSecOps, and authorization** without owning those roles
- Author **decommissioning and data disposition** plans with verification and audit trail
- Operate in **regulated or classified contexts** using generic, NDA-safe framing (no customer dumps)
- Produce lifecycle registers, gate packets, baseline manifests, and retirement checklists

## When NOT to Use

- Run multi-team milestone RAID and steering status only → `technical-program-manager`
- Establish HRO mindset, stop-the-line, and defect-escape prevention culture → `zero-tolerance-for-failure`
- Classify criticality tiers, RTO/RPO, and blast-radius architecture without full lifecycle → `mission-critical`
- Own cleared DevSecOps pipeline, build standards, and release trains only → `classified-software-devsecops-engineer`
- Prove correctness with formal methods, models, or certification evidence → `software-assurance-formal-methods-specialist`
- Automate SOC/ISO audit controls and continuous compliance monitoring → `compliance-engineer`
- Pre-flight architecture or go/no-go on a single change without lifecycle baseline → `build-validator`
- Own enterprise infrastructure portfolio, capex, and DC strategy → `vp-of-infrastructure`

## Related skills

| Need | Skill |
|---|---|
| Criticality tiering, objectives, release governance by tier | `mission-critical` |
| Failure-prevention culture, verification gates, FMEA | `zero-tolerance-for-failure` |
| Program milestones, dependencies, launch readiness | `technical-program-manager` |
| Cleared build/release and DevSecOps pipeline | `classified-software-devsecops-engineer` |
| Formal assurance, proofs, and certification packages | `software-assurance-formal-methods-specialist` |
| Audit evidence pipelines and control automation | `compliance-engineer` |
| Plan/design validation before execution | `build-validator` |
| Infrastructure portfolio and capex | `vp-of-infrastructure` |
| Secure SDLC, CI gates, SBOM | `devsecops` |
| Recovery architecture and restore evidence | `cyber-resilience-engineer` |
| BCM program and enterprise DR | `bcm-disaster-recovery-specialist` |

## Core Workflows

### 1. Scope and lifecycle charter

Define system boundary, assurance level, regulatory/classified interfaces, and lifecycle authority.

**See `references/extreme_lifecycle_scope.md`.**

### 2. Phases and gates

Map concept → design → build → verify → deploy → operate → sustain → dispose with gate criteria.

**See `references/lifecycle_phases_and_gates.md`.**

### 3. Traceability and evidence

Link artifacts across phases; define evidence types, retention, and independence requirements.

**See `references/traceability_and_evidence.md`.**

### 4. Operate, sustain, and obsolescence

Run sustainment reviews, tech refresh, vendor EOL, and operational baseline drift control.

**See `references/operate_sustain_and_obsolescence.md`.**

### 5. Change, baseline, and retirement

Manage baselines, approved deltas, decommissioning, and data disposition with verification.

**See `references/change_baseline_and_retirement.md`.**

### 6. Stakeholders and assurance interfaces

Coordinate owners, ISSO/ATO consumers, assurance, and DevSecOps without owning their deliverables.

**See `references/stakeholders_and_assurance_interfaces.md`.**

## Outputs

- **Lifecycle charter** — scope, phases, RACI, assurance tier, review cadence
- **Gate catalog** — phase × gate → criteria, evidence, approvers, waiver rules
- **Traceability matrix** — requirement/design/test/deploy/ops links with gap flags
- **Configuration baseline manifest** — versions, hashes, environments, approval record
- **Obsolescence and tech-refresh plan** — EOL dates, mitigations, funding hooks
- **Sustainment review record** — support posture, patch debt, spares, drill outcomes
- **Decommissioning package** — shutdown sequence, data disposition, evidence of destruction/archival

## Principles

- **Lifecycle before backlog** — phase gates and baselines drive priority; do not substitute sprint velocity
- **Evidence is the product of governance** — undocumented approval is not control
- **Trace forward and backward** — every production artifact links to intent and verification
- **Baselines are contracts** — change without baseline update is unauthorized state
- **Retire deliberately** — disposal and data disposition are phases, not tickets
- **Stay in lane** — interface with assurance, ATO, and DevSecOps; do not impersonate ISSO or auditor
- **NDA-safe by default** — generic regulated/classified patterns; no counterparty-specific dumps
