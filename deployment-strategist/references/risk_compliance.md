# Risk and compliance

## Table of contents

1. [Change tiers](#change-tiers)
2. [Change windows](#change-windows)
3. [Evidence checklist](#evidence-checklist)

## Change tiers

| Tier | Examples | Approvals |
|---|---|---|
| Low | Copy, internal tool, flag off by default | Team lead |
| Medium | Customer-facing feature, config change | Eng + product |
| High | Auth, payments, schema, infra cutover | CAB + SRE + risk |

## Change windows

- Blackout: peak traffic, holidays, fiscal close
- Preferred: low-traffic window with on-call staffed
- Multi-region: roll forward by region (low-risk region first)

## Evidence checklist

Attach to change ticket:

- [ ] Rollout plan link
- [ ] Rollback tested date
- [ ] Eval/test results
- [ ] Dashboard links for canary
- [ ] Comms sent (if external)
- [ ] Post-deploy verification sign-off
