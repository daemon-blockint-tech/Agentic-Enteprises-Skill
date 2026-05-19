# Routing and overlap

## Table of contents

1. [Routing layers](#routing-layers)
2. [Disambiguation pattern](#disambiguation-pattern)
3. [Merge vs split heuristic](#merge-vs-split-heuristic)

## Routing layers

| Layer | What routes |
|---|---|
| Agent skill metadata | `description` on all installed skills |
| Body | **When NOT to Use** after skill already loaded |
| Related skills table | Secondary handoff |

Optimize layer 1 first — it is always in context.

## Disambiguation pattern

**Primary skill** `description`:

```
Use when [specific triggers]—not for [peer-a], [peer-b].
```

**Secondary skill** `description`:

```
Use when [narrow triggers]—not for [primary] ([when primary wins]).
```

Add matching rows in both Related skills tables.

## Merge vs split heuristic

| Signal | Action |
|---|---|
| Users always need both skills in one task | Merge or add explicit "load both" in TPM-style parent |
| Same `description` keywords | Rewrite triggers; do not merge unless same author domain |
| SKILL.md &gt;500 lines or &gt;8 reference files | Split by variant (see skill_lifecycle) |
| One skill is "strategy" and one is "implementation" | Keep separate; cross-link (e.g. architect vs engineer) |

Common pairs in this repo: `business-consultant` vs `business-analyst`; `incident-management-engineer` vs `support-engineer`; `ai-engineer` vs `applied-ai-architect-commercial-enterprise`.
