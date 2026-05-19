# Evaluation and operations

## Table of contents

1. [Golden datasets](#golden-datasets)
2. [CI eval](#ci-eval)
3. [Production monitoring](#production-monitoring)

## Golden datasets

50–200 examples covering:

- Happy path
- Edge cases
- Refusal/policy cases
- Known historical failures

Version dataset with git tag.

## CI eval

Run on PR when prompts, retrieval, or models change; block on regression of primary metric.

## Production monitoring

- Token usage and cost per feature
- Latency p50/p95
- Refusal and escalation rates
- User thumbs down sampling for review
