# Estimation, diagnostics, and risk measures

## Table of contents

1. [Estimation methods](#estimation-methods)
2. [Maximum likelihood](#maximum-likelihood)
3. [Goodness-of-fit](#goodness-of-fit)
4. [Model diagnostics](#model-diagnostics)
5. [Risk measures](#risk-measures)
6. [Capital implications (technical)](#capital-implications-technical)

## Estimation methods

| Method | Use | Notes |
|---|---|---|
| **MLE** | Parametric severity/frequency | Asymptotic SEs; check regularity |
| **Method of moments** | Quick starts; method-of-moments priors | Less efficient |
| **Percentile matching** | Tail-focused fits | Subjective anchor choice |
| **Bayesian** | Small samples, prior information | Document priors; governance |

Always state **sample period**, **filters**, and **censoring** handling.

## Maximum likelihood

For i.i.d. sample \(x_1,\ldots,x_n\) with parameter \(\theta\):

\[
L(\theta) = \prod f(x_i;\theta), \quad \ell(\theta) = \log L(\theta)
\]

**Severity** on censored data: use survival function contributions for observations above deductible or below limit.

**Frequency** with exposure \(e_i\):

\[
N_i \sim \text{Pois}(\lambda e_i) \Rightarrow \ell(\lambda) = \sum \left( n_i \log(\lambda e_i) - \lambda e_i - \log n_i! \right)
\]

Report:

- Point estimates
- Standard errors (Fisher information or bootstrap)
- Correlation across parameters if multivariate

## Goodness-of-fit

| Test / tool | Application |
|---|---|
| Chi-square | Binned counts; severity or frequency |
| Kolmogorov–Smirnov | Continuous CDF distance; sensitive to center |
| Anderson–Darling | Emphasizes tails |
| QQ / PP plots | Visual alignment |

**Discretization** for continuous severity affects chi-square—document bin widths.

**Overdispersion** tests for frequency (variance/mean ratio; formal tests as available).

Do not accept GOF at \(\alpha=0.05\) alone when **business tail** fails visually.

## Model diagnostics

- **Residuals** — Pearson/deviance for GLM-style fits; outlier flags
- **A/E** by segment — observed vs model-predicted counts or dollars
- **Stability** — refit by accident year; parameter drift
- **Influence** — large claims pull tail parameters
- **Cross-validation** — holdout years for predictive check (conceptual)

List **limitations** explicitly: sparse tail, COVID-era distortion, benefit changes (health).

## Risk measures

For loss random variable \(S\):

**Value at Risk** at confidence \(1-\alpha\):

\[
\mathrm{VaR}_\alpha(S) = \inf\{ s : P(S \le s) \ge \alpha \}
\]

**Tail Value at Risk** (TVaR / CTE):

\[
\mathrm{TVaR}_\alpha(S) = \mathrm{E}[S \mid S > \mathrm{VaR}_\alpha(S)]
\]

**Properties:**

- TVaR is **coherent** subadditive in standard treatments; VaR is not
- Heavy tails: TVaR materially exceeds VaR
- Estimate from **simulated** \(S\) or parametric tail when model trusted

Report **confidence level** (e.g., 99.5%) and **time horizon** (annual aggregate vs per occurrence).

## Capital implications (technical)

At **technical** level only (regulatory capital frameworks → actuary / appointed actuary):

- Higher **TVaR** relative to mean indicates need for **risk load** or reinsurance
- Compare TVaR to **retention** and **reinsurance** attachment
- **Parameter risk** not captured in single fitted distribution—sensitivity bands or Bayesian predictive distributions

Do not map VaR/TVaR to **RBC** or **Solvency II** charges without qualified regulatory context.

Link aggregate percentiles to `aggregate_loss_models.md` simulation output.
