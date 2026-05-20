# Statistics, Time Series, and Panels

## Table of contents

1. [Descriptive foundations](#descriptive-foundations)
2. [Inferential principles](#inferential-principles)
3. [Dependence and effective sample size](#dependence-and-effective-sample-size)
4. [Time-series workflow (high level)](#time-series-workflow-high-level)
5. [Panel data workflow (high level)](#panel-data-workflow-high-level)
6. [Common pitfalls](#common-pitfalls)
7. [Reporting standards](#reporting-standards)

## Descriptive foundations

Before modeling, report:

- **Central tendency** and **dispersion** (mean, median, std, IQR)
- **Skewness** and **excess kurtosis** (fat tails matter for risk)
- **Quantiles** (1%, 5%, 95%, 99%) for return and signal distributions
- **Rolling** statistics with window length stated (e.g., 63-day vol)
- **Correlation** matrices with caution on synchronous overlap at high frequency

Visualize: histograms, QQ plots, rolling mean/vol, drawdown paths.

## Inferential principles

| Principle | Practice |
|---|---|
| Estimands first | Define target parameter (mean spread, slope, IR) |
| Effect size | Report economic magnitude, not only significance |
| Intervals | Prefer CIs over binary significant/not |
| Assumptions | State and test (or acknowledge violation) |
| Multiple testing | Pre-specify families; apply FDR/Bonferroni when exploring many signals |

Avoid interpreting **p-values** from many trials without multiplicity control.

## Dependence and effective sample size

Financial series are rarely i.i.d.:

- **Autocorrelation** in returns and squared returns (vol clustering)
- **Cross-sectional correlation** on the same day (market factor)
- **Overlapping samples** in overlapping holding-period returns

Use **Newey–West** HAC standard errors for time-series regression, or **block bootstrap** for dependent data. Report **effective N** when using overlapping windows.

## Time-series workflow (high level)

1. **Plot** levels and returns; identify structural breaks
2. **Stationarity** intuition: ADF/KPSS as diagnostics, not automatic truth
3. **ACF/PACF** for ARMA order hints; prefer parsimony
4. **Seasonality** for macro (monthly payroll, quarterly earnings seasons)
5. **Regime splits** when single global model is misleading
6. **Out-of-sample** evaluation with rolling origin or expanding window

Methods (workflow-level, not exhaustive implementation):

| Goal | Typical tool class |
|---|---|
| Mean dynamics | ARMA, local level |
| Vol clustering | GARCH family (interpret with care on small samples) |
| Cointegration | Engle–Granger / Johansen framing for spreads |
| VAR | Impulse responses with variable ordering documented |

## Panel data workflow (high level)

Panel = entities \(i\) over times \(t\).

1. Classify structure: **balanced** vs **unbalanced**; attrition reasons
2. Choose **fixed effects** (entity, time) when unobserved heterogeneity is plausible
3. Cluster standard errors at **entity** level (or two-way) for cross-sectional panels
4. Watch **Nickell bias** in short dynamic panels with lagged dependent variables
5. For **factor portfolios**, use Fama–MacBeth or panel regression with clear weighting

| Model intent | Framing |
|---|---|
| Characteristic premium | Regress return on lagged signal; FE optional |
| Event study | Window around event; abnormal return benchmark stated |
| Macro panel | Countries/sectors; heterogeneity and small-N caution |

## Common pitfalls

| Pitfall | Symptom | Mitigation |
|---|---|---|
| Spurious regression | High R² on non-stationary levels | Use returns or cointegration framework |
| Data snooping | Many specs until one "works" | Pre-register; hold out OOS |
| Heteroskedasticity ignored | Wrong SEs | Robust/HAC/clustered SEs |
| Lookahead in lags | Inflated fit | Strict PIT lag rules |
| Simultaneity | Signal uses same-bar return | Align signal to \(t-1\) decision |

## Reporting standards

Every inferential table should include:

- **Sample period** and **N** (entities × dates)
- **Specification** (FE, weights, SE type)
- **Coefficient** + **CI** (or SE) + economic interpretation
- **Robustness** pointer (alt spec in appendix)

Flag when conclusions are **fragile** to window choice or outlier treatment.
