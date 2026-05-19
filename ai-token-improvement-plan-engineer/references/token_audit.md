# Token audit

## Table of contents

1. [Data sources](#data-sources)
2. [Attribution dimensions](#attribution-dimensions)
3. [Baseline worksheet](#baseline-worksheet)
4. [Driver analysis](#driver-analysis)

## Data sources

| Source | What it gives |
|---|---|
| Provider billing API | $ by model, day |
| App telemetry | request_id, feature, tenant, model, in/out tokens |
| Prompt/version registry | Which template was live |
| Eval logs | Tokens per eval run (don't ignore CI cost) |

Reconcile billing $ to token counts monthly; flag missing instrumentation early.

## Attribution dimensions

Minimum viable tags on every LLM call:

- `feature` or `product_surface`
- `model_id`
- `environment` (prod/staging)
- `tenant_id` or tier (if multi-tenant)
- `prompt_version` / `agent_version`
- `input_tokens`, `output_tokens`, `cached_tokens` (if provider supports)

Optional: `turn_index`, `tool_name`, `retrieval_chunk_count`.

## Baseline worksheet

```markdown
| Segment | Sessions/wk | Avg in tok | Avg out tok | $/session | % of total $ |
|---|---|---|---|---|---|
| Feature A | | | | | |
```

Compute:

```
cost_per_session = (in * price_in + out * price_out + cached_discount) / sessions
```

Note **growth rate** week-over-week (usage vs token inflation).

## Driver analysis

For top segment by spend, sample 20–50 traces:

1. Token breakdown: system vs tools vs RAG vs history vs user
2. Longest single block (often fixable)
3. Agent loop count and failed retries
4. Model tier vs task complexity mismatch

Document findings as **evidence-backed drivers**, not guesses.

If traces unavailable, run shadow logging for 48h before finalizing plan.
