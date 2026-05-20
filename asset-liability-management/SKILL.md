---
name: asset-liability-management
description: |
  Guides asset-liability management (ALM)—matching asset and liability cash flows and risks; interest rate
  risk (duration, convexity, key rate duration); surplus and risk appetite; liability-driven investment (LDI),
  immunization, and hedging (rates, inflation, FX); insurer, pension, and bank ALM; stress testing; ALM policy
  and ALCO reporting; capital metrics at high level—not trade execution, security selection alone, pension plan
  design, actuarial reserving, or assumption governance alone. Use when the user mentions asset liability
  management, ALM, duration gap, interest rate risk ALM, liability driven investing, immunization portfolio,
  ALCO, surplus at risk, key rate duration, ALM policy, or match assets and liabilities—not pensions
  (pension-retirement-funds), actuarial models (actuary), assumptions (assumption-setting), P&C
  (property-casualty-insurance), life/health products (life-health-insurance), equity research
  (financial-analyst), or actuarial consulting (actuarial-consulting).
---

# Asset-Liability Management (ALM)

## When to Use

- Frame **ALM objectives**: cash-flow matching, surplus protection, return within risk appetite, regulatory capital efficiency
- Analyze **interest rate risk**: duration, convexity, key rate duration, parallel and non-parallel shocks
- Design **liability-driven investment (LDI)**, **immunization**, and **hedge programs** (rates, inflation, FX)
- Quantify **duration gap**, **surplus sensitivity**, and **surplus-at-risk** concepts for ALCO materials
- Support **insurer**, **pension**, and **bank** ALM contexts with institution-appropriate metrics
- Build **stress and scenario** sets for ALM (rates, spreads, equity, longevity, credit)
- Draft or review **ALM policy**, **risk limits**, and **ALCO** reporting packs (high level)
- Connect ALM to **capital**, **solvency**, and **regulatory** metrics without substituting appointed actuary or risk sign-off
- Explain **reinvestment**, **prepayment**, and **optionality** impacts on asset–liability profiles

## When NOT to Use

- Pension plan design, ERISA funding, PBGC, or DB/DC benefit formulas as primary topic → `pension-retirement-funds`
- Actuarial pricing, reserving, IBNR triangles, mortality table construction, or statutory opinions → `actuary`
- Assumption governance, assumption packs, and change-control workflows without ALM portfolio lens → `assumption-setting`
- P&C underwriting, claims, or line-of-business education without ALM balance-sheet focus → `property-casualty-insurance`
- Life/health product features, distribution, or claims operations without ALM framing → `life-health-insurance`
- Security selection, issuer research, or equity valuation as primary deliverable → `financial-analyst` (if installed)
- Actuarial consulting engagement scoping, SOW, or due diligence program management → `actuarial-consulting`
- Bank intraday liquidity crisis operations, LCR/NSFR runbooks, or treasury payment ops (unless ALM rate-risk context only)
- Trade execution, order management, or portfolio implementation mechanics without ALM risk framing

## Related skills

| Need | Skill |
|---|---|
| DB/DC pensions, funding policy, benefit design, de-risking structures | `pension-retirement-funds` |
| Pricing, reserving, triangles, experience studies, capital overview | `actuary` |
| Assumption documentation, governance, and change control | `assumption-setting` |
| P&C lines, underwriting, claims, cat context | `property-casualty-insurance` |
| Life, health, annuity product and benefit context | `life-health-insurance` |
| Corporate FP&A, investor metrics, security research | `financial-analyst` (if installed) |
| Actuarial engagement scoping, SOW, due diligence | `actuarial-consulting` |
| IFRS 17 / insurance accounting presentation (coordinate) | `ifrs` (if installed) |
| Enterprise risk registers without ALM metrics | `security-risk-analyst` (if installed) |

## Core Workflows

### 1. Engagement scoping

Before analysis:

1. **Institution type** — Insurer (life/P&C), pension fund/trust, bank ALM desk, asset manager LDI mandate
2. **Balance sheet** — Economic, regulatory, accounting, or funding basis for assets and liabilities
3. **Horizon** — Short-term liquidity vs long-term solvency; run-off vs going-concern
4. **Decision** — Hedge design, IPS/ALM policy, ALCO pack, stress test, capital planning input
5. **Material risks** — Rates, credit/spreads, equity, inflation, longevity, FX, liquidity, basis
6. **Governance** — ALCO charter, limits, model inventory, independent validation requirements

**See `references/alm_scope_and_principles.md`.**

### 2. Interest rate risk and duration

1. Define **valuation basis** and **discount curve(s)** for liabilities and assets
2. Compute or interpret **effective duration**, **modified duration**, **DV01**, and **convexity**
3. Extend to **key rate duration** and **partial durations** for non-parallel shocks
4. Quantify **duration gap** and **surplus** sensitivity to rate moves
5. Flag **embedded options** (calls, prepay, guarantees) that break linear duration
6. Coordinate liability cash-flow shapes with `actuary` or `pension-retirement-funds` when needed

