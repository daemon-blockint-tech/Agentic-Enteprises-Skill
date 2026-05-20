# Aggregate loss models

## Table of contents

1. [Compound model definition](#compound-model-definition)
2. [Moments of aggregate S](#moments-of-aggregate-s)
3. [Normal approximation](#normal-approximation)
4. [Exact and numerical methods](#exact-and-numerical-methods)
5. [Percentiles and reinsurance](#percentiles-and-reinsurance)
6. [Dependence extensions](#dependence-extensions)

## Compound model definition

**Collective risk model:**

\[
S = \begin{cases} 0 & N=0 \\ X_1 + \cdots + X_N & N \ge 1 \end{cases}
\]

Standard assumptions:

- \(N\) independent of \(\{X_i\}\)
- \(X_i\) i.i.d. and independent of \(N\)

**Individual risk model** (optional extension): sum over policies with policy-specific \(N_j, X_{jk}\)—use when heterogeneity is policy-specific and not pooled.

## Moments of aggregate S

When \(N\) is independent of \(X_i\):

\[
\mathrm{E}[S] = \mathrm{E}[N] \cdot \mathrm{E}[X]
\]

\[
\mathrm{Var}(S) = \mathrm{E}[N]\mathrm{Var}(X) + \mathrm{Var}(N)(\mathrm{E}[X])^2
\]

These formulas underpin **pure premium** (\(\mathrm{E}[S]/\)exposure) and **normal approximation** variance.

For **compound Poisson** with Poisson mean \(\lambda\):

\[
\mathrm{Var}(S) = \lambda \mathrm{E}[X^2] = \lambda(\mathrm{Var}(X) + (\mathrm{E}[X])^2)
\]

## Normal approximation

Approximate:

\[
S \approx \mathcal{N}(\mathrm{E}[S], \mathrm{Var}(S))
\]

**When reasonable:**

- \(\mathrm{E}[N]\) moderately large
- Severity not extremely heavy-tailed relative to the question (e.g., central percentiles)

**When weak:**

- Low \(\mathrm{E}[N]\) (few claims)
- Heavy-tailed severity for high quantiles (VaR/TVaR)
- Highly skewed frequency

Report **continuity correction** only for discrete severity masses when relevant.

## Exact and numerical methods

| Method | Idea | Notes |
|---|---|---|
| **Panjer recursion** | Recursive distribution for \(S\) when severity discrete | Severity discretization error |
| **FFT** | Convolve frequency pgf with severity characteristic function | Common for discretized severity |
| **Simulation** | Draw \(N\), then \(N\) severities | Flexible; quantify Monte Carlo error |

**Simulation workflow (conceptual):**

1. Fit frequency and severity separately (or joint if specified)
2. For \(b=1,\ldots,B\): draw \(N^{(b)}\), then \(X_1^{(b)},\ldots,X_{N^{(b)}}^{(b)}\); set \(S^{(b)}\)
3. Estimate percentiles and TVaR from \(\{S^{(b)}\}\)

State **seed**, **B**, and whether **reinsurance** transforms \(X\) before aggregation.

## Percentiles and reinsurance

**Reinsurance** transforms severity (e.g., excess-of-loss \(Y=\min(\max(X-a,0), m)\)) before summing—aggregate model must apply transforms at **claim level**, not on \(S\) unless structure allows.

Link percentile of \(S\) to:

- **Risk measures** (see `estimation_diagnostics_and_risk_measures.md`)
- **Occurrence limits** and **aggregate caps** (may require separate treatment of frequency caps)

## Dependence extensions

Default independence is a **material assumption**. If:

- **Catastrophe** drives simultaneous claims → consider common shock or frequency spike models
- **Inflation** correlates severities across claims → time-series methods may exceed ASTAM scope

Flag dependence needs to actuary; copula or hierarchical models route toward `quantitative-researcher` with actuarial oversight.
