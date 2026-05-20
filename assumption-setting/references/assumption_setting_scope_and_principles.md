# Assumption setting scope and principles

## Table of contents

1. [What assumption setting covers](#what-assumption-setting-covers)
2. [Principles](#principles)
3. [Use-case boundaries](#use-case-boundaries)
4. [Relationship to models](#relationship-to-models)
5. [Ethics and reliance](#ethics-and-reliance)

## What assumption setting covers

**Assumption setting** is the discipline of choosing, documenting, and governing inputs that models treat as fixed for a given run—distinct from **model structure** (formulas, segmentation) and **model execution** (coding, runs).

Typical scope:

| Area | Examples |
|---|---|
| Demographic | Mortality, morbidity, longevity improvement, retirement age |
| Behavioral | Lapse, persistency, withdrawal, renewal, claim reporting |
| Economic | Discount rate, inflation, wage growth, asset returns (ALM) |
| Underwriting / claims | Frequency, severity, development, tail, large loss, cat |
| Expense | Acquisition, maintenance, inflation, overhead allocation |
| Credit / counterparty | Default, recovery, collateral (where modeled) |
| Operational | Utilization caps, benefit limits, reinsurance attachment |

Also includes **strategic and planning** assumptions when they feed actuarial or risk outputs (e.g., new business volume, mix shifts)—not standalone corporate FP&A.

## Principles

1. **Purpose-aligned** — Same driver may differ for pricing vs statutory valuation vs economic capital; document basis explicitly.
2. **Traceable** — Every assumption links to source (study, table, policy, judgment) and approver.
3. **Consistent** — Cross-model dependencies (e.g., trend in price and reserve) reconciled or divergence explained.
4. **Materiality-driven** — Effort scales with impact on decisions and metrics.
5. **Conservative where required** — Regulatory or risk frameworks may bias direction; state framework, do not invent rules.
6. **Transparent judgment** — Overrides require written rationale, not undocumented tweaks.
7. **Versioned** — Effective dates, pack IDs, and change logs for audit replay.

## Use-case boundaries

| Use case | Assumption focus |
|---|---|
| **Pricing / rate indication** | Prospective trend, competitive constraints, profit load, near-term emergence |
| **Reserving / valuation** | Development, tail, PYD sensitivity, case vs IBNR drivers |
| **Capital / solvency** | Stress calibrations, correlation, long-horizon scenarios (overview) |
| **ALM / cash flow** | Interest, crediting, asset defaults, liability cash-flow shapes |
| **Planning / ORSA narrative** | High-level scenario sets; may be less granular than technical packs |

**Not in scope:** legal interpretation of filing requirements, appointed-actuary sign-off, or external audit opinions.

## Relationship to models

```
Data → Assumption pack → Model engine → Outputs → Decisions
         ↑ governance
```

- **Assumption pack** — Versioned bundle consumed by one or more models
- **Model** — Defines how assumptions combine (e.g., frequency × severity)
- **Experience study** — Often inputs to assumption updates; technical execution may sit in `actuary`

When the user only needs triangles, ultimates, or indications without governance documentation, route to `actuary`.

## Ethics and reliance

- Disclose **conflicts** when the same party sets assumptions for both pricing and reserving without independent review
- Flag **one-time events** (pandemic, reform, catastrophe year) affecting experience
- Distinguish **indicated** assumption from **implemented** (commercial or regulatory constraint)
- Refer **legal** and **filing** questions to `commercial-counsel` and qualified humans
- Coordinate **IFRS 17** presentation with `ifrs`; this skill owns assumption documentation, not note wording
