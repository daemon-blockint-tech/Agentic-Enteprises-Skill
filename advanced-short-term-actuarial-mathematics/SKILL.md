---
name: advanced-short-term-actuarial-mathematics
description: |
  Guides advanced short-term actuarial mathematics aligned with SOA ASTAM and P&C/health-adjacent
  modeling—severity and frequency distributions, aggregate and compound loss models, Bühlmann and
  Bühlmann-Straub credibility, ratemaking and experience rating, short-term reserving at the math
  level, MLE and goodness-of-fit, and risk measures (VaR, TVaR). Tool-agnostic and concept-first.
  Use when the user mentions advanced short-term actuarial mathematics, ASTAM, severity model,
  frequency model, aggregate loss, compound distribution, Bühlmann credibility, experience rating,
  ratemaking, pure premium, negative binomial frequency, tail factor, TVaR, or short-term actuarial
  models—not life contingencies (life-health-insurance), Excel workpapers only (actuarial-analyst),
  appointed actuary sign-off (actuary, appointed-chief-actuary), assumption governance
  (assumption-setting), P&C legal/operations depth (property-casualty-insurance), or general ML
  (data-scientist, quantitative-researcher).
---

# Advanced Short-Term Actuarial Mathematics

## When to Use

- Select and justify **severity** families (parametric tails, mixtures) and **frequency** models (Poisson, negative binomial, mixtures)
- Build **aggregate loss** models: compound distributions, normal approximation limits, FFT/simulation concepts
- Apply **credibility** (Bühlmann, Bühlmann-Straub, limited fluctuation) and **experience rating** math
- Structure **ratemaking**: pure premium, loss ratio, trend, on-level, indicated change logic
- Explain **short-term reserving** at the mathematical level (chain ladder factors, expected loss ratio)
- Estimate parameters (**MLE**), run **goodness-of-fit** and diagnostics, interpret residuals and tail fit
- Compute **risk measures** (VaR, TVaR) and relate them to capital concepts at a technical level
- Connect modeling choices to **pricing and reserving workflows**; hand execution to `actuarial-analyst`

## When NOT to Use

- Life insurance, annuities, long-term care, or **life contingencies** (mortality, reserves by policy) → `life-health-insurance` or longevity-focused skills
- Triangle workbooks, exhibit production, statutory tie-outs, or model run packs only → `actuarial-analyst`
- Appointed actuary opinions, regulatory sign-off, or enterprise capital policy → `actuary`, `appointed-chief-actuary`
- Enterprise **assumption governance**, assumption papers, and change control → `assumption-setting`
- P&C coverage wording, claims handling, underwriting authority, or DOI filing narrative → `property-casualty-insurance`
- Exam cram or past-exam solutions as the **sole** deliverable (support professional application; exam study is secondary)
- General data science, ML pipelines, or quant research without actuarial loss-model framing → `data-scientist`, `quantitative-researcher`
- Chart design and dashboard craft only → `data-visualization`
- Credential pathway and exam strategy only → `associate-actuary`

## Related skills

| Need | Skill |
|---|---|
| Workpapers, triangles, exhibits, model I/O, analyst QA | `actuarial-analyst` |
| Sign-off, capital overview, governance memos | `actuary` |
| Appointed actuary / chief actuary regulatory framing | `appointed-chief-actuary` |
| ASA/FSO exam pathways and professional standards | `associate-actuary` |
| Assumption governance and enterprise change control | `assumption-setting` |
| P&C lines, underwriting, claims, and policy mechanics | `property-casualty-insurance` |
| Statistical/ML modeling beyond standard actuarial methods | `quantitative-researcher` |
| General ML and predictive pipelines | `data-scientist` |
| Charts, dashboards, and visual design | `data-visualization` |

## Core Workflows

### 1. Problem framing (ASTAM-aligned)

Before fitting distributions:

1. **Horizon** — Short-term (annual or shorter); accident vs calendar year; prospective period for pricing
2. **Random variables** — Severity \(X\), frequency \(N\), aggregate \(S=\sum X_i\); clarify i.i.d. assumptions
3. **Data grain** — Claim-level vs policy-period; censoring/truncation (deductibles, limits)
4. **Deliverable** — Model spec, parameter estimates, diagnostics, business interpretation—not filing sign-off
5. **Peer execution** — Route spreadsheet builds and filing exhibits to `actuarial-analyst`

