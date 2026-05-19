# Write and consolidation

## Table of contents

1. [Extraction](#extraction)
2. [Importance scoring](#importance-scoring)
3. [Consolidation job](#consolidation-job)

## Extraction

Prompt model or smaller model to output JSON:

```json
{ "facts": [{ "text": "...", "confidence": 0.9, "category": "preference" }] }
```

Reject low confidence and duplicate entities.

## Importance scoring

Boost: explicit user preferences, repeated mentions, task-critical constraints.

Penalize: greetings, one-off questions, stale time-bound facts.

## Consolidation job

Nightly per user:

1. Load episodic memories from last 7 days
2. Summarize into semantic profile deltas
3. Mark episodes consolidated; retain audit link
4. Prune superseded facts
