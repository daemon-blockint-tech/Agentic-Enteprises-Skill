# Optimization playbook

## Table of contents

1. [Quick wins](#quick-wins)
2. [Prompt and context](#prompt-and-context)
3. [Model and routing](#model-and-routing)
4. [RAG and tools](#rag-and-tools)
5. [Agents](#agents)
6. [Trade-off summary](#trade-off-summary)

Implement via `ai-context-engineer`, `prompt-engineer`, `ai-engineer`—this file is for **planning** only.

## Quick wins

| Technique | Typical savings | Risk |
|---|---|---|
| Set `max_tokens` on outputs | High out reduction | Format truncation |
| Stop logging huge payloads into prompts | High in | Debuggability |
| Provider prompt caching (static prefix) | High in $ | Stale cache invalidation |
| Remove duplicate instructions across layers | Med in | Missed constraint |

## Prompt and context

| Technique | Typical savings | Risk |
|---|---|---|
| Shorter system prompt (same rules) | Med in | Policy drift |
| Structured sections + drop redundant examples | Med in | Few-shot quality |
| Rolling summary vs full history | High in | Lost nuance |
| Retrieve fewer/smaller chunks | Med in | Recall drop |
| Tool result truncation + summarization | High in | Wrong tool conclusions |

Detail: `ai-context-engineer` references.

## Model and routing

| Technique | Typical savings | Risk |
|---|---|---|
| Router: small model for classify/route | High $ | Mis-route |
| Cheaper model for drafts, premium for final | Med $ | Quality steps |
| Batch API for offline jobs | High $ | Latency N/A |

Always pair with eval matrix per route.

## RAG and tools

| Technique | Typical savings | Risk |
|---|---|---|
| Smaller embedding model (if quality OK) | Infra $ | Retrieval quality |
| Chunk size tuning | Med in | Boundary errors |
| Metadata filter before vector search | Med in | Missed docs |
| Cache retrieval results per session | Med in | Stale answers |

## Agents

| Technique | Typical savings | Risk |
|---|---|---|
| Max tool iterations cap | High | Incomplete tasks |
| Parallel vs serial tool calls | Latency + loops | Race conditions |
| Sub-agent only when needed | High | Architecture complexity |
| Pre-flight token budget abort | High | Hard stops mid-task |

## Trade-off summary

Document per initiative:

- **What we give up** (quality dimension)
- **Who accepts risk** (product, safety, eng)
- **How we detect regression** (metric + threshold)

Never optimize tokens in isolation from latency and success rate.
