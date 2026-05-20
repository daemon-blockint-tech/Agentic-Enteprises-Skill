# Data Scrubbing — Scope and Workflow

## Purpose

Data scrubbing prepares **analysis-ready** tabular data: consistent types, trustworthy keys, documented transformations, and measurable quality. It sits **after** extraction and **before** modeling, BI, or regulatory submissions—not at warehouse platform design.

## In scope

| Activity | Outcome |
|---|---|
| Structural profiling | Null rates, cardinality, type inference, pattern samples |
| Rule definition | Uniqueness, domain, referential, volume, cross-field logic |
| Remediation | Missing, duplicate, outlier, encoding, standardization |
| Record linkage | Deterministic + probabilistic dedupe with match scores |
| Pipeline documentation | Config, version, inputs/outputs, quarantine tables |
| Validation & sign-off | Rule results, thresholds, approver attestation |

## Out of scope (route to peers)

| Activity | Peer skill |
|---|---|
| Star schema, SCD, incremental warehouse loads | `data-warehouse-engineer` |
| Algorithm selection, training, hyperparameters | `data-scientist` |
| Triangle fitting, IBNR, credibility | `actuary` |
| SOC 2 evidence, legal privacy program | `compliance-engineer` |

## End-to-end workflow

```
Intake → Profile → Rule catalog → Remediate (iterative) → Validate → Sign-off → Handoff
```

### Phase 1 — Intake

Capture in a one-page scrub charter:

- **Sources**: files, tables, APIs; refresh cadence
- **Grain**: one row per what (transaction, policy-month, claim)
- **Keys**: natural vs surrogate; composite keys
- **Consumers**: analyst, actuary, ML, regulator
- **Constraints**: immutability of raw layer, retention, PII policy
- **Success metrics**: max null rate, duplicate rate, rule pass rate

### Phase 2 — Profile (baseline)

Minimum profile artifacts:

1. Row count and byte size
2. Per-column: type, null %, distinct count, top values (capped)
3. Numeric: min, max, mean, percentiles (as appropriate)
4. Date: min, max, future-dated count
5. Text: max length, encoding issues, leading/trailing whitespace rate

Store baseline profile with dataset version ID.

### Phase 3 — Rule catalog

For each rule assign:

| Field | Example |
|---|---|
| `rule_id` | `POLICY_KEY_UNIQUE` |
| `severity` | `blocker` / `warning` |
| `expression` | SQL, Great Expectations, or pseudocode |
| `owner` | data steward name |
| `remediation` | quarantine, fix script, manual ticket |

### Phase 4 — Remediate (iterative)

Order of operations (default—adjust when domain requires):

1. Encoding and delimiter fixes
2. Type coercion and parsing quarantine
3. Standardization (codes, units, time zones)
4. Key construction and referential fixes
5. Duplicate resolution / linkage
6. Missing value treatment
7. Outlier treatment (last—after types stable)

Log every transformation in a **change log** table: `step`, `rows_in`, `rows_out`, `rows_quarantined`, `timestamp`.

### Phase 5 — Validate

Re-run full rule suite on scrubbed output. Compare to baseline profile:

- Unexpected null spikes
- Cardinality collapse (over-deduping)
- Distribution shift beyond agreed tolerance

### Phase 6 — Sign-off

Sign-off package (minimum):

1. Scrub charter (updated)
2. Rule catalog with final pass rates
3. Validation report (blockers = 0 unless waived)
4. Pipeline artifact hash / git commit
5. Sample row diff (before vs after) for critical fields
6. Named approver and date

**Waivers**: document rule ID, business justification, expiry, and compensating control.

## Reproducibility requirements

- Pin random seeds where imputation or sampling is used
- Store mapping tables (e.g., state code → region) in version control
- Parameterize paths and dates; no hard-coded production secrets
- Separate **raw**, **staging scrub**, and **published** zones when possible

## Handoff checklist

Before passing to `data-scientist` or `actuary`:

- [ ] Grain documented and verified
- [ ] Primary keys unique at stated grain
- [ ] Critical measures non-null above threshold
- [ ] Date fields parsed and time zone documented
- [ ] PII minimized per policy
- [ ] Validation report attached
- [ ] Known limitations listed (coverage gaps, manual fixes)

## Anti-patterns

- Scrubbing in the only copy of production data without backup
- Dropping rows without quarantine or counts
- Changing keys without lineage to source records
- One-off Excel edits without reproducible pipeline
- Mixing scrub and model training in the same undocumented notebook cell block
