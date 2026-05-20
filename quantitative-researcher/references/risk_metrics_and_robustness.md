# Risk Metrics and Robustness

## Table of contents

1. [Return and volatility](#return-and-volatility)
2. [Drawdown and tail risk](#drawdown-and-tail-risk)
3. [Risk-adjusted ratios](#risk-adjusted-ratios)
4. [Factor exposure and beta](#factor-exposure-and-beta)
5. [Regime analysis](#regime-analysis)
6. [Stress testing](#stress-testing)
7. [Robustness grids](#robustness-grids)

## Return and volatility

Define **return frequency** (daily, weekly) and **annualization factor** explicitly.

| Metric | Definition notes |
|---|---|
| Realized vol | Std of returns × √(periods per year) |
| Downside vol | Std of returns below target (often 0 or MAR) |
| EWMA vol | λ parameter stated; reactive to recent shocks |

Report vol in **percent** and **decimal** consistently; label currency for multi-currency books.

## Drawdown and tail risk

| Metric | Use |
|---|---|
| Max drawdown | Peak-to-trough on cumulative wealth |
| Calmar | CAGR / |max DD| — sensitive to single episode |
| VaR / ES | Quantile and expected shortfall; state confidence level (95%, 99%) |
| Skew / kurtosis | Fat tails invalidate normal VaR |

Show **drawdown path** chart with recovery time (time underwater).

## Risk-adjusted ratios

| Ratio | Limitation |
|---|---|
| Sharpe | Assumes stable mean/vol; punishes upside vol symmetrically; noisy on short samples |
| Sortino | Depends on MAR; downside definition must be fixed |
| Information ratio | Benchmark choice drives result; tracking error estimation matters |
| Treynor | Requires beta stability |

When reporting Sharpe:

- State **risk-free** series used
- Prefer **bootstrap CIs** on Sharpe or returns
- Note **non-normality** and **autocorrelation**
- Avoid ranking strategies on **in-sample** Sharpe alone

## Factor exposure and beta

Run **regression** of portfolio returns on factor returns (Fama–French, macro, custom).

Report:

- **Betas** + **CIs** (HAC SEs)
- **R²** and **residual vol**
- **Rolling beta** plots for stability

Distinguish **risk exposure** from claimed **alpha** after factor adjustment.

## Regime analysis

Segment history by observable regimes:

| Regime axis | Example split |
|---|---|
| Volatility | VIX high/low terciles |
| Rates | Rising/falling yield curve |
| Liquidity | Spread widening episodes |
| Trend | Bull/bear market labels (define rule) |

For each segment, report **mean return**, **vol**, **Sharpe**, **max DD**, and **N** (effective sample).

Avoid **too many** segments on short histories (false precision).

## Stress testing

**Historical stress**: replay portfolio through known windows (2008, 2020, 2022 rates, etc.)

**Hypothetical shocks**:

- Parallel rate shift (+100 bps)
- Equity shock (−20% beta-scaled)
- Vol spike (scale residuals)

Document **linear vs nonlinear** instrument assumptions (options, convexity).

Stress outputs are **scenario illustrations**, not forecasts.

## Robustness grids

Standard grid for research memos:

| Dimension | Variants |
|---|---|
| Sample start/end | ±2 years |
| Universe | Cap cutoffs, liquidity filters |
| Signal lag | +1 period delay |
| Costs | 0 / 5 / 10 bps |
| Weighting | EW vs cap |
| Neutralization | None / industry / industry+size |

Present as **table of key metrics**, not only best cell. Highlight **sign flips** and **magnitude swings**.

Conclude with **stability score** (qualitative): robust / mixed / fragile.
