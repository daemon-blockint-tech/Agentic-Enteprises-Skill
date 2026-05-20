# Continuous monitoring and incidents

## Table of contents

1. [Monitoring scope](#monitoring-scope)
2. [Signal sources](#signal-sources)
3. [Alert handling](#alert-handling)
4. [Vendor incidents](#vendor-incidents)
5. [Re-assessment triggers](#re-assessment-triggers)
6. [Concentration monitoring](#concentration-monitoring)

## Monitoring scope

Prioritize **T1 and T2** vendors for continuous monitoring; sample T3 on change. Monitoring supplements—not replaces—periodic assessment.

## Signal sources

| Signal | Typical action |
|---|---|
| Public breach disclosure | Incident review; customer notification per IR policy |
| Security rating drop (commercial feeds) | Validate; request updated evidence |
| Cert / SOC report expiry | Block renewal or require bridge |
| Material news (M&A, bankruptcy, sanctions) | Re-tier; engage procurement |
| Subprocessor change notices | Update fourth-party register |
| Vulnerability in vendor product (CVE) | Impact analysis on your integration |

Coordinate tool implementation with `information-security-engineer`; analyst defines **what to monitor**, not SIEM parser authoring.

## Alert handling

1. **Triage** — vendor tier, integration criticality, data involved
2. **Correlate** — internal logs, access paths, subprocessors
3. **Classify** — vendor-only vs potential customer impact
4. **Escalate** — IR if customer data or production at risk (`incident-responder` for active IR)
5. **Document** — timeline, decisions, vendor comms status
6. **Track** — remediation and contract protections

## Vendor incidents

When vendor reports or public sources disclose incident:

- Confirm **scope** (products, regions, data types)
- Request **root cause** and remediation timeline (vendor statement)
- Assess **your exposure** — tokens, data sets, admin sessions to revoke
- Update **assessment** and **enterprise risk register** if material
- Coordinate **customer/regulator** messaging with IR and comms—not owned here

Distinguish **vendor cyber incident** from **your misuse** of vendor APIs.

## Re-assessment triggers

Force full or partial re-assessment on:

- Confirmed breach affecting your data or service line
- Failed renewal evidence package
- Major architecture or hosting change
- New T1 subprocessor in restricted region
- Loss of ISO/SOC without replacement
- Questionnaire score regression vs prior year

## Concentration monitoring

Track portfolio-level themes:

- Single hyperscaler region for majority of production
- One IdP, one email security vendor, one backup provider
- Critical SaaS with no qualified alternate

Report concentration explicitly in executive packs; mitigation is often architectural (`information-security-engineer`) or contractual (counsel).
