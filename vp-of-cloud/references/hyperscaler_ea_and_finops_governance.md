# Hyperscaler EA and FinOps governance

## Table of contents

1. [Executive commercial frame](#executive-commercial-frame)
2. [Commit and coverage policy](#commit-and-coverage-policy)
3. [Cloud envelope and forecast](#cloud-envelope-and-forecast)
4. [Showback and accountability](#showback-and-accountability)
5. [Negotiation rhythm](#negotiation-rhythm)
6. [Partner handoffs](#partner-handoffs)

## Executive commercial frame

VP owns **whether** to sign or renew; not contract redlines.

| Input | Skill |
|-------|-------|
| 3-year usage forecast by BU | `finops-analyst` |
| Commit coverage and break-even | `cloud-economist` |
| Regulated spend exclusions | `cloud-compliance-specialist` |
| Legal structure | `commercial-counsel` |
| GL and prepaid treatment | `compute-accounting-manager` |

Document **guardrails** for negotiators:

- Max term and true-up exposure
- Marketplace / third-party carve-outs
- Sovereign or dedicated region premiums
- Flexibility (true-down, burst, multi-cloud credits)

## Commit and coverage policy

Set org policy (example ranges — calibrate to business):

| Instrument | Policy lever |
|------------|--------------|
| Compute SP / CUD / Savings Plans | Target % of steady baseline |
| RI (legacy) | Sunset or grandfather only |
| Spot / preemptible | Batch tiers only |
| EA discount tiers | Tie to growth forecast bands |

Review **utilization** monthly; **reforecast** quarterly before true-up.

Escalate to VP if utilization <threshold or new workload class breaks model (e.g. GPU/AI spike).

## Cloud envelope and forecast

Align with finance on:

| Artifact | Owner |
|----------|-------|
| Annual cloud OpEx envelope | VP + CFO |
| Quarterly forecast | `finops-analyst` |
| Migration one-time funding | VP + TPM |
| Variance narrative | VP for >X% miss |

One **forecast cadence** — avoid separate EA and departmental guesses.

Link envelope to **portfolio gates** — unfunded migrations do not land in prod.

## Showback and accountability

| Mechanism | Purpose |
|-----------|---------|
| Tag policy | Allocate 95%+ spend |
| Showback | Transparency before chargeback |
| Chargeback | P&L ownership when mature |
| Unit metrics | Cost per customer/API/core |

VP sets **accountability model**; `finops-analyst` publishes dashboards.

Product leaders own **optimization actions** in monthly FinOps reviews.

## Negotiation rhythm

| Timing | Action |
|--------|--------|
| T-12 months | Start data pack, scenario model |
| T-6 months | Align growth narrative with CTO/CFO |
| T-3 months | Shortlist structures with `cloud-economist` |
| T-0 | VP sign-off on economics; legal on terms |

Post-signature: communicate **coverage rules** to CCoE and engineering.

## Partner handoffs

| Task | Skill |
|------|-------|
| Daily/weekly anomaly and waste | `finops-analyst` |
| Rightsizing execution | `cloud-engineer`, `cloud-system-administrator` |
| EA utilization dashboards | `finops-analyst` |
| NPV and sensitivity models | `cloud-economist` |
| Enterprise chargeback design | `enterprise-cloud-architect` |
| Full infra envelope (DC + cloud) | `vp-of-infrastructure` |
