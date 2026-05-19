# Documentation, Lineage, and Exposures

## Model documentation

Minimum per mart in `schema.yml`:

- `description` — business purpose
- Column `description` for keys and measures
- `meta` for owner, PII tier, refresh cadence

## Lineage

- dbt docs generate DAG; publish to catalog (dbt Cloud, OpenMetadata, etc.)
- Tag **PII** columns for governance alignment with `data-architect`

## Exposures

Declare downstream dashboards in `exposures.yml`:

```yaml
exposures:
  - name: executive_revenue_dashboard
    type: dashboard
    depends_on:
      - ref('fct_revenue')
```

Use for impact analysis when changing `fct_revenue`.

## CI documentation

- Fail PR if undocumented public mart columns (custom test or linter)
- Auto-deploy docs site on main merge

## README for analysts

Short analyst-facing note:

- Approved tables and grains
- Known limitations and refresh time
- Contact for metric definition changes

## Handoff to BI

| Artifact | Consumer |
|---|---|
| Exposures | Impact analysis |
| Column docs | Looker/Tableau field descriptions |
| Grain statement | Metric validation with `bi-analyst` |
