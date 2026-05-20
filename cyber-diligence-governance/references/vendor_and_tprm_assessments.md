# Vendor and TPRM assessments

## Table of contents

1. [Assessment triggers](#assessment-triggers)
2. [Vendor tiers](#vendor-tiers)
3. [Depth of review by tier](#depth-of-review-by-tier)
4. [Assessment workflow](#assessment-workflow)
5. [Concentration and fourth parties](#concentration-and-fourth-parties)
6. [Renewal and offboarding](#renewal-and-offboarding)
7. [Alignment with compliance-specialist](#alignment-with-compliance-specialist)

## Assessment triggers

Run or refresh assessment when:

- New vendor processes **sensitive** or **regulated** data
- Production access, source code, or customer-facing dependency
- Material contract (revenue, exclusivity, multi-year)
- **M&A** introduces new subprocessors
- Incident, breach notification, or certification lapse at vendor
- Change in processing location, subprocessors, or AI/ML use of customer data

## Vendor tiers

| Tier | Criteria | Review cadence |
|---|---|---|
| Critical | Sensitive data, prod access, or single-point failure | Annual + contract events |
| High | Material subprocessors in customer/audit scope | Annual |
| Medium | Limited data, no prod access | Every 2 years |
| Low | No sensitive data, commodity SaaS | Onboarding questionnaire only |

Document tier rationale in vendor record. Align with `compliance-specialist` subprocessors list for audit scope.

## Depth of review by tier

| Tier | Typical artifacts |
|---|---|
| Critical | SIG/CAIQ + SOC 2 Type II (in date) + pen test summary + interview + architecture diagram |
| High | Questionnaire + SOC/ISO + incident attestation |
| Medium | Short questionnaire + certification or public trust page |
| Low | Security page + DPA template check |

Escalate to **full diligence** (M&A-style) when acquiring vendor technology or assuming their infrastructure.

## Assessment workflow

1. **Intake** — business owner, data types, integrations, contract value
2. **Tier** — apply criteria; security lead confirms
3. **Collect** — questionnaire, reports under NDA, supplemental questions
4. **Analyze** — gaps vs baseline; red flags (see `references/red_flags_and_remediation.md`)
5. **Decide** — approve, approve with conditions, reject, or escalate
6. **Record** — assessment date, approver, conditions, re-review date
7. **Monitor** — cert expiry, breach news, subprocessors change

**Legal terms** (indemnity, liability, audit rights) → `commercial-counsel`.

**Technical validation** (encryption, logging claims) → `information-security-engineer` or `cloud-security-engineer`.

## Concentration and fourth parties

Track:

- Shared IdP, cloud, CDN, or payment processor across critical vendors
- **Fourth parties** listed in vendor SOC reports
- Geographic concentration (residency, sanctions exposure — coordinate with legal/compliance)

Report concentration in governance packs when it affects **blast radius** of a single supplier failure.

## Renewal and offboarding

| Event | Action |
|---|---|
| Renewal | Re-tier; refresh questionnaire if >12 months or post-incident |
| Scope change | New data or prod access → re-assess at higher tier |
| Offboarding | Data return/deletion attestation, access revocation checklist, key rotation |

Feed residual vendor risk into `security-risk-analyst` register when material.

## Alignment with compliance-specialist

- Use **approved response library** and evidence pointers maintained under GRC program where they exist
- Do not invent certification scope; match SOC/ISO report period and trust criteria
- For **customer-facing** questionnaires (your company as vendor), coordinate outbound responses with `compliance-specialist` workflow in `compliance-specialist/references/vendor_and_continuous_compliance.md`
- This skill emphasizes **inbound** evaluation of others and **deal-time** depth; compliance-specialist owns **program** rhythm and audit alignment
