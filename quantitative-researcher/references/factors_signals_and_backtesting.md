# Factors, Signals, and Backtesting

## Table of contents

1. [Economic intuition first](#economic-intuition-first)
2. [Signal construction](#signal-construction)
3. [Portfolio formation](#portfolio-formation)
4. [Backtest mechanics](#backtest-mechanics)
5. [Bias checklist](#bias-checklist)
6. [Overfitting and multiple testing](#overfitting-and-multiple-testing)
7. [Performance attribution framing](#performance-attribution-framing)

## Economic intuition first

A signal should answer:

- **Why** should this predict returns or risk? (risk premium, mispricing, structural flow)
- **Who** trades against it and **why** might the edge persist or decay?
- **Horizon** at which the mechanism operates
- **Capacity** intuition (liquidity, market cap segment)

Document **failure modes** (regime dependence, crowding, regulatory change).

## Signal construction

| Step | Requirement |
|---|---|
| Raw inputs | PIT-safe; document lag vs report date |
| Transform | Winsorize/z-score/rank with **in-sample** vs **rolling** policy stated |
| Neutralization | Industry/size beta removal method explicit |
| Orthogonalization | If stacking signals, order and regression spec documented |

**Decay analysis**: autocorrelation of signal and portfolio turnover vs horizon.

## Portfolio formation

Common patterns:

- **Sorts**: quintiles/deciles on signal; long top, short bottom (or long-only top)
- **Weighting**: equal-weight vs cap-weight; impact on microcap bias
- **Rebalance**: calendar vs threshold; turnover implications
- **Holding period**: align with signal horizon; avoid overlapping return double-count without care

Report **gross** and **net** returns separately.

## Backtest mechanics

Minimum backtest spec:

```text
universe: [definition + PIT membership]
signal: [formula + lag]
rebalance: [frequency]
costs: [bps per side, spread assumption]
borrow: [short rebate / hard-to-borrow if applicable]
capital: [notional, leverage cap]
benchmark: [optional]
```

Include:

- **Cumulative return** and **drawdown** path
- **Hit rate**, **mean spread**, **t-stat** (with HAC where needed)
- **Turnover** and **capacity** proxy (ADV participation)
- **Exposure** to known factors (beta, size, value, momentum)

## Bias checklist

| Bias | Question to ask |
|---|---|
| Lookahead | Could any input have been known before trade time? |
| Survivorship | Does universe include delisted names for full history? |
| Selection | Was universe chosen **after** seeing results? |
| Data mining | How many variants were tried? |
| Corporate actions | Returns and shares aligned on ex-dates? |
| Liquidity | Are illiquid names tradable at assumed prices? |
| Shorting | Are shorts feasible in segment and period? |
| Regime cherry-pick | Was best subperiod highlighted without full sample? |

## Overfitting and multiple testing

Mitigations:

- **Train / validation / test** splits by time
- **Walk-forward** re-estimation of parameters
- **Deflated Sharpe** or **haircut** heuristics when many trials (cite method)
- **Bonferroni / FDR** across signal families explored
- **Simple beats complex** when performance is within noise

Prefer **one** primary backtest spec; others go to robustness appendix.

## Performance attribution framing

Separate:

- **Factor exposure** (market, style) vs **idiosyncratic** residual
- **Timing** vs **selection** when relevant
- **Costs** drag vs **gross** alpha

Do not attribute **in-sample** fit as **expected** live performance without OOS evidence.
