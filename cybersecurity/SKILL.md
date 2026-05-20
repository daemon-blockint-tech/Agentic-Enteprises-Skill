---
name: cybersecurity
description: |
  Guides enterprise cybersecurity across security architecture, control design, vulnerability and
  threat management, incident response, identity security, and GRC alignment (SOC 2, ISO 27001, NIST CSF).
  Use when defining security strategy, assessing risk, designing defense-in-depth, running security
  incidents, scoping penetration tests, writing security policies, or high-level GRC strategy—not for
  hands-on audit evidence automation (compliance-engineer), GRC program/audit prep
  (compliance-specialist),
  embedding scans in CI/CD (devsecops), provisioning cloud networks (infrastructure-engineer), or
  LLM or enterprise red team (ai-redteam, red-team-specialist), binary RE (reverse-engineer),
  web/API pentest (web-pentester), or on-call/SEV program
  (incident-management-engineer).
---

# Cybersecurity

## When to Use

- Define enterprise security strategy, policy, and control architecture
- Assess risk across identity, infrastructure, applications, vendors, and incident readiness
- Design defense-in-depth programs aligned to NIST CSF, ISO 27001, SOC 2, or similar frameworks
- Scope penetration tests, vulnerability management programs, or security incident response
- Prepare high-level GRC, board, or leadership security narratives

## When NOT to Use

- GRC program, framework scope, gap plans, audit prep → `compliance-specialist`
- Implement audit evidence automation or control-by-control mapping → `compliance-engineer`
- Add SAST, SBOM, OIDC, or pipeline security gates → `devsecops`
- Triage SOC alerts, SIEM queues, or SOAR cases → `soc-analyst`
- Proactive threat hunts and hunt program design → `threat-hunter`
- Alert-driven investigation and detection tuning → `defensive-security-analyst`
- Execute authorized penetration tests or PoCs → `penetration-tester`
- Lead red team / adversary simulation campaigns → `red-team-specialist`
- Execute web/API OWASP assessments → `web-pentester`
- Hands-on binary, firmware, or protocol reverse engineering → `reverse-engineer`
- Provision cloud networks, clusters, or infrastructure modules → `infrastructure-engineer`
- Design application integration ADRs → `senior-system-architecture`

## Related skills

| Need | Skill |
|---|---|
| Pipeline scanning, SBOM, CI OIDC | `devsecops` |
| Cloud/K8s hardening implementation | `infrastructure-engineer` |
| AI model risk, policies, EU AI Act | `ai-risk-governance` |
| LLM jailbreaks and prompt injection tests | `ai-redteam` |
| SOC alert triage, playbooks, shift handoffs | `soc-analyst` |
| Proactive threat hunts, ATT&CK campaigns, hunt metrics | `threat-hunter` |
| Alert investigation, detection tuning, DFIR depth | `defensive-security-analyst` |
| Authorized pentest, exploitation, retest | `penetration-tester` |
| CTI function, intel briefs, IOC/TTP production, ISAC sharing | `cti-analyst` |
| Red team, purple team, adversary simulation | `red-team-specialist` |
| Binary RE, patch diff, defensive malware analysis | `reverse-engineer` |
| Network/AD/infra pentest methodology | `network-pentester` |
| Web/API pentest methodology | `web-pentester` |
| Web/API OWASP and proxy-based pentest | `web-pentester` |
| Implement IAM, encryption, SIEM, guardrails | `information-security-engineer` |
| Product multi-tenancy, customer data plane security | `product-infrastructure-security-engineer` |
| GRC program, audit prep, vendor questionnaires | `compliance-specialist` |
| Control implementation, audit evidence automation | `compliance-engineer` |
| On-call, SEV, postmortem, paging integrations | `incident-management-engineer` |
| Active security incident response (CSIRT) | `incident-responder` |
| SOC alert triage | `soc-analyst` |
| Vendor/customer contract security exhibits and DPAs | `commercial-counsel` |
| Solution architecture review (app layer) | `senior-system-architecture` |
| Applied AI / LLM commercial & enterprise architecture | `applied-ai-architect-commercial-enterprise` |
| Crisis and security incident messaging | `communication-lead` |
| Data center facility design and commissioning | `data-center-design-execution-lead` |
| CVD, bounty, disclosure calendar | `technical-program-manager-security-cvd` |
| Evidence acquisition, super-timelines, forensic reports for legal/IR | `digital-forensics-analyst` |
| Risk registers, residual scoring, committee/board risk narrative | `security-risk-analyst` |
| BCM/DRP, RTO/RPO, ransomware recovery, restore tests, tabletops | `bcm-disaster-recovery-specialist` |

## Core Workflows

### 1. Security architecture and control design

1. Identify assets, data classes, and trust boundaries
2. Apply defense-in-depth: prevent, detect, respond, recover
3. Map controls to framework (NIST CSF, ISO 27001 Annex A)
4. Document accepted risks with owner and review date
5. Validate with architecture review before major launches

**See `references/security_architecture.md` for control catalogs and network zoning.**

### 2. Vulnerability and exposure management

**Program cadence:**

| Activity | Frequency |
|---|---|
| External attack surface review | Monthly |
| Vuln scan aggregation + triage | Weekly |
| Patch SLA tracking | Continuous |
| Penetration test | Annual + major changes |

Prioritize: exploitability × exposure × asset criticality.

**See `references/vuln_threat_management.md` for SLAs, pentest scope, and threat intel use.**

### 3. Identity and access security

- Enforce MFA for all human access; phishing-resistant where possible
- Least privilege; periodic access reviews (quarterly for prod)
- Separate break-glass accounts; log and alert on use
- Service accounts: scoped credentials, rotation, no shared passwords

**See `references/identity_access.md` for IAM patterns and PAM considerations.**

### 4. Security incident response

**Phases:** prepare → detect → analyze → contain → eradicate → recover → post-incident.

| Severity | Examples | Response target |
|---|---|---|
| SEV1 | Active breach, ransomware | Immediate, 24/7 |
| SEV2 | Confirmed intrusion attempt | < 1 hour |
| SEV3 | Policy violation, malware contained | Same business day |
| SEV4 | Recon, blocked attack | Track and trend |

**See `references/incident_response.md` for playbooks and evidence preservation.**

### 5. GRC and audit support

- Maintain control matrix linked to evidence
- Track exceptions/waivers with expiry
- Coordinate with legal on breach notification thresholds
- Align third-party risk with vendor reviews

**See `references/grc_compliance.md` for SOC 2 / ISO mapping and audit artifacts.**

## When to load references

- **Architecture and controls** → `references/security_architecture.md`
- **Vulns, pentest, threats** → `references/vuln_threat_management.md`
- **IAM and access** → `references/identity_access.md`
- **Incidents** → `references/incident_response.md`
- **GRC and audits** → `references/grc_compliance.md`