**See `references/interest_rate_risk_and_duration.md`.**

### 3. Liability-driven investing and hedging

1. State **LDI objective**: minimize surplus volatility, maximize hedge ratio, or cash-flow match
2. Map **liability cash flows** (timing, indexation, options) to asset segments
3. Select **hedge instruments**: government bonds, swaps, futures, options, inflation-linked
4. Design **immunization** or **contingent immunization** rules and triggers
5. Address **reinvestment risk**, **curve risk**, and **basis risk** between hedge and liability
6. Separate **strategic asset allocation** from **overlay** and **dynamic de-risking** glide paths

**See `references/liability_driven_investing.md`.**

### 4. Insurance and pension ALM

1. Identify **regime-specific** metrics (e.g., surplus, PVFP, economic capital, funded ratio)
2. For **insurers**: relate ALM to **guarantees**, **asset adequacy**, and **market risk** capital (overview)
3. For **pensions**: link duration, glide paths, and de-risking to **funding** and **accounting** bases
4. For **banks**: distinguish **ALM** (IRRBB, EVE/NII) from **liquidity** risk management
5. Coordinate **longevity**, **lapse**, and **morbidity** with actuarial owners—not duplicate liability models

**See `references/insurance_and_pension_alm.md`.**

### 5. Stress testing and governance

1. Define **scenario set**: historical, hypothetical, regulatory, and reverse stress
2. Shock **rates**, **spreads**, **equity**, **credit**, **inflation**, and **longevity** consistently
3. Report **surplus**, **capital**, and **limit breaches** with clear attribution
4. Align with **ALM policy** limits, **risk appetite**, and **escalation** paths
5. Document **model risk**, data lineage, and **ALCO** decision log

**See `references/stress_scenarios_and_governance.md`.**

### 6. ALM reporting and metrics

1. Build **ALCO dashboard**: surplus, duration gap, hedge ratio, key sensitivities
2. Include **bridges** (market moves, assumption changes, flows, rebalancing)
3. Summarize **forward-looking** metrics: surplus-at-risk, earnings-at-risk (institution-specific)
4. Tie to **capital** and **regulatory** ratios at overview—escalate filings to qualified roles
5. State **limitations** and **basis** in every exhibit footnote

**See `references/alm_reporting_and_metrics.md`.**

## Key metrics (ALM)

| Metric | Typical use |
|---|---|
| Effective / modified duration | Interest rate sensitivity of assets, liabilities, surplus |
| DV01 / PV01 | Dollar change per 1bp parallel shift |
| Key rate duration | Non-parallel yield curve risk |
| Convexity | Second-order rate sensitivity; material for large moves |
| Duration gap | Asset duration − liability duration (definition varies by basis) |
| Funded ratio / surplus ratio | Assets ÷ liabilities or economic surplus measure |
| Hedge ratio | Risk covered by hedges ÷ measured exposure |
| Surplus-at-risk (SaR) | Tail loss on surplus over horizon (method-specific) |
| Net interest income sensitivity | Bank ALM earnings exposure |
| Economic value of equity (EVE) | Bank balance-sheet value sensitivity (overview) |

Always state **measurement basis**, **curve**, and **rebalancing** assumptions.

## Data requests (starter checklist)

When the user has not supplied data, ask for:

1. **Valuation date** and reporting bases (economic, regulatory, accounting, funding)
2. **Liability cash-flow projection** or summary profile (duration, key rates, inflation linkage)
3. **Asset holdings** with classification (government, credit, alternatives, derivatives)
4. **Existing hedge book** (notionals, maturities, counterparties, collateral)
5. **ALM policy** and **risk limits**; prior ALCO materials
6. **Prior stress results** and **capital** model outputs (overview)

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| ALM diagnostic | Objectives, gap analysis, top risks, measurement basis |
| Duration / KRD report | Definitions, curves, asset/liability/surplus sensitivities |
| LDI / hedge proposal | Instruments, hedge ratio, basis risks, implementation phases |
| Stress test summary | Scenarios, surplus/capital impacts, limit breaches, actions |
| ALCO pack | Dashboard, bridges, decisions needed, governance items |
| ALM policy outline | Objectives, limits, roles, review cadence, model standards |

Always state **uncertainty** and **limitations**. Do not present outputs as investment advice, actuarial opinion, regulatory filing, or legal guidance without qualified human review.

## When to load references

- **Scope and principles** → `references/alm_scope_and_principles.md`
- **Interest rate risk and duration** → `references/interest_rate_risk_and_duration.md`
- **LDI, immunization, hedging** → `references/liability_driven_investing.md`
- **Insurance and pension ALM** → `references/insurance_and_pension_alm.md`
- **Stress, scenarios, governance** → `references/stress_scenarios_and_governance.md`
- **Reporting and metrics** → `references/alm_reporting_and_metrics.md`
