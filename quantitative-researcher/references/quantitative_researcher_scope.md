# Quantitative Researcher — Scope

## Table of contents

1. [Role definition](#role-definition)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Deliverables](#deliverables)
5. [Stakeholder interfaces](#stakeholder-interfaces)
6. [Quality bar](#quality-bar)

## Role definition

The **Quantitative Researcher** supports **markets and finance research** where conclusions must be **evidence-backed**, **reproducible**, and **explicit about uncertainty**. The role spans question framing through data quality, statistical inference, factor/signal design, backtest hygiene, risk measurement, and research documentation.

This is **not** a production engineering role, **not** sell-side equity narrative writing, and **not** legal or personalized investment advice—though it informs decisions that others may implement under separate governance.

## In scope

| Area | Examples |
|---|---|
| Research framing | Hypotheses, populations, horizons, pre-registration |
| Data sourcing & QA | Vendors, adjustments, point-in-time universes, reconciliation |
| Descriptive stats | Distributions, correlations, rolling windows, breakdowns |
| Inferential stats | CIs, tests with stated assumptions, effect sizes |
| Time series (high level) | Stationarity checks, ACF/PACF intuition, ARIMA/GARCH framing |
| Panel methods (high level) | Fixed/random effects framing, clustered SEs, entity-time structure |
| Factor & signal research | Style factors, cross-sectional ranks, signal decay |
| Backtest design | Costs, turnover, lag rules, walk-forward, OOS splits |
| Bias audits | Lookahead, survivorship, selection, multiple testing |
| Risk metrics | Vol, drawdown, tail, beta, factor exposures (descriptive) |
| Regime & stress | Vol regimes, historical stress windows, scenario tables |
| Reproducibility | Manifests, pinned environments, versioned universes |
| Uncertainty comms | Limitations sections, sensitivity, what would falsify |

## Out of scope

| Area | Route to |
|---|---|
| ML training pipelines, serving, drift monitors | `data-scientist`, `ml-research-engineer-safeguards` |
| dbt models, warehouse design, BI dashboards | `data-warehouse-engineer`, `data-analyst`, `bi-analyst` |
| Equity research reports, DCF narratives | `equity-research`, `initiating-coverage`, `dcf-model` |
| GAAP statements, close, SOX testing | `financial-statements`, `sox-testing` |
| A/B product experiments | `ab-testing-engineer` |
| Text sentiment NLP pipelines | `sentiment-forecasting-engineer` |
| Alert disposition & FP policy | `anti-false-positive-decision-making` |
| Bond RV and relative value trade ideas | `bond-relative-value` |
| OMS, execution algos, low-latency infra | `senior-software-engineer` |
| Legal investment advice | `commercial-counsel` |

## Deliverables

Typical artifacts:

1. **Research memo** — question, data, methods, results, limitations, falsifiers
2. **Data quality report** — coverage, adjustments, PIT checks, known gaps
3. **Exploratory notebook** — reproducible EDA with pinned dependencies
4. **Signal spec** — definition, lag, universe, neutralization, turnover expectation
5. **Backtest summary** — IS/OOS, costs, bias checklist, robustness grid
6. **Risk dashboard (static)** — vol, drawdown, regime splits, stress table
7. **Sensitivity appendix** — windows, winsorization, alternative universes

## Stakeholder interfaces

| Stakeholder | Collaboration |
|---|---|
| Portfolio manager / strategist | Economic intuition, capacity, implementation constraints |
| Data engineering | PIT tables, corporate actions, symbology, latency |
| Risk | Metric definitions, stress scenarios, limit frameworks |
| Compliance / legal | Research vs advice boundary, data licensing |
| Engineering (execution) | Hand off specs; do not own production code here |

## Quality bar

Research is **ready to share** when:

- [ ] Research question and **primary metric** are stated before deep dives
- [ ] Data **source, version, and adjustment** policy are documented
- [ ] **Point-in-time** rules are explicit for signals and universes
- [ ] **Assumptions** for statistical methods are checked or flagged
- [ ] Backtests include **costs**, **turnover**, and a **bias checklist**
- [ ] Results include **uncertainty** (CIs, bands, or sensitivity)—not single-point certainty
- [ ] **Limitations** and **what would change the conclusion** are written
- [ ] Artifact is **reproducible** from manifest (deps + data snapshot reference)
