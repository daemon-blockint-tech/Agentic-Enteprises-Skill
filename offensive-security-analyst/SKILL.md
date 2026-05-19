---
name: offensive-security-analyst
description: |
  Guides authorized offensive security work—engagement scoping and rules of engagement, reconnaissance,
  vulnerability validation, exploitation proof-of-concept, attack-path chaining, MITRE ATT&CK mapping,
  and remediation-focused reporting for pentests and red-team exercises.
  Use when planning or executing authorized penetration tests, validating findings with reproducible
  PoCs, prioritizing exploitable issues, simulating adversary TTPs within scope, or writing offensive
  findings for engineering remediation—not for SOC alert triage (defensive-security-analyst), security
  program or GRC design (cybersecurity), CI/CD hardening (devsecops), or LLM jailbreak and prompt-injection
  testing (ai-redteam).
---

# Offensive Security Analyst

## When to Use

- Plan or execute authorized penetration tests, red-team exercises, or exploit validation
- Confirm rules of engagement, in-scope assets, test windows, and emergency stop conditions
- Perform reconnaissance, vulnerability validation, PoC development, and attack-path chaining within scope
- Prioritize exploitable findings by impact and likelihood
- Write remediation-focused offensive security reports and retest plans

## When NOT to Use

- Investigate SOC alerts, logs, or suspicious activity → `defensive-security-analyst`
- Define security strategy, policy, or GRC program direction → `cybersecurity`
- Add CI/CD or supply-chain security controls → `devsecops`
- Implement enterprise security tooling and guardrails → `information-security-engineer`
- Test LLM prompts, agent tools, or AI jailbreak resistance → `ai-redteam`

## Related skills

| Need | Skill |
|---|---|
| CVD intake, embargo, advisory publication | `technical-program-manager-security-cvd` |
| Blue-team triage and detections | `defensive-security-analyst` |
| Security program, policies, IR program | `cybersecurity` |
| Pipeline and supply-chain testing in CI | `devsecops` |
| LLM/agent adversarial testing | `ai-redteam` |
| Findings documentation for customers | `tech-writer-researcher` |

## Core Workflows

### 1. Engagement scope and authorization

**Do not test without written authorization.**

1. Confirm signed SOW/ROE: in-scope assets, methods, windows, contacts
2. Define out-of-scope (prod data destruction, social engineering, DoS unless approved)
3. Set severity rubric aligned with customer
4. Establish emergency stop and escalation path
5. Use isolated lab or designated test tenants when possible

**See `references/engagement_scope.md` for ROE checklist and severity rubric.**

### 2. Reconnaissance and enumeration

```
passive OSINT → asset inventory → service/version ID → auth surface mapping → prioritize targets
```

**Document everything:** source, timestamp, tool, raw output hash or path.

**See `references/recon_enumeration.md` for recon phases and asset tracking.**

### 3. Vulnerability assessment and validation

1. Run scans appropriate to scope (authenticated where allowed)
2. **Validate** each finding manually—no report-only scanner noise
3. Classify: exploitable, conditional, informational
4. Map to CWE/CVE and ATT&CK where applicable
5. Note compensating controls that block exploitation

**See `references/vulnerability_assessment.md` for validation criteria and false positive filters.**

### 4. Exploitation and attack paths

**PoC requirements:**

- Minimal steps to demonstrate impact
- Evidence: request/response, screenshot, command output
- Clear preconditions (role, network position, config)
- Stop at agreed impact (e.g., proof of RCE without lateral movement unless scoped)

Chain findings into **attack paths**: initial access → privilege → objective.

**See `references/exploitation_chain.md` for PoC template and chaining worksheet.**

### 5. Post-exploitation (when in scope)

Only within ROE:

- Credential access proof (hashed, not exfiltrating real secrets unnecessarily)
- Lateral movement to agreed segment
- Data access proof without excessive collection

Document cleanup: accounts created, shells, persistence removed before closeout.

### 6. Reporting and remediation

**Per finding:**

| Field | Content |
|---|---|
| Title | Business-readable |
| Severity | Per agreed rubric |
| Description | What and where |
| Impact | Confidentiality, integrity, availability |
| Reproduction | Numbered steps |
| Evidence | Redacted artifacts |
| Remediation | Specific fix + validation retest |

Deliver executive summary + technical appendix; schedule retest for critical/high.

**See `references/reporting_remediation.md` for report structure and retest checklist.**

## When to load references

- **Scope, ROE, authorization** → `references/engagement_scope.md`
- **Recon and enumeration** → `references/recon_enumeration.md`
- **Scanning and validation** → `references/vulnerability_assessment.md`
- **PoCs and attack paths** → `references/exploitation_chain.md`
- **Reports and retest** → `references/reporting_remediation.md`
