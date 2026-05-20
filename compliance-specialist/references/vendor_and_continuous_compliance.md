# Vendor and continuous compliance

## Table of contents

1. [Vendor risk tiers](#vendor-risk-tiers)
2. [Questionnaire workflow](#questionnaire-workflow)
3. [Response library](#response-library)
4. [Continuous compliance program](#continuous-compliance-program)
5. [Metrics and reporting](#metrics-and-reporting)

## Vendor risk tiers

| Tier | Criteria | Review cadence |
|---|---|---|
| Critical | Processes sensitive data, production access, or single-point failure | Annual + contract events |
| High | Material subprocessors in audit scope | Annual |
| Medium | Limited data, no prod access | Every 2 years |
| Low | No sensitive data, commodity SaaS | Questionnaire at onboarding |

Document tier rationale. Align subprocessors list with SOC/ISO scope memo.

## Questionnaire workflow

1. **Intake** — SIG, CAIQ, custom Excel, customer security portal
2. **Triage** — due date, customer revenue tier, repeating vs net-new
3. **Assign** — compliance-specialist coordinates; SMEs answer domain sections
4. **Consistency check** — compare to approved response library; flag conflicts
5. **Evidence attach** — link SOC report (under NDA), pen test summary, policies index
6. **Approval** — security lead or delegate before customer send
7. **Archive** — version, date, approver for reuse

**Legal sections** (indemnity, DPA terms) → `commercial-counsel`, not compliance-specialist alone.

Technical assertions (encryption, logging) → validate with `information-security-engineer` or `cloud-security-engineer`.

## Response library

Maintain approved answers for common themes:

- Organizational security governance
- Access control and MFA
- Change and release management
- Vulnerability and patch management
- Incident response and breach notification **process** (not legal advice)
- BCP/DR and backups
- Subprocessor list and locations
- Certifications in scope (SOC 2, ISO) with report date

Each entry: answer text, last reviewed date, evidence pointer, owner.

When library answer is stale (>6 months or post-incident), block reuse until refresh.

## Continuous compliance program

Shift from **point-in-time audit** to operating rhythm:

| Activity | Cadence |
|---|---|
| Control owner attestation | Quarterly |
| Access reviews | Quarterly minimum |
| Policy review | Annual |
| Tabletop / IR exercise | Annual |
| Vendor critical re-assessment | Annual |
| Exception register review | Monthly |
| Control matrix status update | Monthly |
| Leadership GRC summary | Quarterly |

Integrate drift detection and automated collectors via `compliance-engineer` once matrix defines sources.

Cloud posture dashboards → `cloud-compliance-specialist`.

## Metrics and reporting

Executive dashboard (keep small):

- % controls implemented vs in-scope
- Open gaps by severity and age
- Overdue remediations
- Exceptions past expiry (target zero)
- Customer questionnaire turnaround time
- Audit readiness score (mock assessment trend)

Tie metrics to **risk appetite** discussion with `security-risk-analyst` and `cybersecurity`; do not optimize vanity percentages without risk context.
