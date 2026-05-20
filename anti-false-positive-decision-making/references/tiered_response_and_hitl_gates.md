# Tiered response and human-in-the-loop gates

## Table of contents

1. [Response tier model](#response-tier-model)
2. [Mapping evidence to tiers](#mapping-evidence-to-tiers)
3. [HITL gate types](#hitl-gate-types)
4. [SLAs and capacity](#slas-and-capacity)
5. [Automation guardrails](#automation-guardrails)
6. [Dual control and approvals](#dual-control-and-approvals)
7. [Customer communication](#customer-communication)
8. [Exception handling](#exception-handling)
9. [Examples by domain](#examples-by-domain)

## Response tier model

| Tier | Name | Customer / user impact | Automation |
|---|---|---|---|
| 0 | Observe | None | Full |
| 1 | Enrich & queue | None | Full with rate limits |
| 2 | Analyst review | None until disposition | Auto-route; human decides |
| 3 | Reversible contain | Temporary (hold, step-up, throttle) | Policy-limited auto |
| 4 | Irreversible | Block, close, SAR, report | Human + named approvers only |

**Default posture for low base rate + high FP cost:** start at Tier 0–1; earn Tier 3–4 with evidence tiers (see `evidence_bars_and_corroboration.md`).

## Mapping evidence to tiers

| Max evidence tier | Allowed response tier (default) |
|---|---|
| E0–E1 | 0–1 |
| E2 | 0–2 |
| E3 | 0–3 (contain reversible) |
| E4 | 0–4 with approvals |

Escalation **up** tiers requires new evidence or approver exception—never downgrade evidence requirement silently.

## HITL gate types

| Gate | When | Who |
|---|---|---|
| **G1 — Sample QA** | Random % of benign closes | Team lead |
| **G2 — Mandatory review** | All Tier 3+ or amount > limit | Analyst |
| **G3 — Four-eyes** | Tier 4 or policy list | Second analyst / lead |
| **G4 — Management** | Material loss, regulatory | Compliance / risk |
| **G5 — Legal** | SAR, law enforcement, sanctions confirm | Legal / MLRO |

Document gates in runbooks; do not rely on tribal knowledge.

## SLAs and capacity

Capacity planning prevents **fake precision** from rushed closes:

| Queue | Example SLA | Staffing input |
|---|---|---|
| Low severity | 24–72h | Volume forecast |
| High severity | 1–4h | On-call rotation |
| Tier 3 contain | Time-boxed hold max | Legal max hold policy |
| Tier 4 | Same-day exec path | Named backup approvers |

If SLA routinely missed:

- **Do not** lower evidence bar
- Add enrichment, dedup, or tier-0 routing
- Escalate capacity to operations leadership

Pair with `incident-management-engineer` for major incident severity—not daily alert queues.

## Automation guardrails

Allowed automation **only** with:

1. Written policy mapping tier → action
2. Kill switch and rollback
3. Audit log (who/what/when/version)
4. Rate limits per customer / global
5. Periodic sample QA (G1)

**Prohibited** without explicit risk acceptance:

- Tier 4 without human
- Permanent suppress without expiry
- Cross-customer threshold changes without segment analysis

## Dual control and approvals

| Action | Typical dual control |
|---|---|
| Release funds hold | Analyst + lead |
| Permanent whitelist | Compliance + ops |
| Rule auto-block enable | Engineering + risk |
| SAR filing | Analyst + MLRO |

Record approver identity in case system—not chat only.

## Customer communication

Tier 3–4 often requires **controlled messaging**:

| Situation | Guidance |
|---|---|
| Hold on payment | Factual, minimal, regulatory-safe wording per policy |
| False positive apology | Only after confirmed FP; track goodwill policy |
| No disclosure of internal rules | Avoid tipping fraudsters |

Route **wording** to compliance/legal for regulated text; this skill defines **when** to contact, not copy.

## Exception handling

**Temporary exception** (risk acceptance):

```
Exception ID:
Scope (customers, rules, duration):
Evidence bar waived to tier: ___
Approver:
Expiry (mandatory):
Review date:
```

Exceptions must **expire** automatically; no permanent “VIP skip” without executive register.

## Examples by domain

### Payments fraud

| Signal | Tier |
|---|---|
| Velocity only | 1 → 2 |
| Velocity + device mismatch | 2 → 3 (hold) |
| Confirmed mule pattern + loss | 3 → 4 with G3 |

### Sanctions screening

| Signal | Tier |
|---|---|
| Weak name match | 1 → 2 |
| Strong identifier match | 2 → 3 pending policy |
| Confirmed match per playbook | 4 MLRO path |

### Security (account compromise)

| Signal | Tier |
|---|---|
| Single failed login geo | 0–1 |
| Impossible travel + success login | 2 → 3 step-up |
| EDR confirmed malware + C2 | 3 → 4 isolate |

### AI / automated agent actions

For agentic systems that **act** on alerts:

- Require tool policy: max tier without human token
- Log chain-of-thought **decisions** not raw model rationale for audit
- Use `ai-risk-governance` for model tier; use this reference for **action tier**

## De-escalation

When evidence weakens:

1. Release contain at Tier 3 when disconfirming checks pass
2. Document de-escalation rationale
3. Retain monitor tier (0–1) for cooling period if policy requires
