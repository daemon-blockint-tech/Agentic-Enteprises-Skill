# Testing and debugging

## Table of contents

1. [Test pyramid](#test-pyramid)
2. [Common prod failures](#common-prod-failures)

## Test pyramid

| Layer | Scope |
|---|---|
| Unit | Pure functions, validators, reducers |
| Integration | API routes with test DB or containers |
| E2E | Critical user journeys only |

## Common prod failures

| Symptom | Check |
|---|---|
| 401/403 | Token expiry, role mapping, tenant header |
| 500 spike | Recent deploy, migration, dependency timeout |
| Slow page | N+1 query, missing index, large payload |
| Stale UI | Cache invalidation, CDN, service worker |
