# TPRM intake and tiering

## Table of contents

1. [Intake triggers](#intake-triggers)
2. [Intake record](#intake-record)
3. [Tiering model](#tiering-model)
4. [Inherent risk factors](#inherent-risk-factors)
5. [Assessment depth](#assessment-depth)
6. [Lifecycle events](#lifecycle-events)

## Intake triggers

Open or refresh assessment on:

- **New vendor** before production data or network access
- **Renewal** — use contract date as forcing function
- **Scope change** — new data class, region, AI training use, admin API
- **Acquisition** by vendor or hosting migration
- **Public incident** affecting vendor or material subprocessor
- **Offboarding** — data return, deletion, access revocation risks until exit complete

## Intake record

Capture minimum fields at intake:

| Field | Purpose |
|---|---|
| Vendor legal name and product | Identity in inventory |
| Business owner | Accountable party |
| Use case and integration | Production vs pilot |
| Data types | PII, PHI, PCI, credentials, source code, AI data |
| Access model | SSO, API keys, VPN, break-glass |
| Hosting / residency | Region, hyperscaler, on-prem |
| Spend and contract term | Renewal priority (not security tier alone) |
| Substitutability | Switching cost and timeline |
| Known subprocessors | Seed fourth-party review |

Route legal/privacy questions to counsel; provide **tier and required evidence list** only.

## Tiering model

| Tier | Typical criteria | Assessment cadence |
|---|---|---|
| T1 Critical | Production sensitive data, admin access, single-source, regulated | Annual + continuous monitoring |
| T2 Important | Internal data, material integration, moderate outage impact | Annual |
| T3 Standard | Limited data, replaceable, low integration | Every 2–3 years or on change |
| T4 Low | No sensitive data, no production integration | Lightweight attestation |

Document **tier rationale** in one paragraph. One vendor may map to multiple products with different tiers.

## Inherent risk factors

Score or tag (qualitative or simple matrix):

- **Data sensitivity** and volume
- **Access** to production, identity, or network
- **Criticality** — outage duration if vendor fails
- **Substitutability** — time and cost to replace
- **Geography** — residency, sanctions exposure
- **Concentration** — % workloads or spend on one provider
- **Fourth parties** — opaque subprocessors for T1

Do not conflate **vendor financial health** with cyber tier without finance input.

## Assessment depth

| Tier | Minimum package |
|---|---|
| T1 | Full questionnaire + SOC 2 Type II or ISO 27001 + pen test summary if available + subprocessor list + incident history |
| T2 | Questionnaire + certification or detailed security whitepaper |
| T3 | Short questionnaire or trust center review |
| T4 | Data-handling terms check only |

Escalate to `cyber-diligence-governance` when intake is **deal-specific** (target, portfolio company, major acquisition) rather than operational vendor onboarding.

## Lifecycle events

Re-tier or reassess when:

- Integration moves from pilot to production
- Vendor adds subprocessors in new regions
- Customer contract requires higher assurance
- Monitoring detects breach or sustained outage
- Contract renewal within 90 days (prioritize queue)

Feed material residual vendor risk into enterprise register via `security-risk-analyst`—do not maintain duplicate registers without sync rules.
