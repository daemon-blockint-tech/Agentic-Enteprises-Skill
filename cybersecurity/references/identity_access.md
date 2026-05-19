# Identity and access

## Table of contents

1. [Human access](#human-access)
2. [Service accounts](#service-accounts)
3. [Access reviews](#access-reviews)

## Human access

- SSO to all SaaS; disable local accounts
- Role-based groups; no standing admin for daily work
- Just-in-time elevation with ticket and time bound

## Service accounts

- One account per integration; document owner
- Rotate keys on schedule and on departure
- Prefer workload identity over long-lived keys

## Access reviews

Quarterly for production; verify managers attest removals within SLA.
