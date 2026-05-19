# Compression and efficiency methods

## Table of contents

1. [Method families](#method-families)
2. [Evaluation protocol](#evaluation-protocol)
3. [Failure modes to track](#failure-modes-to-track)
4. [Routing and cascades](#routing-and-cascades)

## Method families

| Family | Research question |
|---|---|
| Summarization / compaction | What is lost at ratio r? |
| Extractive selection | Can selectors beat generative summary? |
| Embedding compression | Do smaller retrievals preserve recall? |
| Prompt compression (LLMLingua-style) | Robustness on instructions? |
| KV cache / prefix reuse | Savings at scale with shared system prompt? |
| Model cascade | Error rate when small model filters? |
| Speculative decoding | Throughput vs quality (often output-side) |
| Quantization | Quality per watt (adjacent to token research) |

Tag studies as **input-token** vs **output-token** vs **latency** primary.

## Evaluation protocol

For each method:

1. Apply at fixed operating point (e.g., 50% input reduction target)
2. Run **full eval suite** + **stress suite** (long tools, multi-turn, non-English)
3. Compare **tokens-to-success** and **primary quality**
4. Cost **human review** on stratified failures only

Report **Pareto frontier** — not single point cherry-pick.

## Failure modes to track

| Failure | Signal |
|---|---|
| Lost constraints | Violates must-not rules |
| Stale state | Wrong entity after compaction |
| Tool hallucination | Calls after schema truncated |
| Retrieval miss | Answerable from dropped chunk |
| Tone/policy drift | Safety or brand violations |

Bucket failures for qualitative appendix.

## Routing and cascades

Research design:

- Define router features (length, intent class, entropy)
- Train/ calibrate on held-out set
- Measure **% traffic to cheap model** vs **regression rate**
- Account **router overhead tokens** in total

Compare to **always large** and **always small** baselines.

Hand off winning thresholds to `ai-token-improvement-plan-engineer` for rollout planning.
