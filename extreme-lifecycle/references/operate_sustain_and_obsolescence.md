# Operate, sustain, and obsolescence

## Table of contents

1. [Operate phase essentials](#operate-phase-essentials)
2. [Operational baseline discipline](#operational-baseline-discipline)
3. [Sustainment program](#sustainment-program)
4. [Obsolescence management](#obsolescence-management)
5. [Technology refresh](#technology-refresh)
6. [Vendor and support lifecycle](#vendor-and-support-lifecycle)
7. [Sustainment review agenda](#sustainment-review-agenda)
8. [Triggers to dispose phase](#triggers-to-dispose-phase)

## Operate phase essentials

**Operate** runs the system within the **approved production baseline** until sustainment or retirement triggers apply.

| Activity | Lifecycle tie |
|---|---|
| Monitoring and alerting | Mapped to baseline manifest and runbook versions |
| Incident response | Preserves forensic and config state per policy |
| Capacity and performance | Changes that alter baseline go through change control |
| Access management | Privileged access logged; ties to assurance interfaces |
| Backup and restore | Drills evidence sustainment of RTO/RPO (`cyber-resilience-engineer`) |

Pair `mission-critical` for **tier-specific escalation**; this skill ensures **baseline identity** is known during incidents.

## Operational baseline discipline

**Operational baseline** = production configuration as authorized (software, infra, network rules, feature flags, secrets references—not secret values).

| Practice | Detail |
|---|---|
| **Drift detection** | Compare live state to manifest; alert on unauthorized delta |
| **Emergency change** | Allowed with post-hoc reconciliation and gate waiver rules |
| **Runbook versioning** | Runbook ID tied to baseline in CMDB |
| **Observability contract** | Required signals listed in baseline manifest |

Undocumented drift is a **lifecycle defect**, not only an ops nuisance.

## Sustainment program

**Sustain** extends economic and technical usefulness after initial deploy.

| Element | Owner (typical) |
|---|---|
| Sustainment plan | System owner + engineering |
| Funding hooks | Program/portfolio (`technical-program-manager` interface) |
| Patch and vulnerability posture | Engineering + `devsecops` |
| Spares / redundancy parts | Ops or hardware team |
| Documentation currency | System owner |
| Training and operator certification | Ops/training org |

**Cadence:** quarterly sustainment review minimum for high assurance; monthly for Tier 0 if policy requires.

## Obsolescence management

Maintain an **obsolescence register**:

| Field | Description |
|---|---|
| Component | Hardware, OS, runtime, library, SaaS, protocol |
| Version in baseline | As deployed |
| Vendor status | Supported / limited / EOL / unknown |
| EOL date | Published or internal |
| Risk | Security, support, compliance, skill scarcity |
| Mitigation | Refresh, replace, accept with waiver |
| Decision date | Refresh funded or retire triggered |

**Categories:**

- **Software dependency** — CVE exposure, unmaintained packages
- **Platform** — OS, hypervisor, cloud service deprecation
- **Hardware** — MTBF, spare exhaustion
- **People/skills** — tacit knowledge, vendor professional services exit

## Technology refresh

**Tech refresh** is a controlled baseline migration—not ad hoc upgrades.

| Step | Action |
|---|---|
| 1 | Refresh candidate in obsolescence register |
| 2 | Impact analysis on traceability and dependents |
| 3 | Design delta or mini-design phase |
| 4 | Build and verify in non-prod |
| 5 | Gate promotion to production baseline |
| 6 | Update manifest and retire old baseline |

Coordinate with `vp-of-infrastructure` when refresh spans **shared platforms** or data center assets.

## Vendor and support lifecycle

| Checkpoint | Question |
|---|---|
| Contract renewal | Support SLAs still meet tier objectives? |
| End of sale / EOL notice | Captured in register within 30 days? |
| License compliance | Counts match deployment manifest? |
| Third-party risk | Vendor stability; subprocessor changes |

Do not auto-renew without sustainment review for high-assurance systems.

## Sustainment review agenda

Standard agenda (60–90 minutes):

1. Baseline manifest vs drift report
2. Open incidents and repeat failures
3. Patch/CVE posture and exceptions
4. Obsolescence register deltas
5. Upcoming vendor EOL and refresh funding
6. Traceability gaps from last gate
7. Assurance/audit open items (interface only)
8. Decision: continue sustain / accelerate refresh / initiate dispose

**Output:** sustainment review minutes with actions, owners, dates.

## Triggers to dispose phase

Initiate **Dispose** when any apply (document rationale):

- Vendor EOL with no viable refresh
- Security or compliance posture cannot be remediated within risk appetite
- Mission need ends; system superseded
- Cost of sustainment exceeds value (with executive acceptance)
- Unrecoverable technical debt blocking verification

Hand off to `change_baseline_and_retirement.md` for decommissioning plan.
