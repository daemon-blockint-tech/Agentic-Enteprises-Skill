# Policies, procedures, and evidence

## Table of contents

1. [Policy hierarchy](#policy-hierarchy)
2. [Procedure outlines](#procedure-outlines)
3. [Evidence requirements](#evidence-requirements)
4. [Quality rules](#quality-rules)

## Policy hierarchy

| Level | Purpose | Example |
|---|---|---|
| Policy | Management intent, mandatory | Information Security Policy |
| Standard | Measurable requirements | Password standard, encryption standard |
| Procedure / SOP | Step-by-step operations | Access provisioning, incident response |
| Guideline | Recommendations | Secure coding tips |

Draft **outlines** for approval; legal or policy committee owns final language.

Minimum policy set for SOC 2 / ISO-style programs:

- Information security
- Acceptable use
- Access control
- Change management
- Incident response
- Vendor / third-party risk
- Business continuity / disaster recovery
- Data classification and handling
- Risk management (may align with `security-risk-analyst` register)

Version every document: number, date, approver, next review date (annual typical).

## Procedure outlines

For each in-scope control family, procedure outline includes:

1. **Purpose and scope**
2. **Roles** — requester, approver, administrator
3. **Triggers** — hire, termination, production change, vulnerability SLA breach
4. **Steps** — numbered, testable
5. **Records** — ticket IDs, logs, sign-offs
6. **Exceptions** — escalation path
7. **Review cadence**

Example families: user access provisioning/review, privileged access, change approval, vulnerability remediation, backup restore test, security awareness training.

## Evidence requirements

Define evidence at the **requirement** level before automation:

| Evidence attribute | Specify |
|---|---|
| Artifact | IdP export, PR list, scan report, training completion |
| Population | All prod users vs sample rules |
| Period | Observation window, quarterly, point-in-time |
| Owner | Who attests accuracy |
| Storage | System of record, retention, access control |
| Redaction | Customer PII rules for auditor folders |

Distinguish:

- **Program evidence** — policy approval, risk acceptance, org chart
- **Operating evidence** — logs, tickets, reviews showing control operated
- **Technical evidence** — configs and API exports (`compliance-engineer`, `cloud-compliance-specialist`)

## Quality rules

Reject evidence that is:

- Undated or screenshot-only without system metadata
- Missing population definition for sample-based controls
- Prepared only for audit with no operating history
- Owned by unnamed "IT" without accountable individual

Prefer **primary sources** (tickets, IdP, CI) over narrative memos.
