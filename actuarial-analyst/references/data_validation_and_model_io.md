# Data validation and model I/O

## Table of contents

1. [Validation principles](#validation-principles)
2. [Source reconciliation](#source-reconciliation)
3. [Triangle and bordereaux checks](#triangle-and-bordereaux-checks)
4. [Assumption and parameter control](#assumption-and-parameter-control)
5. [Model run workflow](#model-run-workflow)
6. [Output reasonability](#output-reasonability)
7. [Handoffs to data-scrubbing](#handoffs-to-data-scrubbing)

## Validation principles

Actuarial conclusions are only as good as inputs. Analyst validation focuses on:

| Principle | Practice |
|---|---|
| Completeness | Record counts and $ totals vs prior period |
| Consistency | Definitions stable period-over-period |
| Accuracy | Tie to GL, policy admin, claims system |
| Timeliness | Cutoff documented; late claims flagged |
| Traceability | Keys link source → exhibit |

Log issues in a **validation register**: ID, severity, $ impact, owner, status.

## Source reconciliation

Typical control totals:

```
Σ policy earned premium  =  GL earned premium (± known adjustments)
Σ claim payments         =  claims warehouse paid (± timing)
Σ case reserves          =  claims system outstanding
```

Steps:

1. Import **control report** from finance or data team
2. Compare at **company, LOB, and segment** level
3. Investigate differences > **materiality threshold** (from actuary)
4. Document **timing** (cutoff, ETL lag) vs **error**

Use `data-scrubbing` for systematic source fixes; analyst documents actuarial impact of corrections.

## Triangle and bordereaux checks

| Check | Rule of thumb |
|---|---|
| Duplicate claim keys | Zero duplicates on (claim_id, valuation_date) |
| Negative incurred | Investigate recoveries and subrogation |
| Future accident dates | Exclude or correct |
| Development age | Valuation - accident ≥ 0 |
| Origin period gaps | No missing AYs in range |

**Triangle tie-out:**

```
Σ incremental cells for origin AY = cumulative at latest lag
Σ all origins at latest valuation = bordereaux total incurred
```

## Assumption and parameter control

| Control | Analyst action |
|---|---|
| Assumption version | Read ID from `assumption-setting` memo; no local edits |
| Effective date | Match valuation date |
| Mapping tables | Hash or version stamp; diff vs prior |
| Economic scenarios | Only run scenarios actuary approved |

If model requires assumption upload:

1. Export from **approved** repository
2. Check row counts and key totals vs memo
3. Store file in run folder with timestamp

## Model run workflow

```
1. Pre-run checklist (data, assumptions, version)
2. Execute model (script, vendor tool, spreadsheet)
3. Capture log (start/end, errors, warnings)
4. Export outputs to standard template
5. Post-run reasonability vs prior
6. Package for actuary review
```

Document:

| Artifact | Purpose |
|---|---|
| `inputs_manifest.csv` | File name, row count, $ total, hash |
| `parameters.json` or tab | Run switches |
| `run_log.txt` | Errors and runtime |
| `outputs/` | Standardized exhibit extracts |

## Output reasonability

Compare current run to **prior quarter** and **plan** (tolerances from actuary):

| Output | Checks |
|---|---|
| Reserve total | % change vs prior; PYD direction |
| Ultimate LR | Within pricing range |
| Cohort reserves | No sign flips without explanation |
| New business strain | Directionally sensible |

Flag **statistical noise** vs **data breaks** (system migration, coding change).

## Handoffs to data-scrubbing

Route to `data-scrubbing` when:

- Repeated ETL failures require pipeline fix
- Master data (class codes, territory) needs normalization at source
- Duplicate policy records need systematic dedupe

Analyst remains accountable for **actuarial reconciliation** after scrubbing completes—re-run controls.
