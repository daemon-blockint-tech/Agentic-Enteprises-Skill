# Actuarial and insurance visualization

## Table of contents

1. [Audience and rigor](#audience-and-rigor)
2. [Loss development triangles](#loss-development-triangles)
3. [Trend and experience panels](#trend-and-experience-panels)
4. [Distributions and large losses](#distributions-and-large-losses)
5. [Scenarios and sensitivity](#scenarios-and-sensitivity)
6. [Coordination with actuarial skills](#coordination-with-actuarial-skills)
7. [Regulatory and external reporting](#regulatory-and-external-reporting)

## Audience and rigor

| Audience | Viz emphasis | Language |
|---|---|---|
| Actuaries | Triangles, link ratios, A/E | Technical labels, development basis |
| Finance / CFO | Ultimate trends, variance bridges | Tie to plan and prior forecast |
| Underwriting | Loss ratio by segment, cat exposure | Exposure-normalized rates |
| Board / regulator | Material drivers, ranges | Definitions, governance footnotes |

Never simplify away **basis** (accident year vs underwriting year vs calendar year).

## Loss development triangles

### Standard heatmap triangle

- **Rows**: accident (or underwriting) period
- **Columns**: development age (12, 24, 36 months…)
- **Cell value**: incurred, paid, or case outstanding—state which
- **Color**: magnitude; use sequential scale; label diagonal and latest column

### Link ratio triangle

- Show **age-to-age** factors adjacent to dollars triangle or on separate tab
- Highlight volatile cells with annotation, not only color

### Annotations

- Mark **large losses** or one-time events in footnotes
- Note **restatements** and valuation date
- Distinguish **gross vs net of reinsurance**

Technical fitting and selection belong to `actuary`; this skill covers **layout and labeling**.

## Trend and experience panels

| Panel | Typical encoding | Notes |
|---|---|---|
| Loss ratio over time | Line by AY or UY | Show earned premium denominator change |
| Frequency / severity | Dual small multiples | Prefer two panels over dual axis |
| A/E vs expected | Bar or dot vs 1.0 reference | Show credibility / volume weight |
| Claim count development | Column by report lag | Watch reporting delay bias |
| Reserve walk | Waterfall | Bridge beginning → movement → ending |

Always show **volume** (exposure, claim count) alongside rates.

## Distributions and large losses

- **Histogram** of claim size: log x-axis often required; cap axis with disclosure
- **Pareto** view: cumulative % of loss vs % of claims
- **CAT** events: separate layer or annotation; do not smooth into trend
- **Outliers**: table appendix with policy/claim IDs per governance rules

For tail risk, prefer **exceedance curve** or **return period** chart with explicit modeling source.

## Scenarios and sensitivity

| Display | Use when |
|---|---|
| Tornado chart | Few drivers, single output metric |
| Small multiples by scenario | Comparing shapes across assumptions |
| Fan chart | Time series with interval forecasts |
| Table of scenarios | Audit and regulator packs |

Rules:

- Label **assumption set** version; link to `assumption-setting`
- Show **ranges**, not false point estimates
- Separate **best estimate** from **stress** visually

## Coordination with actuarial skills

| Topic | Partner skill |
|---|---|
| Triangle mechanics, IBNR, ultimates | `actuary` |
| Assumption packs and governance | `assumption-setting` |
| Consulting deliverables and opinions | `actuarial-consulting` |
| ALM and duration (if balance-sheet lens) | `asset-liability-management` |
| Narrative for non-technical execs | `storytelling` |

## Regulatory and external reporting

- Match **prescribed layouts** when filings mandate forms
- Include **methodology** footnotes and data sources
- Suppress small cells per confidentiality rules; document suppression
- Version charts with **model run ID** and **assumption effective date**

Charts support filings; legal wording and sign-off sit outside this skill.
