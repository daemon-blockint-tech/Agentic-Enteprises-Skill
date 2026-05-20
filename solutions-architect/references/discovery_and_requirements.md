# Discovery and requirements

## Table of contents

1. [Discovery workflow](#discovery-workflow)
2. [Interview guide](#interview-guide)
3. [Current-state capture](#current-state-capture)
4. [Requirements structure](#requirements-structure)
5. [NFR catalog](#nfr-catalog)
6. [Assumptions and risks](#assumptions-and-risks)

## Discovery workflow

1. **Frame** — restate the problem, users, and decision timeline in one paragraph
2. **Discover** — interviews, document review, workshops (see interview guide)
3. **Synthesize** — current state, pain points, constraints, success metrics
4. **Specify** — requirements pack with IDs and priority
5. **Validate** — review with sponsor, security, and delivery lead
6. **Baseline** — version the pack; log changes through the engagement

Do not start detailed architecture until **must-have requirements** and **hard constraints** are written down.

## Interview guide

| Area | Questions |
|---|---|
| Outcomes | What changes for users/customers if this succeeds? How measured? |
| Scope | What is in phase 1 vs later? What is explicitly out? |
| Systems | What systems touch this workflow today? Who owns each? |
| Data | What data is created, read, stored? Classification and residency? |
| Identity | How do users authenticate? B2B federation? Service accounts? |
| Integrations | Batch vs real-time? Existing APIs, ETL, iPaaS, file drops? |
| Volume | Peak users, transactions, data growth over 12–36 months? |
| Operations | Who runs it? SLOs? On-call? Change windows? |
| Security | Required frameworks, past audits, questionnaire deadlines? |
| Commercial | Budget band, build vs buy bias, incumbent vendors? |

Capture **quotes and sources** (interview date, doc name) for contentious requirements.

## Current-state capture

Document at a level sufficient for integration design:

- **Actors** — human roles, external partners, system accounts
- **Systems** — name, owner, hosting, lifecycle (legacy/modern)
- **Flows** — primary happy path and top exceptions
- **Pain** — reliability, latency, manual steps, compliance gaps
- **Technical debt** — blockers called out by customer IT

Use a simple context diagram; defer C4 depth to `senior-system-architecture` for internal product work.

## Requirements structure

Assign stable IDs: `REQ-###`, `NFR-###`.

| Priority | Meaning |
|---|---|
| Must | Deal-breaker; RFP compliance; phase 1 |
| Should | Important; workaround exists |
| Could | Defer without blocking value |
| Won't (now) | Explicit deferral with rationale |

Each requirement:

```
ID: REQ-001
Priority: Must
Statement: As a [actor], I need [capability] so that [outcome].
Acceptance: Given/When/Then or measurable test.
Source: RFP §3.2 / workshop 2024-01-15
Dependencies: REQ-005, integration with System X
```

Maintain a **traceability matrix**: requirement ID → design element → test/PoC scenario → RFP section.

## NFR catalog

| Category | Capture |
|---|---|
| Availability | Tier, uptime target, maintenance windows |
| Performance | Latency, throughput, batch windows |
| Scalability | Headroom, autoscaling expectations |
| Security | AuthN/Z model, encryption, network isolation |
| Privacy | PII handling, retention, deletion |
| Compliance | Frameworks, audit evidence, residency |
| Operability | Logging, alerting, backup/RTO/RPO |
| Interoperability | API standards, versioning, idempotency |
| Cost | Budget cap, unit economics target |
| Supportability | SLAs, escalation, documentation |

Quantify where possible; mark **TBD** with owner and date to resolve.

## Assumptions and risks

**Assumptions log** — anything the design depends on (API availability, data quality, customer provides VPN access).

**Risks** — probability × impact; mitigation or acceptance; owner.

Escalate assumptions that affect **pricing, timeline, or compliance** before solution sign-off.

Deep business case modeling → `business-consultant`. Cloud-specific TCO/NPV → `cloud-economist`.
