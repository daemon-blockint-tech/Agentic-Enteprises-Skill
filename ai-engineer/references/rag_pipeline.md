# RAG pipeline

## Table of contents

1. [Chunking](#chunking)
2. [Retrieval](#retrieval)
3. [Eval metrics](#eval-metrics)

## Chunking

- Start 512–1024 tokens with overlap 10–20%
- Preserve headings in chunk metadata
- Split code and prose differently

## Retrieval

- Metadata filters for tenant_id mandatory in multi-tenant
- Rerank top 20 → pass top 5 to LLM
- Return "insufficient context" when scores below threshold

## Eval metrics

| Metric | Meaning |
|---|---|
| Recall@k | Gold doc in top k |
| Faithfulness | Answer supported by chunks |
| Answer relevance | Addresses question |
