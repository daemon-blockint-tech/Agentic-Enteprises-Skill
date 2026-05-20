# Standardization and Type Coercion

## Objectives

Standardization makes columns **comparable, joinable, and machine-parseable** without changing business meaning. Coercion applies explicit parse rules; failures go to quarantine—not silent coercion to null.

## Naming conventions

| Element | Convention (example) |
|---|---|
| Column names | `snake_case`, no spaces |
| Booleans | `is_active`, `has_reinsurance` |
| Dates | suffix `_date` (date only) or `_at` (timestamp) |
| IDs | suffix `_id`; never reuse for different entities |
| Amounts | suffix `_amount` + `currency_code` column |

Maintain a **data dictionary** synced with scrub pipeline version.

## Categorical standardization

1. Trim whitespace; collapse internal double spaces
2. Upper or lower case per org standard (often upper for codes)
3. Map synonyms via versioned lookup:

| raw_value | standard_code |
|---|---|
| `Calif.` , `CA` , `california` | `CA` |

4. Route unmapped values to `UNKNOWN` quarantine bucket with count threshold alerts

## Numeric standardization

- Remove thousands separators and currency symbols before parse
- Store amounts as decimal type with explicit scale
- Separate **amount** and **currency**; convert FX in dedicated step with rate table version
- Document unit multipliers (thousands vs units)

## Date and time

| Issue | Fix |
|---|---|
| Mixed formats | Specify `strftime` patterns; try ordered parsers |
| Ambiguous MDY/DMY | Require source metadata or reject |
| Time zone | Normalize to UTC or stated zone; store offset |
| Sentinels (`9999-12-31`) | Map to null or `open_ended` flag |

Validate: `birth_date <= transaction_date` where applicable.

## Boolean coercion

Normalize sentinels to true/false/null:

| Raw | Standard |
|---|---|
| `Y`, `Yes`, `1`, `T` | `true` |
| `N`, `No`, `0`, `F` | `false` |
| ``, `NA`, `Unknown` | `null` |

## Type coercion order

1. Read as string (preserve leading zeros on IDs)
2. Apply ID rules: strip only whitespace; **no** numeric cast for policy numbers with leading zeros
3. Parse dates with explicit formats
4. Parse decimals with locale rules
5. Cast integers only when domain confirms integral
6. Quarantine rows failing parse with `parse_error` reason

## Encoding and file hygiene

- Enforce UTF-8 on export; detect BOM
- Replace curly quotes and non-breaking spaces in text fields
- Normalize line endings in CSV ingestion
- Escape delimiters consistently in outputs

## Geographic and industry codes

Use standard code lists where applicable:

- ISO country / currency
- NAIC / LOB codes (insurance) per org reference
- Postal formats validated by country-specific regex

Keep code tables under version control with effective dates.

## Record linkage prep (standardization for matching)

| Field | Normalization |
|---|---|
| Name | Upper, remove punctuation, token sort optional |
| Address | USPS-style abbreviations if US |
| Phone | E.164 digits only |
| Email | Lower, trim |
| DOB | ISO date |

Do not over-normalize away discriminative tokens needed for match quality.

## Derived fields

Document formulas in scrub spec:

```
earned_premium = written_premium * earned_ratio
```

Validate derived fields against source components on sample.

## Versioning mapping tables

Each lookup CSV/SQL table includes:

- `mapping_version`
- `effective_from` / `effective_to`
- `approved_by`

Pipeline records which mapping version ran.

## Validation after coercion

| Check | Purpose |
|---|---|
| Type assertion | Column dtypes match dictionary |
| Parse failure rate | Below threshold |
| Referential | Codes exist in master |
| Reconciliation | Row sums match control totals |

## Tools (non-prescriptive)

| Tool | Role |
|---|---|
| pandas / polars | File scrub, prototypes |
| SQL `CAST` / `TRY_CAST` | Warehouse staging |
| Great Expectations | Type and parse expectations |
| OpenRefine | Interactive cleanup (export rules to pipeline) |

Promote interactive fixes to scripted steps before production sign-off.

## Anti-patterns

- Casting SSN/policy numbers to float (precision loss)
- Implicit locale in `to_datetime` without format
- Mixing `NULL` and empty string without policy
- Applying global title-case to codes
- Hard-deleting rows that fail parse without quarantine
