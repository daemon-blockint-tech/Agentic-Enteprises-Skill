# Security and compliance fit

## Table of contents

1. [Purpose and limits](#purpose-and-limits)
2. [Fit assessment workflow](#fit-assessment-workflow)
3. [Control mapping](#control-mapping)
4. [Common frameworks](#common-frameworks)
5. [Questionnaires and evidence](#questionnaires-and-evidence)
6. [Gap and mitigation format](#gap-and-mitigation-format)

## Purpose and limits

Produce a **technical fit assessment**: how the proposed solution supports customer obligations and your product controls.

- **In scope:** architecture-level controls, data flows, encryption, identity, logging, residency, shared responsibility
- **Out of scope:** legal interpretation, contract language, formal audit opinion, pen test execution

Route legal terms → `commercial-counsel`. SOC 2/ISO evidence packs → `compliance-engineer`. Cloud guardrail implementation → `cloud-security-engineer`.

## Fit assessment workflow

1. **Inventory obligations** — frameworks, customer policies, RFP security section, data classifications
2. **Map solution** — components, data stores, trust boundaries, admin paths
3. **Map controls** — product native, config required, customer responsibility, gap
4. **Threat skim** — STRIDE-lite on key flows (auth, admin, integration, data export)
5. **Document gaps** — mitigation, roadmap, or acceptance with risk owner
6. **Review** — security architect / `cloud-security-engineer` before external commit

## Control mapping

Use a consistent table:

| Control theme | Requirement / RFP ref | Solution element | Status | Notes |
|---|---|---|---|---|
| Access control | REQ-SEC-01 | SSO + RBAC | Met | Customer IdP federation |
| Encryption at rest | REQ-SEC-02 | Managed DB CMK | Partial | Customer-managed keys phase 2 |
| Audit logging | REQ-SEC-03 | Central audit API | Met | 90-day retention default |
| Network isolation | REQ-SEC-04 | Private Link | Gap | Mitigation: IP allowlist PoC |

**Status values:** Met | Partial | Gap | N/A (customer responsibility)

Align with **shared responsibility model**—state who configures, operates, and attests each control.

## Common frameworks

| Framework | Architect focus |
|---|---|
| SOC 2 | Trust services criteria mapping; logging, access, change |
| ISO 27001 | Annex A control themes; ISMS boundaries |
| HIPAA | PHI flows, BAA scope, encryption, audit |
| PCI DSS | Cardholder data environment scope (usually avoid storing CHD) |
| GDPR / privacy | Lawful basis, DPA, residency, deletion, subprocessors |
| FedRAMP / sovereign | Boundary, authorized services, data location |

Do not claim certification coverage beyond your organization's actual attestations.

## Questionnaires and evidence

For SIG, CAIQ, customer security portals:

- **Reuse** approved answers from security/compliance team; do not invent new commitments
- **Flag deltas** where the proposed architecture differs from standard deployment
- **Attach** architecture diagrams and data-flow diagrams requested by questionnaire
- **Track** due dates and owners in engagement RAID (with `technical-program-manager` if program-scale)

Evidence types delivery may need later: pen test summary, SOC report, subprocessors list, encryption whitepaper.

## Gap and mitigation format

```
Gap ID: GAP-001
Control: Customer requires customer-managed keys for all DBs
Current: Platform-managed keys in PoC
Risk: Medium — contractual blocker for production
Mitigation options:
  1) Enable CMK integration in phase 1 (effort: X weeks)
  2) Accept platform keys with supplemental controls (legal review required)
Decision needed by: [date] — Owner: [name]
```

Escalate **Gap** items that block signature or go-live before solution approval.

Cloud-specific threat patterns and guardrails → `cloud-security-engineer`. Enterprise security program → `information-security-engineer`.
