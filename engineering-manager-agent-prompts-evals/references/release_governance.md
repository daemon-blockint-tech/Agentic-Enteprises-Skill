# Release Governance (Prompt & Eval)

## Gate stack (customer-facing agents)

| Gate | Owner | Block? |
|---|---|---|
| Golden CI pass | Eval eng | Yes |
| Tag slice thresholds (safety, tools) | EM + risk | Yes |
| Judge calibration current | Judge owner | Yes if stale |
| Red-team sign-off (Tier 1–2) | `ai-redteam` | Yes |
| Ops kill switch tested | `ai-lead-ops` | Yes |
| Prompt semver + changelog | Prompt eng | Yes |

IC checklist detail: `prompt-engineer-agent-prompts-evals` → `references/prompt_versioning_regression.md`.

## Waiver process

1. Document failing cases and business justification
2. Compensating control (human review, feature flag, limited audience)
3. Risk approver for tier
4. Expiry date and remediation ticket

Log all waivers; review monthly in leadership sync.

## Rollback

- N-1 prompt in config; flag per version
- Eval must pass on N-1 before rollback deploy
- Post-rollback: add regression cases for failure mode

## Internal / low-tier agents

Reduced gates — still require smoke golden set and owner sign-off.

## Manager responsibilities

- Enforce **no hotfix prompt** without trace + case addition
- Align with vertical EM (`engineering-manager-vertical-ai-products`) on launch calendar
- Communicate eval status in ship/no-ship meetings
