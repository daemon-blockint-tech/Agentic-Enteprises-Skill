# Profiling and Quality Rules

## Profiling goals

Profiling answers: **what is in the dataset**, **where it breaks expectations**, and **what must be fixed before use**. Treat profiling as a versioned artifact, not a one-time print statement.

## Structural profile

| Dimension | Checks |
|---|---|
| Volume | Row count, file splits, partition coverage |
| Schema | Column names, order drift vs prior version |
| Types | Inferred vs declared; mixed-type columns |
| Keys | Uniqueness at claimed grain; duplicate key rate |
| Time | Coverage gaps, future dates, timezone consistency |
| Referential | Orphan FKs, unmatched dimension codes |

## Statistical profile (tabular)

For numeric columns:

- Central tendency and spread (mean, median, std, IQR)
- Zero-inflation rate
- Negative values where only positive expected
- Spike detection vs prior period (%, not only absolute)

For categorical columns:

- Cardinality vs expectation
- Rare level concentration (long tail)
- Unknown / OTHER bucket size

For text columns:

- Length distribution
- Regex pattern match rate (email, phone, postal)
- Non-printable character rate

## Column classification

| Class | Typical rules |
|---|---|
| Identifier | Unique, non-null, stable format |
| Foreign key | Exists in parent, null rate bounded |
| Measure | Range, non-negative, unit consistency |
| Dimension | Domain list, no leading/trailing space |
| Date / datetime | Parseable, logical ordering |
| Free text | Length cap, PII scan trigger |
| Derived | Document formula; cross-check to inputs |

## Rule severity model

| Severity | Meaning | Default action |
|---|---|---|
| Blocker | Unusable for stated purpose | Fail pipeline; no publish |
| Warning | Degraded quality | Publish with flag; ticket |
| Info | Observability only | Log only |

## Rule pattern catalog

### Uniqueness

```
COUNT(*) = COUNT(DISTINCT primary_key)  -- at grain G
```

Document composite keys explicitly (e.g., `policy_id + effective_date`).

### Completeness

```
null_rate(column) <= threshold
```

Different thresholds for optional vs required fields.

### Domain / validity

- Enumerated lists (status in {A,B,C})
- Range checks (`0 <= loss_ratio <= 5` with business cap)
- Regex (`^[A-Z]{2}[0-9]{9}$` for internal IDs)

### Consistency (cross-field)

- `effective_date <= expiration_date`
- `paid_amount <= incurred_amount` (unless documented exception)
- `country_code` aligns with `currency` when both present

### Referential integrity

```
child.foreign_key IN parent.primary_key
```

Allow orphan rate threshold with quarantine export.

### Volume and freshness

- Row count within `%` of trailing average
- `max(event_timestamp)` within SLA of clock

### Distribution drift (monitoring)

Compare scrubbed output to prior period:

- PSI or simple bucket shift for key measures
- New categorical levels above rate threshold

## Rule implementation options

| Approach | When |
|---|---|
| SQL assertions in warehouse | Large tables, scheduled jobs |
| Great Expectations / Soda / dbt tests | Team standard, CI integration |
| pandas/polars scripts | Ad hoc files, prototypes |
| Custom YAML rule catalog | Multi-source, shared vocabulary |

Pick one primary framework per pipeline; avoid duplicate conflicting rules.

## Rule documentation template

```yaml
rule_id: CLAIM_AMOUNT_NON_NEGATIVE
severity: blocker
grain: claim_id
description: Incurred amount must be >= 0 unless adjustment_type = 'reversal'
expression: |
  incurred_amount >= 0 OR adjustment_type = 'reversal'
remediation: quarantine to exceptions.claim_amount
owner: claims_data_steward
```

## Profiling outputs

Deliver at minimum:

1. **Profile summary** (HTML/Markdown or notebook export)
2. **Column-level stats** (CSV/Parquet for tooling)
3. **Failed rule summary** with top offending values
4. **Quarantine row extract** (sample + full if small)

## Prioritization

When time-boxed, fix in order:

1. Key integrity and grain errors
2. Blocker domain violations on measures used in models
3. Referential breaks affecting joins
4. Warnings on optional attributes
5. Cosmetic standardization

## Integration with scrub pipeline

```
raw → profile_raw → apply_rules(staging) → quarantine → profile_scrubbed → validate → publish
```

Never publish when blocker count > 0 unless an approved waiver exists on file.
