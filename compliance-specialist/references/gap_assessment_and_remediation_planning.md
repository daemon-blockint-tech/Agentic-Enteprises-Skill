# Gap assessment and remediation planning

## Table of contents

1. [Assessment method](#assessment-method)
2. [Gap classification](#gap-classification)
3. [Remediation plan](#remediation-plan)
4. [Exceptions and risk acceptance](#exceptions-and-risk-acceptance)

## Assessment method

1. **Baseline** — approved policies, prior audit reports, customer questionnaires, incident history
2. **Walkthroughs** — interview control owners; sample one evidence artifact per family
3. **Technical spot-check** — request read-only exports; do not configure systems in this role
4. **Score** each requirement against matrix status
5. **Validate** fixes with re-assessment and linked evidence ticket

Run **mock assessment** 60–90 days before external audit; treat findings like real audit items.

## Gap classification

| Status | Definition | Action |
|---|---|---|
| Implemented | Policy + procedure + control operating; evidence on cadence | Maintain |
| Partial | Control exists but evidence weak, not periodic, or not all systems | Remediate |
| Gap | No control or policy | Remediate or accept with approval |
| N/A | Out of scope with documented rationale | No remediation |
| Inherited | Provider or parent org attests | Document inheritance reference |

Tag gaps with **severity**:

- **Critical** — blocks audit opinion or customer contract
- **High** — likely finding; customer-facing
- **Medium** — should fix before observation end
- **Low** — hygiene; batch with other work

## Remediation plan

Each gap row includes:

| Field | Requirement |
|---|---|
| Gap ID | Stable identifier linked to control matrix |
| Root cause | Missing policy, tooling, staffing, vendor |
| Remediation action | Specific outcome, not "improve security" |
| Owner | Single accountable person |
| Due date | Before observation or contract deadline |
| Dependencies | Budget, vendor, engineering epic |
| Evidence plan | What proof closes the gap |
| Verification | Who signs off and date |

Route **engineering work** to `compliance-engineer` with acceptance criteria copied from evidence plan.

Review remediation plan **weekly** in program standup; escalate overdue critical items to executive sponsor.

## Exceptions and risk acceptance

Maintain an **exception register**:

- Control ID and description of deviation
- Business justification
- Compensating controls
- Approver (role per policy)
- Expiry date (max 12 months unless renewed)
- Re-review trigger (incident, audit, architecture change)

Never leave exceptions verbal-only; auditors will request the register.
