# Memory architecture

## Table of contents

1. [Patterns](#patterns)
2. [Store selection](#store-selection)
3. [Anti-patterns](#anti-patterns)

## Patterns

| Pattern | Description |
|---|---|
| Mem0-style | Extract facts post-turn; vector + optional graph |
| Scratchpad | Agent writes notes tool; human-readable |
| Profile + episodes | Stable profile fields + episodic log |
| RAG-as-memory | Same index as docs; tag `type=memory` |

## Store selection

| Need | Options |
|---|---|
| Semantic recall | pgvector, Pinecone, Weaviate, Qdrant |
| Structured facts | Postgres JSONB, user profile table |
| Graph relations | Neo4j, property graph for entities |
| Fast session | Redis with TTL |

Always filter by `tenant_id` and `user_id` at query time.

## Anti-patterns

- Storing entire chat logs as memory without extraction
- Global shared memory across users
- No deletion path for compliance
- Writing model hallucinations as facts without verification
