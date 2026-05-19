# Solution patterns

## Table of contents

1. [Decision tree](#decision-tree)
2. [Model routing](#model-routing)

## Decision tree

| Need | Pattern |
|---|---|
| Fixed Q&A on static docs | RAG |
| Structured extraction | Single call + JSON schema |
| Multi-step tools/APIs | Agent with tools |
| Domain tone/style | System prompt + few-shot; fine-tune if insufficient |

## Model routing

Route by task complexity:

- Small/fast model for classification and routing
- Large model for synthesis and hard reasoning
- Fallback on timeout with degraded response message
