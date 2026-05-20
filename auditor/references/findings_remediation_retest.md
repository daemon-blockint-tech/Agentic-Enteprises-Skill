# Findings, remediation, and retest

## Table of contents

1. [Purpose](#purpose)
2. [Finding structure (5 C’s)](#finding-structure-5-cs)
3. [Root cause categories](#root-cause-categories)
4. [Deficiency severity](#deficiency-severity-levels)
5. [Design vs operating findings](#design-vs-operating-findings)
6. [Management action plan](#management-action-plan-map)
7. [Remediation retest](#remediation-retest)
8. [Aggregation and trending](#aggregation-and-trending)
9. [Escalation triggers](#escalation-triggers)
10. [Pitfalls](#pitfalls)
11. [Work products](#work-products)

## Purpose

Standardize **finding** documentation, **deficiency** severity, **management action plans (MAP)**, and **retest** procedures for internal and IT audits.

## Finding structure (5 C’s)

| Element | Content |
|---|---|
| **Condition** | What was observed (facts, samples, dates) |
| **Criteria** | Policy, framework, control narrative, regulation cite (not legal advice) |
| **Cause** | Root cause category (see below) |
| **Effect** | Risk / impact if uncorrected |
| **Corrective action** | Recommendation; becomes MAP |

Avoid blame language; state observable facts.

### Example (condensed)

```text
Condition: 3 of 25 terminated users retained VPN access >7 days after HR termination date.
Criteria: IAM-01 requires deprovisioning within 24 hours per Access Control Standard §4.2.
Cause: Manual checklist step not performed when HR ticket category = contractor.
Effect: Unauthorized access risk to production network; inconsistent with least privilege.
Recommendation: Automate deprovisioning from IdP; weekly orphan account report.
```

## Root cause categories

| Category | Examples |
|---|---|
| **Design** | Control not designed to address risk |
| **Operating** | Control exists but not performed |
| **Monitoring** | No detective control to catch failure |
| **Governance** | Ownership unclear, policy outdated |
| **Technology** | Tool limitation, misconfiguration |
| **Human error** | One-off mistake (assess pervasiveness) |
| **Capacity** | Understaffing, missed SLA |
| **Third party** | Vendor failure, CUEC not performed |

Select **primary** cause; note contributing factors.

## Deficiency severity levels

Use levels aligned to **internal audit** and **SOX-style** communication (adapt to company policy):

| Level | Typical definition | Reporting |
|---|---|---|
| **Low** | Isolated, limited impact, compensating controls | Management report detail |
| **Moderate** | More than isolated; needs timely remediation | Management + AC awareness |
| **High** | Significant gap; weak mitigation | AC attention, executive sponsor |
| **Critical** | Material exposure or systemic breakdown | Immediate escalation per charter |

### SOX-adjacent terms (when user scopes financial IT)

| Term | High-level meaning | Audit role |
|---|---|---|
| **Control deficiency** | Design or operation does not meet criteria | Document; management assesses |
| **Significant deficiency** | Important enough to merit attention | Flag for financial audit coordination |
| **Material weakness** | Reasonable possibility of material misstatement | Escalate; do not conclude alone |

This skill **documents** conditions; **management and external auditors** conclude on SOX classifications.

## Design vs operating findings

| Type | Conclude when | Retest focus |
|---|---|---|
| **Design deficiency** | Walkthrough shows control cannot meet objective | Redesign + new walkthrough |
| **Operating deficiency** | Design OK; samples failed | Remediation + sample retest |
| **Combined** | Weak design and poor execution | Fix design first |

## Management action plan (MAP)

Each finding with agreed remediation:

| Field | Required |
|---|---|
| Finding ID | Link to workpaper |
| Action description | Specific, measurable |
| Owner | Name + role |
| Target date | |
| Status | Open / In progress / Closed |
| Compensating control (interim) | If any |
| Evidence of completion | Ticket, config, report |
| Retest date | |
| Retest result | Pass / Fail |

### MAP quality checks

- Action addresses **root cause**, not symptom only
- Target date realistic; **interim** controls for high severity
- **No closure** without retest (unless AC accepts risk)

## Remediation retest

### Retest planning

1. Obtain **evidence of implementation** from owner
2. Determine **retest period** (e.g., 30 days post-fix)
3. Select **sample** (often smaller if fix is systemic automation)
4. Execute **same or updated** procedure
5. Document **pass/fail**; reopen finding if fail

### Retest workpaper

Reference original finding ID; state:

- What changed (config, process, tool)
- What was retested
- Sample and results
- **Closed** or **remains open**

## Aggregation and trending

For AC reporting:

- Count open findings by **severity** and **age**
- Repeat findings (same root cause) — flag **systemic** issue
- **Theme** analysis (access, change, vendor)

## Escalation triggers

Escalate to CAE / AC when:

- Management disputes criteria without policy change
- Remediation past target with no acceptable risk acceptance
- Evidence of **fraud** or **willful override** (involve appropriate functions per charter)
- Scope limitation prevents conclusion

## Pitfalls

| Pitfall | Mitigation |
|---|---|
| Vague recommendations | SMART actions with owner |
| Closing on policy update only | Require operating proof |
| Severity inflation | Use defined matrix |
| Retest by same person without review | Independent reviewer on high findings |

## Work products

- **Finding register** (master list)
- **Individual finding sheets** (5 C’s)
- **MAP tracker**
- **Retest memos**
- **Risk acceptance memo** (if remediation declined)
