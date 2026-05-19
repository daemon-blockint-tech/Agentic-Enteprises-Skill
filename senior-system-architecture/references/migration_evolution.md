# Migration and evolution

## Table of contents

1. [Strategies](#strategies)
2. [Strangler fig pattern](#strangler-fig-pattern)
3. [Dual-write and dual-read](#dual-write-and-dual-read)
4. [Cutover and rollback](#cutover-and-rollback)
5. [Deprecation](#deprecation)

## Strategies

| Strategy | Risk | When |
|---|---|---|
| **Big-bang** | High | Small scope, strong rollback, short freeze OK |
| **Strangler** | Medium | Large legacy; slice-by-slice migration |
| **Parallel run** | Medium | Need confidence via shadow/compare |
| **Freeze + replace** | High | Only if business accepts downtime |

Default to strangler for customer-facing systems with uptime SLOs.

## Strangler fig pattern

1. Put **facade** (gateway, router, or API layer) in front of legacy
2. Route **new capabilities** to new system only
3. Migrate **read paths** first when safe (often lower risk)
4. Migrate **writes** with reconciliation
5. Retire legacy module when traffic and data parity proven

Track per-slice: % traffic, % data migrated, defect rate vs legacy.

## Dual-write and dual-read

**Dual-write:**

- Write to old and new; reconcile on mismatch
- Limit duration; define max drift window
- Use idempotency keys on both sides

**Dual-read:**

- Read new; compare to old in shadow (log diffs only)
- Promote new read when diff rate below threshold

**Reconciliation job:**

- Scheduled compare + quarantine bad rows
- Human playbook for irreconcilable records

## Cutover and rollback

Coordinate with `deployment-strategist`:

- **Go criteria:** parity metrics, error rate, support ticket volume
- **Rollback criteria:** SLO burn, data corruption signal, failed reconciliation
- **Freeze window:** communicate to support and CS

Run **dress rehearsal** on production-like data volume when possible.

## Deprecation

1. Announce timeline (internal + external if API)
2. Metric: callers still on old path
3. Sunset with 410/structured error after window
4. Archive data per retention policy
5. Remove code and infra; close ADR as superseded

Document lessons learned; update architecture principles if gaps found.
