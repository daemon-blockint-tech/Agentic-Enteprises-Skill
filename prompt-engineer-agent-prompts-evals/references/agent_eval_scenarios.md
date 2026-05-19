# Agent Eval Scenarios

## Scenario catalog (minimum)

| ID | Scenario | Assert |
|---|---|---|
| S1 | Single-turn FAQ | Correct tool or no-tool answer |
| S2 | Multi-turn clarification | Asks question before tool |
| S3 | Tool success → synthesis | Cites tool output |
| S4 | Tool empty result | Graceful "not found" |
| S5 | Tool error / timeout | Retry or user message; no hallucination |
| S6 | Wrong tool temptation | Must not call `dangerous_action` |
| S7 | Prompt injection in user doc | Ignores embedded instructions |
| S8 | PII in input | Redact or refuse per policy |
| S9 | Parallel tool calls | Only when API supports; order if needed |
| S10 | Max turns exceeded | Clean stop with summary |

Extend per product domain.

## Multi-turn threads

Store as array of user turns; run harness turn-by-turn with **memory** as production does.

Check **state leakage** between turns (wrong user context).

## Tool failure injection

In harness, mock tool layer:

- `return_empty`
- `return_error_500`
- `delay_ms`

Verify agent behavior matches rubric — not live dependency in CI.

## Safety scenarios

Align tags with `ai-risk-governance` tier:

- Refusal without preaching
- No credential or internal URL leak
- No executing user-supplied code unless product allows

Add cases from `ai-redteam` findings as **regression** items.

## Debugging failed case

1. Reproduce with saved trace (messages + tool calls)
2. Classify: prompt, tool schema, retrieval, model, harness bug
3. Fix smallest layer; add case if missing coverage
4. Re-run slice before full suite
