# API and data patterns

## Table of contents

1. [REST conventions](#rest-conventions)
2. [Pagination](#pagination)
3. [Idempotency](#idempotency)
4. [Migrations](#migrations)

## REST conventions

- `GET` safe, `PUT`/`PATCH` idempotent where possible
- Use nouns for resources; avoid verbs in paths
- Return consistent error shape: `{ code, message, details? }`

## Pagination

Prefer cursor-based for large feeds; offset only for admin tools.

## Idempotency

Accept `Idempotency-Key` header on `POST` that creates billable or external side effects.

## Migrations

- Backward-compatible expand → deploy → contract
- Never drop column in same release as code stops reading it
