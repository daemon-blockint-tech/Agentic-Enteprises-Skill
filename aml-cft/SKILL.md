---
name: aml-cft
description: |
  This skill should be used when the user asks about AML/CFT, counter-terrorist financing, CFT,
  terrorist financing, proliferation financing, PF, targeted financial sanctions, asset freeze,
  TF typology, charitable NPO due diligence, MVTS, FATF Recommendation 6, or STR terrorist financing.
  Guides CFT/PF risk—TF typologies (self-funding, charitable fronts, MVTS, trade-based TF), PF and dual-use
  red flags, TFS and asset-freeze workflows (conceptual), CFT STR/SAR narrative structure, NPO due diligence,
  correspondent and cross-border TF risks, FATF R6–R8 alignment, sanctions screening integration, CFT training
  and independent review, exam readiness—not full AML program (KYC, CDD, TM, MLRO) → aml-compliance; sanctions
  vendor config only; law enforcement tactics; legal determinations. Peers: aml-compliance, compliance-engineer,
  auditor, commercial-counsel, information-security-engineer.
---

# AML / CFT (Counter-Terrorist & Proliferation Financing)

## When to Use

- Assess **terrorist financing (TF)** typologies and red flags distinct from general money laundering
- Design or improve **CFT/PF** controls, policies, and risk appetite—not a full AML program from scratch
- Scope **proliferation financing (PF)** and **dual-use** goods exposure in trade finance or correspondent flows
- Map **targeted financial sanctions (TFS)**, designation lists, and **asset freeze** operational workflows (conceptual)
- Draft **CFT-specific STR/SAR** narrative structure and internal escalation fact packs (not filing legal advice)
- Conduct **charitable NPO** and nonprofit sector due diligence and de-risking decisions
- Evaluate **MVTS** (money/value transfer services), remittance corridors, and informal value transfer risks
- Address **correspondent banking** and **cross-border** TF vulnerabilities and nested-account risks
- Align controls to **FATF Recommendations 6–8** and related interpretive guidance at a high level
- Integrate **sanctions screening** with CFT disposition, true-match escalation, and freeze holds
- Plan **CFT training**, **independent review**, and **exam readiness** for TF/PF-focused questions

## When NOT to Use

- Build or mature a full **risk-based AML program** (KYC tiers, CDD/EDD, TM scenarios, MLRO governance) → `aml-compliance`
- Implement SOC 2, ISO 27001, or technical **control evidence automation** only → `compliance-engineer`
- **Internal/IT audit** workpapers without CFT/PF or sanctions lens → `auditor`
- **Legal advice**, regulatory interpretation as counsel, contract redlines, or filing strategy → `commercial-counsel`
- Deploy SIEM, screening **software engineering**, or IAM (primary) → `information-security-engineer`
- Sanctions **API/oracle integration** only → `chainalysis-sanctions-screening` (pointer), then route CFT context here
- Law enforcement **investigation tactics**, attribution, or victim tracing → blockint / `on-chain-investigator-agent` skills
- General **money laundering** typologies without TF/PF angle → `aml-compliance`

## Related skills

| Need | Skill |
|---|---|
| Full AML program, KYC/CDD, TM tuning, MLRO reporting | `aml-compliance` |
| Technical SOC/ISO evidence, CCM, control automation | `compliance-engineer` |
| IT audit testing, workpapers, sampling | `auditor` |
| Contracts, regulatory interpretation as counsel | `commercial-counsel` |
| SIEM/EDR, screening system deployment | `information-security-engineer` |
| FATF glossary definitions (authoritative terms) | `fatf-glossary-reference` |
| Public sanctions API/oracle (engineering pointer) | `chainalysis-sanctions-screening` |
| Address/transaction screening UI concepts | `address-screening-workflow-concepts`, `transaction-screening-workflow-concepts` |
| Blockchain investigation reports | `on-chain-investigator-agent`, `solana-tracing-specialist` |

## Core Workflows

### 1. CFT/PF risk scoping

1. Inventory products, channels, and geographies with **TF/PF** exposure (NPO, MVTS, trade finance, crypto, correspondent)
2. Document inherent CFT/PF risk separately from general AML inherent risk where useful
3. Map controls to **FATF R6–R8** themes (TFS, PF, NPO) at a high level
4. Prioritize gaps with owners, evidence, and trigger-based refresh (new corridor, designation, exam finding)

**See `references/aml_cft_scope.md`.**

### 2. Typology-led detection and monitoring

1. Select TF typologies relevant to the business model (self-funding, front NPO, MVTS, trade-based TF)
2. Translate typologies into **red flags**, scenarios, and analyst investigation playbooks
3. Separate **CFT** alerts from general AML and fraud where systems differ
4. Tune with documented approvals; track false positives and missed-pattern feedback

**See `references/terrorist_financing_typologies.md` and `references/npo_mvts_and_cross_border_cft.md`.**

### 3. PF, dual-use, and trade exposure

1. Identify customers, corridors, and commodities with **proliferation** or dual-use sensitivity
2. Apply PF red flags (opaque ownership, shell intermediaries, inconsistent shipping docs)
3. Coordinate with trade finance and sanctions teams on holds and escalations

**See `references/proliferation_financing_and_dual_use.md`.**

### 4. TFS, screening, and asset freeze

1. Run sanctions and TFS screening with match disposition and audit trail
2. On true match or designation: initiate **freeze** workflow, block movements, restrict account access (per policy)
3. Document reporting to competent authority where required—escalate legal/compliance for timing and content
4. Manage delisting, unfreeze, and license/Exception pathways only with counsel guidance

**See `references/targeted_sanctions_and_asset_freeze.md`.**

### 5. Reporting, governance, and exam readiness

1. Assemble **CFT-focused STR/SAR** fact packs: TF purpose indicators, networks, channels, NPO links
2. Maintain need-to-know, confidentiality, and record retention per policy
3. Prepare CFT/PF exam samples: TFS policies, NPO procedures, MVTS oversight, training logs, independent review

**See `references/reporting_governance_and_exam_readiness.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Mission, boundaries, handoffs vs aml-compliance | `references/aml_cft_scope.md` |
| TF typologies and red flags | `references/terrorist_financing_typologies.md` |
| PF, dual-use, trade-based proliferation | `references/proliferation_financing_and_dual_use.md` |
| TFS, asset freeze, screening integration | `references/targeted_sanctions_and_asset_freeze.md` |
| NPO, MVTS, correspondent, cross-border CFT | `references/npo_mvts_and_cross_border_cft.md` |
| STR narratives, training, independent review, exams | `references/reporting_governance_and_exam_readiness.md` |

## Operating principles

- **Typology-first** — anchor controls and investigations to known TF/PF patterns, not only ML rules
- **Separate TF from ML** — document why activity suggests terrorist or proliferation purpose
- **No legal conclusions** — provide fact packs and draft structures; MLRO/counsel decide filings and freezes
- **Sanctions are immediate** — treat TFS hits as priority; do not process pending legal comfort informally
- **NPO nuance** — apply risk-based approach; avoid blanket de-risking without governance
- **Label uncertainty** — screening and open-source intel are heuristic; document confidence and gaps
