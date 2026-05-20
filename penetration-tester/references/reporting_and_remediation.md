# Reporting and remediation

## Table of contents

1. [Report structure](#report-structure)
2. [Finding template](#finding-template)
3. [Executive summary](#executive-summary)
4. [Remediation guidance](#remediation-guidance)
5. [Handoff](#handoff)

## Report structure

Deliverables (per SOW):

1. **Executive summary** — risk posture, top issues, business impact (non-technical audience)
2. **Technical report** — all findings with reproduction and evidence
3. **Appendices** — scope, ROE, tools, glossary, cleanup attestation
4. **Retest plan** — dates and criteria for critical/high (if included)

Use consistent finding IDs across report, ticket system, and retest.

## Finding template

| Field | Guidance |
|---|---|
| **ID** | Stable (e.g., PT-2026-014) |
| **Title** | Specific and readable |
| **Severity** | Per agreed rubric |
| **CVSS** | Optional; explain if used |
| **Affected assets** | Host, URL, parameter, cloud resource |
| **Description** | What is wrong and why it matters |
| **Impact** | Confidentiality, integrity, availability, compliance |
| **Preconditions** | Auth, network, config |
| **Steps to reproduce** | Numbered, minimal |
| **Evidence** | Redacted screenshots, requests, hashes |
| **Remediation** | Specific fix (config, code pattern, control) |
| **References** | CWE, OWASP, vendor docs |
| **Retest criteria** | Observable pass condition |

## Executive summary

Include:

- Engagement type, dates, and scope summary
- Overall risk rating (qualitative)
- Count by severity
- Top 3–5 themes (e.g., broken access control, secrets in repos)
- Positive observations (defenses that worked)
- Recommended prioritization for remediation

Avoid jargon; link to technical section for detail.

## Remediation guidance

Write remediation **actionable for engineering**:

| Weakness | Weak remediation | Strong remediation |
|---|---|---|
| IDOR | "Fix access control" | Enforce server-side object ownership check on `orderId`; add integration test |
| SQLi | "Use prepared statements" | Parameterize query in `UserDAO.find`; SAST rule; WAF as defense in depth |
| Cloud IAM | "Reduce permissions" | Replace `*:*` with least-privilege policy attached to role X |

Note **compensating controls** already present and what remains exploitable.

## Handoff

| Audience | Provide |
|---|---|
| Engineering | Technical report + tickets per finding |
| Leadership | Executive summary |
| `information-security-engineer` / `cloud-security-engineer` | Control-oriented fixes for platform issues |
| `compliance-engineer` | Factual summary only if audit timeline requires; not legal attestation |
| SOC (optional) | IOCs or test IPs used; expected alert volume |

Schedule **readout**; capture questions and scope for retest.
