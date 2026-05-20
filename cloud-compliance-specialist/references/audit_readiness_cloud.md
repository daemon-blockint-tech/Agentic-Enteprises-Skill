# Audit readiness and customer assurance

## Table of contents

1. [Pre-audit checklist](#pre-audit-checklist)
2. [Assessor walkthrough](#assessor-walkthrough)
3. [Customer questionnaires](#customer-questionnaires)
4. [Gap remediation](#gap-remediation)

## Pre-audit checklist

4–6 weeks before observation end:

- [ ] Scope memo current (accounts, regions, services)
- [ ] Control-evidence matrix complete; owners assigned
- [ ] CCM critical findings at zero or excepted
- [ ] CloudTrail/org logs retained full period
- [ ] Access reviews completed with sign-off
- [ ] Backup/restore test evidence for in-scope data
- [ ] Provider SOC/BAA/AOC artifacts versioned
- [ ] Sample populations defined and dry-run collected
- [ ] Narratives drafted for inherited vs customer controls

## Assessor walkthrough

Agenda (60–90 min technical session):

1. Architecture and scope (diagram, data flow)
2. Shared responsibility matrix
3. IAM and access (live console read-only or exports)
4. Logging and monitoring (trail query demo)
5. Encryption (KMS, default encryption)
6. Change management link to CI (`devsecops` evidence)
7. CCM dashboard and recent remediations
8. Q&A log with follow-up owners

Prepare **read-only** role; no production changes during session.

## Customer questionnaires

CAIQ, SIG, VSA responses:

- Reuse **control library** answers mapped to cloud evidence
- Attach **latest** Config/Security Hub summary (redacted)
- Reference provider compliance artifacts where allowed under NDA
- Do not overclaim inherited controls — state customer configuration explicitly
- Align answers with **actual** regions and services sold

Legal review for contractual commitments → `commercial-counsel`.

## Gap remediation

Gap lifecycle:

1. **Identify** — internal assessment, CCM, or assessor draft
2. **Classify** — observation vs finding; severity
3. **Remediate** — `cloud-security-engineer` implements; compliance verifies evidence
4. **Validate** — re-run rule or assessor re-test
5. **Close** — evidence attached to control ID

Track open gaps in shared register with due dates before **report issuance**.

For org-wide gaps spanning non-cloud → escalate to `compliance-engineer`.
