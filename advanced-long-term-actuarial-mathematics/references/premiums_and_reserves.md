# Premiums and reserves

## Table of contents

1. [Equivalence principle](#equivalence-principle)
2. [Net and gross premiums](#net-and-gross-premiums)
3. [Reserve definitions](#reserve-definitions)
4. [Thiele's equation](#thieles-equation)
5. [Deficiency and emerging cost](#deficiency-and-emerging-cost)

## Equivalence principle

**Equivalence principle**: actuarial present value of benefits = actuarial present value of premiums (at issue, for net premium).

\[
\text{APV}(\text{benefits}) = \text{APV}(\text{premiums})
\]

Solve for **level net premium** \(P\) over \(m\) payments on an \(n\)-year policy:

\[
P \cdot \ddot{a}_{x:\overline{m\|}} = \text{APV}(\text{benefits})
\]

Document **funding period** vs **benefit period** when they differ.

## Net and gross premiums

| Type | Includes | Typical use |
|---|---|---|
| **Net premium** | Benefits only | Reserves, pricing margin analysis |
| **Gross premium** | Benefits + expenses + profit load | Customer premium, emerging cost |

Expense formats:

- **Percent of premium** (renewal commission analog)
- **Percent of sum insured** per year
- **Fixed** per policy per year

Gross premium equivalence: \(\text{APV}(\text{benefits}+\text{expenses}) = \text{APV}(\text{gross premiums})\).

Hand **expense studies** and **experience allocation** to `actuarial-analyst`.

## Reserve definitions

At duration \(t\) (prospective, net premium reserve):

\[
{}_t V = \text{APV}(\text{future benefits}) - \text{APV}(\text{future net premiums})
\]

**Retrospective** form (when applicable):

\[
{}_t V = \text{APV}(\text{past premiums}) - \text{APV}(\text{past benefits}) \quad \text{(with adjustments)}
\]

**Gross premium reserve** uses gross premium income and includes **unearned** expense allowances per convention.

**Prospective vs retrospective** reconciliation is a standard control—state assumptions if they differ.

## Thiele's equation

Continuous **Thiele** reserve dynamics:

\[
\frac{d}{dt} {}_t V = \delta \, {}_t V + P_t - \mu_{x+t} \,(1 - {}_t V) - \text{(other decrements)}
\]

Interpretation:

- \(\delta \, {}_t V\) — interest on reserve
- \(P_t\) — premium income rate
- \(\mu_{x+t}(1 - {}_t V)\) — death benefit outgo net of reserve released

Discrete analogs step reserves year-by-year with \(q_x\), \(p_x\), and expense cash flows.

Use Thiele for **sensitivity** and **profit emergence**; discrete recursions for **valuation** tables.

## Deficiency and emerging cost

**Deficiency** (conceptual): prospective reserve negative at some duration under net premium basis—signals inadequate premium or high early benefits.

**Emerging cost** / **profit testing**:

1. Project cash flows by policy year (premiums, claims, expenses, investment)
2. Discount at **earned rate** or **hurdle** rate
3. Allocate **profit** by duration; test **IRR** and **NPV** under scenarios

Link **assumption changes** to `assumption-setting`; full model builds to `actuarial-analyst`.
