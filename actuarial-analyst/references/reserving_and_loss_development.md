# Reserving and loss development (analyst)

## Table of contents

1. [Data preparation](#data-preparation)
2. [Triangle construction](#triangle-construction)
3. [Development factors](#development-factors)
4. [Ultimates and IBNR](#ultimates-and-ibnr)
5. [Diagnostics checklist](#diagnostics-checklist)
6. [Bridges and roll-forwards](#bridges-and-roll-forwards)
7. [Large losses and catastrophes](#large-losses-and-catastrophes)
8. [Analyst exhibits](#analyst-exhibits)

## Data preparation

Before building triangles:

1. Confirm **valuation date** and **accident period** definition (AY, policy year, report year)
2. Align **paid**, **incurred** (paid + case), and **counts** from same cutoff
3. Map **reinsurance** (gross, ceded, net) consistently across periods
4. Flag **large losses** per threshold in actuarial memo
5. Reconcile triangle totals to **bordereaux** or claims warehouse control report

| Field | Common failure |
|---|---|
| Accident date vs report date | Mis-bucketed origin year |
| Case reserve restatements | Calendar-year distortion |
| Subrogation recoveries | Net vs gross inconsistency |

## Triangle construction

Standard layout:

- **Rows** — Origin periods (oldest at top or bottom—match prior workpaper)
- **Columns** — Development age (12, 24, … months or annual)
- **Cells** — Cumulative paid or incurred; incremental optional tab

Build separate tabs for:

- Paid losses
- Incurred losses
- Reported claim counts (if BF or count-severity support)
- Optional: **incremental** triangle for diagnostic charts

## Development factors

| Step | Analyst action |
|---|---|
| Age-to-age | Compute raw factors; exclude obviously distorted cells per instruction |
| Selection | Document selected vs alternative; $ impact on oldest origin |
| Tail | Extend beyond last observed age per actuary pick |
| Volume-weighted | Use standard formulas; show weights in support tab |

Methods (execute per actuary direction—see `actuary` for judgment):

- **Chain ladder** — Cumulative age-to-age to ultimate
- **Bornhuetter-Ferguson** — Expected LR × % reported
- **Cape Cod** — Iterative blend when specified

**Do not** finalize method or tail without actuary sign-off.

## Ultimates and IBNR

```
ultimate = reported_to_date + IBNR   (incurred basis, typical)
IBNR = ultimate - reported_incurred
```

Produce tables:

| Table | Content |
|---|---|
| Ultimates by AY | Reported, IBNR, ultimate, implied LR |
| Summary | Total reserve, change from prior |
| IBNR split | Case vs IBNR vs bulk if required |

Compare **implied ultimate loss ratio** to pricing plan and prior memo; flag outliers in open-items list.

## Diagnostics checklist

Run and retain screenshots or tabs for:

- [ ] **Factor stability** — Last N ages vs historical
- [ ] **Calendar-year** implied ultimates vs accident-year
- [ ] **Paid vs incurred** factor divergence
- [ ] **Count × severity** vs incurred ultimates (if applicable)
- [ ] **Oldest origin** immaturity — BF vs CL spread
- [ ] **Outlier AYs** — cat, large loss, one-time reserve releases

Document **alternative factor sets** with dollar impact on total IBNR.

## Bridges and roll-forwards

**Reserve roll-forward** (analyst exhibit):

```
opening_reserve
+ incurred_losses (calendar period)
- paid_losses
+/- prior_year_development (if shown separately)
= closing_reserve
```

**PYD bridge** (change in prior AY ultimates):

```
prior_ultimate_at_old_valuation
- prior_ultimate_at_new_valuation
= PYD (sign convention per firm standard)
```

Tie every line to **GL or statutory schedule** when tie-out is in scope.

## Large losses and catastrophes

| Treatment | Analyst task |
|---|---|
| Per-claim cap | Apply in data prep; document threshold |
| Separate cat module | Isolate cat AY; do not mix with attritional without approval |
| Excess of loss | Confirm ceded recovery timing in paid triangle |

Never **delete** cat years without actuary approval—flag distortion in diagnostics.

## Analyst exhibits

Minimum reserving pack:

1. Data reconciliation to source
2. Triangles (paid, incurred, counts)
3. Factor development and selections
4. Ultimates and IBNR summary
5. Diagnostic charts or tables
6. PYD and roll-forward
7. Open questions for actuary

File naming example: `20241231_stat_P&C_CL_v03.xlsx`
