# Agents and tools

## Table of contents

1. [Tool schema](#tool-schema)
2. [Loop controls](#loop-controls)
3. [Failure handling](#failure-handling)

## Tool schema

- Clear name and description for when to call
- Required fields explicit; enums for fixed choices
- Validate arguments before execution

## Loop controls

- Max iterations (e.g., 10)
- Max wall-clock time
- Stop when final answer tool invoked

## Failure handling

- Retry transient errors with backoff
- Surface tool error to model once; do not infinite retry
- Human escalation path for repeated failures
