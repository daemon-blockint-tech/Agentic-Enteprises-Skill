# Zero-tolerance scope and limits

## Table of contents

1. [Purpose and boundaries](#purpose-and-boundaries)
2. [Zero-defect aspiration vs error budgets](#zero-defect-aspiration-vs-error-budgets)
3. [Perfectionism and blame traps](#perfectionism-and-blame-traps)
4. [In scope vs out of scope](#in-scope-vs-out-of-scope)
5. [Domains of application](#domains-of-application)
6. [Charter elements](#charter-elements)

## Purpose and boundaries

**Zero-tolerance for failure** (operational excellence lens) means building **systems and culture** where preventable failures are designed out, caught early, and learned from—without claiming literal zero defects everywhere.

This skill sits between:

- **Reliability operations** (`site-reliability-engineer`) — SLOs, error budgets, capacity
- **Incident program** (`incident-management-engineer`) — SEV, on-call, postmortem process
- **Recovery engineering** (`cyber-resilience-engineer`) — backup, RTO/RPO, restore tests
- **Build validation** (`build-validator`) — automated CI gates

Own **prevention philosophy, verification depth, HRO behaviors, and prevention metrics**—not paging policy, restore architecture, or lint rules alone.

## Zero-defect aspiration vs error budgets

| Concept | Appropriate use | Misuse |
|---|---|---|
| **Zero-defect aspiration** | Safety-critical, auth, payments, classified control planes, OT interlocks | Demanding 100% uptime on experimental features |
| **Error budget** | Customer-facing SLO trade-offs, release velocity vs reliability (`site-reliability-engineer`) | Excusing preventable escapes in tier-0 controls |
| **Zero critical escapes** | Defects that reach production in tier-0/1 without gate bypass | Counting all minor UI bugs as culture failures |
| **Near-miss reporting** | Learning system; mandatory in HRO contexts | Punitive scorecards tied to individual blame |

**Decision rule:** If failure implies **harm, compromise, or regulatory breach**, bias to **prevention, gates, and fail-closed** design. If failure implies **degraded UX or revenue** within agreed SLO, pair with **error budgets** and mitigation—still track escapes.

## Perfectionism and blame traps

| Healthy zero-tolerance | Toxic pseudo zero-tolerance |
|---|---|
| Fix systems that allow repeat incidents | Fire individuals for first honest mistake |
| Celebrate stop-the-line and near-miss reports | Hide problems to meet velocity metrics |
| Invest in verification and independent review | Add paperwork without changing risk |
| Transparent residual risk with owners | “Zero incidents” slogans with no measurement |
| Learning reviews with action owners | Public shaming or “name and blame” postmortems |

Escalate **HR or legal disciplinary** questions out of this skill—stay on engineering and operational norms.

## In scope vs out of scope

| In scope | Out of scope (route to peer skill) |
|---|---|
| Failure-prevention charter, principles, RACI | SLO/error-budget policy → `site-reliability-engineer` |
| Verification gates, independent checks, hold points | War-room command → `incident-management-engineer` |
| Fail-safe/fail-closed and degradation design | Backup/immutability architecture → `cyber-resilience-engineer` |
| Pre-mortem, FMEA, risk registers | CI job definitions only → `build-validator` |
| Stop-the-line triggers and authority | ATO/accreditation packages → `classified-cyber-security-senior-manager` |
| Defect escape, near-miss, repeat-incident metrics | ADR templates without prevention lens → `senior-system-architecture` |

## Domains of application

| Domain | Prevention emphasis |
|---|---|
| **Software** | AuthZ fail-closed, idempotency, invariant tests, canary + rollback, feature flags with safe defaults |
| **Infrastructure** | Blast-radius limits, config drift detection, staged rollouts, break-glass with audit |
| **Safety-critical OT** | Interlocks, manual overrides logged, dual-channel commands, provenance of setpoints |
| **Classified programs** | Two-person rules, change boards, inspection readiness—pair `classified-cyber-security-senior-manager` |

## Charter elements

1. **Scope** — tiers/systems covered; explicit exclusions
2. **Principles** — fail-closed, independent verification, stop-the-line
3. **Governance** — who can bypass gates; audit requirements
4. **Interfaces** — SRE, IR, QA, security, BCM
5. **Metrics** — defect escape, near-miss, repeat incidents, gate bypass rate
6. **Review cadence** — quarterly norm check; after material escape or near-catastrophe

Store charter and gate definitions in a **durable, version-controlled** repository accessible to builders and reviewers.
