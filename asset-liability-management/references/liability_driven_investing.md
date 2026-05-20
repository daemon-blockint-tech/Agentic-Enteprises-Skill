# Liability-driven investing

## Table of contents

1. [LDI objectives](#ldi-objectives)
2. [Cash-flow matching vs duration matching](#cash-flow-matching-vs-duration-matching)
3. [Immunization strategies](#immunization-strategies)
4. [Hedge instruments](#hedge-instruments)
5. [Hedge ratio and implementation](#hedge-ratio-and-implementation)
6. [Basis and reinvestment risk](#basis-and-reinvestment-risk)
7. [Dynamic de-risking and glide paths](#dynamic-de-risking-and-glide-paths)
8. [Implementation phases](#implementation-phases)

## LDI objectives

**Liability-driven investing (LDI)** aligns the asset portfolio structure with **liability risk drivers**—primarily interest rates, inflation, and (where relevant) longevity—rather than maximizing benchmark-relative return in isolation.

Typical goals:

| Goal | Metric / outcome |
|---|---|
| Surplus volatility reduction | Lower \(\sigma(\Delta S)\) for rate shocks |
| Hedge ratio target | % of liability rate risk covered |
| Cash-flow adequacy | Liquidity to pay benefits/claims |
| Funding improvement | Higher funded ratio over time (pensions) |
| Capital efficiency | Lower economic/regulatory capital drag (insurers) |

State whether the mandate is **minimum risk** (pension de-risking) or **return-seeking within surplus risk budget**.

## Cash-flow matching vs duration matching

### Dedicated cash-flow matching

- Hold assets whose **coupons and maturities** align with liability payment schedule
- Strong for **known** fixed cash flows; weak when liabilities are **uncertain** (options, longevity, inflation)

### Duration / factor matching

- Match **duration**, **key rates**, or **factor exposures** rather than each cash flow
- Uses **pooled** instruments (bonds, swaps) with reinvestment of intermediate coupons

| Approach | Strength | Weakness |
|---|---|---|
| Cash-flow ladder | Intuitive, liquidity planning | Reinvestment risk; scale constraints |
| Duration matching | Scalable; works with swaps | Model risk; basis vs liability curve |
| Factor / KRD matching | Handles complex curves | Data and governance heavy |

## Immunization strategies

**Classical immunization** (Redington): match **PV** and **duration** (sometimes convexity) so surplus is insulated to small parallel rate changes.

**Contingent immunization**:

1. Start in **return-seeking** portfolio while surplus cushion exceeds threshold
2. **Trigger** move to immunized portfolio if surplus falls below floor
3. Requires clear **governance** and **execution** playbook

**Horizon matching**:

- As liability horizon shortens, reduce duration of assets (**glide**)
- Coordinate with pension **de-risking** milestones

## Hedge instruments

| Instrument | Use case | ALM notes |
|---|---|---|
| Government bonds | Direct duration; high-quality match | Supply, reinvestment, liquidity |
| Interest rate swaps | Pay-fixed/receive-fixed to adjust duration | Collateral, CSA, counterparty limits |
| Futures / options | Tactical overlay, convexity management | Roll, margin, basis |
| Inflation-linked bonds / swaps | Indexed pensions, real liabilities | Index mismatch (CPI vs RPI) |
| FX forwards | Cross-currency liabilities | Hedge accounting treatment |
| Swaptions / caps / floors | Tail protection, asymmetric payoffs | Cost vs benefit; ALCO approval |

Distinguish **economic hedge** from **accounting hedge** designation—coordinate with finance; not legal advice.

## Hedge ratio and implementation

**Hedge ratio** examples:

\[
HR = \frac{\text{Dollar duration of hedges}}{\text{Dollar duration of liability rate risk}}
\]

or PV-weighted coverage of **key rates**.

Implementation considerations:

1. **Notional** sizing vs **DV01** targeting
2. **Rebalancing** bands (e.g., re-hedge when HR drifts ±5%)
3. **Transaction costs** and **market impact**
4. **Collateral** and **liquidity** under stress
5. **Separate account** vs **pooled** implementation (pensions, insurers)

Document **allowed instruments** and **counterparty** limits in ALM policy.

## Basis and reinvestment risk

**Basis risk**: hedge instrument does not move 1:1 with liability discount rate.

Sources:

- **Credit spread** on liability discount vs **government** hedge
- **OIS/LIBOR/SOFR** convention differences
- **Smoothed** actuarial valuation rates vs market hedges

**Reinvestment risk**: intermediate coupons must be reinvested at unknown future rates—immunization drifts unless rebalanced.

Mitigations:

- Shorter **bucket** ladders for near benefits
- **Key-rate** hedges at long tenors
- **Overlay** swaps with explicit roll policy

## Dynamic de-risking and glide paths

**Glide path** reduces risk as funded status improves or participants age.

Typical triggers:

| Trigger | Action |
|---|---|
| Funded ratio > 105% (example) | Increase LDI allocation |
| Calendar date (plan maturity) | Reduce equity, extend duration |
| Volatility control | Cut risk when realized vol spikes |

Link glide paths to **pension risk transfer** readiness (`pension-retirement-funds`) without duplicating legal structuring.

## Implementation phases

1. **Diagnostic** — duration gap, KRD, surplus sensitivities, basis inventory
2. **Policy** — objectives, limits, permitted instruments, HR targets
3. **Pilot** — partial hedge (e.g., 50% HR) with monitoring
4. **Scale** — full LDI; integrate with manager mandates and benchmarks
5. **Review** — quarterly ALCO; annual policy refresh

Do not specify individual **trades** without user mandate and compliance context—frame as **program design**.
