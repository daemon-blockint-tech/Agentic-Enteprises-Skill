# Customer data protection

## Table of contents

1. [Key hierarchy](#key-hierarchy)
2. [Deletion](#deletion)
3. [Backups](#backups)

## Key hierarchy

- Platform CMK for infrastructure
- Optional per-tenant DEK for regulated tiers
- Envelope encryption: DEK wrapped by CMK; rotate DEKs on tenant offboarding where required

Document which fields are encrypted and at which layer (app vs DB TDE).

## Deletion

Account closure workflow:

1. Disable access immediately
2. Mark tenant deleted; stop schedulers
3. Purge or crypto-shred per policy timeline
4. Verify backups and replicas respect retention
5. Audit log retention separate from customer data policy

## Backups

- Backups encrypted; restore tested without cross-tenant restore paths
- Restore drills must use synthetic tenant in non-prod
