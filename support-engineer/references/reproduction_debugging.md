# Reproduction and debugging

## Table of contents

1. [Repro template](#repro-template)
2. [Log fields](#log-fields)

## Repro template

```markdown
## Environment
- Tenant / account:
- Product version or build:
- Browser or SDK version:

## Steps
1.
2.

## Expected

## Actual

## Attachments
- HAR / curl (secrets redacted)
- Request ID:
```

## Log fields

Collect when available:

- `request_id`, `trace_id`, `correlation_id`
- HTTP status and response body (truncate PII)
- User ID and resource IDs (not passwords or tokens)
