# Catalog and inventory

## Table of contents

1. [Scan the repo](#scan-the-repo)
2. [Inventory table](#inventory-table)
3. [Gap and duplicate signals](#gap-and-duplicate-signals)

## Scan the repo

Skills in this layout: one directory per skill, `SKILL.md` at depth 2:

```
repo/
├── skill-a/SKILL.md
├── skill-b/SKILL.md
└── ...
```

List names:

```bash
find . -mindepth 2 -maxdepth 2 -name SKILL.md | sed 's|/SKILL.md||' | xargs -I{} basename {}
```

## Inventory table

| name | purpose (≤15 words) | top triggers | refs | overlap notes | owner | reviewed |
|---|---|---|---|---|---|---|
| `support-engineer` | … | ticket, repro | 5 | vs customer-ops | @team | 2026-05 |

Refresh quarterly or when adding/removing skills.

## Gap and duplicate signals

**Gap:** user requests that match no `description` keyword — candidate new skill or extend existing.

**Duplicate:** same verbs in two descriptions (e.g. "incident" in both `devops` and `incident-management-engineer`) — tighten **when NOT** lines.

**Orphan:** skill with no inbound cross-links from peers — add Related skills rows in adjacent domains.

Repo-level index for humans may live in root `README.md`; do not add per-skill README files.
