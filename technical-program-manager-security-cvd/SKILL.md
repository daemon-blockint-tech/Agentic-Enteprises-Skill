---
name: technical-program-manager-security-cvd
description: |
  Guides technical program management for security coordinated vulnerability disclosure (CVD)—
  disclosure policy, intake and triage SLAs, researcher coordination, fix/remediation tracking,
  embargo and publication timelines, CVE/advisory coordination, bug bounty program operations,
  and cross-functional gates (security engineering, legal, comms, product).
  Use when running a CVD or responsible disclosure program, disclosure calendar, bounty ops,
  or unblocking multi-team remediation for reported vulnerabilities—not for hands-on pentest
  (offensive-security-analyst), SOC triage (defensive-security-analyst), vuln scanning in CI
  (devsecops), enterprise security strategy (cybersecurity), generic non-security programs
  (technical-program-manager), or contract redlines (commercial-counsel).
---

# Technical Program Manager, Security (Coordinated Vulnerability Disclosure)

## When to Use

- Stand up or improve **CVD / responsible disclosure** policy and operating model
- Run **intake triage** queue (email, portal, bounty platform) with SLAs
- Coordinate **researcher** communication, extensions, and safe harbor questions
- Track **remediation** milestones across product and platform teams
- Manage **embargo**, coordinated disclosure date, and publication checklist
- Operate **bug bounty** scope, rewards, and platform workflows
- Produce **program status**, RAID, and steering updates for security leadership
- Plan **advisory/CVE** release with legal and communications

## When NOT to Use

- Execute authorized exploitation or write PoCs → `offensive-security-analyst`
- Triage SOC alerts or tune detections → `defensive-security-analyst`
- Implement scanner gates, SBOM, pipeline fixes → `devsecops`
- Remediate findings in code (own the fix) → `information-security-engineer`, `senior-software-engineer`
- Enterprise security architecture or GRC strategy → `cybersecurity`, `compliance-engineer`
- Generic multi-team delivery (non-security) → `technical-program-manager`
- Customer contract security exhibits → `commercial-counsel`
- Public crisis comms narrative (non-advisory) → `communication-lead`

## Related skills

| Need | Skill |
|---|---|
| Generic TPM patterns (charter, RAID, status) | `technical-program-manager` |
| Security strategy and vuln management program | `cybersecurity` |
| Fix implementation and validation in infra | `information-security-engineer` |
| Pipeline scanning and CI evidence | `devsecops` |
| Pentest / offensive validation | `offensive-security-analyst` |
| Legal terms for bounty / safe harbor | `commercial-counsel` |
| Public messaging for security incidents | `communication-lead` |
| Audit evidence for vuln SLAs | `compliance-engineer` |
| AI-specific red team findings | `ai-redteam` |

## Core Workflows

### 1. CVD program charter

Policy scope, channels, SLAs, roles, escalation.

**See `references/program_charter_cvd.md`.**

### 2. Intake and triage

Receive report, dedupe, severity, assign DRI, researcher ack.

**See `references/intake_triage.md`.**

### 3. Remediation and validation tracking

Fix milestones, retest, waiver/exception path.

**See `references/remediation_tracking.md`.**

### 4. Coordinated disclosure timeline

Embargo, extensions, publication date, multi-party coordination.

**See `references/disclosure_timeline.md`.**

### 5. Advisory and publication

CVE, advisory draft, legal/comms gates, customer notification.

**See `references/advisory_publication.md`.**

### 6. Bug bounty operations

Scope, rewards, platform hygiene, researcher relations.

**See `references/bug_bounty_operations.md`.**

## Outputs

Prefer structured artifacts:

- **Intake record** — reporter, asset, severity, status, DRI, dates
- **Disclosure tracker** — embargo end, parties, blockers, go/no-go
- **Weekly program status** — inflow, SLA breaches, aging criticals, upcoming publications
- **RAID** — risks (premature leak, incomplete fix), actions, decisions (severity disputes)
- **Publication checklist** — signed advisory, CVE, comms, support/KB, bounty payout

## Principles

- **Coordinated disclosure by default** — align publication with fix readiness unless active exploitation forces earlier notice
- **Single intake DRI** — one queue owner; engineering DRIs per product/component
- **Document researcher comms** — timestamps, promises, extension rationale
- **No legal advice** — route safe harbor, bounty terms, and advisory language to qualified counsel
- **Separate incident response** — active exploitation in production may parallel IR (`incident-management-engineer`) while CVD track continues
