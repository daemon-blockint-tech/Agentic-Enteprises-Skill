# API and database

## Table of contents

1. [REST defaults](#rest-defaults)
2. [Pagination](#pagination)
3. [Migrations](#migrations)

## REST defaults

- `POST` create, `GET` read, `PATCH` partial update, `DELETE` remove
- Validate body and query params at entry
- Return consistent error shape: `{ code, message, details? }`

## Pagination

Prefer cursor-based for large lists:

```
GET /items?cursor=abc&limit=20
→ { items: [], next_cursor: "def" }
```

## Migrations

- One logical change per migration
- Backfill in batches for large tables
- Test rollback on staging
- Never drop column until code no longer reads it (expand-contract)
