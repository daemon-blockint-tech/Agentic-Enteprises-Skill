# Measurement and KPIs

## Table of contents

1. [Primary KPIs](#primary-kpis)
2. [Guardrail KPIs](#guardrail-kpis)
3. [Eval gates](#eval-gates)
4. [Reporting cadence](#reporting-cadence)

## Primary KPIs

| KPI | Definition | Target example |
|---|---|---|
| Cost per session | $/successful session | −20% in 90d |
| Tokens per session | in+out mean/median | −25% in 90d |
| Cost per successful task | $/task completion | −15% |
| Cache hit rate | cached_in / total_in | >40% static prefix |

Segment all KPIs by feature and tier—global averages hide regressions.

## Guardrail KPIs

Do not worsen beyond threshold:

| Guardrail | Typical threshold |
|---|---|
| Task success / golden eval | ≤2% absolute drop |
| Safety eval pass rate | 0 regressions on blockers |
| p95 latency | ≤+10% |
| User thumbs-down rate | ≤+5% relative |
| Escalation to human | ≤+10% relative |

Define thresholds with product owner before phase 1 ships.

## Eval gates

**Pre-merge (per initiative):**

- [ ] Golden set run on old vs new (same model unless initiative is routing)
- [ ] Diff report for failures (categorize: acceptable vs blocker)
- [ ] Token/count comparison on same fixture set

**Pre-prod:**

- [ ] Canary 5–10% traffic or internal dogfood 48h+
- [ ] Cost dashboard shows expected delta
- [ ] No guardrail breach

**Post-ship (7d):**

- [ ] Sustained savings vs baseline window
- [ ] No support spike tagged to AI quality

Link safety runs to `ai-redteam` for tier-2+ surfaces.

## Reporting cadence

| Audience | Cadence | Content |
|---|---|---|
| Eng squad | Weekly | Initiative status, eval blockers |
| AI lead / ops | Weekly | $ vs budget, top features |
| Leadership | Monthly | Plan progress, ROI, risks |

Use same baseline window for before/after comparisons (avoid holiday skew).
