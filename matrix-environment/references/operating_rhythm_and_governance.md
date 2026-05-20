# Operating Rhythm and Governance

## Forum ladder (example)

| Forum | Cadence | Participants | Decides |
|---|---|---|---|
| **Team sync** | Weekly | Squad | Sprint commitments |
| **Chapter / guild** | Biweekly | Discipline | Craft standards, training |
| **Product + platform** | Weekly | PM, Eng, platform | Priorities, blockers |
| **Security council** | Monthly | AppSec, GRC, SOC lead, eng reps | Policy, exceptions, metrics |
| **Reliability review** | Monthly | SRE, eng, product | SLO breaches, toil themes |
| **SteerCo** | Monthly/quarterly | CTO, CISO, VP infra, product VP | Cross-matrix conflicts, investment |
| **Board / audit committee** | Quarterly | Exec | Material risk, appetite |

Right-size: fewer forums with **decision logs** beat many status meetings.

## Intake and prioritization

### Unified intake principles

1. One **tool of record** per work type (vuln, incident, env request, architecture review)
2. Triage role named in RACI—not "the security team"
3. **WIP limits** per central team to prevent infinite queue
4. **Tiered service** — express path for incidents, standard for enhancements

### Prioritization lenses

| Lens | Owner | Use for |
|---|---|---|
| Risk | GRC / risk analyst | Audit, regulatory, materiality |
| Reliability | SRE | SLO, error budget |
| Security exploitability | AppSec / vuln mgmt | CVE, exposure |
| Customer impact | Product | Revenue, SLA to customers |
| Cost | FinOps / platform | Efficiency themes |

SteerCo resolves **conflicts** when lenses disagree; do not stack rank in every team separately.

## Governance gates (risk-based)

| Gate | Trigger (examples) | Participants |
|---|---|---|
| **Lightweight** | Low-risk change, paved road | Automated + owner |
| **Architecture / security review** | New data class, external exposure, auth change | AppSec C, architect C |
| **CAB / change advisory** | Prod infra, privileged access, blackout override | Platform, SRE, security C |
| **Exception** | Policy deviation | GRC A, CISO A if material |

Map gates to **environment tier** promotions—prod always highest tier.

## Operating metrics (org health)

| Metric | Indicates |
|---|---|
| Handoff time between queues | Interface friction |
| % findings closed by due SLA | Accountability |
| Repeat incidents same root cause | PIR execution gap |
| Exception count + age | Policy fit or risk appetite stress |
| Champion participation rate | Embed model health |
| Platform self-service adoption | Platform product-market fit |
| SteerCo decision cycle time | Executive alignment |

Pair with functional metrics in peer skills (KRIs, SLOs, audit grades).

## Decision log (minimum fields)

- Decision ID, date, forum
- Context and options considered
- **Accountable** role (name + function)
- Effective date and review date
- Links to RACI / policy updated?

## Rituals that reinforce the matrix

- **Joint backlog review** — security + platform + top product lines quarterly
- **Blameless post-incident** — actions assigned with single A; chapter picks systemic fixes
- **Onboarding pack** — one-page "who decides what" for new engineers and security staff
- **Annual operating model retrospective** — explicit keep/change/stop for forums and interfaces

## Handoffs to peer skills

| Topic | Skill |
|---|---|
| Company-wide EOS/OKR/L10 | `company-os` |
| DACI workshops for contested decisions | `daci-framework` |
| SOP and RACI documentation | `process-doc` |
| Incident program (SEV, on-call) | `incident-management-engineer` |
| Board and appetite | `chief-information-security-officer` |
