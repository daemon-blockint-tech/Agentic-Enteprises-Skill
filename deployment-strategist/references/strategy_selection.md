# Strategy selection

## Table of contents

1. [Decision tree](#decision-tree)
2. [Trade-off matrix](#trade-off-matrix)
3. [Coupled releases](#coupled-releases)

## Decision tree

```
Need instant traffic rollback at LB?
  yes → blue-green or canary with traffic manager
  no  → rolling may suffice

Schema or data migration required?
  yes → expand-contract + phased deploy; avoid big-bang

Canary metrics trustworthy within 5–15 min?
  yes → canary (5% → 25% → 100%)
  no  → blue-green with manual validation window

User-facing behavior risky?
  yes → feature flags decouple deploy from release
```

## Trade-off matrix

| Strategy | Downtime | Rollback speed | Infra cost | Complexity |
|---|---|---|---|---|
| Rolling | Minimal | Medium | Low | Low |
| Blue-green | Near zero | Fast (traffic switch) | High (2x) | Medium |
| Canary | Near zero | Fast (weight to 0) | Medium | High |
| Feature flags | N/A | Instant (flag off) | Low | Medium (flag debt) |
| Recreate | Possible | Slow | Low | Low |

## Coupled releases

| Coupling | Mitigation |
|---|---|
| API + mobile client | Backward-compatible API first; force upgrade only if needed |
| Service A + Service B | Deploy consumer tolerant first; contract tests |
| App + DB schema | Expand-contract; never break old code on same deploy |
| Model + prompt + index | Single version bundle; pin all three in release manifest |
