# Sensitivity, scenarios, and stress

## Table of contents

1. [Purpose and materiality](#purpose-and-materiality)
2. [Sensitivity testing](#sensitivity-testing)
3. [Scenario design](#scenario-design)
4. [Stress and reverse stress](#stress-and-reverse-stress)
5. [Correlation and ordering](#correlation-and-ordering)
6. [Reporting standards](#reporting-standards)

## Purpose and materiality

Sensitivities and scenarios support:

- **Governance** — Show robustness of decisions before approval
- **Risk** — ORSA, risk appetite, board narrative (overview)
- **Pricing** — Margin adequacy under adverse drivers
- **Reserving** — Reasonability of central estimate

Start from **materiality** (from prior runs or one-way shocks) to limit grid size.

## Sensitivity testing

### One-way sensitivities

| Practice | Guidance |
|---|---|
| Shock size | Meaningful but plausible (e.g., ±10% trend, +100 bps rates) |
| Metric | Same output metric as decision (ultimate LR, reserve, PV surplus) |
| Label | Clear driver name; avoid ambiguous "stress 1" |
| Base | Locked central assumption pack |

### Tornado / ranking

Rank drivers by **absolute impact** on target metric; focus documentation on top 3–5.

### Interaction (selective)

Test **key pairs** only when interaction is material (e.g., lapse × crediting rate).

## Scenario design

| Scenario type | Typical use |
|---|---|
| **Base** | Approved central assumptions |
| **Adverse** | Combined worsening of material drivers |
| **Favorable** | Upside for pricing competitiveness checks |
| **Regulatory / prescribed** | Framework-defined stresses (overview only) |
| **Historical** | Replay of past shock years where relevant |

### Scenario narrative

Each scenario document should list:

- **Assumption overrides** (table vs base)
- **Rationale** (macro narrative, combined plausibility)
- **Metrics** impacted
- **Limitations** (not exhaustive of all risks)

## Stress and reverse stress

**Stress testing** — Push drivers beyond plausible one-ways to find breaking points (capital, liquidity, reinsurance exhaustion).

**Reverse stress** — Identify scenarios that breach constraint (e.g., RBC ratio, internal limit); work backward to required assumption combination.

Do not invent regulatory stress parameters; reference internal or public framework and mark **verify with compliance/actuary**.

## Correlation and ordering

State explicitly:

- **Independent** one-ways vs **joint** scenario
- **Ordering** if scenarios applied sequentially (e.g., shock then recalc dynamic lapse)
- **Consistent** economic paths (rates and inflation) when combined

Avoid double-counting the same economic shock in multiple assumption lines.

## Reporting standards

Minimum sensitivity exhibit:

| Column | Content |
|---|---|
| Driver | Assumption name |
| Shock | Definition (+25% morbidity trend, etc.) |
| Base metric | Central output |
| Stressed metric | Output under shock |
| Delta | Absolute and % change |

For scenarios, add **scenario ID**, **description**, and **assumption override manifest** linked to pack version.

Sensitivities support decisions; they are not substitutes for **capital model validation** or **appointed-actuary** work.
