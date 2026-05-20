# Survival models and mortality

## Table of contents

1. [Life table notation](#life-table-notation)
2. [Force of mortality](#force-of-mortality)
3. [Select vs ultimate mortality](#select-vs-ultimate-mortality)
4. [Joint-life structures](#joint-life-structures)
5. [Practical checks](#practical-checks)

## Life table notation

Given radix \(l_0\) (often \(l_0 = 100{,}000\)):

| Symbol | Meaning |
|---|---|
| \(l_x\) | Number alive at age \(x\) |
| \(d_x\) | Deaths between \(x\) and \(x+1\): \(d_x = l_x - l_{x+1}\) |
| \(q_x\) | Annual death probability: \(q_x = d_x / l_x\) |
| \(p_x\) | Annual survival probability: \(p_x = 1 - q_x = l_{x+1}/l_x\) |
| \({}_n p_x\) | \(n\)-year survival: \({}_n p_x = l_{x+n}/l_x\) |
| \({}_n q_x\) | \(n\)-year death probability: \({}_n q_x = 1 - {}_n p_x\) |

**Curtate vs complete** life assumptions affect fractional-year benefits; state which convention applies.

## Force of mortality

**Force of mortality** at age \(x\):

\[
\mu_x = \lim_{t \to 0} \frac{{}_t q_x}{t}
\]

Under constant force between integer ages: \({}_t p_x = e^{-\int_0^t \mu_{x+s}\,ds}\).

Discrete link (common approximation):

\[
q_x \approx 1 - e^{-\mu_x}, \quad \mu_x \approx -\ln(1 - q_x)
\]

Use **consistent** conversion when moving between continuous and discrete models.

## Select vs ultimate mortality

- **Ultimate** table: mortality depends on attained age only
- **Select** table: lower mortality shortly after underwriting (**select period**), then merges to ultimate

Document:

1. **Select period** length and basis (e.g., duration since issue)
2. **Ultimate** rates used after select wears off
3. Whether **aggregate** or **individual** underwriting applies

Misapplying select tables (e.g., on renewals without selection) biases pricing and reserves.

## Joint-life structures

For lives \((x)\) and \((y)\) with independence (unless modeling dependence explicitly):

- **Joint survival** \({}_n p_{xy} = {}_n p_x \cdot {}_n p_y\)
- **Last survivor** probabilities combine survival and single-death events
- **First death** benefits use \({}_n q_{xy}\) or complementary structures

State **correlation** or **common shock** if independence is relaxed (escalate to specialist models).

## Practical checks

1. **Monotonicity** — \(l_x\) non-increasing; \(q_x \in [0,1]\)
2. **Closure** — \(l_{x+1} = l_x (1 - q_x)\) within rounding
3. **Radix and age** — Issue age vs attained age; birthday conventions
4. **Gender/smoker** — Segment tables; do not blend without explicit rules
5. **Improvement** — Distinguish base table from projection scale (see `longevity_improvement_and_estimation.md`)

Hand **experience studies** and **credibility-weighted** table construction execution to `actuarial-analyst`; assumption approval to `assumption-setting`.
