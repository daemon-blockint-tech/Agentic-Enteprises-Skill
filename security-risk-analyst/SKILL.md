---
name: security-risk-analyst
description: |
  Guides information security risk analysis—risk identification and scoring, risk registers,
  threat/vulnerability/control mapping, treatment recommendations (accept/mitigate/transfer/avoid),
  third-party and supply-chain risk framing, business impact analysis, KRIs, and risk committee or
  board narratives. Aligns with ISO 27005 and NIST RMF concepts without full compliance audits.
  Use for security risk assessment, risk register maintenance, inherent/residual risk scoring,
  FAIR-style quantitative framing, treatment decisions, third-party risk tiers, or executive risk
  reporting—not SOC alert triage (soc-analyst), pentest execution (penetration-tester, web-pentester,
  network-pentester), control implementation (information-security-engineer, cloud-security-engineer),
  GRC program and audit prep (compliance-specialist), audit evidence automation
  (compliance-engineer, cloud-compliance-specialist), AI model risk programs
  (ai-risk-governance), or adversary simulation (red-team-specialist).
---

# Security Risk Analyst

## When to Use

- Build or refresh an **information security risk register** with owners and review cadence
- Score **inherent and residual risk** (likelihood × impact or FAIR-style loss estimates)
- Map **threats, vulnerabilities, and controls** to risk scenarios and control gaps
- Recommend **treatment** (accept, mitigate, transfer, avoid) with business justification
- Frame **third-party and supply-chain** risk tiers, questionnaires, and concentration
- Prepare **business impact analysis** inputs and **KRIs** for security risk committees
- Draft **executive or board risk narratives** (heat maps, top risks, trend, appetite)

## When NOT to Use

- Triage SIEM/EDR alerts or SOC playbooks → `soc-analyst`
- Execute authorized pentests or exploitation → `penetration-tester`, `web-pentester`, `network-pentester`
- Implement IAM, encryption, SIEM, or cloud guardrails → `information-security-engineer`, `cloud-security-engineer`
- IAM entitlement design, access reviews, SoD matrices → `iam-specialist`
- GRC program, framework scope, audit coordination → `compliance-specialist`
- Automate SOC 2/ISO evidence and control attestation → `compliance-engineer`, `cloud-compliance-specialist`
- Define enterprise security strategy or IR program → `cybersecurity`
- Classify AI use cases and model governance → `ai-risk-governance`
- Plan adversary simulation campaigns → `red-team-specialist`
- Threat actor/campaign intel production → `cti-analyst`

## Related skills

| Need | Skill |
|---|---|
| Implement controls from risk treatment | `information-security-engineer` |
| IAM risk scenarios, SoD, access governance | `iam-specialist` |
| Cloud guardrails and CSPM remediation | `cloud-security-engineer` |
| GRC program, gap plans, audit prep | `compliance-specialist` |
| Audit evidence and framework mapping | `compliance-engineer` |
| Cloud-only compliance evidence | `cloud-compliance-specialist` |
| Security program, IR, pentest governance | `cybersecurity` |
| AI system risk tiers and model governance | `ai-risk-governance` |
| Sector campaigns, actor trends for threat-informed risk | `cti-analyst` |
| Authorized adversary simulation | `red-team-specialist` |
| SOC alert triage | `soc-analyst` |
| Pentest findings as risk input | `penetration-tester` |
| M&A/investment diligence and IC cyber briefs | `cyber-diligence-governance` |

## Core Workflows

### 1. Risk assessment intake

1. Define **scope** (business unit, system, vendor, program)
2. Identify **assets**, data classes, and dependencies
3. Capture **threat events** and **vulnerabilities** (see references)
4. Document existing **controls** and their effectiveness
5. Score **inherent** risk (before controls) and **residual** (after controls)
6. Compare to **risk appetite** and escalation thresholds

**See `references/risk_identification_and_scoring.md`.**

### 2. Risk register maintenance

Maintain one row per material risk scenario:

| Field | Purpose |
|---|---|
| Risk ID | Stable identifier |
| Scenario | What could go wrong |
| Owner | Accountable business or tech lead |
| Inherent / residual | Scores and rationale |
| Treatment | accept / mitigate / transfer / avoid |
| Target date | For mitigation or acceptance expiry |
| KRI | Measurable indicator |

Review quarterly minimum; re-score on major change, incident, or audit finding.

**See `references/security_risk_analyst_scope.md` for boundaries.**

### 3. Threat–vulnerability–control mapping

```
threat actor/event → vulnerability/condition → impact → existing controls → gap → residual risk
```

Link pentest, vuln scan, audit, and threat intel inputs without duplicating execution work.

**See `references/threat_vulnerability_control_mapping.md`.**

### 4. Treatment and acceptance

For each risk above appetite:

1. Propose treatment option(s) with cost, effort, and residual risk
2. Obtain **risk owner** and **risk committee** decision where required
3. Record **accepted risks** with approver, expiry, and compensating controls
4. Track mitigation tasks to closure; re-score residual on completion

**See `references/treatment_and_acceptance.md`.**

### 5. Third-party and supply-chain risk

Tier vendors by data access, criticality, and concentration. Align questionnaire depth to tier. Feed inherent risk into enterprise register; do not replace legal review.

**See `references/third_party_and_supply_chain_risk.md`.**

### 6. Reporting and governance

Produce committee-ready packs: top risks, heat map, trend, KRIs, treatment status, exceptions nearing expiry. Separate **risk analysis** from **compliance attestation** narratives.

**See `references/reporting_and_governance.md`.**

## When to load references

- **Scope and role boundaries** → `references/security_risk_analyst_scope.md`
- **Scoring scales and FAIR-style framing** → `references/risk_identification_and_scoring.md`
- **TVC mapping and control gaps** → `references/threat_vulnerability_control_mapping.md`
- **Treatment and risk acceptance** → `references/treatment_and_acceptance.md`
- **Vendor and supply chain** → `references/third_party_and_supply_chain_risk.md`
- **KRIs, committees, board narrative** → `references/reporting_and_governance.md`
