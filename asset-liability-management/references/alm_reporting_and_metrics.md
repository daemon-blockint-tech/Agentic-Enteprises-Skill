# ALM reporting and metrics

## Table of contents

1. [Reporting audiences](#reporting-audiences)
2. [Core ALM dashboard](#core-alm-dashboard)
3. [Sensitivity and exposure metrics](#sensitivity-and-exposure-metrics)
4. [Tail and horizon metrics](#tail-and-horizon-metrics)
5. [Bridges and attribution](#bridges-and-attribution)
6. [Benchmarking and IPS alignment](#benchmarking-and-ips-alignment)
7. [Capital and regulatory exhibits](#capital-and-regulatory-exhibits)
8. [Exhibit quality checklist](#exhibit-quality-checklist)

## Reporting audiences

| Audience | Focus | Tone |
|---|---|---|
| **ALCO** | Limits, hedge decisions, scenario breaches | Technical, decision-ready |
| **Board / risk committee** | Surplus trend, tail risks, policy compliance | Summary, narrative |
| **CFO / finance** | Accounting earnings impact, hedge P&L | Basis-specific |
| **Regulators** (overview) | Prescribed templates, ORSA/ICAAP summaries | Factual, qualified review |
| **Rating agencies** (overview) | Risk management quality, liquidity | Consistent with public disclosures |

Tailor depth; avoid mixing bases without reconciliation tables.

## Core ALM dashboard

Recommended panels (institution-dependent):

1. **Surplus or funded ratio** — level and 12-month trend
2. **Duration gap** — total and key-tenor breakdown
3. **Hedge ratio** — by risk factor (rates, inflation, FX)
4. **Limit utilization** — traffic-light vs policy
5. **Largest sensitivities** — top three drivers of \(\Delta S\)
6. **Upcoming cash flows** — benefit/claim payments vs asset maturities (12–24m)
7. **Derivative exposure** — notional, DV01, collateral

Include **as-of date**, **currency**, and **basis** in header/footer.

## Sensitivity and exposure metrics

| Metric | Definition (typical) | Notes |
|---|---|---|
| DV01 (asset, liability, net) | PV change per 1bp parallel | Specify curve |
| Effective duration | % PV change per 100bp | Options need effective |
| Key rate DV01 | Sensitivity to tenor bucket | Show net KRD chart |
| Spread DV01 | PV change per 1bp OAS | Credit books |
| Equity beta to surplus | Regression or stress grid | Pension risk assets |
| Inflation DV01 | PV change per 1bp real rate / CPI | Index definition |

Present **gross** and **hedged** columns where overlays exist.

## Tail and horizon metrics

| Metric | Description | Caveats |
|---|---|---|
| **Surplus-at-risk (SaR)** | Tail loss on surplus over horizon at confidence level | Method varies (parametric vs simulation) |
| **VaR / ES** | Value-at-risk / expected shortfall on surplus or NAV | Holding period must be stated |
| **Earnings-at-risk (EaR)** | NII or accounting earnings impact (banks, insurers) | Accounting vs economic |
| **Shortfall risk** | Probability funded ratio < threshold | Pension-specific |

Always disclose:

- **Confidence level** (95%, 99%)
- **Horizon** (1y, 3y)
- **Rebalancing** assumptions
- **Correlations** source

## Bridges and attribution

### Surplus bridge (example components)

\[
S_1 - S_0 = \underbrace{\text{market}}_{\text{rates, spreads, equity}} + \underbrace{\text{flows}}_{\text{contributions, benefits}} + \underbrace{\text{assumptions}}_{\text{actuarial}} + \underbrace{\text{other}}_{\text{FX, fees}}
\]

### Funded ratio bridge (pensions)

- Asset return
- Liability interest cost / discount rate change
- Contributions and benefit payments
- Demographic experience

Require **consistent basis** across periods; flag one-offs.

## Benchmarking and IPS alignment

ALM reporting should connect to **Investment Policy Statement (IPS)**:

- **Strategic asset allocation** ranges vs actual
- **LDI allocation** vs policy target
- **Tracking error** to liability benchmark (if used)
- **Risk budget** consumption (equity, credit, illiquids)

Distinguish **policy benchmark** from **peer** comparison—peers optional for ALCO, not core ALM risk.

## Capital and regulatory exhibits

High-level mapping only—specialists own filings.

| Exhibit | ALM content |
|---|---|
| ORSA / risk appetite | SaR, stress outcomes vs appetite |
| RBC projection (insurance) | Rate/spread stress on surplus and capital |
| IRRBB (bank) | EVE/NII stress vs limits |
| Pension disclosure support | Sensitivity tables coordinated with actuary |

Footnote: **not** substitute for appointed actuary, auditor, or regulatory submission.

## Exhibit quality checklist

Before distributing ALCO materials:

- [ ] **Basis** and **currency** on every page
- [ ] **Curve** IDs and shock definitions match risk system
- [ ] **Net** exposures shown, not assets alone
- [ ] **Hedged vs unhedged** clearly separated
- [ ] **Limits** with utilization % and trend
- [ ] **Scenarios** dated and versioned
- [ ] **Narrative** explains breaches and proposed actions
- [ ] **Disclaimers** on non-advice and model limitations
- [ ] **Data cut** timestamp and reconciliation to finance records

Coordinate liability exhibits with `actuary` or `pension-retirement-funds` owners before external distribution.
