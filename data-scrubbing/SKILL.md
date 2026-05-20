---
name: Data Scrubbing
description: |
  Guides cleaning and standardizing tabular datasets before analysis, modeling, or reporting—profiling,
  quality rules, missing values, duplicates, outliers, type coercion, encoding fixes, record linkage,
  deduplication, high-level PII handling (not legal advice), actuarial/insurance field scrubbing,
  reproducible scrub pipelines, validation checks, and sign-off. Distinct from warehouse ETL or
  statistical modeling. Use when the user asks for "data scrubbing", "clean this dataset", "scrub the
  data", "data cleaning", "dedupe records", "handle missing values", "outlier treatment",
  "standardize columns", "data quality rules", "profile this table", or "prepare data for modeling".
  Not warehouse pipelines (data-warehouse-engineer), ML modeling (data-scientist, actuary), privacy
  programs (compliance-engineer), FinOps only (finops-analyst), or assumption governance
  (assumption-setting).
---

# Data Scrubbing

## When to Use

- Profile a table or file and define data-quality rules before analysis or modeling
- Clean, standardize, dedupe, or link records in CSV, Parquet, SQL extracts, or notebook pipelines
- Treat missing values, duplicates, outliers, types, encodings, and column naming consistently
- Document a reproducible scrub pipeline with validation checks and sign-off criteria
- Scrub actuarial/insurance fields (policy keys, claims triangles, exposure bases) for downstream reserving or pricing prep
- Flag or redact PII at a technical level before sharing extracts (coordinate with compliance for legal requirements)

## When NOT to Use

- Star/snowflake modeling, warehouse ETL/ELT, CDC, or platform ingestion design → `data-warehouse-engineer`
- Predictive modeling, A/B tests, causal inference, feature engineering for ML, or MLOps → `data-scientist`
- Loss development, IBNR, pricing models, or appointed-actuary sign-off → `actuary`
- Assumption sets, governance memos, or model assumption workshops → `assumption-setting`
- SOC 2 / ISO control mapping, audit evidence automation, or privacy legal program → `compliance-engineer`
- Cloud cost allocation, FinOps dashboards, or unit economics only → `finops-analyst`
- Spreadsheet formula integrity or cell-level model audit without a scrub pipeline → `audit-xls` (if available)

## Related skills

| Need | Skill |
|---|---|
| Dimensional modeling, ETL/ELT, warehouse SQL performance | `data-warehouse-engineer` |
| ML modeling, experiments, production model monitoring | `data-scientist` |
| Reserving, triangles, IBNR, pricing actuarial methods | `actuary` |
| Assumption documentation and governance | `assumption-setting` |
| Technical compliance controls and audit evidence | `compliance-engineer` |
| Cloud spend attribution and cost optimization | `finops-analyst` |
| Enterprise data governance and catalog design | `data-architect` |
| Analytics engineering (dbt layers, mart tests) | `analytics-data-engineer` |

## Core Workflows

### 1. Intake and scope

1. Identify source(s), grain, primary keys, and downstream consumer (report, model, regulatory filing)
2. Record business definitions for critical fields and acceptable quality thresholds
3. Choose deliverables: scrubbed dataset, rule catalog, pipeline code, validation report, sign-off checklist
4. Confirm what must **not** change (audit trail, raw landing zone immutability)

**See `references/data_scrubbing_scope_and_workflow.md`.**

### 2. Profile and define quality rules

1. Run structural profile: row/column counts, types, null rates, cardinality, min/max, patterns
2. Classify columns: identifier, measure, dimension, date, free text, PII-sensitive
3. Draft rules: uniqueness, referential checks, range/domain, regex, cross-field logic, volume gates
4. Prioritize rules by severity (blocker vs warning) and tie each to a remediation action

**See `references/profiling_and_quality_rules.md`.**

### 3. Remediate missing values, duplicates, outliers

1. Apply documented strategies per column (impute, flag, drop, split, business rule)
2. Deduplicate at correct grain; preserve lineage for merged records
3. Treat outliers with explicit policy (cap, winsorize, exclude, investigate)—never silent deletion
4. Re-run profile deltas after each major remediation pass

**See `references/missing_duplicates_and_outliers.md`.**

### 4. Standardize and coerce types

1. Normalize names, units, currencies, time zones, and categorical vocabularies
2. Coerce types with explicit parse rules and quarantine rows that fail
3. Fix encoding (UTF-8), delimiters, locale-specific decimals, and boolean sentinels
4. Version mapping tables (code → label) alongside the pipeline

**See `references/standardization_and_type_coercion.md`.**

### 5. PII and governance (technical, not legal advice)

1. Inventory sensitive columns; classify using organizational taxonomy when provided
2. Apply minimization: drop, hash/tokenize, mask, or aggregate per approved pattern
3. Log scrub actions; restrict outputs; never commit secrets or production PII to public repos
4. Escalate legal basis, retention, and cross-border rules to `compliance-engineer` / counsel

**See `references/pii_redaction_and_governance.md`.**

### 6. Actuarial / insurance scrubbing

1. Validate policy/claim keys, effective/accident dates, and triangle orientation
2. Align exposure bases and earned premium logic with documented definitions
3. Scrub large losses, sublimits, and reinsurance fields without distorting triangle structure
4. Hand off reserving/pricing math to `actuary` after data is signed off for modeling

**See `references/actuarial_insurance_data_scrubbing.md`.**

### 7. Validate, document, sign off

1. Execute rule suite on scrubbed output; compare to thresholds and prior period if applicable
2. Produce validation report: pass/fail counts, quarantine volume, top failure reasons
3. Package reproducible pipeline (script/SQL/notebook), config, and rule catalog with version hash
4. Obtain owner sign-off before promoting to modeling or reporting consumers

**See `references/data_scrubbing_scope_and_workflow.md` (sign-off section).**

## When to load references

| Topic | Reference |
|---|---|
| Scope, workflow, sign-off | `references/data_scrubbing_scope_and_workflow.md` |
| Profiling and quality rules | `references/profiling_and_quality_rules.md` |
| Missing, duplicates, outliers | `references/missing_duplicates_and_outliers.md` |
| Standardization and types | `references/standardization_and_type_coercion.md` |
| PII and governance | `references/pii_redaction_and_governance.md` |
| Actuarial / insurance data | `references/actuarial_insurance_data_scrubbing.md` |
