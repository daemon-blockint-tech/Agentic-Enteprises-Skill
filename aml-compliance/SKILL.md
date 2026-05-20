---
name: AML/Compliance
description: |
  This skill should be used when the user asks about AML compliance, anti-money laundering, KYC, CDD, EDD,
  PEP screening, sanctions screening, transaction monitoring, SAR, STR, suspicious activity, FATF, BSA,
  financial crime compliance, travel rule, AML risk assessment, or MLRO. Guides risk-based AML/CFT programs,
  alert triage, SAR narrative structure (not legal filing), governance, crypto AML, and exam readiness—not
  ISO/SOC only (compliance-engineer), cloud attestations (cloud-compliance-specialist), contracts
  (commercial-counsel), IT audit workpapers (auditor), FinOps (finops-analyst), SIEM build
  (information-security-engineer), or blockchain LE investigations (blockint skills).
---

# AML / Compliance

## When to Use

- Design or mature a **risk-based AML/CFT program** (policies, roles, three lines of defense)
- Scope and execute **KYC, CDD, EDD**, periodic refresh, and **PEP/sanctions screening** workflows
- Conduct **AML risk assessment** (customer, product, channel, geography) and map controls
- Define **transaction monitoring** scenarios, thresholds, alert triage, and escalation paths
- Draft **SAR/STR narrative structure**, supporting facts, and internal escalation (not filing legal advice)
- Plan **recordkeeping**, audit trails, and **exam readiness** (requests, walkthroughs, sampling)
- Map obligations at a high level to **FATF Recommendations**, **BSA/USA PATRIOT** concepts, **EU AMLD/AMLA**, **UK MLR**
- Address **crypto/virtual asset** AML, blockchain analytics touchpoints, and **travel rule** operational design
- Support **correspondent banking** and wire due diligence, **MLRO** and board reporting packs
- Scope **training**, **independent testing**, and **AML analytics model validation** (conceptual)

## When NOT to Use

- Implement SOC 2, ISO 27001, HIPAA, or PCI **technical controls and evidence automation** only → `compliance-engineer`
- Cloud shared-responsibility, FedRAMP/PCI-in-cloud evidence packages → `cloud-compliance-specialist`
- GRC program charter without AML/financial-crime lens → `compliance-specialist`
- **Legal advice**, regulatory interpretation as counsel, contract redlines, or DPA negotiation → `commercial-counsel`
- **Internal/IT audit** workpapers, COSO walkthroughs, ITGC testing without AML program focus → `auditor`
- Cloud billing, tagging, and FinOps cost optimization → `finops-analyst`
- Build SIEM rules, IdP, or TM **software implementation** (primary) → `information-security-engineer`
- On-chain investigation for law enforcement or victim tracing narratives → blockint / `on-chain-investigator-agent` skills
- Sanctions **oracle/API integration** engineering only → `chainalysis-sanctions-screening` (pointer), then route AML context here

## Related skills

| Need | Skill |
|---|---|
| Technical SOC/ISO evidence, CCM, control automation | `compliance-engineer` |
| Cloud framework evidence, residency, CSPM mapping | `cloud-compliance-specialist` |
| GRC scope, gap plans, vendor questionnaires (non-AML) | `compliance-specialist` |
| Contracts, DPAs, regulatory interpretation as counsel | `commercial-counsel` |
| IT audit testing, workpapers, ITGC/SOX-adjacent | `auditor` |
| Cloud spend analysis and allocation | `finops-analyst` |
| SIEM/EDR deployment, logging architecture | `information-security-engineer` |
| Enterprise security strategy (non-AML primary) | `cybersecurity` |
| Security risk registers and treatment | `security-risk-analyst` |
| Cyber threat intel briefs and IOC packages | `cti-analyst` |
| Blockchain investigation and tracing reports | `on-chain-investigator-agent`, `solana-tracing-specialist` |
| Public sanctions API/oracle (engineering pointer) | `chainalysis-sanctions-screening` |
| FATF glossary definitions (authoritative terms) | `fatf-glossary-reference` |
| Address/transaction screening UI concepts | `address-screening-workflow-concepts`, `transaction-screening-workflow-concepts` |
| Behavioral monitoring heuristics (educational) | `behavioral-risk-screening-concepts` |

## Core Workflows

### 1. Program scoping and risk assessment

1. Inventory legal entities, licenses, products, channels, and geographies
2. Document **inherent risk** by customer type, product, delivery channel, and geography
3. Define **residual risk** after controls; align appetite with board
4. Prioritize gaps with owners, due dates, and evidence of remediation
5. Refresh on trigger events (new product, corridor, enforcement action, exam finding)

**See `references/aml_compliance_scope.md` and `references/risk_assessment_and_program_governance.md`.**

### 2. Customer due diligence and screening

1. Tier customers (retail, SME, corporate, PEP, correspondent, VASP)
2. Apply **CDD** vs **EDD** triggers; define refresh cadence and event-driven reviews
3. Run **PEP, sanctions, and adverse media** with match disposition and audit trail
4. Document **beneficial ownership** and control persons where required
5. Escalate true matches and inconclusive cases per policy—not ad hoc overrides

**See `references/kyc_cdd_and_screening.md`.**

### 3. Transaction monitoring and alert operations

1. Map scenarios to risks (structuring, rapid movement, high-risk geography, mule patterns)
2. Calibrate thresholds using labeled data and analyst feedback loops
3. Define **alert triage** queues, SLAs, investigation steps, and closure codes
4. Separate **AML** alerts from fraud/chargeback where systems differ
5. Track **false positive** burden and tune with documented approvals

**See `references/transaction_monitoring_and_alerts.md`.**

### 4. Suspicious activity reporting and records

1. Decide escalation threshold for **SAR/STR** consideration (internal policy)
2. Assemble **narrative structure**: who, what, when, where, why suspicious, amounts, accounts
3. Maintain **supporting documentation** index; restrict need-to-know
4. **Do not** advise whether to file, legal sufficiency, or regulator strategy—escalate to MLRO/counsel
5. Retain records per jurisdictional schedule; protect confidentiality

**See `references/sar_str_reporting_and_records.md`.**

### 5. Crypto, travel rule, and examinations

1. Classify virtual asset activities (custody, exchange, transfer, staking) in risk assessment
2. Integrate blockchain analytics as **decision support** with documented limitations
3. Design **travel rule** counterparty data exchange and exception handling
4. Prepare **exam readiness**: org chart, policies, risk assessment, sample populations, tuning logs
5. Coordinate **independent test** and **model validation** scope for AML models

**See `references/crypto_travel_rule_and_exam_readiness.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Mission, boundaries, handoffs | `references/aml_compliance_scope.md` |
| KYC, CDD, EDD, screening | `references/kyc_cdd_and_screening.md` |
| Risk assessment, MLRO, governance | `references/risk_assessment_and_program_governance.md` |
| TM scenarios, tuning, triage | `references/transaction_monitoring_and_alerts.md` |
| SAR/STR narratives, recordkeeping | `references/sar_str_reporting_and_records.md` |
| Crypto AML, travel rule, exams | `references/crypto_travel_rule_and_exam_readiness.md` |

## Operating principles

- **Risk-based** — proportion controls to documented inherent and residual risk
- **Audit trail** — decisions, overrides, and dispositions retrievable with actor and timestamp
- **No legal conclusions** — provide fact packs and draft structures; MLRO/counsel decide filings
- **Separate roles** — first line owns customers; second line AML compliance; third line audit
- **Tune with governance** — threshold changes versioned, approved, and back-tested where possible
- **Label uncertainty** — screening and blockchain analytics are heuristic; document confidence
