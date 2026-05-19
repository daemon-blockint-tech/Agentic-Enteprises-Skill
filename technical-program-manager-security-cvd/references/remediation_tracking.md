# Remediation tracking

## Table of contents

1. [Work breakdown](#work-breakdown)
2. [Milestones](#milestones)
3. [Exceptions](#exceptions)
4. [Validation](#validation)

## Work breakdown

Per finding, track:

| Field | Notes |
|---|---|
| Component / service | Single engineering DRI |
| Fix version or PR | Link when available |
| Target date | Aligned to severity SLA |
| Dependencies | Other teams, vendors, upstream |
| Customer impact | Hosted vs on-prem; config-only mitigations |
| Compensating controls | WAF rule, feature flag — interim only |

Use same RAID patterns as `technical-program-manager` — risks: slip on embargo, incomplete backport, missing test env.

## Milestones

Typical sequence:

1. **Confirmed** — reproducible, in scope
2. **Fix in progress** — PR or patch branch
3. **Fix in staging** — ready for security retest
4. **Fix in production** — or shipped release train
5. **Validated** — security sign-off on retest
6. **Ready to disclose** — publication checklist started

Flag **critical path** items blocking coordinated date (e.g., mobile app store review).

## Exceptions

| Situation | Program action |
|---|---|
| Won’t fix (by design) | Document rationale; counsel review; close with reporter |
| Fix infeasible short term | Mitigation + extended timeline; researcher agreement |
| Duplicate of known issue | Link parent; align disclosure to parent |
| Third-party dependency | Track vendor advisory; communicate dependency to reporter |

## Validation

Before closing remediation:

- [ ] Original PoC no longer works in target environment
- [ ] Regression test or automated check where applicable
- [ ] No scope creep (adjacent issues filed separately)
- [ ] Bounty severity finalized if applicable

Validation owner: security engineering — TPM confirms checklist complete.
