---
name: IFRS
description: |
  This skill should be used when the user asks about IFRS, International Financial Reporting Standards,
  IFRS 15 revenue, IFRS 16 leases, IFRS 9 financial instruments, IFRS 10 consolidation, IAS 36 impairment,
  IFRS 13 fair value, IFRS disclosure notes, IFRS recognition, first-time adoption IFRS, or IFRS vs GAAP.
  Guides application and explanation of IFRS financial reporting—recognition and measurement by standard,
  presentation and disclosure (IAS 1, IFRS 7), fair value hierarchy, going concern and materiality,
  significant judgments and estimates, first-time adoption (IFRS 1), consolidation and business
  combinations, local GAAP convergence context, and audit-ready note disclosure structure—not US GAAP-only
  ASC deep dives (note high-level differences only), tax law advice, legal entity structuring, full
  external audit execution (auditor), ERP configuration (senior-software-engineer), or management
  accounting without a reporting-standards lens.
---

# IFRS

## When to Use

- Apply **recognition and measurement** under key IFRS standards (IFRS 9, 15, 16, 38; IAS 12, 16, 36; IFRS 2, 3, 10)
- Structure **financial statement presentation** and **note disclosures** (IAS 1, IFRS 7, industry supplements)
- Document **fair value** measurement and **IFRS 13** hierarchy disclosures
- Assess **going concern**, **materiality**, and **accounting policy** choices under IAS 1 / IAS 8
- Prepare **significant judgments and estimates** narratives for the financial statements
- Plan **first-time adoption** (IFRS 1) and opening balance sheet mechanics
- Explain **consolidation**, **business combinations**, and **share-based payment** accounting
- Compare **IFRS vs local GAAP / US GAAP** at a reporting level for convergence or dual-reporting entities
- Draft **audit-ready** disclosure checklists and tie-outs to the primary statements

## When NOT to Use

- **US GAAP-only** technical deep dives (ASC-by-ASC) without IFRS context → note US GAAP difference at high level only; use US GAAP resources for ASC detail
- **Tax law**, tax provision computation, or transfer pricing → tax specialists; IAS 12 covers **accounting for income taxes**, not tax advice
- **Legal entity structuring**, incorporation, or corporate law → `commercial-counsel`
- **Full external audit execution**, sampling, workpapers, or attestation → `auditor`
- **ERP / system configuration**, chart of accounts build, or automation implementation → `senior-software-engineer` or IT finance systems teams
- **Management accounting only** (budgets, variances, KPI dashboards) without IFRS reporting impact → finance ops; return here when amounts hit the general ledger or external reports
- **Contract legal redlines** or regulatory interpretation as counsel → `commercial-counsel`
- **Broad strategy** without accounting standard application → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| ASC 606 / IFRS 15 contract revenue mechanics and SSP | `senior-revenue-accountant` |
| Month-end close, P&L/BS/CF preparation and variance commentary | `financial-statements` (if installed) |
| Ratio analysis, valuation, and investor-facing metrics | `financial-analyst` (if installed) |
| Internal / IT audit, control testing, workpapers | `auditor` |
| Commercial terms affecting revenue or leases (legal) | `commercial-counsel` |
| Executive business case without standards application | `business-consultant` |

## Core Workflows

### 1. Scope the reporting question

1. Identify **reporting entity**, functional currency, and reporting period
2. Confirm **consolidation** boundary (IFRS 10) and any **separate** parent-only requirements
3. List **standards in play** (revenue, leases, financial instruments, taxes, impairment, combinations)
4. Gather **facts**: contracts, lease terms, instrument terms, acquisition agreements, impairment triggers
5. Flag **judgment areas** and **estimate** inputs early

**See `references/ifrs_scope.md`.**

### 2. Recognition and measurement

1. Map each balance sheet and P&L line to the **applicable standard**
2. Apply recognition criteria; measure at initial and subsequent amounts
3. Document **policy elections** permitted by the standard (e.g., IFRS 9, IFRS 16 practical expedients)
4. Reconcile to **general ledger** and subledgers
5. Capture **effective date** and transition requirements if standards newly adopted

**See `references/recognition_measurement_by_standard.md`, `references/revenue_leases_and_financial_instruments.md`, and `references/consolidation_and_business_combinations.md`.**

### 3. Presentation, disclosure, and fair value

1. Align primary statements with **IAS 1** classification (current/non-current, OCI, equity)
2. Build **note disclosure** packs by topic (accounting policies, risk, fair value, related parties)
3. Apply **IFRS 7** (financial instruments) and **IFRS 13** fair value hierarchy where relevant
4. Draft **materiality** filter and **comparative** restatement notes if needed
5. Tie each disclosure to **supporting schedules** and auditor request lists

**See `references/references_presentation_disclosure_and_fair_value.md`.**

### 4. Judgments, adoption, and GAAP differences

1. Draft **significant judgments and sources of estimation uncertainty** (IAS 1.122–125)
2. For **first-time adopters**, execute IFRS 1 mandatory exceptions and optional exemptions log
3. Summarize **IFRS vs other GAAP** differences affecting reported results (high level)
4. Prepare **management representation** support topics and open items list for audit

**See `references/references_judgments_first_adoption_and_gaap_differences.md`.**

## Outputs

- **Accounting memo** — facts, standard citations, conclusion, journal entry outline
- **Policy paper** — elected options, measurement bases, presentation choices
- **Disclosure checklist** — IAS 1 / IFRS 7 / standard-specific requirements with preparer status
- **Judgments register** — assumption, sensitivity, and conclusion per estimate
- **IFRS 1 transition log** — exemptions, adjustments, reconciliations
- **GAAP difference summary** — key reconciling items for investors or dual reporters

## Principles

- **Standard-first** — cite the IFRS requirement before concluding; distinguish mandatory vs optional
- **Fact-driven** — no conclusion without contract, market, or entity-specific inputs
- **Disclosure-complete** — if recognized in the statements, explain it in the notes at appropriate granularity
- **Audit-ready** — schedules tie to GL; judgments are explicit and reviewable
- **Stay in lane** — explain accounting; do not provide tax, legal, or audit opinions

## Reference map

| Topic | File |
|---|---|
| Role boundaries, framework overview, engagement types | `references/ifrs_scope.md` |
| Cross-standard recognition and measurement map | `references/recognition_measurement_by_standard.md` |
| IFRS 9, 15, 16 deep workflow | `references/revenue_leases_and_financial_instruments.md` |
| IFRS 10, IFRS 3, IFRS 2 | `references/consolidation_and_business_combinations.md` |
| IAS 1, IFRS 7, IFRS 13 presentation and disclosure | `references/references_presentation_disclosure_and_fair_value.md` |
| Judgments, IFRS 1, GAAP differences | `references/references_judgments_first_adoption_and_gaap_differences.md` |

## Disclaimer

This skill supports **IFRS accounting analysis and disclosure drafting** workflows. It does not provide legal, tax, or audit attestation advice. Qualified accountants, auditors, and counsel must review conclusions before filing, publishing, or signing financial statements.
