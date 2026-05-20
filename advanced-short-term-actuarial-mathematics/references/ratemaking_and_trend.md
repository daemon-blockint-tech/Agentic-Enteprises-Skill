# Ratemaking and trend

## Table of contents

1. [Pure premium ratemaking](#pure-premium-ratemaking)
2. [Loss ratio and balance point](#loss-ratio-and-balance-point)
3. [On-level and trend](#on-level-and-trend)
4. [Indicated rate change](#indicated-rate-change)
5. [Short-term reserving math](#short-term-reserving-math)
6. [Link to analyst execution](#link-to-analyst-execution)

## Pure premium ratemaking

**Pure premium** per exposure unit:

\[
\hat{p} = \hat{\mathrm{E}}[S] / e = \hat{\mathrm{E}}[N] \cdot \hat{\mathrm{E}}[X] / e
\]

or credibility-weighted:

\[
\hat{p}_Z = Z \cdot \hat{p}_{\text{obs}} + (1-Z) \cdot p_{\text{manual}}
\]

Document:

- Exposure definition (car-year, $1,000 payroll, etc.)
- Loss basis (paid, incurred, reported)
- Reinsurance and large-loss treatment

## Loss ratio and balance point

**Loss ratio** \(LR = L / P\) (losses over premium).

**Balance point** rate change (conceptual, no expenses):

\[
\text{Indicated factor} \approx \frac{LR_{\text{target}}}{LR_{\text{experience on-level trended}}}
\]

Expense-loaded indications add **fixed** and **variable** expense ratios and profit provisions—state formula explicitly.

| Component | Typical inclusion |
|---|---|
| Expected losses | Credibility-weighted |
| Expenses | UW, LAE, other |
| Profit / contingency | Risk load |

## On-level and trend

| Adjustment | Purpose |
|---|---|
| **On-level** | Restate historical earned premium to **current** rate manual level |
| **Loss trend** | Project historical losses to **prospective** period |
| **Excess trend** | Large-loss or limit changes |

**On-level factor** for year \(t\):

\[
OLF_t = \frac{\text{current rate level}}{\text{rate level in year }t}
\]

**Trend** (compound):

\[
TF = (1 + \tau)^{(t_{\text{pros}} - t_{\text{base}})}
\]

Document index choice (CPI, industry, internal) and **from/to** dates.

Sensitivity: ±1 point annual trend on indicated change when material.

## Indicated rate change

Present:

1. **Gross** experience indication
2. **Credibility-weighted** indication
3. **Constraints** (caps, floors, competitive) — note but do not treat as actuarial necessity
4. **Implemented** rate — operational; may differ from indication

\[
\text{Indicated change} = \frac{\hat{p}_Z}{p_{\text{current}}} - 1
\]

or loss-ratio equivalent.

## Short-term reserving math

At **mathematical** level (full triangles → `actuarial-analyst`):

**Chain ladder** (volume-weighted age-to-age factor):

\[
\hat{f}_j = \frac{\sum_i C_{i,j+1}}{\sum_i C_{i,j}}
\]

Ultimate for origin \(i\):

\[
\hat{U}_i = C_{i,n} \cdot \hat{f}_j \cdots \hat{f}_{n-1}
\]

**Expected loss ratio (ELR)** method:

\[
\hat{U}_i = \text{Earned premium}_i \times ELR_{\text{selected}}
\]

**Bornhuetter–Ferguson** blends ELR prior with observed development—state weighting conceptually.

**Tail factor** — extension beyond last observed age; sensitivity critical for long-tail lines.

Relate **IBNR** to ultimate minus reported/paid at valuation date—do not conflate with severity model IBNR noise in pricing data.

## Link to analyst execution

| Math topic | Analyst deliverable |
|---|---|
| Credibility blend | Rating exhibit with \(Z\), complement |
| Trend/on-level | Factor worksheet with dates |
| CL / ELR | Triangle, factors, ultimates, diagnostics |
| Indicated change | Summary table for actuary memo |

This skill supplies **formulas and interpretation**; `actuarial-analyst` supplies **workpapers and tie-outs**.
