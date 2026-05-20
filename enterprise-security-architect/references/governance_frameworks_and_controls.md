# Governance, frameworks, and controls

## Table of contents

1. [Framework mapping](#framework-mapping)
2. [Control tiers](#control-tiers)
3. [Exception lifecycle](#exception-lifecycle)
4. [Risk and GRC interfaces](#risk-and-grc-interfaces)
5. [Metrics](#metrics)

## Framework mapping

Map **architecture building blocks** to framework clauses (not a substitute for audit):

| Framework | Use in architecture |
|---|---|
| NIST CSF 2.0 | Organize capabilities: Govern, Identify, Protect, Detect, Respond, Recover |
| ISO 27001 Annex A | Control themes for standards catalog cross-walk |
| CIS Controls | Prioritized safeguards for implementation backlog |
| SOC 2 Trust Criteria | Customer-facing attestation alignment |
| NIST 800-53 (optional) | Federal or highly regulated overlays |

**Control-to-architecture matrix** columns:

| Column | Content |
|---|---|
| Control ID | Framework reference |
| Architecture block | Pattern ID or domain |
| Implementation owner | Team or role |
| Evidence type | Config, log, design doc, test |
| Automation potential | Manual / semi / full |

Coordinate program scope and audit prep with `compliance-specialist`; automated evidence with `compliance-engineer`.

## Control tiers

| Tier | Definition | Architecture treatment |
|---|---|---|
| Mandatory | Required for all in-scope systems | No ARB waiver without CISO risk acceptance |
| Recommended | Default unless documented deviation | Exception with expiry ≤ 12 months |
| Conditional | Required when trigger applies (e.g., PCI) | Document triggers in standards catalog |
| Prohibited | Banned patterns | Block in design review and procurement |

Examples of **mandatory** patterns: central SSO, no shared admin accounts, encrypted sensitive data at rest, security logging for T0/T1.

## Exception lifecycle

1. **Request** — system, control gap, proposed compensating control
2. **Risk assessment** — inherent/residual input from `security-risk-analyst`
3. **Approval** — authority per tier (ARB lead, CISO delegate)
4. **Conditions** — expiry date, monitoring, remediation plan
5. **Review** — quarterly until closed or renewed with fresh risk acceptance

Never allow **indefinite** exceptions for mandatory controls without executive risk acceptance on record.

## Risk and GRC interfaces

| Activity | Enterprise security architect | Peer |
|---|---|---|
| Control intent and patterns | Owns | — |
| Risk scoring and register rows | Informs | `security-risk-analyst` |
| Audit scope and walkthroughs | Provides architecture evidence | `compliance-specialist` |
| Control implementation | Defines standards | `information-security-engineer`, `cloud-security-engineer` |
| Board risk heat maps | Contributes architecture themes | `security-risk-analyst`, CISO office |

Architecture answers **what good looks like**; risk answers **how much is enough**; GRC answers **what auditors need**.

## Metrics

| Metric | Purpose |
|---|---|
| % T0/T1 on mandatory patterns | Standards adoption |
| Open exceptions past expiry | Governance health |
| Mean time to close ARB findings | Delivery friction |
| Identity coverage (SSO/MFA) | Zero-trust progress |
| Log source coverage | Detect/respond readiness |
| Acquisition integration SLA | M&A risk reduction |

Tie metrics to **investment cases** in executive briefings; avoid vanity counts without remediation owners.
