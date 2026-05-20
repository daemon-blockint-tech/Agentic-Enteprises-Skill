# Probability and statistics foundations

## Table of contents

1. [Core objects](#core-objects)
2. [Key distributions](#key-distributions)
3. [Expectation and variance](#expectation-and-variance)
4. [Conditioning](#conditioning)
5. [LLN and CLT intuition](#lln-and-clt-intuition)
6. [Actuarial bridges](#actuarial-bridges)
7. [Common pitfalls](#common-pitfalls)

## Core objects

| Object | Actuarial use |
|---|---|
| Sample space, event | Claim occurs / does not; policy in force |
| Random variable \(X\) | Claim size, count of claims, time to death (later) |
| pmf / pdf | Discrete counts vs continuous severity |
| CDF \(F(x)=P(X\le x)\) | Percentiles, deductibles (intro) |

**Independence** — State explicitly when multiplying probabilities is valid; many actuarial models assume i.i.d. claims until told otherwise.

## Key distributions

| Distribution | Typical actuarial role | Moments (know) |
|---|---|---|
| Bernoulli / Binomial | Claim indicator; number of claims in \(n\) policies | \(E,\ Var\) |
| Poisson | Claim counts; low-mean frequency | \(E=\lambda,\ Var=\lambda\) |
| Exponential | Waiting times; simple severity | Memoryless property (intro) |
| Gamma | Severity (sum of exponentials) | Shape-scale intuition |
| Normal | Approximations; aggregate (later) | CLT link |
| Lognormal | Positive severity | Right skew |

For **parameter estimation** and GOF at professional depth, see `advanced-short-term-actuarial-mathematics`.

## Expectation and variance

- **Linearity**: \(E[aX+b]=aE[X]+b\) always; \(E[X+Y]=E[X]+E[Y]\) always
- **Variance**: \(Var(aX+b)=a^2 Var(X)\); \(Var(X+Y)=Var(X)+Var(Y)\) **if independent**
- **Indicators**: \(E[I_A]=P(A)\)
- **Moments**: Mean, variance, skewness (awareness)—severity tails matter in insurance

Teach **reasonability checks**: mean claim size vs sample average; variance non-negative.

## Conditioning

| Tool | Use |
|---|---|
| \(P(A\mid B)=P(A\cap B)/P(B)\) | Updated probabilities given information |
| Law of total probability | Mix over scenarios (segments, years) |
| Law of total expectation | \(E[X]=E[E[X\mid Y]]\) — credibility preview |
| Law of total variance | Decompose process vs parameter uncertainty (intro) |

**Actuarial example**: Expected claims given class \(i\); overall expected claims as weighted average.

## LLN and CLT intuition

- **Law of large numbers**: Sample mean → population mean as exposure grows → supports **risk pooling**
- **Central limit theorem**: Sum/average of many small risks → approximately normal under conditions → normal approximation for aggregates (advanced skill)

Do not overclaim CLT for **heavy-tailed** severity without caveats.

## Actuarial bridges

| Foundation topic | Advanced skill topic |
|---|---|
| Poisson / NB counts | Frequency models → `advanced-short-term-actuarial-mathematics` |
| Compound \(S=\sum X_i\) | Aggregate loss models |
| Conditioning / Bayes | Experience rating, limited info |
| Survival (preview only) | Life contingencies → `advanced-long-term-actuarial-mathematics` |

## Common pitfalls

- Treating **sample** statistics as **parameters** without uncertainty language
- Using normal model for **sparse** or **heavy-tailed** counts/severity
- Assuming independence when **calendar year** or **common shock** exists
- Confusing **unconditional** and **conditional** expectations in multi-step problems
