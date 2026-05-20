# ASTAM scope and principles

## Table of contents

1. [Purpose and alignment](#purpose-and-alignment)
2. [Short-term vs long-term](#short-term-vs-long-term)
3. [Core random structures](#core-random-structures)
4. [Modeling principles](#modeling-principles)
5. [Boundaries with peer skills](#boundaries-with-peer-skills)
6. [Ethics and reliance](#ethics-and-reliance)

## Purpose and alignment

This reference supports **advanced short-term actuarial mathematics** in the spirit of SOA **ASTAM** (Advanced Short-Term Actuarial Models): stochastic models for **non-life** and **short-duration** health-adjacent coverages where claim counts and severities drive aggregate outcomes.

The skill is **tool-agnostic** and **concept-first**. Implementation in R, Python, Excel, or vendor tools belongs in `actuarial-analyst` unless the user explicitly wants formulas and interpretation only.

## Short-term vs long-term

| Dimension | Short-term (in scope) | Long-term (out of scope) |
|---|---|---|
| Horizon | Annual or shorter policy/claim development | Multi-year life reserves, mortality tables |
| Building blocks | Frequency, severity, aggregate \(S\) | Life contingencies, survival models |
| Typical lines | P&C, short-tail health, group AD&D-style | Life, annuity, LTC |
| Reserving math | CL factors, ELR at formula level | Long-duration liability models |

Route life/contingency work to `life-health-insurance` and qualified actuary review.

## Core random structures

Standard **collective risk** setup:

- **Severity** \(X\) — payment per claim (possibly censored/truncated by deductible/limit)
- **Frequency** \(N\) — claim count in a period (often Poisson or negative binomial)
- **Aggregate** \(S = X_1 + \cdots + X_N\) with \(N\) independent of \(\{X_i\}\) unless modeling dependence explicitly

**Policy** random variables (per-policy frequency/severity) appear in some curricula; default to collective model unless data structure requires otherwise.

## Modeling principles

1. **Define the estimand** — Pure premium, loss ratio, percentile of \(S\), IBNR factor—not “the model” in isolation
2. **Document censoring/truncation** — Deductibles and limits change the effective severity distribution
3. **Segment homogeneity** — Split classes before fitting; credibility handles partial pooling later
4. **Tail honesty** — Parametric tails extrapolate; justify with diagnostics and sensitivity
5. **Prospective vs retrospective** — Trend and on-level bridge historical experience to future periods
6. **Reproducibility** — State data cuts, exclusion rules, and random seeds for simulation

## Boundaries with peer skills

| Topic | This skill | Peer |
|---|---|---|
| Distribution theory, compound models, credibility formulas | Lead | — |
| Triangle exhibits, workpapers, filing tie-outs | Concepts only | `actuarial-analyst` |
| Sign-off, capital policy, regulatory opinion | Escalate | `actuary`, `appointed-chief-actuary` |
| Assumption papers and governance | Escalate | `assumption-setting` |
| P&C product and claims context | Light cross-ref | `property-casualty-insurance` |
| ML / non-standard predictors | Escalate | `data-scientist`, `quantitative-researcher` |

## Ethics and reliance

- Present results as **technical modeling** pending actuary review
- Do not substitute for **appointed actuary** statements or **rate filing** legal adequacy
- Cite **data limitations**, regime changes, and immature years in limitations
- Exam preparation may use this material but should not reduce deliverables to **memorized exam templates** without business context
