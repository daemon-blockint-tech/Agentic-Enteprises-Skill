# Testing and quality

## Table of contents

1. [Test pyramid](#test-pyramid)
2. [What to test](#what-to-test)
3. [Flaky tests](#flaky-tests)

## Test pyramid

| Layer | Scope |
|---|---|
| Unit | Pure logic, validators |
| Integration | API + DB (test container) |
| E2E | Critical user journeys only |

## What to test

- Authz matrix for new endpoints
- Edge cases in validation
- Regression for every production bug fix

## Flaky tests

Quarantine with ticket; fix or delete within 2 sprints—do not retry indefinitely without investigation.
