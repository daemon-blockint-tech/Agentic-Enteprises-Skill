# Rollback and recovery

## Table of contents

1. [Rollback triggers](#rollback-triggers)
2. [Playbooks](#playbooks)
3. [Drills](#drills)

## Rollback triggers

Define before deploy:

| Trigger | Action |
|---|---|
| Error rate > X% for Y min | Auto or on-call rollback |
| Failed smoke test | Block promotion; rollback canary |
| SLO burn alert | Rollback or scale + investigate |
| Manual abort | Rollback immediately |

## Playbooks

**Application rollback (preferred):**

1. Stop traffic to bad version (canary weight 0 or blue-green switch)
2. Deploy previous known-good digest from registry
3. Run smoke tests
4. Confirm metrics normalized within 15 min

**Feature-flag rollback:**

1. Disable flag globally
2. Keep deploy in place if code path is inert when flag off

**Database rollback:**

- Avoid if possible; use forward fix
- Restore from backup only with explicit approval and RPO acceptance

## Drills

Quarterly: rollback prod-like staging to previous digest in < RTO target.

Document actual elapsed time and gaps.
