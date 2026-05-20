# ALTAM scope and principles

## Table of contents

1. [Purpose and alignment](#purpose-and-alignment)
2. [Long-term vs short-term](#long-term-vs-short-term)
3. [Core building blocks](#core-building-blocks)
4. [Modeling principles](#modeling-principles)
5. [Boundaries with peer skills](#boundaries-with-peer-skills)
6. [Ethics and reliance](#ethics-and-reliance)

## Purpose and alignment

This reference supports **advanced long-term actuarial mathematics** in the spirit of SOA **ALTAM** (Advanced Long-Term Actuarial Models): stochastic and deterministic models for **life contingencies**, **annuities**, and **pension-adjacent** liabilities where survival, decrements, and long-dated cash flows drive outcomes.

The skill is **tool-agnostic** and **concept-first**. Implementation in R, Python, Excel, Prophet, or vendor valuation systems belongs in `actuarial-analyst` unless the user explicitly wants formulas and interpretation only.

## Long-term vs short-term

| Dimension | Long-term (in scope) | Short-term (out of scope) |
|---|---|---|
| Horizon | Multi-year; lifetime or long benefit payment streams | Annual or shorter; claim development |
| Building blocks | Survival, decrements, APV, reserves | Frequency, severity, aggregate \(S\) |
| Typical products | Life, annuity, pension liability, LTC math | P&C, short-tail health |
| Reserving math | Net/gross premium reserves, Thiele, multi-state | Chain ladder, ELR at formula level |

Route P&C aggregate-loss work to `advanced-short-term-actuarial-mathematics`.

## Core building blocks

Standard **life contingency** setup:

- **Survival** — \(l_x\), \(q_x\), \(p_x\), \(\mu_x\); select vs ultimate tables
- **Benefits** — Death, survival, annuity payments with defined timing (due vs immediate)
- **Discounting** — Interest \(i\) or force \(\delta\); term structures for long liabilities
- **Premiums/reserves** — Equivalence principle; prospective and retrospective balances
- **Decrements** — Death, lapse, disability, retirement in single or multi-state form

**Joint lives** and **last-survivor** benefits extend the state space; **Markov** models generalize decrements.

## Modeling principles

1. **Define the estimand** — APV, net premium, reserve, funded status contribution—not notation alone
2. **State payment timing** — Continuous vs discrete; due vs immediate; fractional year conventions
3. **Document mortality basis** — Table name, year, select period, improvement scale, credibility of experience
4. **Interest and inflation** — Nominal vs real; flat vs curve; alignment with ALM when relevant
5. **Prospective purpose** — Pricing vs valuation vs funding; net vs gross; statutory vs economic (overview)
6. **Reproducibility** — Assumption set ID, table version, and rounding rules for published factors

## Boundaries with peer skills

| Topic | This skill | Peer |
|---|---|---|
| Contingency formulas, survival, reserves at math level | Lead | — |
| Workpapers, exhibits, model runs, filing tie-outs | Concepts only | `actuarial-analyst` |
| Sign-off, capital policy, regulatory opinion | Escalate | `actuary`, `appointed-chief-actuary` |
| Assumption papers and enterprise governance | Escalate | `assumption-setting` |
| Life/health product, underwriting, claims context | Light cross-ref | `life-health-insurance` |
| Pension law, ERISA, fiduciary governance | Escalate | `pension-retirement-funds` |
| LDI, duration, hedge design | High-level cross-ref | `asset-liability-management` |
| ML / non-standard predictors | Escalate | `data-scientist`, `quantitative-researcher` |

## Ethics and reliance

- Present results as **technical modeling** pending actuary review
- Do not substitute for **appointed actuary** statements, **rate filing** adequacy, or **pension actuarial opinion**
- Cite **table vintage**, **improvement uncertainty**, and **small experience** in limitations
- Exam preparation may use this material but should not reduce deliverables to **memorized exam templates** without business context
