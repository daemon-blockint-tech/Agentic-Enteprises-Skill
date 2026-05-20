# Red flags and remediation

## Table of contents

1. [Severity rubric](#severity-rubric)
2. [Common red flags](#common-red-flags)
3. [Deal and procurement responses](#deal-and-procurement-responses)
4. [Remediation planning](#remediation-planning)
5. [Acceptance and residual risk](#acceptance-and-residual-risk)
6. [Pentest and audit inputs](#pentest-and-audit-inputs)

## Severity rubric

| Level | Definition | Typical action |
|---|---|---|
| Critical | Imminent material harm, active compromise, or deal stopper | Escalate immediately; pause or condition close |
| High | Major gap vs baseline; regulatory or customer breach likely if exploited | Remediate before close or strong covenant; price/escrow |
| Medium | Meaningful gap with compensating controls or clear path | Timed remediation; monitor |
| Low | Improvement opportunity; minor documentation drift | Backlog |
| Informational | Observation; no action required | Note only |

Document **evidence**, **affected systems**, and **business impact** for each finding.

## Common red flags

| Signal | Why it matters |
|---|---|
| Undisclosed or poorly documented **breach** | Liability, integration, trust |
| No MFA on **admin** or prod access | Account takeover path |
| Stale **SOC 2** or scope mismatch | Unknown control state |
| Critical vulns **open beyond policy SLA** | Exploit window |
| Shared credentials or **no PAM** on critical systems | Non-repudiation failure |
| Missing **IR plan** or no recent tabletop | Recovery uncertainty |
| Shadow IT / unknown **cloud accounts** | Data exfiltration, compliance |
| Weak **SDLC** on revenue-facing apps | Supply chain to customers |
| **Subprocessor** sprawl without notice | Privacy/regulatory exposure |
| Aggressive **AI** data use without governance | Route AI depth to `ai-risk-governance` |
| Concentration on one **hosting or IdP** provider | Blast radius |

Corroborate red flags with evidence; distinguish **confirmed** vs **suspected**.

## Deal and procurement responses

| Response | When |
|---|---|
| Further diligence | Access or time insufficient; material unknowns |
| Conditions precedent | Fix before close (specific, testable) |
| Post-close covenant | Milestones with dates and verification |
| Escrow / holdback | Quantified remediation or liability tail |
| Price adjustment | Documented cost to remediate |
| Walk away | Critical unresolved exposure |

Coordinate legal mechanisms with `commercial-counsel` and deal process with `transaction-manager`. This skill supplies **security fact pack** and recommended **posture**, not binding legal advice.

## Remediation planning

For each High/Medium finding:

1. **Root cause** — people, process, technology
2. **Remediation action** — specific, measurable
3. **Owner** — named role
4. **Target date** — aligned to Day 1 / 30 / 90 or vendor contract
5. **Verification** — how completion is proven
6. **Dependency** — budget, integration, vendor

Track in shared backlog; review in governance cadence (`references/governance_cadence_and_reporting.md`).

## Acceptance and residual risk

When remediation before close is infeasible:

1. Document **residual risk** in business terms
2. Define **compensating controls** and monitoring
3. Obtain **risk acceptance** per policy with named approver and **expiry**
4. Register in `security-risk-analyst` risk register when material

Do not accept Critical findings without executive and legal alignment.

## Pentest and audit inputs

| Source | Use in diligence |
|---|---|
| Third-party pen test | Validate scope, dates, retest status; do not re-run tests here |
| Vuln scans | Trend and SLA adherence |
| SOC/ISO reports | Control coverage; read exceptions and CARs |
| Internal audit | Thematic gaps |

Commission new testing via `penetration-tester` when deal risk justifies **fresh** validation; incorporate results into findings register.
