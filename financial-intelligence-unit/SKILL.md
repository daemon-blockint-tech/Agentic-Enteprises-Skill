---
name: FIU (Financial Intelligence Unit)
description: |
  This skill should be used when the user asks about FIU, financial intelligence unit, AML FIU,
  case analysis, alert triage, suspicious activity analysis, escalate to MLRO, FIU reporting,
  transaction monitoring investigation, or FIU workflow. Operates the Financial Intelligence Unit
  within an AML/CFT program—alert and case intake/triage, financial flow and counterparty analysis,
  typology-driven investigations, case documentation, QA/peer review, MLRO escalation packs,
  internal management reporting (not legal filing advice), coordination with TM/compliance/investigations,
  and FIU metrics/backlog—not enterprise AML policy design (aml-compliance), sole STR/SAR narrative
  drafting (str-report), CFT/PF-only typologies (aml-cft), IT audit fieldwork (auditor), or technical
  control evidence (compliance-engineer).
---

# FIU (Financial Intelligence Unit)

## When to Use

- Run **FIU operations**: alert queues, case assignment, triage, and investigation lifecycle
- Perform **financial analysis** on suspicious activity—flows, networks, counterparties, products, corridors
- Document **case files** with facts, chronology, hypotheses tested, and disposition rationale
- Prepare **MLRO escalation packs**—fact summaries, open questions, recommendation options (not filing decisions)
- Apply **typology-driven analysis** (structuring, layering, mule, trade-based ML, VASP/crypto patterns)
- Coordinate with **transaction monitoring**, second-line compliance, and **investigations** (fraud, security)
- Support **internal FIU reporting**—backlog, SLA, quality metrics, management information (not regulator filing advice)
- Run **quality assurance**, peer review, and case reconstruction for audits or lessons learned
- Design **handover, training**, and playbook updates from closed cases and tuning feedback
- Integrate **adverse media** context at a high level (route deep NLP/sentiment pipelines elsewhere)

## When NOT to Use

- Design or mature the **full AML/CFT program**, policies, KYC tiers, or enterprise risk assessment → `aml-compliance`
- **CFT/PF-only** typologies, TFS/asset-freeze programs, or NPO sector controls without general FIU case work → `aml-cft`
- Draft or finalize **STR/SAR narratives** for filing templates as the primary deliverable → `str-report`
- Execute **internal/IT audit** workpapers, SOC 2 testing, or control effectiveness sampling → `auditor`
- Implement **technical controls**, evidence automation, or screening/TM **engineering** → `compliance-engineer`
- **Legal advice**, filing duty, regulatory interpretation, or entity structuring → `commercial-counsel`
- **Per-text sentiment labeling** or aggregate sentiment forecasting → `sentiment-analysis-engineer`, `sentiment-forecasting-engineer`
- Law enforcement **blockchain forensics** as primary output → blockint / `on-chain-investigator-agent` skills

## Related skills

| Need | Skill |
|---|---|
| Full AML program, KYC/CDD, TM scenarios, program governance | `aml-compliance` |
| STR/SAR narrative structure and filing-oriented drafting | `str-report` |
| Terrorist financing / proliferation financing typologies | `aml-cft` |
| IT audit workpapers, control testing, sampling | `auditor` |
| SOC/ISO evidence pipelines, technical control automation | `compliance-engineer` |
| Legal interpretation, contracts, filing duty as counsel | `commercial-counsel` |
| Per-text sentiment / NLP labeling for media streams | `sentiment-analysis-engineer` |
| FATF standardized terms (STR, CDD, etc.) | `fatf-glossary-reference` |
| Transaction screening UI and rescreen concepts | `transaction-screening-workflow-concepts` |
| Behavioral monitoring heuristics (educational) | `behavioral-risk-screening-concepts` |
| Blockchain tracing for investigation support | `on-chain-investigator-agent`, `solana-tracing-specialist` |

## Core Workflows

### 1. Intake and triage

1. Classify source (TM alert, referral, law-enforcement request, ad hoc)
2. Assign priority using risk, amount, SLA, and repeat-subject rules
3. Confirm **minimum data** before investigation (KYC, alert details, lookback window)
4. Route duplicates, false-positive candidates, and out-of-scope items with coded dispositions

**See `references/case_intake_and_triage.md`.**

### 2. Financial analysis and typologies

1. Reconstruct **flows** (accounts, instruments, corridors, counterparties)
2. Map **networks** and related parties; separate verified facts from inference
3. Test **typology hypotheses** against observable indicators; document innocent explanations considered
4. Request blockchain or external intelligence with **confidence labels** when needed

**See `references/financial_analysis_and_typologies.md`.**

### 3. Documentation, QA, and escalation

1. Maintain case chronology, exhibit index, and decision log
2. Run **peer review** or QA sampling before MLRO handoff
3. Package **MLRO escalation**: summary facts, suspicion elements, gaps, and options—not legal conclusions
4. Hand off to `str-report` when narrative drafting for filing is the next step

**See `references/escalation_and_mlro_handoff.md` and `references/quality_assurance_and_documentation.md`.**

### 4. Reporting, coordination, and metrics

1. Produce **internal MI** (volumes, aging, typologies, outcomes)—not filing advice
2. Coordinate with TM on **tuning feedback** and scenario performance
3. Track **backlog, SLA, rework**, and quality defect rates
4. Capture **training** topics and playbook updates from closed cases

**See `references/reporting_coordination_and_metrics.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Mission, boundaries, handoffs | `references/fiu_scope.md` |
| Queues, prioritization, routing | `references/case_intake_and_triage.md` |
| Flows, networks, typologies | `references/financial_analysis_and_typologies.md` |
| MLRO packs and escalation | `references/escalation_and_mlro_handoff.md` |
| Case files, peer review, QA | `references/quality_assurance_and_documentation.md` |
| MI, TM coordination, metrics | `references/reporting_coordination_and_metrics.md` |

## Operating principles

- **Facts first** — chronology and amounts before suspicion narrative
- **Typology-led, evidence-bound** — hypotheses tied to observable indicators
- **Segregation of duties** — investigators vs QA vs MLRO; log overrides
- **Need-to-know** — restrict sensitive case materials; access audited
- **No legal filing advice** — internal packs and MI only; MLRO/counsel decide filings
- **Close the loop** — feed TM tuning and training from dispositions and QA findings
