# Reporting and workpapers

## Table of contents

1. [Workpaper structure](#workpaper-structure)
2. [Exhibit numbering and index](#exhibit-numbering-and-index)
3. [Roll-forwards and bridges](#roll-forwards-and-bridges)
4. [Statutory and management tie-outs](#statutory-and-management-tie-outs)
5. [Memo support vs narrative](#memo-support-vs-narrative)
6. [Version control](#version-control)
7. [Pension and group benefit schedules](#pension-and-group-benefit-schedules)

## Workpaper structure

Recommended workbook tabs (adapt to firm standards):

| Tab | Purpose |
|---|---|
| `00_Index` | Exhibit list, owners, status |
| `01_Definitions` | Metrics, basis, cutoff |
| `02_Data` | Frozen source pull |
| `03_Calc` | Triangles, pricing, model extracts |
| `04_Exhibits` | Presentation-ready tables |
| `05_TieOut` | GL / statutory reconciliation |
| `06_ChangeLog` | Version history |

Keep **logic** on calc tabs; **exhibits** link or paste values—avoid fragile cross-book links for filings.

## Exhibit numbering and index

Example index columns:

| Exhibit | Title | Source tab | Prior period ref | Status |
|---|---|---|---|---|
| A-1 | Paid loss triangle | 03_Calc!B2 | Q3-2024 A-1 | Final |
| A-2 | Selected factors | 03_Calc!F40 | Q3-2024 A-2 | Draft |

Align numbering with **actuarial memo** outline. If memo not yet drafted, use placeholder titles actuary can rename.

## Roll-forwards and bridges

**Reserve roll-forward** (calendar period):

| Line | Source |
|---|---|
| Opening reserve | Prior closing / GL |
| Incurred | Calendar incurred losses |
| Paid | Calendar payments |
| PYD | Actuarial schedule |
| Closing reserve | Model or triangle output |
| Difference | Should be zero or explained |

**Premium earned bridge** (if in scope):

```
written premium
± change in unearned
= earned premium
```

Footnote **reinsurance** (gross vs net) on every bridge.

## Statutory and management tie-outs

Build a **mapping table**:

| External line (schedule) | Workpaper cell | Amount | Diff | Explanation |
|---|---|---|---|---|
| Stat Page X Line Y | Exhibits!H45 | | | |

Materiality: actuary sets threshold; analyst lists **all** differences with suggested classification (timing, reclass, error).

Do not **force** tie with unexplained plugs—use open items.

## Memo support vs narrative

| Analyst provides | Actuary / consulting provides |
|---|---|
| Numbered exhibits | Executive summary |
| Definition appendix | Professional conclusions |
| Reconciliation tables | Regulatory narrative |
| Diagnostic charts (data-focused) | Stakeholder storyline → `actuarial-consulting` |

Use **neutral labels** in exhibits ("Selected factor" not "Correct factor").

## Version control

| Practice | Detail |
|---|---|
| File name | `YYYYMMDD_basis_LOB_vNN.ext` |
| Frozen data | Copy values on data tab; note pull timestamp |
| Change log | Who, what, why, date |
| Distribution | Draft watermark until actuary releases |

For collaborative tools, export **PDF or xlsx archive** at sign-off milestone.

## Pension and group benefit schedules

Analyst support for `pension-retirement-funds` / actuary valuations:

| Task | Output |
|---|---|
| Census reconciliation | Headcount and status bridge |
| Liability roll-forward | Tie to prior valuation file |
| Contribution / expense schedules | Tie to finance if requested |
| Assumption table | Copy from approved memo only |

Do not certify **funding adequacy** or **ERISA** conclusions—prepare schedules only.
