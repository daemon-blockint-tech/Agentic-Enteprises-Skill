# Interest rate risk and duration

## Table of contents

1. [Concepts and definitions](#concepts-and-definitions)
2. [Duration measures](#duration-measures)
3. [Convexity and optionality](#convexity-and-optionality)
4. [Key rate duration](#key-rate-duration)
5. [Duration gap and surplus sensitivity](#duration-gap-and-surplus-sensitivity)
6. [Curve construction and consistency](#curve-construction-and-consistency)
7. [Common pitfalls](#common-pitfalls)
8. [Worked patterns (conceptual)](#worked-patterns-conceptual)

## Concepts and definitions

**Interest rate risk** is the potential change in **value** or **cash flows** due to changes in yield curves and related market variables.

For ALM, focus on **net** exposure: assets minus liabilities (surplus), not asset duration alone.

| Term | Definition |
|---|---|
| **PV** | Present value of future cash flows at a discount curve |
| **DV01 / PV01** | Change in PV for a 1bp parallel shift in rates |
| **Yield** | Internal rate of return that equates price to cash flows (context-specific) |

Clarify whether shocks are **instantaneous** (valuation impact) or **over a horizon** with reinvestment (ALM simulation).

## Duration measures

### Modified duration

Approximate percentage price change for a small parallel yield change:

\[
\Delta P/P \approx -D_{\text{mod}} \cdot \Delta y
\]

Used for **fixed-rate bonds** without embedded options when yields are well-defined.

### Effective duration

Duration from **numerical** revaluation under curve shocks—required when cash flows change with rates (options, structured products, some liabilities).

\[
D_{\text{eff}} = -\frac{P_{-} - P_{+}}{2 P_0 \cdot \Delta y}
\]

### Macaulay duration

Weighted average time to cash flows; linked to modified duration via yield for simple bonds. Useful for **immunization** intuition (match Macaulay durations for a single liability payment).

### Dollar duration

\(D_{\$} = D \times P\) — useful for **hedge sizing** in dollar space.

## Convexity and optionality

**Convexity** captures curvature: for large rate moves, linear duration understates gains when rates fall (positive convexity) on plain bonds.

\[
\Delta P/P \approx -D \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2
\]

**Embedded options** (calls, puts, prepayment, policyholder options) create **negative convexity** and **extension/contraction** risk—duration alone is insufficient.

ALM implications:

- Report **effective duration** and, where material, **convexity** or full **grid** revaluation
- Stress **non-linear** products with scenario grids, not only parallel ±100bp

## Key rate duration

**Key rate duration (KRD)** measures sensitivity to changes at specific curve tenors while holding other key points fixed (method varies by vendor).

Use KRD when:

- Liabilities are **long** and **pension-like** (sensitivity at 10y–30y)
- Hedges use **butterflies** or **barbells** rather than parallel swaps
- **Steepening/fl flattening** scenarios dominate risk

Present KRD tables for **assets**, **liabilities**, and **net** with the same curve methodology.

## Duration gap and surplus sensitivity

**Duration gap** (informal):

\[
\text{Gap} \approx D_A \cdot A - D_L \cdot L
\]

Definitions vary: some use **dollar duration** on market values; pensions may use **funded** weights.

**Surplus duration** (economic):

\[
D_{\text{surplus}} \approx \frac{D_A \cdot A - D_L \cdot L}{A - L}
\]

when surplus \(S = A - L\) is positive and liabilities are measured on a consistent market basis.

Interpretation:

- Positive net duration → surplus **falls** when rates **rise** (if liabilities are longer duration than assets)
- Sign depends on **relative** durations and **weights**, not asset duration alone

Always pair with **convexity** and **key-rate** profile for material books.

## Curve construction and consistency

ALM requires **one coherent framework**:

1. **Risk-free** or **swap** curve for discounting (policy choice)
2. **Credit spreads** for corporate holdings—separate from liability curve unless liability is credit-based
3. **Inflation** curve for real-linked cash flows (breakeven or RPI/CPI-specific)

**Basis risk** arises when:

- Liabilities are discounted on **corporate bond** yields but hedged with **government** swaps
- **OIS** vs **LIBOR/SOFR** legacy conventions differ across books
- **Smoothed** funding curves vs **market** hedge curves (pensions)

Document curve IDs, valuation timestamps, and **parallel vs bucketed** shock conventions.

## Common pitfalls

| Pitfall | Mitigation |
|---|---|
| Asset duration only | Always report liability and **net** |
| Mixing accounting liability with market-valued hedges | Reconcile bases or use economic mirror |
| Using book yield for liabilities | Use curve-consistent effective duration |
| Ignoring options | Effective duration + scenario grids |
| Static hedge ratio | Model **rebalancing** and **drift** |
| Wrong compounding on shocks | Align with risk system (continuous vs annual) |

## Worked patterns (conceptual)

### Parallel shock bridge

1. Start surplus \(S_0\)
2. Apply +100bp parallel to assets and liabilities (full revaluation preferred)
3. Report \(\Delta S\), implied \(D_{\text{net}}\), compare to duration estimate

### Key-rate steepener

1. +50bp at 2y, −25bp at 30y (example)
2. Show impact on **pension** liabilities vs **barbell** hedge

### Immunization check

For a single deterministic liability payment at time \(T\):

- Match **Macaulay duration** and **PV** of assets to liability
- Monitor **rebalancing** as time passes and coupons arrive

Hand off liability cash-flow engineering to `actuary` or `pension-retirement-funds` when full projections are required.
