# Prevention, verification, and gates

## Table of contents

1. [Defense in depth](#defense-in-depth)
2. [Verification layers](#verification-layers)
3. [Gate catalog pattern](#gate-catalog-pattern)
4. [Independent checks](#independent-checks)
5. [Bypass and emergency change](#bypass-and-emergency-change)
6. [Evidence and audit trail](#evidence-and-audit-trail)

## Defense in depth

Layer controls so no single failure defeats safety or integrity:

| Layer | Examples |
|---|---|
| **Requirements** | Threat model, misuse cases, safety cases |
| **Design** | Fail-closed authZ, least privilege, blast-radius limits |
| **Implementation** | Static analysis, invariant tests, fuzzing on parsers |
| **Build** | Reproducible builds, signed artifacts (`build-validator`) |
| **Deploy** | Canary, progressive delivery, automated rollback |
| **Runtime** | Rate limits, circuit breakers, anomaly detection |
| **Operations** | Runbook verification, game days, access reviews |

Map layers to **tier** (crown jewels vs standard services)—do not apply maximum depth everywhere without cost trade-off documentation.

## Verification layers

| Layer | Intent | Typical artifacts |
|---|---|---|
| **Self-check** | Author confidence | Unit tests, local integration |
| **Peer review** | Catch logic and design gaps | PR review, architecture review |
| **Independent verification** | Separation of duties | QA sign-off, security review, ops readiness |
| **Environment proof** | Behavior in realistic conditions | Staging soak, shadow traffic, chaos in non-prod |
| **Operational proof** | Humans can run and roll back | Runbook drill, on-call shadow |

**Rule:** Tier-0/1 requires at least **one independent layer** beyond author self-check before production.

## Gate catalog pattern

Document each **hold point** in a gate catalog:

| Field | Description |
|---|---|
| **Gate ID** | Stable identifier |
| **Trigger** | Change types that require this gate |
| **Owner** | Role accountable for pass/fail |
| **Entry criteria** | What must be true to start review |
| **Evidence** | Tests, scans, sign-offs, diagrams |
| **Exit criteria** | Objective pass conditions |
| **SLA** | Max wait time; escalation path |
| **Bypass** | Who can authorize; required post-facto review |

Example gates: architecture review, threat model, ops readiness, DR fit check (`cyber-resilience-engineer`), classified change board (`classified-cyber-security-senior-manager`).

## Independent checks

| Practice | Purpose |
|---|---|
| **Four-eyes on prod change** | Reduce single-actor risk |
| **Reviewer ≠ author** | On critical merges and config pushes |
| **Automated policy gates** | OPA, admission control, protected branches |
| **Sampling audit** | Random deep review of “routine” changes |
| **Red team / tabletop** | Validate assumptions before launch |

Pair automated CI gates (`build-validator`) with **human judgment** for context CI cannot see.

## Bypass and emergency change

| Requirement | Detail |
|---|---|
| **Narrow criteria** | Safety, active incident, regulatory deadline—document which |
| **Time box** | Maximum bypass duration; mandatory follow-up gate |
| **Approver** | Named role; cannot be sole implementer |
| **Telemetry** | Log bypass ID in change ticket and monitoring |
| **After-action** | Retro within 5 business days; convert to permanent fix |

Track **bypass rate** and **repeat bypass reasons**—chronic bypass indicates broken gates, not heroic ops.

## Evidence and audit trail

Store for each gate passage:

- Ticket/link to change record
- Test results, scan reports, review notes
- Approver identity and timestamp
- Residual risks accepted with owner and date

Evidence must be **durable and searchable** for inspections—not only chat threads.
