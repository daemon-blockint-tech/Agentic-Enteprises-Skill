# Data quality, bias, and events

## Table of contents

1. [Coverage and completeness](#coverage-and-completeness)
2. [Bot and inorganic noise](#bot-and-inorganic-noise)
3. [Sample and platform bias](#sample-and-platform-bias)
4. [Language and product drift](#language-and-product-drift)
5. [Shock and event taxonomy](#shock-and-event-taxonomy)
6. [Mitigation playbook](#mitigation-playbook)

## Coverage and completeness

| Check | Signal | Action |
|---|---|---|
| Ingest lag | Timestamp gap vs wall clock | Flag nowcast staleness |
| API quota drops | Volume cliff | Pause forecasts; widen intervals |
| Source outage | Single channel → 0 | Impute vs suppress stratum |
| Dedup failures | Inflated volume | Fix pipeline before re-forecast |

Track **effective sample size** per window; suppress headline index when below threshold.

## Bot and inorganic noise

Detection signals (combine, do not rely on one):

- Repetitive text / template hashes
- Young accounts with burst posting
- Coordinated timing clusters
- Engagement mismatch (views ≫ plausible reach)

**Policy choices:**

- Hard drop suspected bots from index
- Down-weight by bot probability
- Separate **organic** vs **all-in** series for transparency

Document bot rules; changing rules requires index version bump.

## Sample and platform bias

| Bias type | Manifestation | Mitigation |
|---|---|---|
| Platform mix | Twitter vs Reddit shift | Mix-adjust or fixed basket |
| Demographic skew | Age/geo not representative | Weight to census or customer base |
| Selection bias | Only angry customers review | Pair with surveys; strata |
| Survivorship | Deleted posts | Archive at ingest |
| Amplification | Press picks up social | Tag earned media separately |

State **who is not heard** in the index footnote for stakeholder briefs.

## Language and product drift

Monitor:

- Language share shifts (new locale launch)
- Topic model drift (new product names)
- Classifier score distribution shift (prior calibration)

Triggers for **retrain or remap**:

- Population stability index on scores
- Sudden neutral→positive ratio jump without volume story
- Human audit sample failure rate ↑

## Shock and event taxonomy

| Class | Examples | Forecast behavior |
|---|---|---|
| Exogenous shock | Recall, CEO scandal, outage | Widen bands; scenario mode |
| Endogenous spike | Viral campaign (planned) | Annotate; optional exclude from train |
| Data artifact | Crawler bug, double count | Halt publish; fix upstream |
| Regime change | Rebrand, M&A, platform ban | New index version |

Maintain an **event register** with start/end, affected strata, and whether historical restatement is required.

## Mitigation playbook

1. **Detect** — automated QA + human spot checks on volume/velocity anomalies
2. **Classify** — artifact vs organic vs planned
3. **Respond** — suppress, annotate, or scenario-forecast; never hide uncertainty
4. **Review** — post-mortem on bot filter and index formula
5. **Version** — document changes for reproducibility
