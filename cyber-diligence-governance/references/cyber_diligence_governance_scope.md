# Cyber diligence and governance scope

## Table of contents

1. [Program purpose](#program-purpose)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Boundaries vs peer skills](#boundaries-vs-peer-skills)
5. [Roles and RACI](#roles-and-raci)
6. [Lifecycle and cadence](#lifecycle-and-cadence)

## Program purpose

Enable **informed decisions** on cyber risk in transactions and third-party relationships by:

- Structuring **diligence** so findings are evidence-backed, prioritized, and actionable
- Supporting **governance cadence** so security posture and exceptions are visible to leadership
- Bridging **deal, legal, and engineering** without owning closing mechanics or control deployment

This skill covers **analysis, synthesis, and governance design**—not hands-on testing or tool configuration.

## In scope

| Area | Examples |
|---|---|
| M&A / investment diligence | Request lists, VDR review, control maturity, breach history, integration risk |
| Vendor / TPRM | Tiering, assessments, concentration, renewal and offboarding |
| Questionnaires | SIG, CAIQ, custom portals; evidence mapping; consistency checks |
| Gap analysis | Control themes vs baseline (e.g., identity, vuln mgmt, IR, SDLC) for diligence context |
| Integration risk | Identity merge, data separation, tooling overlap, key-person dependency |
| Reporting | IC memo, board appendix, steering updates, remediation trackers |
| Governance | Security committee agenda, metrics, exception register review |

## Out of scope

| Topic | Route to |
|---|---|
| Pentest execution and exploit proof | `penetration-tester`, `web-pentester`, `network-pentester` |
| AI use-case classification, model cards, AI policy | `ai-risk-governance` |
| Enterprise risk register, FAIR, appetite (standing program) | `security-risk-analyst` |
| GRC framework scope, audit prep, attestation | `compliance-specialist` |
| Evidence automation from IdP/CSPM/CI/CD | `compliance-engineer` |
| Contract redlines, DPA negotiation | `commercial-counsel` |
| Closing matrix, CPs, signing, funds flow | `transaction-manager` |
| IAM/SIEM/EDR implementation | `information-security-engineer` |
| CISO strategy, risk appetite, board operating model | `chief-information-security-officer` |
| Live CSIRT / SOC operations | `incident-responder`, `soc-analyst` |
| Standing TPRM intake, scoring, continuous monitoring | `vendor-cyber-risk-analyst` |

## Boundaries vs peer skills

### `vendor-cyber-risk-analyst`

- **Vendor analyst owns:** ongoing TPRM operations—intake queues, tiering at scale, questionnaire scoring, continuous monitoring, vendor risk dashboards, renewal/offboarding **program** execution.
- **This skill owns:** **deal- and investment-weighted** diligence (M&A, IC/board packs, integration risk) and **governance cadence** across transactions and leadership forums; vendor assessment **in that context** or when procurement needs a diligence-style summary.
- **Handoff:** Day-to-day vendor assessments and monitoring → `vendor-cyber-risk-analyst`; M&A target review or IC cyber brief → this skill.


### `ai-risk-governance`

- **AI skill owns:** model/system documentation, AI use-case tiers, AI acceptable use, AI vendor data/fine-tuning terms, NIST AI RMF / ISO 42001 / EU AI Act–style mapping for AI systems.
- **This skill owns:** enterprise cyber diligence on a **target or vendor as a whole** (including AI as one workstream), transaction integration of AI tooling, and board/deal narrative on cyber materiality.
- **Handoff:** When diligence centers on autonomous agents, training data, or regulated AI products, pull `ai-risk-governance` for tiering and documentation depth; fold summary into deal findings.

### `security-risk-analyst`

- **Risk analyst owns:** ongoing risk register, inherent/residual scoring, treatment options, KRIs, and standing third-party risk **tiers in the enterprise program**.
- **This skill owns:** **time-boxed** diligence and governance packs for a **specific deal, investment, or vendor event**; findings that feed (not replace) the register.
- **Handoff:** After close or vendor approval, transfer accepted risks and mitigations to `security-risk-analyst` with owners and review dates.

### `compliance-specialist`

- **Compliance owns:** audit program, control matrices for attestation, continuous compliance operating model, approved questionnaire **library** maintenance.
- **This skill owns:** **evaluating** third-party or target responses during diligence/procurement; gap themes for deal terms; governance reporting on security posture.
- **Handoff:** Align questionnaire answers with compliance library where possible; escalate attestation scope changes to `compliance-specialist`.

## Roles and RACI

| Activity | Deal lead / Corp dev | Cyber diligence lead | Legal | IT / Security engineering | CISO / Security leadership |
|---|---|---|---|---|---|
| Diligence scope | A | R | C | C | I |
| Request list | C | R | C | C | I |
| Evidence review | I | R | C | C | C |
| Findings severity | C | R | C | C | A |
| IC / board brief | C | R | C | C | A |
| Deal protections (terms) | C | C | R | I | C |
| Post-close integration backlog | A | C | I | R | A |

R = responsible, A = accountable, C = consulted, I = informed. Adjust titles to your organization.

## Lifecycle and cadence

| Phase | Typical activities |
|---|---|
| Plan | Scope memo, access plan (VDR, interviews), timeline vs signing |
| Execute | Requests, evidence triage, interviews, technical deep dives as needed |
| Synthesize | Findings register, red flags, valuation/integration implications |
| Decide | IC/board/deal committee; conditions, escrows, holdbacks (with legal) |
| Transition | Day 1 / 30 / 90 security backlog; identity and tooling integration |
| Operate | Quarterly governance pack; vendor renewals; exception expiry |

Review governance cadence at least **quarterly**; re-run diligence on material vendor or target changes.
