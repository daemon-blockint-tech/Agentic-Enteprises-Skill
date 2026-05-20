# Compliance specialist scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Program charter](#program-charter)
3. [Stakeholders and RACI](#stakeholders-and-raci)
4. [Deliverables](#deliverables)

## Role boundary

| compliance-specialist | Partner skill |
|---|---|
| GRC program design, scope, gap plans, audit prep | `compliance-engineer` — technical mapping, evidence automation, CCM |
| Cloud assessor packages and API evidence | `cloud-compliance-specialist` |
| Control implementation (IAM, logging, hardening) | `information-security-engineer`, `cloud-security-engineer` |
| Security strategy and IR program | `cybersecurity` |
| Risk register and residual risk scoring | `security-risk-analyst` |
| Contracts, DPAs, legal interpretation | `commercial-counsel` |
| Pentest execution | `penetration-tester` |

**Do not** provide legal conclusions, attest on behalf of the company, or implement infrastructure.

## Program charter

Capture in one page:

- **Objectives** — customer contracts, market entry, insurance, board mandate
- **Frameworks in scope** — e.g., SOC 2 TSC, ISO 27001 Annex A subset, HIPAA safeguards, PCI SAQ level
- **Systems and environments** — prod vs non-prod, SaaS vs on-prem, geographies
- **Data classes** — PII, PHI, PCI CHD, confidential IP
- **Calendar** — target report date, observation period, internal mock-audit dates
- **Success criteria** — clean opinion, no material exceptions, customer questionnaire turnaround SLA

Revisit charter when product, M&A, or major vendor changes occur.

## Stakeholders and RACI

| Activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| Framework scope | CISO / compliance lead | compliance-specialist | Legal, Eng | Exec sponsor |
| Control matrix | compliance-specialist | Control owners | `compliance-engineer` | Auditors (read-only) |
| Policy approval | General counsel / policy owner | compliance-specialist draft | HR, IT, Security | All staff (publish) |
| Evidence collection | Control owners | `compliance-engineer` | IT ops | compliance-specialist |
| Audit walkthroughs | compliance-specialist | SMEs per domain | `cybersecurity` | Leadership |

Assign **one named owner per control family** (access, change, vuln, logging, vendors).

## Deliverables

Minimum viable program artifacts:

1. Scope memo (approved)
2. Control matrix with status (implemented / partial / gap / N/A)
3. Gap remediation plan with dates
4. Policy index with version and approver
5. Exception register with expiry
6. Audit request tracker
7. Vendor tier list and review schedule

Hand off technical evidence build to `compliance-engineer` once matrix columns for **evidence source** and **automation** are defined.
