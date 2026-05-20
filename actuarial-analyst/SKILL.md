---
name: actuarial-analyst
description: |
  Guides hands-on actuarial analyst work for insurance, reinsurance, and pension—reserving and loss
  development (IBNR, triangles, chain-ladder diagnostics), pricing and rate indication support
  (experience, trend, credibility, basic GLM at spec level), data validation and model I/O review,
  reporting packs and workpapers, assumption application under actuary direction, and statutory
  tie-outs at analyst depth. Use when the user mentions actuarial analyst, loss development, IBNR,
  reserve analysis, rate indication, pricing support, actuarial workpaper, triangle analysis,
  credibility, experience study, actuarial reporting, or reserve roll-forward—not actuary sign-off
  (actuary), consulting engagements (actuarial-consulting), assumption governance (assumption-setting),
  ALM strategy (asset-liability-management), P&C legal depth (property-casualty-insurance), charts only
  (data-visualization), or ETL-only pipelines (data-scrubbing).
---

# Actuarial Analyst

## When to Use

- Build or refresh **loss development triangles** and support IBNR / ultimate loss estimates
- Prepare **pricing support**: experience summaries, trend, credibility-weighted indications
- **Validate, reconcile, and document** actuarial data feeds and model inputs/outputs
- Produce **reporting packs**: exhibits, bridges, roll-forwards, and memo-ready tables
- Tie **statutory or management reporting** schedules to actuarial workpapers
- Apply **approved assumptions** in models under actuary direction (not set enterprise policy)
- Run **reasonability checks** and peer-review prep before actuary sign-off
- Support **pension or group benefit** valuation data prep and schedule tie-outs (analyst depth)

## When NOT to Use

- Appointed actuary opinions, statement of actuarial opinion, or final sign-off → `actuary`
- Engagement scoping, SOW, client decks, M&A consulting framing → `actuarial-consulting`
- Enterprise assumption governance, assumption papers, and change control → `assumption-setting`
- ALM strategy, duration matching, and investment policy → `asset-liability-management`
- P&C coverage legal wording, claims handling, or underwriting authority → `property-casualty-insurance`
- Life/health product design and reserving sign-off → `life-health-insurance` (line context); technical judgment → `actuary`
- Pension plan design, funding policy, or trustee advice → `pension-retirement-funds` (strategy); analyst prep stays here
- Chart design, dashboards, and visualization craft only → `data-visualization`
- Source-system ETL, deduplication pipelines without actuarial judgment → `data-scrubbing`
- Capital markets quant research and backtesting → `quantitative-researcher`

## Related skills

| Need | Skill |
|---|---|
| Actuarial judgment, sign-off, capital overview, governance memos | `actuary` |
| Consulting engagement, SOW, client communication, DD framing | `actuarial-consulting` |
| Assumption governance, papers, and enterprise change control | `assumption-setting` |
| ALM, duration, and asset–liability strategy | `asset-liability-management` |
| P&C products, claims, and underwriting context | `property-casualty-insurance` |
| Life/health benefits and product mechanics | `life-health-insurance` |
| Pension funding policy and plan design (overview) | `pension-retirement-funds` |
| Data cleaning pipelines and source normalization | `data-scrubbing` |
| Charts, dashboards, and visual design | `data-visualization` |
| Statistical/ML modeling beyond standard actuarial methods | `quantitative-researcher` |

## Core Workflows

### 1. Task intake and scope (analyst)

Before opening triangles or models:

1. **Assignment type** — Reserving, pricing support, reporting tie-out, model run, data prep
2. **Basis** — Statutory, GAAP, IFRS 17, management; valuation date and cutoff
3. **LOB and segment** — Direct vs assumed; reinsurance netting rules
4. **Deliverable** — Exhibit list, workpaper IDs, deadline, reviewer (actuary name if known)
5. **Source of truth** — Prior memo, approved assumptions version, model build ID
6. **Out of scope** — Flag sign-off, legal interpretation, or assumption changes needing `actuary` / `assumption-setting`

**See `references/actuarial_analyst_scope.md`.**

### 2. Reserving and loss development

1. Pull **paid, incurred, case**, and count triangles by origin and development age
2. Run **diagnostics** (factor stability, calendar-year check, paid/incurred divergence)
3. Apply selected methods (chain ladder, BF, Cape Cod) per actuary instruction—document picks and alternatives
4. Build **IBNR** and ultimate tables; reconcile to prior evaluation
5. Prepare **PYD bridge** and reserve roll-forward exhibits
6. Escalate tail, cat, or large-loss treatment questions to actuary

**See `references/reserving_and_loss_development.md`.**

### 3. Pricing and rate indication support

1. Aggregate **experience** by segment (exposure, frequency, severity, pure premium)
2. Compute **trend** and on-level adjustments per documented methodology
3. Apply **credibility** weights as specified; show gross vs credibility-weighted indications
4. Summarize **indicated rate change** vs current; tie to loss ratio targets if provided
5. Document **data cuts**, outliers, and one-time events in a support schedule
6. Outline **GLM or multivariate** specs for actuary or modeler—do not present as final model without review

**See `references/pricing_and_rate_indication.md`.**

### 4. Data validation and model I/O

1. Reconcile **premium, exposure, and claim** feeds to control totals
2. Validate **triangle dimensions**, accident/valuation dates, and duplicate keys
3. Compare **model inputs** to source exhibits; log exceptions with $ impact where possible
4. Review **model outputs** for reasonability vs prior run and plan metrics
5. Archive **run logs**, parameter files, and data cut manifests for audit trail
6. Route **assumption changes** to actuary; do not alter approved assumption tables without approval

**See `references/data_validation_and_model_io.md`.**

