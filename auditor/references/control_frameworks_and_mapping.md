# Control frameworks and mapping

## Table of contents

1. [Purpose](#purpose)
2. [COSO](#coso-internal-control--integrated-framework-high-level)
3. [COBIT](#cobit-2019-conceptual-use)
4. [SOC 2 TSC](#soc-2-trust-services-criteria-tsc)
5. [SOX ITGC](#sox-itgc-adjacent)
6. [Control narrative template](#control-narrative-template)
7. [Walkthrough procedure](#walkthrough-procedure)
8. [Design vs operating](#design-vs-operating-effectiveness)
9. [Mapping matrix](#framework-mapping-matrix-example-snippet)
10. [Third-party reliance](#reliance-on-third-party-controls)
11. [Pitfalls](#pitfalls)

## Purpose

Map business and IT controls to **COSO**, **COBIT** concepts, and **SOC 2** trust service criteria at a **high level**—enough to structure narratives and findings without replacing framework official guidance.

## COSO Internal Control — Integrated Framework (high level)

Five components and 17 principles (2013) — use for **internal audit** criteria alignment:

| Component | Audit focus examples |
|---|---|
| **Control environment** | Tone, ethics, board oversight, org structure |
| **Risk assessment** | Objectives, change identification, fraud risk |
| **Control activities** | Approvals, reconciliations, segregation of duties |
| **Information & communication** | Reporting quality, whistleblower, policies |
| **Monitoring activities** | Ongoing eval, separate evaluations, deficiency escalation |

**Mapping tip:** Each tested control should cite at least one **principle** when reporting to AC audiences familiar with COSO.

## COBIT 2019 (conceptual use)

Use COBIT as a **vocabulary** for IT governance and management objectives—not full COBIT assessor certification in routine engagements.

| Area | Example management objectives |
|---|---|
| **EDM** (Evaluate, Direct, Monitor) | Governance alignment, benefit delivery |
| **APO** (Align, Plan, Organize) | Strategy, architecture, risk, vendor |
| **BAI** (Build, Acquire, Implement) | Requirements, change, assets |
| **DSS** (Deliver, Service, Support) | Operations, security, continuity |
| **MEA** (Monitor, Evaluate, Assess) | Performance, compliance, internal control |

**Mapping tip:** ITGC domains align loosely: access → DSS05; change → BAI06; operations → DSS01/DSS04.

## SOC 2 Trust Services Criteria (TSC)

Common **in-scope** categories for service organizations:

| Criterion | Themes |
|---|---|
| **Security (CC)** | Common Criteria — always in scope for SOC 2 |
| **Availability (A)** | Uptime, capacity, monitoring |
| **Processing integrity (PI)** | Complete, accurate, timely processing |
| **Confidentiality (C)** | Protection per agreement |
| **Privacy (P)** | Notice, choice, retention (if applicable) |

### CC series structure (simplified)

- **CC1** — Control environment
- **CC2** — Communication and information
- **CC3** — Risk assessment
- **CC4** — Monitoring activities
- **CC5** — Control activities
- **CC6** — Logical and physical access
- **CC7** — System operations
- **CC8** — Change management
- **CC9** — Risk mitigation (vendor)

**Internal audit use:** When supporting a SOC readiness review, map company controls to **CC6–CC8** for ITGC-heavy narratives.

## SOX ITGC (adjacent)

When user scopes **SOX ITGC**, map to classic domains:

| Domain | Typical controls |
|---|---|
| **Access** | Provisioning, termination, periodic review, privileged access |
| **Change** | SDLC, approval, segregation, emergency change |
| **Computer operations** | Batch monitoring, backup, job scheduling |
| **Program development** | For in-scope custom financial apps |

Distinguish **ITGC** from **application controls** (e.g., automated three-way match)—test both when they support financial assertions.

## Control narrative template

For each control:

```text
Control ID:
Control objective:
Risk addressed:
Control type: Preventive / Detective | Manual / Automated
Frequency:
Owner:
Performer:
Evidence typically retained:
Dependencies (systems, vendors):
COSO principle(s):
SOC TSC (if applicable):
Design conclusion: Effective / Deficient / N/A
Operating conclusion: (after testing)
```

## Walkthrough procedure

1. Select **representative transaction** or event (hire, change deploy, user termination)
2. Interview owner; obtain SOP or policy
3. Trace **evidence** at each step (ticket, approval, log, config)
4. Note **breaks** (skipped step, override, undocumented approval)
5. Conclude **design**: would a properly operating control prevent/detect the risk?
6. Identify **key reports** and **configs** relied upon (for operating tests)

## Design vs operating effectiveness

| Phase | Question | Typical procedures |
|---|---|---|
| **Design** | Is the control suitably designed? | Walkthrough, narrative update |
| **Operating** | Did it run consistently? | Sample testing over period |

Do not test operating effectiveness if design is **deficient** unless documenting failure modes for the report.

## Framework mapping matrix (example snippet)

| Company control ID | Description | COSO | SOC CC | SOX ITGC |
|---|---|---|---|---|
| IAM-01 | Joiner/mover/leaver | CC5, CC6 | CC6.1–6.3 | Access |
| CHG-02 | Production change approval | CC5, CC8 | CC8.1 | Change |
| OPS-03 | Backup restore test | CC7 | CC7.4 | Operations |

Maintain matrix in GRC tool or spreadsheet; version when policies change.

## Reliance on third-party controls

When a control is **performed by a vendor** (IdP, cloud, payroll):

1. Obtain **SOC 1/2** report (correct type and period)
2. Review **bridge letter** for gap period
3. Evaluate **CUECs** — test company-side controls
4. Document **not tested** vendor controls clearly

Do not assert vendor controls were tested unless procedures say so.

## Pitfalls

| Pitfall | Fix |
|---|---|
| Criteria soup (mixing frameworks in one finding) | Pick primary criteria; cross-ref in appendix |
| Mapping every control to all frameworks | Map primary + optional secondary |
| Confusing policy existence with control | Test operation, not only document review |
| Ignoring subservice organizations | Explicit CUEC testing plan |
