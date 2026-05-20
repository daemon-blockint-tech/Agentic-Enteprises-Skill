# Safeguards request path

## Table of contents

1. [Stage ordering](#stage-ordering)
2. [Pre-model filters](#pre-model-filters)
3. [Post-model filters](#post-model-filters)
4. [Failure modes](#failure-modes)
5. [Latency](#latency)

## Stage ordering

Default order (adapt per policy):

1. **Auth / tenancy** — who is calling
2. **Rate limit / abuse** — volumetric
3. **Input normalization** — encoding, length trim
4. **Pre-classifiers** — prompt injection, PII detect, policy categories
5. **Main model** — only if pre-stages pass or soft-flag path
6. **Post-classifiers** — toxic output, leakage, tool-output scan
7. **Response shaping** — redaction, refusal templates

Document **short-circuit** rules: which stage can block without calling model.

## Pre-model filters

| Check | Goal |
|---|---|
| Jailbreak / injection heuristics | Block or route to hardened model |
| Category classifiers | Policy violations before spend |
| PII in prompt | Block, mask, or route to private stack |
| Allow/deny lists | Customer-specific policy packs |

Run **fast checks first** (regex, small model) before large LLM call.

## Post-model filters

- Harmful content, self-harm, illegal instructions (per policy)
- **Data exfiltration** patterns in output (secrets, system prompt leak)
- Tool call validation if agent path
- Structured output schema validation

On block: return **safe completion** with stable error code — not raw model output.

## Failure modes

| Failure | Policy options |
|---|---|
| Classifier timeout | Fail closed (block) vs fail open (log + allow) — tier by use case |
| Classifier error (5xx) | Retry with budget; then degrade |
| Model up, safety down | Usually **no unguarded path** in production |
| Partial stage outage | Shed traffic; route to backup region/model |

Align fail-open vs fail-closed with `ai-risk-governance` sign-off.

## Latency

Allocate **per-stage budget** (e.g. pre 30ms, model 2s, post 50ms p99).

- Parallelize independent classifiers where safe
- Cache benign prompt hashes cautiously — risk of stale policy
- Async human review **after** synchronous path for non-blocking tiers

Track `safety_path_ms` separately from `model_ms` in traces.
