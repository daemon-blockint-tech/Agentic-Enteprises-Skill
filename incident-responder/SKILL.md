---
name: incident-responder
description: |
  Guides CSIRT-style security incident response—declaring incidents, scoping and severity,
  timeline reconstruction, evidence preservation, containment/eradication/recovery coordination,
  stakeholder communication templates, post-incident review, lessons learned, and regulatory
  notification preparation (not legal advice).
  Use when a security incident is declared or suspected, coordinating active IR, building incident
  timelines, preserving forensic evidence, drafting internal/exec/customer IR updates, running
  blameless post-incident reviews, or preparing breach-notification fact packs for legal/compliance—not
  for routine SOC alert triage (soc-analyst), incident program/on-call/paging design
  (incident-management-engineer), enterprise security strategy or ISMS (cybersecurity,
  information-security-engineer), pentest (penetration-tester), adversary simulation
  (red-team-specialist), LLM red team (ai-redteam), binary RE (reverse-engineer), audit evidence
  (compliance-engineer), or CI pipeline gates (devsecops).
---

# Incident Responder (CSIRT)

## When to Use

- **Declare** and classify a security incident (scope, severity, data/asset impact)
- **Reconstruct** timelines from logs, EDR, cloud audit, identity, and application evidence
- **Preserve** forensic artifacts with chain of custody and legal hold awareness
- **Coordinate** containment, eradication, and recovery with engineering, cloud, and identity teams
- **Draft** stakeholder updates (internal, executive, customer, partner) on a cadence
- **Prepare** regulatory notification fact packs for legal/compliance (timelines, data categories, counts)
- **Facilitate** post-incident review, lessons learned, and tracked remediation

## When NOT to Use

- Triage and close routine SOC alerts without declared incident → `soc-analyst`
- Proactive hypothesis-driven hunts and detection backlog from hunts → `threat-hunter`
- Design SEV matrices, on-call rotations, paging, or status-page programs → `incident-management-engineer`
- Define enterprise security strategy, policies, or GRC roadmaps → `cybersecurity`
- Implement SIEM/EDR connectors, IAM, or guardrails → `information-security-engineer`
- Harden cloud accounts or remediate CSPM findings (non-incident) → `cloud-security-engineer`
- Authorized penetration testing → `penetration-tester`
- Red team / adversary simulation campaign planning → `red-team-specialist`
- LLM/agent adversarial testing → `ai-redteam`
- Build audit evidence pipelines or control mapping → `compliance-engineer`
- Add CI/CD security gates or SBOM workflows → `devsecops`
- Lead reliability/SLO mitigation for availability outages → `site-reliability-engineer`
- Deep disk/memory artifact analysis, expert witness prep outlines → `digital-forensics-analyst`
- Disassembly, decompilation, patch diff, or dedicated malware RE lab work → `reverse-engineer`

## Related skills

| Need | Skill |
|---|---|
| SOC alert triage, initial investigation, escalation to CSIRT | `soc-analyst` |
| Proactive threat hunts, hunt reports, detection feedback before/during IR | `threat-hunter` |
| Incident program, SEV definitions, on-call, paging, postmortem process | `incident-management-engineer` |
| Security strategy, IR policy, board narratives | `cybersecurity` |
| SIEM/EDR/IdP implementation and tooling | `information-security-engineer` |
| Cloud forensics logs, account isolation, KMS | `cloud-security-engineer` |
| Pentest validation of fixes | `penetration-tester` |
| Red team / purple team exercises | `red-team-specialist` |
| LLM/agent incident reproduction and safety retest | `ai-redteam` |
| Breach notification legal thresholds and audit evidence | `compliance-engineer` |
| Pipeline compromise, secrets in CI, artifact integrity | `devsecops` |
| Customer-facing crisis messaging approval | `communication-lead` |
| Availability outage and SLO impact | `site-reliability-engineer` |
| BCP/DRP, RTO/RPO, ransomware recovery sequencing, restore tests | `bcm-disaster-recovery-specialist` |
| Forensic acquisition, super-timelines, investigation reports for counsel | `digital-forensics-analyst` |
| Binary/protocol RE, patch analysis, defensive malware deep dive | `reverse-engineer` |
| Operational intel, campaign context, IOC packages during IR | `cti-analyst` |

## Core Workflows

### 1. Intake and declaration

1. Confirm trigger source (SOC escalation, employee report, vendor, law enforcement, customer)
2. Assign incident ID; open record and comms channel
3. Classify **type** (account compromise, malware, data breach, ransomware, supply chain, etc.)
4. Set **severity** from impact and urgency; document rationale
5. Notify incident commander, legal, and comms per severity matrix

**See `references/incident_declaration_and_severity.md`.**

### 2. Scope and timeline

1. Identify affected users, systems, accounts, regions, and data classes
2. Establish **first known compromise** and **detection** timestamps (UTC)
3. Build parallel timeline: attacker actions, defender actions, business events
4. List evidence sources still available; flag gaps and retention risks
5. Update scope statement when new facts emerge (version each change)

**See `references/timeline_and_evidence_handling.md`.**

### 3. Containment → eradication → recovery

1. **Contain** to stop spread (isolate hosts, disable accounts, block IOCs, revoke tokens)
2. **Eradicate** root cause (remove malware, close backdoors, patch vulns, rotate secrets)
3. **Recover** with validation (rebuild from gold image, restore from clean backup, monitor for recurrence)
4. Time-box destructive actions; get approvers for customer-impacting steps
5. Hand off long-term hardening to owning engineering/security skills

**See `references/containment_eradication_recovery.md`.**

### 4. Stakeholder and regulatory communications

1. Set update cadence by severity (e.g., 30–60 min for SEV1 security)
2. Separate **facts** from **hypotheses** in every update
3. Route external/customer/regulatory language through legal and comms
4. Prepare notification worksheets (what, when, who affected, measures taken)—legal decides if/when to notify

**See `references/stakeholder_and_regulatory_comms.md`.**

### 5. Post-incident review

1. Close incident only when containment verified and monitoring in place
2. Run blameless review within agreed SLA (e.g., 5 business days for major incidents)
3. Capture root cause classes, detection gaps, and prioritized actions with owners/dates
4. Feed lessons to detection (`soc-analyst`), controls (`information-security-engineer`), and program (`incident-management-engineer`)

**See `references/post_incident_review.md`.**

## When to load references

- **Role boundaries and handoffs** → `references/incident_responder_scope.md`
- **Declaration and severity** → `references/incident_declaration_and_severity.md`
- **Timeline and evidence** → `references/timeline_and_evidence_handling.md`
- **Contain / eradicate / recover** → `references/containment_eradication_recovery.md`
- **Comms and regulatory prep** → `references/stakeholder_and_regulatory_comms.md`
- **Post-incident review** → `references/post_incident_review.md`

## Outputs

- **Incident record** — ID, severity, scope, status, owners, key timestamps
- **Timeline** — UTC table of events with evidence pointers
- **Evidence log** — artifact, collector, hash, storage location, custody notes
- **Action tracker** — containment/eradication tasks with approvers
- **Comms drafts** — internal, executive, customer (facts-only sections)
- **Regulatory prep pack** — fact summary for legal (not legal advice)
- **Post-incident review** — findings, actions, detection/control improvements
