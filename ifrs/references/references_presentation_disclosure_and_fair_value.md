# Presentation, disclosure, and fair value

## Table of contents

1. [Purpose](#purpose)
2. [IAS 1 — Presentation of financial statements](#ias-1--presentation-of-financial-statements)
3. [Statement structure and classification](#statement-structure-and-classification)
4. [IFRS 7 — Financial instruments disclosures](#ifrs-7--financial-instruments-disclosures)
5. [IFRS 13 — Fair value measurement](#ifrs-13--fair-value-measurement)
6. [Going concern and materiality](#going-concern-and-materiality)
7. [Audit-ready note architecture](#audit-ready-note-architecture)
8. [Disclosure checklist (core)](#disclosure-checklist-core)

## Purpose

Structure **primary statements** and **notes** under IAS 1, layer **financial instrument** risk disclosures under IFRS 7, and apply **IFRS 13** for fair value measurement and hierarchy reporting.

## IAS 1 — Presentation of financial statements

### Complete set (general purpose)

- Statement of financial position
- Statement of profit or loss (and OCI)
- Statement of changes in equity
- Statement of cash flows
- Notes (including accounting policies)
- Comparative information for prior period

### Fundamental principles

- **Fair presentation** and compliance with IFRS
- **Accrual basis** (except cash flow information)
- **Going concern**
- **Materiality** and aggregation
- **Offsetting** prohibited unless permitted by a standard

### OCI presentation

Items permitted or required in OCI (e.g., FVOCI debt, cash flow hedges, revaluation surplus, foreign exchange on subsidiaries) — present in single statement or two-statement approach.

## Statement structure and classification

### Statement of financial position

- **Current vs non-current** distinction (unless liquidity order more relevant)
- Minimum line items per IAS 1.54 (assets, equity, liabilities)
- Additional subtotals if relevant to understanding

### Statement of profit or loss

- **Nature** vs **function** expense classification (function requires specific allocations)
- **Extraordinary items** not permitted — classify within income/expense
- **Discontinued operations** (IFRS 5) — separate presentation

### Statement of cash flows (IAS 7)

- **Operating, investing, financing** activities
- **Direct** or **indirect** method for operating cash flows
- Reconcile to cash and cash equivalents in statement of financial position

## IFRS 7 — Financial instruments disclosures

Organize by **class** of instrument and **risk** type:

| Risk category | Typical disclosures |
|---|---|
| **Credit risk** | ECL methods, staging, collateral, concentration |
| **Liquidity risk** | Maturity analysis, funding policies |
| **Market risk** | Interest rate, currency, equity price sensitivities |

Also disclose:

- Carrying amounts by category (amortized cost, FVOCI, FVTPL)
- Fair value (when carrying amount ≠ fair value)
- Offsetting, collateral, and master netting arrangements
- Hedge accounting policies and effectiveness

Cross-reference **IFRS 9** accounting policies in note 1.

## IFRS 13 — Fair value measurement

### Definition

**Exit price** in an **orderly transaction** between market participants at the **measurement date**.

### Hierarchy

| Level | Inputs |
|---|---|
| **1** | Quoted prices in active markets for identical assets/liabilities |
| **2** | Observable inputs other than Level 1 (e.g., quoted prices for similar items, yields, curves) |
| **3** | Unobservable inputs (models, assumptions) |

### Valuation techniques

- Market approach, income approach, cost approach
- Maximize use of **observable** inputs; minimize **unobservable**

### Disclosures (for recurring and non-recurring FV)

- Fair value at period end by hierarchy level
- Transfers between levels (policy at period end)
- Level 3 reconciliation and sensitivity (where applicable)
- Valuation processes and techniques

**Day 1 gains/losses:** Document when transaction price ≠ fair value.

## Going concern and materiality

### Going concern (IAS 1)

Assess whether entity can continue for at least **12 months** from reporting date.

- If material uncertainty exists → disclose (IAS 1.25)
- If not going concern → do not prepare on going concern basis (extremely rare)

### Materiality

- Misstatements or omissions that could influence decisions
- Apply to **presentation** (aggregation), **disclosure** (omit immaterial note lines), and **recognition**

Document **quantitative** thresholds and **qualitative** factors in the close file.

## Audit-ready note architecture

Recommended note order (adapt to entity):

1. **Corporate information** and basis of preparation
2. **Significant accounting policies** (by standard)
3. **Critical judgments and estimates** (or integrate per policy)
4. **Segment information** (IFRS 8 if applicable)
5. **Revenue, leases, tax, PPE, intangibles, financial instruments**
6. **Provisions, contingencies, related parties**
7. **Subsequent events, commitments**
8. **Group composition** (if consolidated)

Each note should include:

- **Lead schedule** reference
- **Roll-forward** (opening, movements, closing)
- **Tie-out** to trial balance account range
- **Preparer / reviewer** initials

## Disclosure checklist (core)

| Item | IAS 1 / other | Status |
|---|---|---|
| Accounting policies for new standards | IAS 8 | |
| Capital management | IAS 1.134–136 | |
| Dividends proposed/declared | IAS 1.137 | |
| Events after reporting period | IAS 10 | |
| Related party transactions | IAS 24 | |
| Fair value hierarchy tables | IFRS 13 | |
| Financial risk disclosures | IFRS 7 | |
| Earnings per share | IAS 33 | |
| Operating segments | IFRS 8 | |

Route **judgments register** and **IFRS 1** items to `references_judgments_first_adoption_and_gaap_differences.md`.
