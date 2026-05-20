---
name: penetration-tester
description: |
  Guides authorized penetration testing—scoping and rules of engagement, reconnaissance,
  vulnerability identification, exploitation within scope, post-exploitation documentation,
  evidence and remediation reporting, and retest validation. Emphasizes written authorization,
  RoE boundaries, and safe/legal testing. Use for pentest, penetration test, ethical hacking,
  authorized assessment—not enterprise adversary simulation or purple-team campaigns
  (red-team-specialist), dedicated network/AD/infra pentest
  (network-pentester), deep web/API-only assessments (web-pentester), SOC alert triage
  (soc-analyst), incident command (incident-responder),
  forensic imaging (digital-forensics-analyst), binary/firmware RE (reverse-engineer),
  LLM/adversarial AI testing (ai-redteam), or implementing cloud guardrails
  (cloud-security-engineer).
---

# Penetration Tester

## When to Use

- Plan or execute **authorized** penetration tests (cloud workload, wireless) spanning multiple domains under one ROE
- Coordinate dedicated **network/AD/infra** assessments → `network-pentester`
- Draft or validate **rules of engagement**, asset lists, and emergency stop procedures
- Perform **reconnaissance** and **vulnerability identification** with manual validation
- Develop **proof-of-concept exploitation** and document **attack paths** within agreed impact
- Execute **in-scope post-exploitation** (credential proof, lateral movement, objective demo) with cleanup
- Produce **remediation-focused reports** and **retest** critical/high findings

## When NOT to Use

- Deep **web application or API-only** assessments (OWASP, proxy methodology, GraphQL) → `web-pentester`
- Dedicated **internal/external network, AD, segmentation, wireless** methodology → `network-pentester`
- Triage SIEM/EDR alerts or run SOC playbooks → `soc-analyst`
- Lead live incident command, war room, or stakeholder comms → `incident-responder`
- Acquire and analyze forensic disk/memory images → `digital-forensics-analyst`
- Disassembly, decompilation, patch diff, or malware RE lab work → `reverse-engineer`
- Jailbreak LLMs, prompt injection, or agent tool abuse → `ai-redteam`
- Campaign planning, purple team, detection validation at program level → `red-team-specialist`
- Implement cloud IAM, CSPM, landing zone guardrails → `cloud-security-engineer`
- Map audit controls or continuous compliance evidence → `compliance-engineer`
- Add CI/CD security gates or SBOM pipelines → `devsecops`

## Related skills

| Need | Skill |
|---|---|
| Web/API-focused OWASP and proxy-based testing | `web-pentester` |
| Network, AD, lateral movement, segmentation, wireless | `network-pentester` |
| Security program, pentest program governance, GRC | `cybersecurity` |
| Implement fixes for findings (IAM, WAF, SIEM) | `information-security-engineer` |
| Threat context for findings; IOC/TTP intel (not pentest execution) | `cti-analyst` |
| Cloud control implementation and misconfig remediation | `cloud-security-engineer` |
| LLM/agent adversarial testing | `ai-redteam` |
| Red team campaigns, purple team, ATT&CK emulation | `red-team-specialist` |
| SOC alert triage and playbooks | `soc-analyst` |
| Proactive threat hunts from pentest hypotheses | `threat-hunter` |
| Live IR command and containment cadence | `incident-responder` |
| Post-incident forensic artifacts | `digital-forensics-analyst` |
| Binary/protocol RE and patch analysis | `reverse-engineer` |
| Audit evidence and control mapping | `compliance-engineer` |
| Pipeline/supply-chain testing in CI | `devsecops` |
| Offensive reporting for customers | `tech-writer-researcher` |

## Core Workflows

### 1. Scope and authorization

**Do not test without written authorization.**

1. Confirm signed SOW/ROE: assets, methods, windows, contacts
2. Define out-of-scope (third parties, prod PII, physical access, DoS unless approved)
3. Agree severity rubric and evidence handling
4. Establish emergency stop and escalation path
5. Prefer isolated lab or designated test tenants

**See `references/scoping_rules_of_engagement.md` and `references/penetration_tester_scope.md`.**

### 2. Reconnaissance and vulnerability identification

```
passive OSINT → asset inventory → service/version ID → auth surface mapping → validate findings
```

Document source, timestamp, tool, and raw output references. **Validate** scanner output manually.

**See `references/recon_and_vulnerability_identification.md`.**

### 3. Exploitation and post-exploitation (in scope only)

- Minimal PoC steps; redacted evidence
- Clear preconditions (role, network position, config)
- Stop at agreed impact; chain into attack paths when useful
- Post-exploitation only per ROE; **remove** persistence and test artifacts before closeout

**See `references/exploitation_and_post_exploitation.md`.**

### 4. Reporting, remediation, and retest

Per finding: title, severity, impact, reproduction, evidence, remediation, retest criteria. Deliver executive summary + technical appendix; schedule retest for critical/high.

**See `references/reporting_and_remediation.md` and `references/retest_and_safe_practices.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries | `references/penetration_tester_scope.md` |
| Authorization and ROE | `references/scoping_rules_of_engagement.md` |
| Recon and vuln ID | `references/recon_and_vulnerability_identification.md` |
| Exploitation and post-ex | `references/exploitation_and_post_exploitation.md` |
| Reports and remediation | `references/reporting_and_remediation.md` |
| Retest and safe practices | `references/retest_and_safe_practices.md` |
