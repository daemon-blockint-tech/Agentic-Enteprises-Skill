# Evidence and attestation review

## Table of contents

1. [Evidence hierarchy](#evidence-hierarchy)
2. [SOC 2 review](#soc-2-review)
3. [ISO 27001 review](#iso-27001-review)
4. [Penetration test summaries](#penetration-test-summaries)
5. [Trust centers and security pages](#trust-centers-and-security-pages)
6. [Bridge letters and gaps](#bridge-letters-and-gaps)
7. [Subprocessors and fourth parties](#subprocessors-and-fourth-parties)

## Evidence hierarchy

Prefer stronger evidence for T1 claims:

1. Independent attestation (SOC 2 Type II, ISO certificate + SoA summary)
2. Third-party pen test **executive summary** or attestation letter (scoped to service)
3. Detailed security whitepaper with named standards mapping
4. Trust center assertions without report
5. Questionnaire self-attestation alone — insufficient for T1 material controls

Record **evidence date**, **scope**, and **reviewer**; set expiry aligned to report period end.

## SOC 2 review

Check:

- **Report type** — Type I vs Type II; prefer Type II for T1
- **Period covered** — reject if ended >12 months ago without bridge
- **Trust services criteria** — Security minimum; Availability/Confidentiality as contracted
- **Scope description** — systems and services **you consume** included
- **Subservice organizations** — carved-in vs carved-out; impact on your risk
- **Exceptions** — map each to finding severity
- **Complementary user entity controls (CUEC)** — assign internal owners

Do not treat SOC 2 as **zero findings**; exceptions and CUECs drive remediation.

## ISO 27001 review

Check:

- Certificate validity and certification body
- **Statement of Applicability** — controls excluded with justification
- Scope statement vs your integration
- Alignment to questionnaire answers on ISMS topics

## Penetration test summaries

Validate:

- **Test date** and retest of critical findings
- **Scope** includes the SaaS/product line you use
- **Methodology** (external, authenticated app, API)
- **Critical/high** open items and vendor remediation status

Pentest letters are **input** to vendor risk, not a substitute for your own testing (`penetration-tester` when contractually required).

## Trust centers and security pages

Use for T3/T4 or preliminary T1 screening only. Note:

- Last updated date
- Certifications claimed vs documents offered under NDA
- Subprocessor list presence
- Incident history disclosure

Upgrade to full attestation before production for T1.

## Bridge letters and gaps

When report period lapsed:

- Require **bridge letter** from auditor or vendor management assertion
- List **changes** since last report (breaches, architecture, subprocessors)
- Shorten re-assessment interval until new Type II received

## Subprocessors and fourth parties

For T1 vendors:

- Obtain subprocessor list with **purpose** and **location**
- Flag **concentration** (same hyperscaler, same IdP, same email security vendor)
- Inherit subprocessors into scenario library (e.g., unknown subprocessor breach)
- Require notification clauses in tier guidance for legal—not legal drafting here

If subprocessors are carved out of SOC scope, treat as **increased inherent risk** until evidenced.
