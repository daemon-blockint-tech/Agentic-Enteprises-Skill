# Measurement and instrumentation

## Table of contents

1. [Token counting](#token-counting)
2. [Logging schema](#logging-schema)
3. [Fair comparison](#fair-comparison)
4. [Cost translation](#cost-translation)

## Token counting

| Source | Use |
|---|---|
| Provider usage API | Ground truth for billed tokens |
| Local tokenizer (`tiktoken`, etc.) | Offline sweeps; must match deployment model |
| Logprobs / metadata | Per-turn breakdown when available |

Log **input**, **output**, **cached**, and **reasoning** tokens separately if provider splits them.

Document **system + tools + retrieval** as included in input — not just user message.

## Logging schema

Minimum per request:

```
run_id, model, tokenizer_id, timestamp
input_tokens, output_tokens, cached_tokens
feature_id, experiment_arm, prompt_hash
latency_ms, finish_reason
quality_label (pass/fail/score)
retrieval_tokens (if RAG)
compaction_applied (bool), pre_post_token_counts
```

Store **prompt template version** and **retrieval chunk IDs** for replay.

## Fair comparison

- Same eval queries and order (or stratified random seed)
- Same max output cap unless studying stop behavior
- Same tool definitions across arms (tool schemas dominate tokens)
- Warmup discarded for latency; not for token totals
- Report **distribution** (p50, p90), not mean only

Watch **hidden tokens**: image patches, audio frames, repeated tool results.

## Cost translation

Build price table by model tier:

```
cost = in_tokens * rate_in + out_tokens * rate_out + cached * rate_cached
```

Sensitivity analysis when list prices change mid-study.

Separate **research GPU cost** from **production inference cost** in memos.
