# Auditor scope and boundaries

## Purpose

Define what **internal / IT / compliance audit** assurance covers in this skill, how it differs from adjacent roles, and which engagement types apply.

## Engagement types

| Type | Focus | Typical outputs |
|---|---|---|
| **Internal audit** | Enterprise risk, governance, operations, finance support | Annual plan, audit reports to AC |
| **IT audit** | Applications, infrastructure, data, ITGC | ITGC test results, system narratives |
| **Integrated audit** | Financial process + underlying IT | Combined walkthroughs, shared samples |
| **Follow-up / retest** | Prior findings, MAP closure | Retest memos, open-item tracker |
| **Pre-audit readiness** | Gap identification before external SOC/ISO | Readiness list (not attestation) |
| **Co-sourced / guest auditor support** | Workpaper prep under CAE direction | Indexed evidence for lead reviewer |

## In scope

- Risk-based **audit planning** and scope memos
- **Control design** assessment via walkthroughs
- **Operating effectiveness** testing with documented samples
- **ITGC** domains: access management, change management, computer operations, backup/DR (high level)
- **SOC 2** trust criteria mapping and bridge letters (high level—not signing SOC opinion)
- **SOX ITGC** and application controls supporting financial reporting (when user scopes IT)
- **Deficiency** grading, root cause, and **management action plans**
- **Remediation retest** planning and execution
- **Third-party** SOC report review and CUECs (complementary user entity controls)
- **Audit committee** and management reporting **summaries**

## Out of scope (route elsewhere)

| Topic | Route to |
|---|---|
| Pentest, exploit validation, red team | `penetration-tester`, `ai-redteam`, `security-engineer` |
| Control implementation, IaC, CCM collectors | `compliance-engineer` |
| GRC program design without testing | `compliance-specialist` |
| Legal/regulatory interpretation | `commercial-counsel` |
| Full financial statement audit (PCAOB) | Narrow to ITGC or defer to financial audit team |
| Journal entries, revenue recognition testing | `audit-support`, finance audit |
| Blockchain tracing | Investigation / blockint skills |
| Security architecture design | `information-security-engineer` |
| Sprint/program delivery management | `technical-program-manager` |

## Independence and objectivity

- Document **scope limitations** (access denied, system retired, management override) in the report.
- Do not **implement** remediations being tested in the same engagement without CAE approval and scope split.
- Rotate assignments where practical; disclose conflicts (prior implementation role, compensation tied to area audited).

## Stakeholders

| Role | Audit interaction |
|---|---|
| **Chief Audit Executive (CAE)** | Plan approval, quality review, AC liaison |
| **Audit committee** | Charter, plan, significant findings, follow-up |
| **Process / control owners** | Walkthroughs, evidence, MAP ownership |
| **CISO / IT leadership** | ITGC scope, risk input, remediation resources |
| **External auditors** | Reliance discussions, PBC coordination |
| **Compliance / GRC** | Framework alignment; avoid duplicating program design |

## Engagement lifecycle (summary)

1. **Initiate** — charter, prior reports, risk inputs
2. **Plan** — universe, scope, resources (`audit_planning_and_risk.md`)
3. **Understand** — narratives, walkthrough, framework map
4. **Test** — samples, evidence, workpapers
5. **Report** — findings, MAP, governance comms
6. **Follow-up** — retest, trending, next-cycle plan

## Deliverable quality bar

Every engagement should leave:

- Traceable **criteria** (policy, framework, control ID)
- **Population** and **sample** description where applicable
- **Preparer / reviewer** sign-off on workpapers
- **Clear finding language** (condition vs criteria vs cause vs effect)

## When to narrow scope with the user

Ask explicitly if the request implies:

- **Attestation** or **sign-off** on SOC/ISO (auditors advise; management asserts)
- **Legal compliance** conclusion (route legal; audit cites control failures only)
- **Financial statement** opinion support beyond ITGC
- **Real-time monitoring** build (engineering skill)

Default to **ITGC + SOC 2 mapping + internal audit methodology** unless the user specifies financial process depth.
