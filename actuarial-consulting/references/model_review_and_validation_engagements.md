# Model review and validation engagements

## Table of contents

1. [Engagement types](#engagement-types)
2. [Scope and criteria](#scope-and-criteria)
3. [Testing themes](#testing-themes)
4. [Findings and severity](#findings-and-severity)
5. [Remediation and re-test](#remediation-and-re-test)
6. [Opinion support coordination](#opinion-support-coordination)

## Engagement types

| Type | Purpose | Typical client |
|---|---|---|
| Independent validation | Third-party fit-for-purpose assessment | CRO, model risk |
| Peer review | Qualified actuary review pre-sign-off | Appointed actuary |
| Opinion support | Workpapers for regulatory or statutory opinion | Chief actuary |
| Use test (overview) | Model appropriate for stated use | Finance, audit |

Define **independence** requirements before accepting validation of models the firm built.

## Scope and criteria

Document in SOW:

- **Model name**, version, owner, platform
- **Intended use** (pricing, reserving, capital, ALM)
- **Materiality** threshold for findings
- **Standards** referenced (firm model risk policy, SR 11-7 overview for banks if relevant)
- **Access**: code, parameters, test data, change logs

Deliverable: validation report + finding register + management letter if required.

## Testing themes

| Theme | Questions |
|---|---|
| Conceptual soundness | Right methods for product and data? |
| Inputs | Data lineage, completeness, overrides logged? |
| Implementation | Code matches spec; version control? |
| Output reasonability | Sensitivities, benchmarks, prior period |
| Governance | Owner, approval, change management, access |
| Documentation | User guide, limitation, known issues |

Depth scales with **model materiality** and **regulatory classification** (overview only).

## Findings and severity

| Severity | Definition | Example |
|---|---|---|
| Critical | Material misstatement risk or control failure | Wrong loss development applied system-wide |
| High | Significant issue requiring fix before use | Unapproved assumption override |
| Medium | Issue with workaround or limited scope | Incomplete documentation |
| Low | Improvement | Enhanced monitoring |

Finding format:

- **ID**, **title**, **severity**, **description**, **evidence**
- **Recommendation**, **management response**, **target date**

## Remediation and re-test

Track to closure:

1. Management **action plan** with owner and date
2. **Re-test** evidence for Critical/High items
3. **Conditional approval** language if issues remain
4. **Annual re-validation** trigger for material model changes

Do not sign **unqualified** validation language while Critical findings are open unless scope explicitly allows with disclosure.

## Opinion support coordination

When supporting statutory or regulatory opinion:

- Align **data cutoff** with opinion date
- Reconcile validation conclusions to **statement of actuarial opinion** exhibits
- Maintain **reviewer documentation** separate from client marketing materials
- Escalate **legal interpretation** of filing requirements to `commercial-counsel`

Consulting owns **process and documentation index**; appointed actuary owns **opinion text and sign-off**.
