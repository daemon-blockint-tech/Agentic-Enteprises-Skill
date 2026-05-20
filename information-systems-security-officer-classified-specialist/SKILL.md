---
name: information-systems-security-officer-classified-specialist
description: |
  Guides Information Systems Security Officer (ISSO) work for classified systems and enclaves—system
  security plan (SSP), control status, continuous monitoring, POA&M, assessor coordination, authorization
  packages, change impact, vulnerability interfaces, incident reporting to ISSM/PM, common control
  inheritance, documentation-level boundaries. Cleared environments; cross-domain rules at high level. Use
  when acting as ISSO, maintaining SSP or POA&M, supporting A&A or RMF, coordinating assessors, control
  inheritance, classified boundaries, or ATO packages—not classified portfolio
  (classified-cyber-security-senior-manager), CISO/board (chief-information-security-officer), SOC
  (soc-analyst), IR (incident-responder), engineering (information-security-engineer), audit automation
  (compliance-engineer), enterprise GRC (compliance-specialist), reference architecture
  (enterprise-security-architect), risk registers (security-risk-analyst), CISSP prep
  (certified-information-systems-security-professional).
---

# Information Systems Security Officer (ISSO) — Classified Specialist

## When to Use

- **Steward** the system security plan (SSP) — scope, boundaries, control narratives, inheritance
- **Track** control implementation status and evidence pointers for the authorization boundary
- **Operate** continuous monitoring — ongoing control effectiveness, significant changes, deviations
- **Manage** POA&M entries — milestones, risk ratings, closure evidence, assessor questions
- **Support** assessment and authorization — readiness packages, assessor requests, remediation plans
- **Analyze** change impact on security posture — patches, architecture, data flows, interconnections
- **Interface** with vulnerability management — scan cadence, findings triage, POA&M linkage
- **Report** security incidents and anomalies to ISSM, PM, or AO per program procedures
- **Document** classified boundaries and interconnections at the documentation level (not engineering design)
- **Coordinate** inheritance from common controls, leveraged authorizations, and shared services

## When NOT to Use

- Lead the entire classified cyber portfolio, staffing, or multi-system program → `classified-cyber-security-senior-manager`
- Set enterprise security strategy, board briefings, or risk appetite → `chief-information-security-officer`
- Triage SOC alerts or run shift operations → `soc-analyst`
- Command active incident response, containment, or forensics → `incident-responder`
- Deploy IAM, SIEM, EDR, hardening, or remediate technical findings → `information-security-engineer`
- Build enterprise audit evidence pipelines or automate SOC 2/ISO control tests → `compliance-engineer`
- Own enterprise GRC program charter, framework scope, or vendor questionnaire programs → `compliance-specialist`
- Define enterprise reference architecture, zero-trust patterns, or ARB standards → `enterprise-security-architect`
- Build FAIR-style risk registers and treatment scoring → `security-risk-analyst`
- Study for CISSP certification without system authorization work → `certified-information-systems-security-professional`

## Related skills

| Need | Skill |
|---|---|
| Classified portfolio program management | `classified-cyber-security-senior-manager` |
| Executive security strategy and board reporting | `chief-information-security-officer` |
| Enterprise GRC scope, gap plans, audit prep | `compliance-specialist` |
| Technical control mapping and evidence automation | `compliance-engineer` |
| Control implementation and tooling | `information-security-engineer` |
| Enterprise security reference architecture | `enterprise-security-architect` |
| Declared incident response execution | `incident-responder` |
| Risk registers and residual risk scoring | `security-risk-analyst` |

## Core Workflows

### 1. Establish system context

1. Confirm authorization boundary, classification level, and data categories in scope
2. Identify system owner, ISSM, AO, and assessor points of contact
3. Map inherited vs system-specific controls and leveraged authorizations
4. Load current SSP, POA&M, and last authorization decision artifacts

**See `references/isso_classified_scope.md`.**

### 2. SSP and control inheritance

1. Align SSP sections with program templates (boundary, architecture, controls, procedures)
2. Document control inheritance from common control providers with pointers, not duplication
3. Keep control narratives testable — who, what frequency, evidence location
4. Flag gaps between as-implemented state and selected baseline

**See `references/ssp_and_control_inheritance.md`.**

### 3. Continuous monitoring and POA&M

1. Run monthly (or program-defined) control effectiveness checks
2. Record significant changes and security-relevant events in the monitoring plan
3. Open, update, and close POA&M items with verifiable milestones
4. Escalate overdue or high-risk POA&M items to ISSM and system owner

**See `references/continuous_monitoring_and_poams.md`.**

### 4. Assessment and authorization support

1. Prepare authorization package index — SSP, SAP, SAR inputs, POA&M, contingency plans
2. Track assessor data calls and evidence due dates
3. Draft remediation plans for findings with realistic dates and owners
4. Support AO decision briefs — residual risk, POA&M acceptability, continuous monitoring commitment

**See `references/assessment_and_authorization_support.md`.**

### 5. Classified boundaries and operations

1. Maintain documentation-level boundary and interconnection diagrams (no export-controlled detail)
2. Apply program rules for classified processing, storage, and transmission at a high level
3. Coordinate cross-domain or controlled interface changes through designated authorities
4. Align physical, personnel, and technical security references in SSP without duplicating classified specs

**See `references/classified_boundaries_and_operations.md`.**

### 6. Stakeholder coordination and reporting

1. Run cadence with system owner, ISSM, AO staff, and control implementers
2. Report incidents and security-relevant events per program timelines
3. Brief leadership on posture, POA&M aging, and authorization risk between assessments
4. Hand off engineering work to implementers; retain package ownership and traceability

**See `references/stakeholder_coordination_and_reporting.md`.**

## Output Standards

- Use program templates for SSP updates, POA&M rows, and authorization correspondence
- Cite control IDs, evidence locations, and dates — avoid unattributed status claims
- Mark classification of deliverables per program marking guidance; do not paste classified content into unclassified channels
- Separate **facts** (scan dates, finding counts) from **judgments** (residual risk recommendations)
- Do not provide legal conclusions, attest on behalf of the AO, or substitute for official security classification guidance

## Reference Files

| File | Use when |
|---|---|
| `references/isso_classified_scope.md` | Role boundaries, RACI, minimum artifacts |
| `references/ssp_and_control_inheritance.md` | SSP structure, inheritance, narratives |
| `references/continuous_monitoring_and_poams.md` | ConMon cadence, POA&M lifecycle |
| `references/assessment_and_authorization_support.md` | A&A packages, assessor coordination |
| `references/classified_boundaries_and_operations.md` | Boundaries, cross-domain, classified ops |
| `references/stakeholder_coordination_and_reporting.md` | ISSM/AO/PM reporting and cadence |