**See `references/astam_scope_and_principles.md`.**

### 2. Severity and frequency modeling

1. Explore **severity** empirical tail; candidate families (exponential, gamma, lognormal, Pareto, generalized Pareto for tail)
2. Explore **frequency** dispersion; test Poisson vs negative binomial vs mixtures
3. Document **moments**, tail indices, and parameter stability across segments
4. State **dependence** assumptions (usually independence for standard compound model; flag if copula needed → escalate)
5. Summarize **model selection** criteria (AIC/BIC, Anderson–Darling, QQ plots)—not a single automatic pick

**See `references/severity_and_frequency_models.md`.**

### 3. Aggregate and compound losses

1. Define compound model \(S = X_1 + \cdots + X_N\)
2. Apply **normal approximation** when conditions hold; state when it fails (heavy tail, low frequency)
3. Outline **FFT** and **simulation** approaches for discrete/continuous severity (conceptual steps)
4. Relate **percentiles** of \(S\) to risk measures and reinsurance layers (technical only)

**See `references/aggregate_loss_models.md`.**

### 4. Credibility and experience rating

1. Choose **limited fluctuation**, **Bühlmann**, or **Bühlmann-Straub** per homogeneity and data structure
2. Compute **credibility weights** \(Z\); define complement (manual, industry, prior)
3. Blend **observed** experience with complement for pure premium or loss ratio
4. Document **heterogeneity** across classes/years and structural parameters

**See `references/credibility_and_experience_rating.md`.**

### 5. Ratemaking and short-term reserving (math level)

1. **Pure premium** indication: frequency × severity with documented adjustments
2. **Loss ratio** and **on-level** premium; **trend** to prospective period
3. **Indicated change** vs constraints; distinguish technical indication from implemented rate
4. **Reserving**: chain-ladder factor algebra, expected loss ratio method—link full triangle work to `actuarial-analyst`

**See `references/ratemaking_and_trend.md`.**

### 6. Estimation, diagnostics, and risk measures

1. Fit via **MLE** (or method of moments where standard); report standard errors when available
2. Run **goodness-of-fit** and tail diagnostics; document limitations
3. Compute **VaR** and **TVaR** at stated confidence levels; interpret for capital layers (non-regulatory)
4. Package **assumptions**, **alternatives**, and **sensitivity** for actuary review

**See `references/estimation_diagnostics_and_risk_measures.md`.**

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Model specification | Random variables, independence, censoring/truncation, segment definition |
| Parameter table | Estimates, method, uncertainty, stability notes |
| Diagnostics | QQ/PP, GOF tests, tail plot, A/E if applicable |
| Business bridge | Pure premium, credibility blend, indicated change or reserve factor (math only) |
| Limitations | Data volume, tail extrapolation, regime change, outlier treatment |

Label output as **technical modeling support**, not actuarial opinion, legal advice, or filed regulatory submission.

## Assignment type matrix

| Trigger phrase | Primary workflow | Lead reference |
|---|---|---|
| severity model / tail behavior | Severity families and selection | `severity_and_frequency_models.md` |
| frequency model / negative binomial | Frequency and dispersion | `severity_and_frequency_models.md` |
| aggregate loss / compound distribution | Compound \(S\) | `aggregate_loss_models.md` |
| Bühlmann credibility | Credibility weights | `credibility_and_experience_rating.md` |
| experience rating / pure premium | Rating blend | `credibility_and_experience_rating.md` |
| ratemaking / trend / on-level | Indication math | `ratemaking_and_trend.md` |
| chain ladder / ELR (math) | Reserving formulas | `ratemaking_and_trend.md` |
| MLE / goodness-of-fit | Estimation and GOF | `estimation_diagnostics_and_risk_measures.md` |
| VaR / TVaR | Risk measures | `estimation_diagnostics_and_risk_measures.md` |

## When to load references

- **Scope, ASTAM alignment, principles** → `references/astam_scope_and_principles.md`
- **Severity and frequency** → `references/severity_and_frequency_models.md`
- **Aggregate and compound losses** → `references/aggregate_loss_models.md`
- **Credibility and experience rating** → `references/credibility_and_experience_rating.md`
- **Ratemaking, trend, reserving math** → `references/ratemaking_and_trend.md`
- **Estimation, GOF, VaR/TVaR** → `references/estimation_diagnostics_and_risk_measures.md`
