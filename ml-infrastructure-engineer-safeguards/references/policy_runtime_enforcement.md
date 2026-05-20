# Policy runtime enforcement

## Table of contents

1. [Policy artifacts](#policy-artifacts)
2. [Actions](#actions)
3. [Tiers and tenants](#tiers-and-tenants)
4. [Human-in-the-loop](#human-in-the-loop)

## Policy artifacts

Versioned config (not hardcoded in app):

- Category thresholds and score → action mapping
- Model IDs per region and tier
- Refusal message templates (locale)
- Feature flags for experimental policies
- Allowlist/denylist references (synced from secure store)

Store in **config service** with audit log; promote dev → staging → prod.

## Actions

| Action | When |
|---|---|
| Allow | Pass through |
| Block | Fixed refusal; no model or discard output |
| Rewrite | Mask PII, strip segment |
| Route | Alternate model or stricter stack |
| Log-only | Monitor mode for rollout |
| Escalate | Queue for human review |

Return **machine-readable reason codes** to clients (not internal policy names if sensitive).

## Tiers and tenants

| Dimension | Example |
|---|---|
| Risk tier | Internal tool vs customer-facing vs regulated |
| Tenant | Enterprise custom policy pack |
| Geography | EU vs US data residency routing |

Enforce at gateway using claims + tenant metadata — single enforcement point.

## Human-in-the-loop

Infrastructure hooks:

- **Review queue** — payload metadata + hashed content id
- SLA for reviewer turnaround; expiry → default action
- Audit trail: who approved, policy version, model version
- No PII in queue titles; encrypt at rest

Product workflow design may involve `ai-risk-governance`; own pipes and storage here.
