# Caching and prefetch

## Table of contents

1. [Prompt caching](#prompt-caching)
2. [Invalidation](#invalidation)
3. [Prefetch](#prefetch)

## Prompt caching

Cache stable prefix: system prompt + tool definitions + static RAG boilerplate.

Measure cache hit rate and $ savings in observability.

## Invalidation

Bump `prompt_version` in config; new version = new cache key.

## Prefetch

On typing pause, start retrieval; discard if user message changes materially (hash mismatch).
