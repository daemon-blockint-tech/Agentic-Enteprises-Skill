# Multiple decrement and state models

## Table of contents

1. [Multiple decrement tables](#multiple-decrement-tables)
2. [Associated single decrements](#associated-single-decrements)
3. [Markov multi-state models](#markov-multi-state-models)
4. [Pension and disability applications](#pension-and-disability-applications)
5. [Implementation notes](#implementation-notes)

## Multiple decrement tables

**Multiple decrement** model: several exit causes (death, lapse, retirement, disability) in the same interval.

Notation (example causes \(j=1,\ldots,m\)):

- \(q_x^{(j)}\) — probability of decrement \(j\) between \(x\) and \(x+1\)
- \(q_x^{(\tau)}\) — total decrement probability: \(q_x^{(\tau)} = \sum_j q_x^{(j)}\) (if mutually exclusive)
- \(l_x^{(\tau)}\) — survivors in active state before decrements

\[
l_{x+1}^{(\tau)} = l_x^{(\tau)} (1 - q_x^{(\tau)})
\]

**Dependent decrements** — all causes compete in the same interval (standard for pension active populations).

**Independent decrements** — assume each cause operates on a hypothetical population; use only when theory or regulation requires.

## Associated single decrements

**Associated single decrement rate** \(q_x^{'(j)}\): rate for cause \(j\) if it were the only decrement.

Common relationship (Makeham-style independence assumption):

\[
1 - q_x^{(\tau)} = \prod_j (1 - q_x^{'(j)})
\]

Document when converting **experience** by cause to **pricing** tables.

## Markov multi-state models

States \(S = \{1,\ldots,K\}\); transition intensity \(\mu_{ij}(t)\) from \(i\) to \(j\).

**Kolmogorov forward equations** for probabilities \(P_{ij}(s,t)\):

\[
\frac{\partial}{\partial t} P_{ij}(s,t) = \sum_k P_{ik}(s,t)\,\mu_{kj}(t) - \mu_{ij}(t)\,P_{ij}(s,t)
\]

**Actuarial present values** weight cash flows by state occupancy probabilities.

Typical state spaces:

| Context | States |
|---|---|
| Disability | Active → disabled → dead; recovery optional |
| Pension | Active → retired → dead; terminated |
| Long-term care | Healthy → care → dead |

## Pension and disability applications

**Pension liability** measurement (conceptual):

1. Project **benefit accrual** by status and service
2. Apply **decrements** (termination, mortality, disability, retirement)
3. Discount with **segment rates** or curve (overview) — detail in `pension-retirement-funds`
4. Sum **APV** of projected benefits

**Disability income** — payment while disabled; recovery to active; waiver of premium as rider math.

Do not conflate **funding** vs **accounting** vs **economic** measurement bases.

## Implementation notes

1. **Conservation** — decrements sum to at most total exit probability
2. **Timing** — decrements at start vs end of interval
3. **Selection** — disability rates often depend on duration in state
4. **Data** — sparse causes need graduation or pooling
5. **Peer skills** — plan design narrative → `pension-retirement-funds`; tables → `actuarial-analyst`
