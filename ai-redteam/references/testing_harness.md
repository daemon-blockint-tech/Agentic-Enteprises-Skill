# Testing harness

## Table of contents

1. [Harness design](#harness-design)
2. [Dataset sources](#dataset-sources)

## Harness design

```text
for attack in dataset:
  response = app.send(attack)
  score = judge(policy_violation, leakage, tool_abuse)
  log(transcript, score)
```

- Pin model and prompt versions per run
- Parallelize with rate limits
- Compare to baseline after mitigations

## Dataset sources

- Internal policy violation probes
- Public harm benchmarks (use responsibly)
- Custom cases from support tickets (sanitized)
- Mutations of failed cases from prior runs
