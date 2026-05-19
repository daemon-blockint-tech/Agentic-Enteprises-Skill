# Rollout planning

## Table of contents

1. [Plan template](#plan-template)
2. [Phase criteria](#phase-criteria)
3. [RACI](#raci)

## Plan template

```markdown
# Rollout: [Release name]
**Date / window:**  
**Owner:**  
**Risk tier:** Low | Medium | High

## Summary
[What ships and why]

## Scope
- Services:
- Regions:
- Feature flags:

## Phases
| Phase | % traffic | Entry criteria | Exit criteria | Owner |
|-------|-----------|----------------|---------------|-------|

## Rollback
**Triggers:**  
**Steps:**  
**Data impact:**

## Comms
- Internal:
- External:

## Verification
- [ ] Smoke tests
- [ ] Dashboards
- [ ] On-call briefed
```

## Phase criteria

**Example canary exit (all required):**

- Error rate ≤ baseline + 0.1%
- p95 latency ≤ baseline + 10%
- No SEV1/2 alerts
- 30 minutes stable at current weight

## RACI

| Role | Deploy | Approve prod | Rollback decision | Comms |
|---|---|---|---|---|
| Eng lead | R | A | R | C |
| SRE/on-call | C | I | C | I |
| Product | C | C | I | A |
| Risk/compliance | I | C (high tier) | I | C |
