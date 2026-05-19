# API integration

## Table of contents

1. [Client patterns](#client-patterns)
2. [Error handling](#error-handling)

## Client patterns

- Central `fetch` wrapper: base URL, auth header/cookies, JSON parse
- Map HTTP status to user-visible messages
- Cancel in-flight requests on route change when safe

## Error handling

| Status | UI behavior |
|---|---|
| 400 | Show field errors from body |
| 401 | Redirect login or refresh token once |
| 403 | Permission message |
| 404 | Not found state |
| 429 | Rate limit message; backoff |
| 5xx | Generic error + support ID |
