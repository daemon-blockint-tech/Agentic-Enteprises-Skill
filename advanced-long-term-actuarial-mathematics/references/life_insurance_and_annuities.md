# Life insurance and annuities

## Table of contents

1. [Actuarial present value (APV)](#actuarial-present-value-apv)
2. [Life insurance benefits](#life-insurance-benefits)
3. [Annuities](#annuities)
4. [Varying benefits and expenses](#varying-benefits-and-expenses)
5. [Joint-life and group extensions](#joint-life-and-group-extensions)

## Actuarial present value (APV)

**Actuarial present value** of a payment stream:

\[
\text{APV} = \mathbb{E}\left[\sum \text{payments} \times \text{discount} \times \text{survival/decrement indicators}\right]
\]

Standard **commutation** notation (ultimate mortality, interest \(i\)):

| Symbol | Definition |
|---|---|
| \(D_x = l_x v^x\) | Discounted survivors |
| \(N_x = \sum_{t=x}^{\omega} D_t\) | Annuuity numerator |
| \(C_x = d_x v^{x+1}\) | Death benefit weight |
| \(M_x = \sum_{t=x}^{\omega} C_t\) | Insurance numerator |
| \(v = 1/(1+i)\) | Discount factor |

State whether functions are **due** (\(D_x\) at start of year) or **immediate**.

## Life insurance benefits

Common **unit** benefits (pay 1 on event):

| Product | Event | Typical APV form (discrete) |
|---|---|---|
| **Term** \(n\) | Death before \(x+n\) | \(A_{x:\overline{n\|}}^{1} = (M_x - M_{x+n})/D_x\) |
| **Whole life** | Death whenever | \(A_x = M_x / D_x\) |
| **Endowment** | Death or survival at \(n\) | \(A_{x:\overline{n\|}}^{1} + {}_n E_x\) |

**Deferred** insurance multiplies by \({}_m p_x\) and discount for deferral period \(m\).

## Annuities

| Annuity | Payment pattern | Common notation |
|---|---|---|
| **Temporary** \(n\) years | While alive, max \(n\) | \(\ddot{a}_{x:\overline{n\|}} = (N_x - N_{x+n})/D_x\) |
| **Whole life** | While alive | \(\ddot{a}_x = N_x / D_x\) |
| **Immediate** | End of period | \(a_x = \ddot{a}_x - 1\) (adjust for timing) |

**Continuous** annuities use \(\bar{A}\), \(\bar{a}\) with \(\delta\) instead of \(i\).

**Temporary annuity certain** adds non-life contingency layer when guaranteed periods apply.

## Varying benefits and expenses

- **Level** vs **increasing** benefits (e.g., \( (1+j)^t \) — document inflation linkage)
- **Expense** charges as percent of premium or per policy; route gross premium work to `premiums_and_reserves.md`
- **Refund** or **return of premium** features alter death benefit path

Product wording and rider mechanics → `life-health-insurance`.

## Joint-life and group extensions

- **Joint-life annuity** — pay while both alive; APV uses joint survival
- **Last survivor** — pay until last death; requires joint decrement logic
- **Group** certificates often use **salary scales** and **service** — pension state models in `multiple_decrement_and_state_models.md`

Do not present APV factors as **pricing** without expense, persistency, and capital margins.