### 5. Reporting and workpapers

1. Build **exhibit index** aligned to filing or management pack structure
2. Produce **bridges** (reserve change, premium earned, claim counts) with footnoted definitions
3. Tie **external schedules** (statutory blanks, management reports) to internal workpapers
4. Draft **memo support tables** (facts and exhibits)—not full executive narrative unless asked
5. Version files: `YYYYMMDD_basis_LOB_vNN` with change log tab or README row

**See `references/reporting_and_workpapers.md`.**

### 6. Quality review and documentation

1. Complete **analyst checklist** before actuary review (below)
2. Ensure **formulas trace** and no hard-coded plugs without comment
3. Cross-foot **subtotals** and tie to GL or bordereaux where required
4. List **open items** with owner and target date
5. Package **review folder**: inputs, outputs, diagnostics, reconciliation, change log

**See `references/quality_review_and_documentation.md`.**

## Analyst checklist (before actuary review)

```
Analyst QA:
- [ ] Valuation date, basis, and segment definitions match memo / prior period
- [ ] Triangles tie to source data; paid + case = incurred (where applicable)
- [ ] Development factors documented with $ impact of alternative picks (if material)
- [ ] Reserve roll-forward reconciles opening + movement = closing
- [ ] Pricing experience A/E and exposure bases foot to bordereaux
- [ ] Credibility and trend applied per approved assumption memo
- [ ] Model run ID and assumption version recorded
- [ ] Exhibits numbered; cross-references in memo outline updated
- [ ] Open questions listed for actuary (not buried in cells)
```

## Key metrics (analyst must define each time)

| Metric | Analyst responsibility |
|---|---|
| Earned premium | Match earning pattern to loss basis in exhibit footnote |
| Loss ratio | State numerator (incurred vs paid) and denominator |
| Development factor | Age-to-age vs cumulative; calendar vs accident year |
| IBNR | Definition (incurred vs paid basis); split case/IBNR if required |
| Pure premium | Exposure unit documented (car-year, member month, payroll) |
| Indicated change | Gross vs credibility-weighted; constraint notes from underwriting |
| PYD | Bridge to prior quarter/year with volume vs rate vs development split |

## Tool patterns (agnostic)

| Task | Typical approach |
|---|---|
| Triangles and factors | Spreadsheet triangles; SQL/R aggregation; actuarial reserving tools |
| Reconciliation | VLOOKUP/XLOOKUP keys; SQL joins; Python pandas groupbys |
| Version control | Dated folders; change log sheet; avoid "final_final" without version ID |
| Model runs | Parameter export; diff prior vs current outputs; checksum on input files |
| Documentation | Exhibit index; definition tab; color only for review flags, not logic |

Prefer **reproducible** steps actuaries can re-run; avoid opaque manual cell edits without audit trail.

## Line-of-business notes (analyst)

| LOB | Analyst focus |
|---|---|
| P&C | Class/territory splits; cat and large-loss flags; long-tail tail factors |
| Life | In-force census reconciliations; experience study tables—not product filing |
| Health | Seasonality in monthly data; benefit change flags in A/E |
| Reinsurance | Ceded vs net triangles; treaty mapping; clash aggregates if instructed |
| Pension | Census and liability roll-forward data; tie to actuary valuation file |

## Deliverable standards (analyst)

| Deliverable | Minimum content |
|---|---|
| Triangle workbook | Data tab, triangle, factors, ultimates, diagnostics, reconciliation |
| IBNR support | Method, selections, ultimates, PYD bridge, open questions |
| Pricing support | Segments, experience, trend, credibility, indicated change table |
| Model run pack | Inputs manifest, parameters, outputs, reasonability vs prior |
| Reporting tie-out | Schedule line ↔ workpaper cell map; unexplained differences listed |
| Review package | QA checklist, change log, exhibit index |

State **limitations** (data gaps, one-time events, immature years). Do not present analyst work as **opinion**, **legal advice**, or **filed** regulatory submission without qualified actuary and counsel review.

## Assignment type matrix

| Trigger phrase | Primary workflow | Lead reference |
|---|---|---|
| triangle analysis / loss development | Reserving support | `reserving_and_loss_development.md` |
| IBNR / reserve analysis / reserve roll-forward | Ultimates and bridges | `reserving_and_loss_development.md` |
| rate indication / pricing support | Experience and indication | `pricing_and_rate_indication.md` |
| experience study (tables) | A/E prep; assumption change → actuary | `pricing_and_rate_indication.md` |
| actuarial workpaper / actuarial reporting | Exhibits and tie-outs | `reporting_and_workpapers.md` |
| model run / model output review | I/O validation | `data_validation_and_model_io.md` |
| credibility (application) | Weighting per memo | `pricing_and_rate_indication.md` |

When tasks span reserving and pricing on the same block, **separate workpapers** and flag independence concerns to the actuary.

## Ethics and reliance (analyst)

- Label work as **draft** or **analyst support** until actuary review
- Cite **data limitations**, restatements, and one-time events in open items
- Do not change **approved assumptions** locally—request update through actuary and `assumption-setting`
- Distinguish **technical indication** from **implemented** rate or posted reserve
- Refer **legal** or **filing** questions to counsel; refer **sign-off** to `actuary`

## When to load references

- **Scope, boundaries, ethics** → `references/actuarial_analyst_scope.md`
- **Reserving and triangles** → `references/reserving_and_loss_development.md`
- **Pricing and indication** → `references/pricing_and_rate_indication.md`
- **Data and model I/O** → `references/data_validation_and_model_io.md`
- **Reporting and workpapers** → `references/reporting_and_workpapers.md`
- **QA and documentation** → `references/quality_review_and_documentation.md`
