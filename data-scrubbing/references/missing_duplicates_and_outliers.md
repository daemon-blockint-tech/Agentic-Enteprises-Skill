# Missing Values, Duplicates, and Outliers

## Missing values

### Classify missingness first

| Pattern | Interpretation | Typical action |
|---|---|---|
| MCAR | Random | Simple impute or drop with care |
| MAR | Explained by observed fields | Model-based or group impute |
| MNAR | Related to hidden value | Domain rule; do not blind impute |

Document assumption in scrub charter; escalate structural MNAR to domain owner.

### Treatment options (choose explicitly per column)

| Strategy | Use when | Risk |
|---|---|---|
| Leave null | Optional field; model handles missing | Downstream breakage if undeclared |
| Flag column (`was_imputed`) | Audit trail required | Wider schema |
| Constant sentinel | Legacy compatibility only | Confuses with real values |
| Group statistic impute | Stable categories | Bias if MNAR |
| Forward/back fill | Time series at entity grain | Leakage across entities |
| Drop row | Low volume, invalid grain | Selection bias |
| Business rule fill | Known derivations | Needs sign-off |

**Default**: prefer **flag + impute** over silent fill for fields used in modeling.

### Missing value workflow

1. Report null rate by column and segment (product, region, year)
2. Cross-tab nulls across related fields (co-missing patterns)
3. Select strategy per column with written rationale
4. Apply in reproducible step; quarantine rows that fail derivation
5. Re-profile null rates; attach before/after table

## Duplicates

### Define grain before deduping

Example grains:

- Customer: one row per `customer_id`
- Policy-month: `policy_id` + `calendar_month`
- Claim: `claim_id` (not claim line unless line grain intended)

Deduping at wrong grain destroys information or leaves hidden duplicates.

### Duplicate types

| Type | Detection | Resolution |
|---|---|---|
| Exact duplicate | Hash all columns or business subset | Keep one; log count removed |
| Key duplicate | Same PK, different attributes | Survivorship rules |
| Fuzzy duplicate | Similar name/address | Linkage score + review queue |
| Cross-source duplicate | Same entity, different IDs | Master ID assignment |

### Survivorship rules (deterministic)

When multiple rows share a key, pick winner by ordered criteria:

1. Most recent `updated_at`
2. Source system precedence (e.g., core admin > portal)
3. Most complete record (fewest nulls on critical fields)
4. Manual override table

Document merged-field logic: non-key fields may use `COALESCE` priority list.

### Record linkage (fuzzy)

High-level steps:

1. Standardize blocking keys (soundex, postal, phone digits)
2. Generate candidate pairs within blocks
3. Score pairs (Fellegi-Sunter, ML classifier)
4. Auto-merge above high threshold; queue medium for review
5. Never auto-merge below low threshold

Preserve `source_ids[]` and `match_score` on golden record.

## Outliers

### Distinguish outlier types

| Type | Example | Action |
|---|---|---|
| Data error | Negative age | Fix or quarantine |
| Valid extreme | CAT loss | Keep; optional cap flag |
| Fraud / anomaly | Impossible combo | Route to investigation |
| Structural change | New product mix | Segment; do not global drop |

### Detection methods (use multiple)

- IQR / z-score on log-transformed positives
- Percentile caps (p99.5) for reporting views only
- Business caps (max claim by line of business)
- Multivariate (isolation forest) for anomaly **flags**, not silent drops

### Treatment policies (document one per measure)

| Policy | Effect |
|---|---|
| Investigate | Export to exceptions; no change until reviewed |
| Cap / winsorize | Replace with bound; add `was_capped` flag |
| Exclude from modeling sample | Keep in full ledger |
| Transform | log1p for skew; document inverse for interpretation |

**Never** remove outliers without counts, flags, and approver awareness for material fields.

## Combined workflow diagram

```
Profile nulls → classify → impute/flag/quarantine
       ↓
Profile dupes at grain → survivorship / linkage → golden table
       ↓
Profile distributions → outlier flags → cap/investigate/keep
       ↓
Re-validate keys and rule suite
```

## Metrics to report

| Metric | Formula / note |
|---|---|
| Null rate delta | After − before per column |
| Duplicate rate | `1 - distinct_keys / rows` at grain |
| Rows quarantined | By reason code |
| Outlier flag rate | % rows flagged per measure |
| Imputation rate | % filled per column |

## Handoff notes for modeling

Tell `data-scientist` explicitly:

- Which fields were imputed and how
- Whether outliers were capped or excluded from training slice
- Dedup grain and survivorship order
- Any MNAR concerns on target variable

Tell `actuary` explicitly:

- Whether large losses were capped or segmented
- Triangle completeness after claim dedupe
- Exposure adjustments applied before scrub sign-off
