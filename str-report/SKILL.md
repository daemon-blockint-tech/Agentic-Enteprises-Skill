---
name: str-report
description: |
  This skill should be used when the user asks to draft or structure STR reports, suspicious transaction reports,
  SAR, suspicious activity reports, draft STR, STR narrative, file suspicious activity, AML STR, goAML,
  FinCEN SAR, suspicion narrative, or MLRO report. Guides jurisdiction-agnostic STR/SAR drafting—narrative
  structure (who, what, when, where, why suspicious), red flags and typologies, transaction aggregation and
  chronology, subject identification fields, supporting documentation checklists, quality review before filing,
  and escalation to MLRO/compliance—not TM rule building (aml-compliance), full LE case management, legal
  filing duty determination (commercial-counsel), or deep blockchain tracing (blockint skills). Complements
  aml-compliance, aml-cft, auditor, compliance-engineer, and commercial-counsel.
---

# STR Report

## When to Use

- Draft or restructure a **suspicious transaction report (STR)** or **suspicious activity report (SAR)** narrative for AML compliance filing or internal MLRO review
- Build the **who / what / when / where / why** suspicion story with clear chronology and aggregated transaction facts
- Map **red flags** and **typologies** (structuring, layering, trade-based ML, etc.) to observable facts—not conclusions without evidence
- Compile **subject and customer identification** fields, related parties, accounts, and product/channel context for filing templates
- Produce a **supporting documentation checklist** and exhibit index aligned to the narrative
- Run **quality review** (completeness, consistency, tone, PII handling) before submission to MLRO or regulator-facing systems
- Compare **jurisdiction-agnostic** structure with high-level **US (FinCEN SAR)**, **EU**, and **goAML** field concepts (not legal filing advice)
- Distinguish **STR/SAR** from internal case notes, management summaries, or **law enforcement** referral packages
- Escalate and **hand off** to MLRO/compliance with a structured fact pack and open questions

## When NOT to Use

- Design **transaction monitoring rules**, thresholds, alert tuning, or TM scenario libraries → `aml-compliance`
- Build a full **AML/CFT program**, KYC/CDD policy, or enterprise risk assessment → `aml-compliance`, `aml-cft`
- Determine **legal obligation to file**, statute of limitations, or regulator-specific filing deadlines as counsel → `commercial-counsel`
- Conduct **internal or IT audit** workpapers, SOC 2 testing, or control effectiveness sampling → `auditor`
- Implement **technical controls**, evidence automation, or screening system engineering → `compliance-engineer`
- Perform **on-chain investigation**, wallet tracing, or blockchain intelligence reports → `on-chain-investigator-agent`, `solana-tracing-specialist`, blockint skills
- Draft **law enforcement** tactical packages, subpoena responses, or victim tracing narratives → route to investigation skills; keep STR factual and filing-oriented
- **CFT/TF-only** typologies without broader STR narrative needs → `aml-cft` (then return here for unified STR assembly)

## Related skills

| Need | Skill |
|---|---|
| Full AML program, KYC/CDD, TM scenarios, alert triage | `aml-compliance` |
| Terrorist financing / proliferation financing STR angles | `aml-cft` |
| IT audit workpapers, control testing, sampling | `auditor` |
| SOC/ISO evidence pipelines, technical control automation | `compliance-engineer` |
| Legal interpretation, contracts, filing duty as counsel | `commercial-counsel` |
| FATF standardized terms (STR, CDD, etc.) | `fatf-glossary-reference` |
| Transaction screening UI and rescreen concepts | `transaction-screening-workflow-concepts` |
| Address screening and list policy concepts | `address-screening-workflow-concepts` |
| Behavioral monitoring heuristics (educational) | `behavioral-risk-screening-concepts` |
| Blockchain tracing and forensic reports | `on-chain-investigator-agent`, `solana-tracing-specialist` |

## Core Workflows

### 1. Intake and scope

1. Confirm **jurisdiction**, **entity**, **filing type** (STR vs SAR vs internal referral), and **case ID**
2. Collect alert source, investigation notes, and **already-reviewed** transactions (do not re-investigate beyond narrative needs)
3. Identify **subjects** (customer, beneficial owners, counterparties, unknown parties) and **reporting institution** role
4. Flag gaps requiring analyst follow-up before MLRO sign-off

**See `references/str_report_scope.md`.**

### 2. Facts, aggregation, and chronology

1. Normalize amounts, currencies, dates (UTC vs local—state assumption)
2. **Aggregate** related transactions (account, counterparty, corridor, instrument)
3. Build a **chronological timeline** with anchors (onboarding, profile change, alert, key txs)
4. Separate **verified facts** from **inference**; label each suspicion element

**See `references/subject_and_transaction_detail.md`.**

### 3. Narrative and typologies

1. Open with **summary suspicion** in plain language (one short paragraph)
2. Develop **who / what / when / where / why** sections with cross-references to exhibits
3. Tie **red flags** to typologies and observable indicators—avoid legal conclusions
4. Address **innocent explanations** considered and why rejected or unresolved

**See `references/narrative_structure_and_quality.md` and `references/red_flags_and_typologies.md`.**

### 4. Format, review, and handoff

1. Map narrative blocks to **jurisdiction template** fields at a high level (FinCEN SAR, goAML, etc.)
2. Complete **supporting documentation checklist** and quality gates
3. Run **MLRO/compliance** escalation pack: decision requested, risks, open items
4. Record version, reviewers, and **not legal advice** disclaimer where appropriate

**See `references/jurisdiction_formats_and_filing.md` and `references/review_escalation_and_handoff.md`.**

## Output Standards

- Use **past tense for facts**, **present tense for ongoing risk** where helpful; avoid sensational language
- Every suspicion statement should cite **specific transactions, dates, amounts, or documents**
- Minimize **PII** in drafts shared broadly; full detail in MLRO/regulator packages per policy
- Include **disclaimer**: output supports compliance drafting—not legal advice on whether or when to file
- Deliver: executive summary, full narrative, chronology table, subject/account appendix, exhibit checklist, open questions

## Reference Files

| File | Use when |
|---|---|
| `references/str_report_scope.md` | Boundaries, definitions, STR vs SAR vs internal notes |
| `references/narrative_structure_and_quality.md` | Who/what/when/where/why, tone, completeness |
| `references/red_flags_and_typologies.md` | Indicators, typology mapping, fact-to-suspicion links |
| `references/subject_and_transaction_detail.md` | IDs, accounts, aggregation, chronology tables |
| `references/jurisdiction_formats_and_filing.md` | FinCEN SAR, goAML, EU concepts (high level) |
| `references/review_escalation_and_handoff.md` | QA gates, MLRO pack, escalation |
