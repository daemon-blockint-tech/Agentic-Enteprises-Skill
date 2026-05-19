# Web app architecture

## Table of contents

1. [Environment config](#environment-config)
2. [Routing](#routing)

## Environment config

| Variable | Expose to browser? |
|---|---|
| Public API URL | Yes (`NEXT_PUBLIC_`, `VITE_`) |
| API keys (server-only) | Never |
| Feature flags | Yes if non-secret |

Use separate configs for dev/stage/prod; no prod data in local dev.

## Routing

- Public routes: marketing, login, password reset
- Protected routes: middleware or loader checks session
- 404/500 pages branded; log server errors with request ID
