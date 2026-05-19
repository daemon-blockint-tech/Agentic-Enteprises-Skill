# Read and retrieval

## Table of contents

1. [Query construction](#query-construction)
2. [Injection format](#injection-format)
3. [Ranking](#ranking)

## Query construction

Combine: latest user message + session summary + active entity IDs.

## Injection format

```xml
<user_memories>
- [mem_12] Prefers metric units (source: 2024-01-10)
- [mem_45] Project codename: Apollo (source: 2024-02-01)
</user_memories>
```

Instruct model: use memories only when relevant; do not invent new memories.

## Ranking

1. Vector similarity
2. Metadata filter (tenant, user, not expired)
3. Cross-encoder rerank top 20 → top 5
4. Drop if score < threshold
