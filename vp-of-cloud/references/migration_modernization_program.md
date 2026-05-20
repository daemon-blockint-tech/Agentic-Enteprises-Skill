# Migration and modernization program

## Table of contents

1. [Program charter](#program-charter)
2. [Discovery and assessment](#discovery-and-assessment)
3. [7Rs and wave design](#7rs-and-wave-design)
4. [Stage gates](#stage-gates)
5. [Funding and ROI](#funding-and-roi)
6. [Risks and rollback](#risks-and-rollback)

## Program charter

Define upfront:

| Element | Content |
|---------|---------|
| Scope | Apps, data platforms, DC exits in scope / out of scope |
| Sponsor | VP Cloud; steering with CFO/CTO |
| Delivery | TPM for RAID; architects for design; engineers for cutover |
| Non-goals | No big-bang without rollback; no migration without owner sign-off |

Align charter with **cloud strategy** (`cloud_strategy_and_portfolio.md`).

## Discovery and assessment

Run portfolio discovery:

| Artifact | Owner skill |
|----------|-------------|
| Application inventory | TPM + EA |
| Dependency map | `cloud-architect` |
| Compliance tier per app | `cloud-compliance-specialist` |
| TCO per 7R option | `cloud-economist` |
| Landing zone fit | `enterprise-cloud-architect` |

Classify each workload: **tier** (regulatory, revenue, internal), **complexity**, **data gravity**.

## 7Rs and wave design

| Strategy | When | VP decision |
|----------|------|-------------|
| Rehost | Fast exit DC, low change tolerance | Fund wave if ROI and risk acceptable |
| Replatform | DB or runtime upgrade in move | Require architecture sign-off |
| Refactor | Material cloud-native benefit | Prioritize if unit economics prove |
| Repurchase | SaaS replacement | Partner with procurement |
| Retire | Low value | Mandate decommission dates |
| Retain | Not ready | Explicit deferral with review date |
| Relocate | Same stack, new region/zone | Sovereignty or latency driver |

**Wave rules:**

- Max **N apps** or **M TB** per wave (set N/M from team capacity)
- No wave mixes **unrelated blast radius** (shared DB, shared auth)
- **Pilot wave** on non-critical tier first
- **Freeze windows** aligned with product calendar

Technical wave design → `cloud-architect`; portfolio order → VP Cloud.

## Stage gates

| Gate | Exit criteria |
|------|----------------|
| G0 Intake | Owner, tier, rough 7R, ROM cost |
| G1 Design | ADR, security review, landing zone target |
| G2 Build | IaC in non-prod, data replication tested |
| G3 Pilot | SLO met in cloud; rollback tested |
| G4 Cutover | Runbook executed; hypercare staffed |
| G5 Optimize | Rightsizing, commit fit, tag compliance |

VP approves **G0→G1** for large spend; delegates lower gates.

## Funding and ROI

| Cost type | Include in business case |
|-----------|--------------------------|
| Migration labor | Internal + partner |
| Dual-run | Parallel DC and cloud months |
| Licenses | BYOL, marketplace, egress |
| Run-rate delta | 12–36 month view |

`cloud-economist` builds model; VP presents **funding ask** and **payback** to finance.

Track **benefits realization** quarterly — not one-time slide.

## Risks and rollback

Escalate to VP when:

- Regulated data may cross border without approval
- Shared service cutover affects >1 revenue product
- EA commit requires new multi-year obligation
- Security exception beyond ARB threshold

Every wave requires: **rollback trigger**, **RTO/RPO**, **communication plan**.

Post-wave: blameless review; feed standards back to CCoE (`landing_zone_ccoe_governance.md`).
