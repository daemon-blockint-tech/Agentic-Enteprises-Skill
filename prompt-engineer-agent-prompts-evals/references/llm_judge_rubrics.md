# LLM Judge Rubrics

## When to use a judge

| Use judge | Prefer deterministic |
|---|---|
| Open-ended quality, tone, completeness | Tool name, JSON schema, regex |
| Summarization fidelity | Exact codes/enums |
| Multi-criteria scoring | Binary pass/fail rules |

## Rubric structure

```
Criterion: Grounded in retrieved context only
Scale: 1–5 (1 = hallucination, 5 = fully grounded with citations)
Failure examples: Invents policy not in context
```

Publish rubric in repo; version with prompt.

## Reducing judge bias

- **Blind** model to prompt variant labels
- **Separate** judges per criterion vs one vague score
- **Anchor** with 2–3 scored examples in judge prompt
- **Calibrate** monthly against human labels (target κ or % agreement)
- Use **different model family** than agent under test when affordable

## Judge prompt template

```
You are an evaluator. Score only on [criterion].
Context: ...
Agent output: ...
Rubric: ...
Respond JSON: { "score": int, "reason": string }
```

## Human calibration

| Step | Action |
|---|---|
| Sample | 30–50 cases stratified by tags |
| Dual label | Two humans or human + judge |
| Agreement | Measure; fix rubric ambiguity |
| Threshold | Set min score for CI pass |

## Abuse

Judges can be gamed — combine with **spot human audit** and **deterministic** safety cases.

For adversarial robustness use `ai-redteam`, not judge alone.
