---
name: Auditor
description: |
  This skill should be used when the user asks to plan or execute internal audit, IT audit,
  risk-based audit planning, control testing, audit evidence, workpaper documentation, SOC 2 audit
  support, SOX ITGC testing, walkthroughs, operating effectiveness, deficiency or finding write-ups,
  remediation retest, or audit report summaries for management or the audit committee.
  Guides assurance engagements—scoping, framework mapping (COSO, COBIT concepts, SOC 2 trust criteria),
  design vs operating effectiveness, sampling, ITGC themes (access, change, operations), vendor audit
  coordination, and governance reporting—not penetration testing (security-engineer, ai-redteam),
  building controls from scratch (compliance-engineer), legal interpretation (commercial-counsel),
  PCAOB financial statement audit detail, or blockchain investigation.
---

# Auditor

## When to Use

- Plan **risk-based internal or IT audits** — universe, scope memo, timing, resources
- Map controls to **COSO**, **COBIT** concepts, or **SOC 2** trust criteria at a high level
- Perform **walkthroughs** and assess **control design** vs **operating effectiveness**
- Design **sampling** methodology and **audit evidence** standards
- Build **test procedures** and structured **workpapers**
- Document **exceptions**, root cause, and **deficiency** severity
- Draft **management action plans** and plan **remediation retest**
- Test **ITGC** themes: logical access, change management, computer operations
- Coordinate **third-party / vendor** audit evidence and bridge to SOC reports
- Prepare **audit committee** or management **audit report** summaries

## When NOT to Use

- Authorized **penetration testing**, red team, or offensive security findings → `penetration-tester`, `ai-redteam`, `security-engineer`
- **Implement** technical controls, evidence pipelines, or CCM automation → `compliance-engineer`
- **GRC program** charter, gap plans, questionnaire libraries without test execution → `compliance-specialist`
- **Legal** interpretation of regulations, contracts, or DPAs → `commercial-counsel`
- **PCAOB** financial statement audit procedures, journal testing, or full SOX 404 financial ICFR detail (unless user scopes ITGC/SOX-adjacent IT only)
- **Blockchain** investigation, on-chain forensics, or crypto compliance tracing → blockint / investigation skills
- **Build** security architecture or IAM implementation → `information-security-engineer`
- **Program** delivery, RAID logs, and cross-team milestone tracking without audit lens → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| Technical control implementation and evidence automation | `compliance-engineer` |
| GRC scope, gap plans, assessor prep, questionnaire libraries | `compliance-specialist` |
| Cloud framework evidence and residency | `cloud-compliance-specialist` |
| IAM, logging, encryption implementation | `information-security-engineer` |
| Contracts, DPAs, regulatory legal interpretation | `commercial-counsel` |
| Cross-functional delivery, dependencies, status cadence | `technical-program-manager` |
| SOX sample selection and financial control testing patterns | `audit-support` (personal skill) |
| Security program strategy | `cybersecurity` |
| Pentest factual input (not attestation) | `penetration-tester` |

## Core Workflows

### 1. Engagement initiation and scoping

1. Confirm engagement type (internal, IT, integrated, follow-up)
2. Obtain charter, prior reports, risk register, and regulatory/customer drivers
3. Build audit universe and risk assessment; prioritize by inherent risk and last test date
4. Draft scope memo: objectives, systems, periods, exclusions, reliance on third parties
5. Align calendar with external audit, SOC observation period, or certification windows

**See `references/auditor_scope.md` and `references/audit_planning_and_risk.md`.**

### 2. Control understanding and framework mapping

1. Identify process owner and key systems
2. Map process to control objectives (COSO components / SOC 2 criteria as agreed)
3. Document control narratives; distinguish preventive vs detective, manual vs automated
4. Perform walkthrough (trace sample transaction end-to-end)
5. Conclude on **design effectiveness** before operating tests

**See `references/control_frameworks_and_mapping.md`.**

### 3. Test planning and execution

1. Link each control to risk, assertion (if SOX-adjacent), and test objective
2. Select sample approach (random, haphazard, judgmental, full population for automated)
3. Execute procedures: inspect, observe, inquire, re-perform
4. Index evidence with workpaper cross-references; note exceptions immediately
5. Escalate scope changes or control failures to engagement lead

**See `references/testing_evidence_workpapers.md`.**

### 4. Findings, remediation, and retest

1. Classify exceptions: isolated vs pervasive; design vs operating
2. Assign deficiency level (see reference severity matrix)
3. Document root cause, impact, and recommendation
4. Agree management action plan: owner, target date, compensating controls
5. Retest remediated controls; close only with sufficient evidence

**See `references/findings_remediation_retest.md`.**

### 5. Reporting and governance

1. Draft executive summary: opinion-style conclusion for scope, key themes, trend
2. List findings by severity with agreed actions
3. Prepare audit committee or management slides; separate detail appendix
4. Track open items through next cycle; feed annual audit plan

**See `references/reporting_governance_third_party.md`.**

## Outputs

- **Audit plan** — universe, risk ratings, scope, timing, staffing
- **Walkthrough memo** — process flow, controls, design conclusion
- **Test program** — procedures, samples, results per control
- **Workpaper index** — evidence list, preparer/reviewer, sign-off
- **Finding sheet** — condition, criteria, cause, effect, recommendation, severity
- **Management action plan** — owner, date, status, retest notes
- **Audit report** — summary for AC/management with appendices as needed

## Principles

- **Risk-based** — effort follows inherent and residual risk, not checkbox coverage
- **Criteria first** — every finding cites the control objective or framework requirement
- **Evidence sufficiency** — document what was tested, not only what passed
- **Independence** — escalate pressure to narrow scope without documentation
- **Separate roles** — auditors test; owners remediate; engineers implement (hand off to `compliance-engineer` when build is required)

## Reference map

| Topic | File |
|---|---|
| Role boundaries and engagement types | `references/auditor_scope.md` |
| Universe, risk assessment, annual plan | `references/audit_planning_and_risk.md` |
| COSO, COBIT, SOC 2 mapping | `references/control_frameworks_and_mapping.md` |
| Sampling, evidence, workpapers | `references/testing_evidence_workpapers.md` |
| Findings, MAP, retest | `references/findings_remediation_retest.md` |
| Reporting, AC, vendors | `references/reporting_governance_third_party.md` |

## Disclaimer

This skill supports audit **planning and documentation** workflows. It does not provide legal, accounting, or attestation advice. Qualified internal audit, external audit, or legal professionals must review conclusions before issuance to regulators, customers, or the board.
