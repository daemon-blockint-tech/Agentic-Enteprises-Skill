# Quality assurance and documentation

## Table of contents

1. [Case file standards](#case-file-standards)
2. [Documentation elements](#documentation-elements)
3. [Peer review](#peer-review)
4. [QA sampling program](#qa-sampling-program)
5. [Defect taxonomy](#defect-taxonomy)
6. [Rework and sign-off](#rework-and-sign-off)
7. [Audit and exam support](#audit-and-exam-support)

## Case file standards

Every investigated case should be **reconstructable** by a second analyst without oral history.

| Standard | Requirement |
|---|---|
| **Completeness** | Triage, analysis, disposition, approvals present |
| **Accuracy** | Amounts match source systems; currency assumptions stated |
| **Clarity** | Facts vs opinion labeled |
| **Traceability** | Source system, pull date, and query parameters noted |
| **Timeliness** | Contemporaneous notes; late additions flagged |
| **Access control** | Need-to-know; no copies in unsecured channels |

## Documentation elements

Minimum artifacts by stage:

| Stage | Artifacts |
|---|---|
| **Triage** | Priority score, minimum data check, route/disposition |
| **Investigation** | Chronology table, flow summary, typology worksheet |
| **Analysis** | Hypothesis log, innocent-explanation tests |
| **Escalation** | MLRO pack (if applicable) |
| **Closure** | Final rationale, closure code, TM feedback fields |
| **QA** | Reviewer checklist, findings, rework record |

**Exhibit index**: number, title, source, date obtained, sensitivity.

**Decision log**: date, actor, decision, rationale (overrides, priority changes, reopen).

## Peer review

Use peer review before MLRO escalation when policy requires or case exceeds thresholds.

Reviewer confirms:

- Scope appropriate; no material txs omitted
- Typologies tested against facts
- Innocent explanations documented
- Escalation pack complete and internally consistent
- No **prohibited language** (legal conclusions, guaranteed filing)

Peer reviewer **must not** be the primary analyst or the KYC officer who approved exceptions on same customer.

## QA sampling program

| Parameter | Guidance |
|---|---|
| **Population** | All closed and escalated cases in period |
| **Sample size** | Risk-based: higher for new analysts, new scenarios, STR-path cases |
| **Frequency** | Monthly operational QA; quarterly thematic deep dives |
| **Themes** | Structuring, crypto, PEP, high-value, repeat subjects |

Score cases with a **rubric** (see defect taxonomy). Trend scores by team, scenario, and source system.

## Defect taxonomy

| Severity | Examples |
|---|---|
| **Critical** | Wrong disposition; missed mandatory escalation; factual error on amount/subject |
| **Major** | Incomplete chronology; untested typology; missing innocent-explanation review |
| **Minor** | Formatting; typo in non-material field; late but complete documentation |
| **Advisory** | Style; optional enhancement |

Critical defects require **rework and supervisor sign-off** before closure stands.

## Rework and sign-off

1. QA issues **finding sheet** with severity and due date
2. Analyst **remediates** with tracked changes
3. Reviewer **re-checks** remediated items only or full file per severity
4. Supervisor **signs off** on critical/major closure
5. Feed **root cause** into training and playbooks

## Audit and exam support

For `auditor` or regulator requests:

- Provide **sample lists** with case ID, disposition, date, analyst (not full narrative in email)
- Redact **third-party** and LE-sensitive material per policy
- Explain **QA methodology** and metrics trend
- Distinguish FIU QA from **independent AML testing** (`aml-compliance` scope)

Do not alter historical records; attach **addenda** for corrections with approver.
