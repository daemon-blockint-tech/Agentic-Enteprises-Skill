# Eval Harness Patterns

## Harness responsibilities

1. Load prompt version + tool definitions
2. Run agent on each case (fixed model + temperature for CI)
3. Assert expectations (tools, text, schema, trajectory)
4. Emit report (pass rate, diffs, traces)

## Metrics

| Metric | Definition |
|---|---|
| **Pass rate** | Cases meeting all assertions |
| **Tool accuracy** | Correct tool selected / args valid |
| **Format compliance** | JSON/schema parse success |
| **Latency / tokens** | Regression budgets |
| **Judge score** | Mean rubric score when prose evaluated |

Track **per-tag** pass rate to spot weak slices.

## Assertion styles

```text
assert_tool_called(name, args_subset)
assert_no_tool()
assert_json_schema(schema_id)
assert_refusal(category)
assert_judge_score(rubric_id, min_score)
```

Prefer deterministic checks; use judge for nuance.

## CI integration

| Gate | Policy |
|---|---|
| PR | Run on changed prompt/tools + full set if small |
| Nightly | Full golden set + sampled production replay |
| Pre-prod | Block if pass rate drops > agreed delta vs main |

Store traces as artifacts for failed cases.

## Flakiness control

- Fixed model version in CI
- Low temperature (0–0.2) for deterministic suites
- Separate **flaky** quarantine folder with stricter retry policy
- Human review queue for judge disagreement

## Integration with `ai-engineer`

Harness code lives in app repo; this skill defines **what** to measure and **case design** — implement runners per stack (LangSmith, custom, etc.).
