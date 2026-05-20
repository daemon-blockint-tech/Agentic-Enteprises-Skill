# Quality review and documentation

## Table of contents

1. [Analyst QA layers](#analyst-qa-layers)
2. [Formula and spreadsheet controls](#formula-and-spreadsheet-controls)
3. [Peer review prep](#peer-review-prep)
4. [Documentation standards](#documentation-standards)
5. [Open items and escalation](#open-items-and-escalation)
6. [Archive and retention](#archive-and-retention)
7. [Common defects](#common-defects)

## Analyst QA layers

| Layer | When | Focus |
|---|---|---|
| Self-QA | Before any handoff | Tie-outs, definitions, footnotes |
| Analyst peer | Optional firm policy | Second pair of eyes on formulas |
| Actuary review | Required for external use | Methods, assumptions, conclusions |
| EQ / consulting QA | Client engagements | Independence, narrative → `actuarial-consulting` |

Complete **self-QA** using the checklist in `SKILL.md` every time.

## Formula and spreadsheet controls

| Control | Implementation |
|---|---|
| No hard-coded plugs | Comment cell; link to support schedule |
| Consistent signs | Payments negative or positive—one convention per file |
| Range names | Optional; document in definitions tab |
| Error traps | `IFERROR` only with visible flag—not silent zero |
| Circular refs | Avoid; document if unavoidable |
| Units | $000 vs $1 in header on every exhibit |

Run **balance checks**:

- Triangles sum to control totals
- Subsegments sum to total
- Roll-forward closes

## Peer review prep

Package for reviewer:

```
review_folder/
  00_README.md          # Purpose, basis, valuation date
  01_index.xlsx         # Or index tab
  02_inputs/            # Frozen data
  03_workpapers/        # Main file(s)
  04_outputs/           # PDF exhibits if needed
  05_open_items.md      # Questions and resolutions
```

In `05_open_items.md` use:

| ID | Description | Severity | Owner | Status |
|---|---|---|---|---|
| OI-01 | Tail factor AY 2018 | High | Actuary | Open |

Reviewer comments: use **cell comments** or review tool; resolve with initials and date.

## Documentation standards

Every exhibit should answer:

1. **What** is this table?
2. **Source** data and cutoff?
3. **Definition** of each column?
4. **Change** from prior period?
5. **Limitations** (thin data, one-time events)?

**Assumption references:**

```
Assumptions per: [Memo ID], version [X], effective [date]
Model: [Name], build [Y], run [timestamp]
```

## Open items and escalation

| Severity | Criteria | Action |
|---|---|---|
| High | Could change reserve or indication > materiality | Stop external distribution; escalate actuary |
| Medium | Method question; data gap with workaround | Document; actuary decides before final |
| Low | Formatting, labeling | Fix in next version |

Escalate to `assumption-setting` when **enterprise assumption** change is requested, not just application error.

## Archive and retention

At actuary sign-off (or project end):

1. Freeze **final** workpaper and inputs manifest
2. Store in firm document system per retention policy
3. Record **distribution list** if sent externally
4. Delete **scratch** copies from shared drives or mark superseded

Do not archive **PII** in unsecured locations—follow firm privacy policy.

## Common defects

| Defect | Prevention |
|---|---|
| Wrong accident year definition | Definitions tab; validate sample claims |
| Net/gross mix | Reinsurance flag on every tab |
| Double-counted claims | Duplicate key check |
| Trend applied twice | Separate trend audit tab |
| Broken links after refresh | Paste values on exhibits before distribution |
| Credibility on thin segments | Flag Z < 1 with exposure count |
| Unexplained tie-out diff | Open item—not plug |

Use `data-visualization` only after numbers are **correct**—charts do not fix logic errors.
