# Prompt Versioning and Regression

## Versioning

| Artifact | Version scheme |
|---|---|
| System prompt | Semver or date tag (`agent-system@1.3.0`) |
| Tool schemas | Lockfile hash or semver |
| Eval dataset | `evalset@2026.04.1` |
| Judge rubrics | Same as prompt minor bump |

Store in git; tag releases aligned with app deploy.

## Change workflow

1. Branch prompt change
2. Run harness vs **baseline** on golden set
3. Document delta: pass rate by tag, new failures, token delta
4. SME review for critical tag regressions
5. Merge with required approvers (eng + risk if Tier 1–2)

## Regression policy

| Change type | Required evidence |
|---|---|
| Wording only | No pass rate drop on safety/refusal tags |
| New tool | New cases + existing suite pass |
| Tool description | Tool-accuracy slice unchanged or improved |
| Model swap | Full re-baseline + cost/latency report |

Allow **waivers** with risk sign-off — logged in release notes.

## Rollback

- Keep **N-1** prompt in config for instant revert
- Feature flag per prompt version
- Post-deploy monitor: judge sample + error rate 24h

## PR template (minimal)

```
Prompt version: x.y.z
Eval dataset: ...
Pass rate: baseline → candidate (by tag table)
Notable failures: links to traces
SME sign-off: Y/N
```

Coordinate gates with `engineering-manager-vertical-ai-products` for customer-facing launches.
