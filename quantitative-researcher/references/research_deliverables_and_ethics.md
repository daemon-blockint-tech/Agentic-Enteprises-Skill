# Research Deliverables and Ethics

## Table of contents

1. [Deliverable types](#deliverable-types)
2. [Notebook and report structure](#notebook-and-report-structure)
3. [Reproducibility](#reproducibility)
4. [Uncertainty communication](#uncertainty-communication)
5. [Research vs advice boundary](#research-vs-advice-boundary)
6. [Data ethics and licensing](#data-ethics-and-licensing)
7. [Peer review checklist](#peer-review-checklist)

## Deliverable types

| Artifact | Audience | Contents |
|---|---|---|
| Research memo | PM, risk, leadership | Question, summary, limitations, no code dump |
| Technical notebook | Quants, reviewers | Full pipeline, charts, tests |
| Signal spec | Engineering / execution | Formula, lag, universe, refresh cadence |
| Backtest pack | IC, risk committee | IS/OOS, costs, bias checklist signed |
| Data manifest | Data eng | Sources, hashes, PIT rules |

Match **detail level** to decision stakes.

## Notebook and report structure

Recommended memo flow:

1. **Executive summary** (5–10 bullets: finding, magnitude, uncertainty, caveats)
2. **Research question** and pre-registered primary metric
3. **Data** (sources, period, universe, known gaps)
4. **Methods** (assumptions, equations at high level)
5. **Results** (tables, CIs, key charts)
6. **Robustness** (grid summary)
7. **Limitations** and **falsifiers**
8. **Appendix** (extra specs, code pointers)

Notebooks: keep **one** logical path; move sweeps to appendix cells or separate notebooks.

## Reproducibility

Minimum package:

- `environment.yml` or `requirements.txt` with **pinned** versions
- **Random seeds** for bootstrap and MC draws
- **Data manifest** (paths or DVC hashes; no secrets in repo)
- **Config file** for parameters (YAML/JSON), not hardcoded toggles
- **Makefile** or single entry command: `make research`

CI optional: smoke test that notebook **executes** on sample data.

## Uncertainty communication

Use language that reflects **epistemic limits**:

| Avoid | Prefer |
|---|---|
| "Will outperform" | "Historical sample showed positive spread with 95% CI [a, b]" |
| "Significant alpha" | "Post-cost spread was X bps/month (t=Y); fragile to cost assumption" |
| "Proven" | "Consistent with hypothesis H over 2000–2020; failed in 2021–2022" |

Always include:

- **Sample size** and **time span**
- **Sensitivity** to key assumptions
- **What would falsify** the conclusion

## Research vs advice boundary

This skill supports **analytical research**, not personalized investment recommendations.

- Do not tailor conclusions to an individual's **financial situation**
- Do not imply **fiduciary** or **suitability** determinations
- Flag when outputs require **compliance** or **legal** review before external distribution
- Separate **historical simulation** from **forward promises**

Stakeholders implement trades under their own governance; research informs, does not direct.

## Data ethics and licensing

- Respect **vendor ToS** and **MNPI** walls (no material nonpublic information)
- Document **personal data** if alt data touches individuals (usually out of scope)
- Cite **academic** and **vendor** sources; do not plagiarize proprietary research
- Store credentials in **secrets manager**, not notebooks

## Peer review checklist

Before circulation:

- [ ] Question and primary metric stated upfront
- [ ] PIT and survivorship addressed
- [ ] Costs and turnover included in backtests
- [ ] Multiplicity / overfitting acknowledged
- [ ] Risk metrics defined with windows
- [ ] Limitations and falsifiers present
- [ ] Reproducibility manifest attached
- [ ] Language avoids advice and certainty overclaim
