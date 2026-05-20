# Model and safeguard version rollout

## Table of contents

1. [Versioning model](#versioning-model)
2. [Canary strategy](#canary-strategy)
3. [Rollback](#rollback)
4. [Config-only changes](#config-only-changes)

## Versioning model

Independent versions:

- **Main LLM** weights or vendor model string
- **Classifier/moderation** models per stage
- **Policy config** (thresholds, categories)
- **Gateway routing** rules

Tag every response metadata: `{policy_v, classifier_v, llm_v}` for incident debug.

## Canary strategy

1. Deploy new version to **shadow** (log decisions, do not enforce) OR
2. **Traffic slice** 1% → 5% → 25% → 100% with gates

Gate criteria examples:

- Block rate within ±X% of baseline on golden set
- No increase in safety-path 5xx
- p99 latency within budget
- Zero critical misses on mandatory `ai-redteam` suite for that release

Automate promotion; manual approve for high-risk tiers.

## Rollback

- One-click revert routing to last known good **triple** (LLM + classifier + policy)
- Keep N-1 images/models warm for fast switch
- Document **data compatibility** — embedding index version if RAG adjacent

Post-rollback: incident timeline with version IDs.

## Config-only changes

Threshold tweaks without model swap:

- Still require canary — small threshold moves change block rate sharply
- Diff config in PR; peer review with `ai-risk-governance` for regulated tiers
- Feature flags per tenant for enterprise exceptions

Never hot-patch prod without audit trail.
