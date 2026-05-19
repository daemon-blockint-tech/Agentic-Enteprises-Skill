# Debugging context

## Table of contents

1. [Instrumentation](#instrumentation)
2. [Replay](#replay)

## Instrumentation

Log per request (redacted):

- Token count per block
- Retrieval IDs and scores
- Prompt version
- Model ID

Store last assembled context in secure debug mode for support (time-limited).

## Replay

Re-run assembly with same inputs in staging to reproduce "ignored instruction" bugs.

Compare diffs when prompt or compression changes.
