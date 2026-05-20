# Selection methodology and judgment

## Table of contents

1. [Selection workflow](#selection-workflow)
2. [Experience-based selection](#experience-based-selection)
3. [Credibility and blending](#credibility-and-blending)
4. [Level, trend, and volatility](#level-trend-and-volatility)
5. [Expert judgment](#expert-judgment)
6. [Coordination with actuary](#coordination-with-actuary)

## Selection workflow

1. **Hypothesis** — What changed in portfolio, market, or regulation?
2. **Evidence** — A/E, external benchmarks, sensitivity of prior assumption
3. **Proposal** — Point estimate or surface (by age, duration, territory)
4. **Challenge** — Independent review, reasonability vs related assumptions
5. **Approval** — Per governance tier
6. **Implementation** — Pack version bump; model regression check

## Experience-based selection

When company data supports the update:

| Step | Action |
|---|---|
| Define population | Match model segments; exclude outliers with footnotes |
| Align basis | Same exposure measure as model (earned premium, member months) |
| Compute A/E | By dimension; investigate interactions before changing |
| Propose change | Level shift, trend change, or table swap |
| Back-test | Apply proposed assumption to holdout period if feasible |

Technical study design and triangle methods → `actuary` (`references/assumptions_experience_studies.md`).

## Credibility and blending

Blend **observed** with **prior** (last approved, manual, industry):

| Approach | Use when |
|---|---|
| **Full credibility** | Exposure exceeds threshold; stable A/E |
| **Partial credibility** | Z-weight on observed; document formula |
| **No credibility** | Use industry or judgment; disclose thin data |

Report **Z**, exposure, and **full credibility threshold** per segment in the assumption paper appendix.

## Level, trend, and volatility

Decompose when decisions depend on it:

| Component | Question |
|---|---|
| **Level** | What is the central best estimate today? |
| **Trend** | How fast does the driver change going forward? |
| **Volatility** | What variability around trend for pricing margin or capital? |

Examples:

- Health morbidity: separate **utilization** trend vs **unit cost** trend
- P&C: separate **loss trend** for severity vs exposure inflation
- Lapse: **base rate** vs **dynamic** sensitivity to rates (ALM coordination)

Avoid double-counting trend in both severity and frequency without documentation.

## Expert judgment

Use judgment when data is insufficient, distorted, or forward-looking:

| Situation | Documentation required |
|---|---|
| New product | Comparable product proxy; ramp-down of judgment over time |
| Regulatory change | Expected behavioral response; range of outcomes |
| One-time event | Exclusion period; phased return to experience |
| Competitive action | Non-repeatable market move |

Judgment overrides should state:

- **Who** approved
- **Why** data was insufficient
- **When** to revisit (trigger or date)
- **Impact** vs data-only alternative

## Coordination with actuary

| This skill owns | `actuary` often owns |
|---|---|
| Assumption register structure and governance | Triangle development, IBNR, indicated rates |
| Pack versioning and approval trail | Technical A/E computation and factor fitting |
| Scenario definitions for governance | Model build, exhibits, regulatory filing detail |

Hand off when the user needs **numerical model output** without assumption documentation—or assumption work without model execution.
