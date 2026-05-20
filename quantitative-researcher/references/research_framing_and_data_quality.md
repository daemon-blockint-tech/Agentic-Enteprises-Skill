# Research Framing and Data Quality

## Table of contents

1. [Question framing](#question-framing)
2. [Hypothesis and pre-registration](#hypothesis-and-pre-registration)
3. [Data sourcing](#data-sourcing)
4. [Corporate actions and returns](#corporate-actions-and-returns)
5. [Point-in-time and survivorship](#point-in-time-and-survivorship)
6. [Profiling checklist](#profiling-checklist)
7. [Research snapshots](#research-snapshots)

## Question framing

Start from a **decision or learning objective**, not from a dataset.

| Weak framing | Stronger framing |
|---|---|
| "Find predictive features" | "Does factor X explain cross-sectional returns in US large-cap equities, 2010–2024, after industry neutralization?" |
| "Backtest this signal" | "Does signal Y survive 5 bps round-trip costs at monthly rebalance with PIT fundamentals?" |
| "Is Sharpe good?" | "How stable is risk-adjusted return across vol regimes with 95% bootstrap CIs?" |

Capture:

- **Asset class** and **investable universe** definition
- **Horizon** (holding period, rebalance frequency)
- **Sample period** and rationale for start/end (IPO bias, regime change)
- **Primary estimand** (mean return spread, IR, hit rate, regression coefficient)

## Hypothesis and pre-registration

Document before analysis:

1. **Null hypothesis** (e.g., no difference in mean spread after costs)
2. **Alternative** and direction if one-sided
3. **Primary test statistic** and **significance** or **CI** approach
4. **Planned robustness** (subperiods, alternative neutralization, alt data vendor)
5. **Stopping rules** for iterative research (avoid unbounded peeking without correction)

For exploratory work, label sections **exploratory** and cap **claims** accordingly.

## Data sourcing

| Concern | Action |
|---|---|
| License | Record permitted use (research vs redistribution vs live trading) |
| Symbology | Map tickers/CUSIP/FIGI; document rename and merger handling |
| Timezone | Align timestamps (exchange local vs UTC); document session filters |
| Staleness | Note publication lag for fundamentals and macro releases |
| Revision | Macro series may revise; store **as-of** date for each pull |

Maintain a **data dictionary**: field name, unit, frequency, source, transformation.

## Corporate actions and returns

Define return construction explicitly:

- **Price return** vs **total return** (dividends reinvested)
- **Split adjustment** method (backward-adjusted prices vs separate factors)
- **Currency** conversion for ADRs and global universes (FX source and timing)

Reconcile a random sample of names across **two sources** after major corporate actions.

## Point-in-time and survivorship

**Point-in-time (PIT)** means inputs available **at decision time**, not with future restatements.

| Failure mode | Mitigation |
|---|---|
| Lookahead in fundamentals | Use PIT fundamental databases; lag reporting dates |
| Survivorship in price panels | Use historical index membership or dead-stock databases |
| Backfilled index composition | Use membership files with effective dates |
| Restated macro | Tag vintage or use real-time release archives |

Document **universe entry/exit** rules (IPO seasoning, liquidity filters, delisting handling).

## Profiling checklist

Run on every new dataset:

- [ ] Row counts by date; detect gaps and duplicate keys
- [ ] Missingness heatmap by field and time
- [ ] Outlier scan (winsorization policy decided **after** viewing, not ad hoc per result)
- [ ] Cross-section size per date (survivorship drops show as jumps)
- [ ] Join integrity (signals ⊂ prices ⊂ universe)
- [ ] Label leakage scan (features correlated with future-only fields)

## Research snapshots

Freeze artifacts for reproducibility:

```text
snapshot_id: 2024Q4-us-equity-v3
data_vendor: [name]
pull_date: YYYY-MM-DD
universe_file: universe_2024Q4.csv (hash: …)
price_adjustment: total_return_backward
signal_code_git_sha: …
```

Store hashes or version IDs; avoid "latest" in final memos.
