# Actuarial and Insurance Data Scrubbing

## Purpose

Prepare **insurance and actuarial** tabular inputs—policies, claims, premiums, exposures—for reserving, pricing, experience studies, and management reporting. Scrubbing ensures correct grain, keys, and field semantics; **reserve math and assumption selection** belong to `actuary` and `assumption-setting`.

## Common datasets

| Dataset | Typical grain | Scrub focus |
|---|---|---|
| Policy admin | policy × term segment | keys, dates, earned logic inputs |
| Claims | claim or claim-feature | status, amounts, linkage to policy |
| Premium | transaction or earned monthly | written vs earned, cancellations |
| Exposure | exposure unit × period | base definition, audit vs stat |
| Claims triangle | accident year × development lag | orientation, completeness |
| Reinsurance ceded | treaty × layer | attachment, limits, recoverables |

## Policy fields

Validate and standardize:

| Field | Checks |
|---|---|
| `policy_id` | Unique at intended grain; no float cast |
| `effective_date` / `expiration_date` | `effective <= expiration`; open policies flagged |
| `line_of_business` | Maps to approved LOB table |
| `state` / `country` | Valid codes; aligns with filing territory rules |
| `status` | In-force, cancelled, expired—mutually consistent with dates |
| `premium` components | Written vs return premium; fees separated if required |

Document mid-term endorsements: grain may be **policy segment** not static policy row.

## Claims fields

| Field | Checks |
|---|---|
| `claim_id` | Unique; stable across development |
| `loss_date` / `report_date` / `close_date` | Logical ordering |
| `incurred` / `paid` / `reserve` | Non-negative except documented adjustments |
| `claim_status` | Open/closed aligns with close_date |
| `cause_of_loss` | Domain list; map legacy codes |
| Large losses | Flag above threshold; do not drop without actuary direction |

Subrogation and salvage: separate columns; do not net into incurred without specification.

## Premium and earning

Scrub inputs to earned premium logic, not the actuarial formula itself:

- Identify cancellation timing and return premium rows
- Separate audit vs written premium when both exist
- Align policy term with earning pattern (pro-rata, short-rate) via metadata flags

Hand off earned calculations to `actuary` when actuarial standard required.

## Exposure bases

Exposure must match **rating variable definition**:

| Line | Examples |
|---|---|
| Auto | car years, mileage band |
| GL | payroll, sales, units |
| Property | TIV, location count |

Checks:

- Exposure period aligns with policy term
- Units match filing manual (no mixed units in one column)
- Zero exposure with positive premium flagged

## Claims triangles

Before triangle construction:

1. Confirm **orientation**: rows = accident period, cols = development lag (or document transpose)
2. Consistent **valuation date** for all cells
3. Exclude incomplete latest diagonal only with documented rule
4. Handle negative development from corrections via adjustment rows, not silent cell edits
5. Reconcile triangle totals to claim register control

Route triangle methodology and tail selection to `actuary`.

## Reinsurance

| Field | Checks |
|---|---|
| Treaty ID | Maps to contract master |
| Layer attachment / limit | Numeric consistency |
| Ceded % | Between 0 and 1 (or 0–100 with documented scale) |
| Recoverables | Tie to claim keys where applicable |

## Catastrophe and large loss

- Tag CAT codes separately from attritional
- Do not cap CAT losses in scrub without explicit modeling policy
- Geographic coordinates: validate range; generalize if PII concern

## Experience study prep

For ratemaking experience:

- Align policy year / accident year definitions
- Filter to target segment **after** documenting exclusion counts
- On-level factors: store indices in versioned tables, not ad hoc spreadsheet columns
- Credibility weights: compute in actuarial workflow, not hidden in scrub

## Coordination with peers

| Need | Skill |
|---|---|
| IBNR, chain ladder, tail factors | `actuary` |
| Assumption memos and governance | `assumption-setting` |
| P&C product coverage context | `property-casualty-insurance` |
| Pension fund specifics | `pension-retirement-funds` |
| Regulatory control evidence | `compliance-engineer` |

## Sign-off (actuarial data)

Additional gates before `actuary` modeling:

- [ ] Triangle/register reconciliation within tolerance
- [ ] LOB and state mapping signed by actuarial data owner
- [ ] Large loss and CAT flags reviewed
- [ ] Development lag completeness documented
- [ ] Known reformations (COVID, rate changes) flagged by period

## Anti-patterns

- Mixing accident year and policy year in one column without label
- Dropping open claims to "clean" triangles
- Applying loss development factors during scrub (belongs in modeling)
- Changing historical earned premium without restatement flag
- Using scrubbed triangle for regulatory filing without actuary review
