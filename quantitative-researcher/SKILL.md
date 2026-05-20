---
name: quantitative-researcher
description: |
  Guides quantitative research for markets and finance—research question framing, data sourcing
  and quality checks, descriptive and inferential statistics, time series and panel methods (high
  level), factor and signal research, backtest design and pitfalls (lookahead, survivorship),
  risk metrics (volatility, drawdown, Sharpe limitations), regime and stress analysis, and
  reproducible notebooks or reports with explicit limitations and uncertainty communication.
  Use when the user mentions "quantitative research", "quant researcher", "factor research",
  "signal backtest", "time series analysis", "panel regression", "alpha research", "Sharpe ratio
  analysis", "survivorship bias", "lookahead bias", "econometric analysis", or "risk factor
  model". Not for production ML pipelines (data-scientist, ml-research-engineer), equity narrative
  reports (equity-research skills), SOX accounting (financial-statements), legal investment advice,
  or trading execution systems (senior-software-engineer).
---

# Quantitative Researcher

## When to Use

- Frame a **research question**, null hypotheses, and falsifiable claims before touching data
- Source, license-check, and **profile** market or macro datasets (missingness, staleness, corporate actions)
- Run **descriptive** and **inferential** statistics with documented assumptions
- Apply **time-series** or **panel** methods at workflow level (stationarity, autocorrelation, fixed effects—when appropriate)
- Design **factor**, **signal**, or **alpha** research with clear economic intuition and testable predictions
- Structure **backtests** with realistic costs, point-in-time universes, and bias checklists
- Compute and interpret **risk metrics** (volatility, drawdown, tail risk) and stress **regimes**
- Produce **reproducible** notebooks or research memos with limitations, sensitivity, and uncertainty bands
- Communicate **what would change the conclusion**—not point forecasts presented as advice

## When NOT to Use

- Production **ML pipelines**, feature stores, model serving, or MLOps → `data-scientist`, `ml-research-engineer-safeguards`, `ml-ops-engineer`
- Executive **BI dashboards**, KPI definitions, or warehouse metric layers → `data-analyst` (if installed), `bi-analyst`, `analytics-data-engineer`
- **Equity initiation**, earnings narrative, or sell-side style research reports → `equity-research`, `initiating-coverage`, `earnings-analysis` (if installed)
- **SOX** close, journal entries, or GAAP financial statements → `financial-statements`, `compute-accounting-manager`
- **Legal** investment advice, suitability, or regulatory filings → `commercial-counsel`, compliance skills
- **Trading execution**, OMS, or low-latency production systems → `senior-software-engineer` (if installed)
- **Product A/B tests** and experiment platform design → `ab-testing-engineer`
- **Text sentiment** forecasting without quant factor/backtest framing → `sentiment-forecasting-engineer`, `sentiment-analysis-engineer`
- **Alert threshold** and false-positive decision policy → `anti-false-positive-decision-making`
- **Bond RV**, curve trades, or issuer credit narrative → `bond-relative-value` (if installed)
- **Ratio analysis** and corporate finance storytelling without research design → `financial-analyst` (if installed)

## Related skills

| Need | Skill |
|---|---|
| Classical ML, causal inference, production model eval | `data-scientist` |
| SQL exploration, dashboards, business reporting | `data-analyst` (if installed) |
| Financial ratios, valuation framing, investor metrics | `financial-analyst` (if installed) |
| Bond richness/cheapness, spread decomposition, curve context | `bond-relative-value` (if installed) |
| Text-derived sentiment features and forecast pipelines | `sentiment-forecasting-engineer` |
| Experiment design, power, randomization, readouts | `ab-testing-engineer` |
| Evidence bars before acting on weak signals | `anti-false-positive-decision-making` |
| Macro stress and scenario communication (non-trading) | `scenario-war-room` (if installed) |
| DCF / comps equity workpapers | `dcf-model`, `comps-analysis` (if installed) |

## Core Workflows

### 1. Frame the research question

1. State the **decision or learning goal** (not "find alpha" without a mechanism)
2. Define **population**, **horizon**, and **frequency** (daily bars vs intraday changes methods)
3. Pre-register **primary** statistic or metric; list **secondary** and **robustness** checks
4. Document **null** and **alternative**; specify what evidence would **reject** the hypothesis
5. List **data requirements** and known **limitations** upfront

**See `references/research_framing_and_data_quality.md`.**

### 2. Acquire and validate data

1. Record **vendor**, **version**, **as-of** rules, and **adjustment** policy (splits, dividends, total return)
2. Profile: coverage, gaps, duplicates, timezone alignment, survivorship in universe files
3. Run **reconciliation** spot checks against a second source where feasible
4. Freeze a **research snapshot** (hash, date range, universe version) before analysis

**See `references/research_framing_and_data_quality.md`.**

### 3. Explore and model (descriptive → inferential)

1. Start with **descriptive** stats and visual diagnostics (distributions, outliers, breaks)
2. Choose methods matched to **dependence structure** (i.i.d. vs time series vs panels)
3. Report **effect sizes**, **confidence intervals**, and **assumption checks**—not p-values alone
4. Run **sensitivity** to window, winsorization, and sample exclusions

**See `references/statistics_time_series_and_panels.md`.**

### 4. Factors, signals, and backtests

1. Tie each signal to an **economic story** and **holding period**
2. Build signals with **point-in-time** inputs only; document lag and publication delay
3. Backtest with **transaction costs**, **capacity** intuition, and **turnover** reporting
4. Audit **lookahead**, **survivorship**, **selection**, and **overfitting** (multiple testing)

**See `references/factors_signals_and_backtesting.md`.**

### 5. Risk, robustness, and regimes

1. Report **volatility**, **drawdown**, and **tail** metrics with window definitions
2. Interpret **Sharpe** and related ratios with known limitations (non-normality, short samples)
3. Segment by **regime** (vol, rates, liquidity) and run **stress** scenarios
4. Compare **in-sample** vs **out-of-sample** and **walk-forward** where applicable

**See `references/risk_metrics_and_robustness.md`.**

### 6. Deliver and document

1. Ship a **reproducible** artifact (notebook + pinned deps + data manifest)
2. Include **limitations**, **assumptions**, and **uncertainty** language suitable for stakeholders
3. Separate **research findings** from **implementation** or **execution** recommendations
4. Archive **parameters**, **random seeds**, and **version** metadata

**See `references/research_deliverables_and_ethics.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and deliverables | `references/quantitative_researcher_scope.md` |
| Question framing and data quality | `references/research_framing_and_data_quality.md` |
| Statistics, time series, panels | `references/statistics_time_series_and_panels.md` |
| Factors, signals, backtesting | `references/factors_signals_and_backtesting.md` |
| Risk metrics and robustness | `references/risk_metrics_and_robustness.md` |
| Deliverables, reproducibility, ethics | `references/research_deliverables_and_ethics.md` |
