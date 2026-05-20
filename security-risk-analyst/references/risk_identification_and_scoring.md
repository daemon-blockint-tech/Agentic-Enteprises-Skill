# Risk identification and scoring

## Table of contents

1. [Identify scenarios](#identify-scenarios)
2. [Qualitative scales](#qualitative-scales)
3. [Inherent vs residual](#inherent-vs-residual)
4. [FAIR-style quantitative framing](#fair-style-quantitative-framing)
5. [Risk appetite and escalation](#risk-appetite-and-escalation)
6. [Common mistakes](#common-mistakes)

## Identify scenarios

Write risks as **events**, not control names:

- Bad: "Missing MFA"
- Good: "Unauthorized access to production via stolen credentials due to absent MFA on admin console"

Sources: threat intel, incidents, pentests, vuln scans, architecture reviews, vendor assessments, regulatory change.

Group duplicates; one register row per **material** scenario per scope.

## Qualitative scales

Default **5×5** likelihood × impact (adjust only with documented org scale):

| Likelihood | Guide |
|---|---|
| 1 Rare | < once per 5 years in scope |
| 2 Unlikely | Every few years |
| 3 Possible | About yearly |
| 4 Likely | Several times per year |
| 5 Almost certain | Monthly or more |

| Impact | Guide (information security) |
|---|---|
| 1 Negligible | No sensitive data; brief inconvenience |
| 2 Minor | Limited internal data; recoverable < 1 day |
| 3 Moderate | Regulated or customer data; multi-day recovery |
| 4 Major | Large breach, regulatory notice, material revenue hit |
| 5 Severe | Existential, safety, or systemic failure |

**Inherent score** = likelihood × impact **before** controls. **Residual** = after controls, with documented control effectiveness (full / partial / none).

## Inherent vs residual

1. Score inherent from threat + vulnerability without assuming controls.
2. List **existing controls** (preventive, detective, corrective).
3. Adjust likelihood and/or impact for **effective** controls only—cite evidence (config, test, audit).
4. Residual above appetite → treatment required or formal acceptance.

Re-score when: major architecture change, control failure, incident, or audit finding.

## FAIR-style quantitative framing

Use when leadership requires **loss exposure** in currency:

- **Loss event frequency (LEF)** × **loss magnitude (LM)** → annualized loss exposure (ALE)
- Decompose LM: primary response, secondary (fines, churn), fines where applicable
- Document assumptions; ranges beat false precision
- Calibrate with historical incidents and industry benchmarks where available

Qualitative heat maps and FAIR estimates may coexist for the same portfolio—label methodology per row.

## Risk appetite and escalation

Document organizational **appetite** (acceptable residual band) per category (e.g., customer data, OT, third party).

| Residual band | Typical action |
|---|---|
| Within appetite | Monitor via KRI |
| Above appetite | Mitigation plan or transfer |
| Critical | Risk committee within 30 days |
| Beyond board threshold | Board or delegate approval for acceptance |

Never accept **critical** residual without named executive approver and expiry.

## Common mistakes

- Scoring controls instead of scenarios
- Residual = inherent because controls are "planned" not implemented
- Ignoring **concentration** (one vendor, one region, one key person)
- Using audit **compliance pass** as proof of low residual risk without threat context
