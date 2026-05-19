# UI Data States

## Boundary responsibility

UI engineer consumes **existing API**; does not design schema.

| Concern | Owner |
|---|---|
| Endpoint contract | Backend / fullstack |
| Loading UI | UI engineer |
| Error message display | UI + copy spec |
| Retry action | UI + product |

## Async UI pattern

```
idle → loading → success | error | empty
```

| Phase | UI |
|---|---|
| **Loading** | Skeleton matching layout (not generic spinner only for full page) |
| **Success** | Render data; handle partial lists |
| **Empty** | Designed empty state; not blank screen |
| **Error** | User-safe message; retry if idempotent |

## Forms

- Disable submit while **pending**
- Show **field errors** from API validation map
- Preserve user input on recoverable error
- Success: toast or redirect per spec

## Lists and tables

- Pagination or infinite scroll per spec
- Row actions disabled while mutation in flight
- Optimistic UI only if fullstack documents rollback behavior

## Escalation

- New endpoint or contract change → `fullstack-software-engineer`
- Auth redirect / 401 handling in app shell → `web-application-developer`
