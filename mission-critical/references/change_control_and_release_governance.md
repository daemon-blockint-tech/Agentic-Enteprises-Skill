# Change control and release governance

## Table of contents

1. [Governance principles](#governance-principles)
2. [Change categories](#change-categories)
3. [Tiered release gates](#tiered-release-gates)
4. [Emergency change](#emergency-change)
5. [Rollback and verification](#rollback-and-verification)
6. [Interfaces with SRE and prevention](#interfaces-with-sre-and-prevention)

## Governance principles

High-criticality change management optimizes for **predictable outcomes**, not maximum deploy frequency:

- **Evidence before production** — tests, peer review, security review proportionate to tier
- **Independence** — separate build, verify, approve roles for Tier 0 (`zero-tolerance-for-failure`)
- **Reversibility** — every Tier 0/1 change has tested rollback or forward-fix with same rigor
- **Audit trail** — who approved, what artifact hash, what window, what validation ran
- **Freeze alignment** — honor error-budget freeze **and** regulatory/contractual blackouts

## Change categories

| Category | Examples | Typical path |
|---|---|---|
| **Standard** | Routine config within policy | Automated pipeline + policy checks |
| **Normal** | Feature release, schema migration | CAB or delegated approver by tier |
| **Emergency** | Active SEV, safety patch, active exploit | Expedited approvers + post-implementation review |
| **Maintenance** | Planned outage, DR test | Pre-notified window; customer comms hook |

Tag every change record with **service tier** and **blast-radius estimate**.

## Tiered release gates

Illustrative gate matrix—adapt to org process:

| Gate | Tier 0 | Tier 1 | Tier 2+ |
|---|---|---|---|
| **Architecture / ARB** | Required | Required for structural change | As needed |
| **Security review** | Required | Required for trust boundary | Risk-based |
| **Peer review** | Two-person + specialist | Two-person | Standard |
| **Automated test** | Full suite + contract tests | Full suite | Standard CI |
| **Canary / progressive** | Mandatory; defined success criteria | Mandatory | Recommended |
| **PRR / readiness** | Formal sign-off (`site-reliability-engineer`) | Checklist | Lightweight |
| **CAB approval** | Executive + ops + security | Service owner + delegate | Team lead |
| **Comms / customer** | Pre-approved template | If user-visible | Optional |

**Hold points:** pipeline must **stop** until human approval for Tier 0 production deploy.

## Emergency change

Allowed when **active harm** exceeds delay risk:

1. **Declare** emergency change ID linked to incident if applicable
2. **Minimum approvers** — named roster (not “any manager”)
3. **Scope limit** — smallest change that mitigates; defer unrelated fixes
4. **Real-time comms** — ops bridge + stakeholder awareness
5. **PIR within 48–72h** — retroactive evidence, test gap, tier appropriateness

Document **why normal path was unsafe**; repeated emergencies signal tier or architecture debt.

## Rollback and verification

| Element | Tier 0/1 requirement |
|---|---|
| **Rollback artifact** | Previous version pinned; DB migration reversible or forward-only plan |
| **Health checks** | Automated post-deploy; synthetic journey success |
| **Integrity checks** | Reconciliation, sample transactions, config drift detection |
| **Observation window** | Minimum soak before closing change; on-call staffed |
| **Stop-the-line** | Any ambiguous signal → rollback first (`zero-tolerance-for-failure`) |

## Interfaces with SRE and prevention

| Peer | Contribution |
|---|---|
| `site-reliability-engineer` | PRR, canary metrics, error-budget linkage |
| `zero-tolerance-for-failure` | Independent verification, gate catalog, stop-the-line |
| `build-validator` | CI quality gates—not substitute for Tier 0 CAB |
| `deployment-strategist` | Cutover choreography for large migrations |
| `devops` | Pipeline implementation of hold points |

Your deliverable: **release governance matrix** mapping change type × tier → gates, owners, evidence.
