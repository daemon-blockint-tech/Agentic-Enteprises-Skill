---
name: compliance-engineer
description: |
  Guides compliance engineering—mapping regulatory and framework requirements to technical controls,
  automating audit evidence, continuous compliance monitoring, gap remediation tracking, and
  audit-ready documentation for security and privacy programs (SOC 2, ISO 27001, GDPR technical
  measures, HIPAA safeguards, PCI scope boundaries, NIST CSF).
  Use when implementing controls for audits, building evidence pipelines from infrastructure and
  CI systems, designing continuous control monitoring, preparing auditor evidence packages,
  translating policies into testable technical checks, or tracking remediation before attestations—not
  for contract negotiation or commercial redlines (commercial-counsel), physical data center
  design and commissioning (data-center-design-execution-lead), financial SOX journal controls (senior-revenue-accountant),
  broad security strategy without audit lens (cybersecurity), pipeline scan configuration only
  (devsecops), or AI model regulatory classification (ai-risk-governance).
---

# Compliance Engineer

## When to Use

- Map security, privacy, or operational frameworks to technical controls
- Build audit evidence pipelines from infrastructure, CI/CD, IdP, or ticketing systems
- Design continuous control monitoring and exception workflows
- Prepare evidence packages and remediation tracking for SOC 2, ISO 27001, GDPR, HIPAA, PCI, or NIST CSF
- Translate policy requirements into testable engineering checks

## When NOT to Use

- Contract negotiation, DPAs, or commercial redlines → `commercial-counsel`
- Corporate governance, board approvals, or entity matters → `corporate-counsel`
- Financial close controls, journal entries, or SOX accounting evidence → `senior-revenue-accountant`
- Broad security strategy without audit/control mapping → `cybersecurity`
- CI/CD scan configuration without compliance evidence requirements → `devsecops`

## Related skills

| Need | Skill |
|---|---|
| Infrastructure capex SOX and asset controls | `director-infrastructure-capex-accounting` |
| Security program and IR strategy | `cybersecurity` |
| CI gates, SBOM, SSDF evidence from pipelines | `devsecops` |
| IAM, encryption, guardrail implementation | `information-security-engineer` |
| Data governance and privacy architecture | `data-architect` |
| AI system risk tiers and model governance | `ai-risk-governance` |
| Financial SOX control testing | `senior-revenue-accountant` |
| Commercial contract review and negotiation | `commercial-counsel` |
| Corporate governance, entity, board packages | `corporate-counsel` |
| HRIS access reviews, training completion ops | `people-operations-specialist` |
| Physical DC design and commissioning evidence | `data-center-design-execution-lead` |

## Core Workflows

### 1. Framework scoping

1. Identify in-scope systems, data classes, and subprocessors
2. Select frameworks (e.g., SOC 2 Type II, ISO 27001, GDPR, HIPAA, PCI)
3. Define trust service criteria / Annex A controls in scope
4. Document exclusions with risk acceptance
5. Align calendar: observation period, audit windows, evidence cutoffs

**See `references/framework_scoping.md` for common scope boundaries.**

### 2. Control design and mapping

Translate each control to **testable** technical implementation:

| Layer | Examples |
|---|---|
| Policy | Approved access policy |
| Process | Quarterly access review ticket |
| Technical | SSO enforced; IAM policy as code |
| Evidence | IdP export + review sign-off |

Avoid controls that cannot be evidenced automatically or manually on schedule.

**See `references/control_mapping.md` for SOC 2 / ISO mapping patterns.**

### 3. Evidence automation

```
control ID → evidence source (API, Git, SIEM) → collector → storage → reviewer attestation
```

**Evidence quality rules:**

- Timestamped, tamper-evident storage
- Named owner per control
- Sample size documented for population controls
- Redact customer PII in shared audit folders

**See `references/evidence_automation.md` for source catalog and collection cadence.**

### 4. Continuous control monitoring

- Detect drift from baseline (public buckets, open SGs, missing MFA)
- Alert owners before audit finding
- Integrate CSPM, Git policy checks, and HRIS for joiner/leaver
- Weekly dashboard: pass/fail per control, trend

**See `references/continuous_monitoring.md` for CCM metrics and alert routing.**

### 5. Gap assessment and remediation

1. Run gap analysis against chosen framework
2. Classify: missing control, partial, implemented
3. Assign remediation with owner, due date, evidence plan
4. Verify fix with re-test and attach proof
5. Track exceptions with expiry and approver

**See `references/audit_readiness.md` for pre-audit checklist.**

### 6. Auditor engagement (engineering)

Prepare **evidence packages** per control family:

- Access (IdP, reviews, privileged accounts)
- Change management (PR approvals, deploy logs)
- Vulnerability management (scan reports, SLAs)
- Logging and monitoring (retention config, alert samples)
- Vendor risk (subprocessor list, reviews)

Provide narrative only where logs are insufficient; prefer primary artifacts.

**See `references/audit_readiness.md` for walkthrough agenda and FAQ for auditors.**

### 7. Privacy engineering hooks (GDPR-style)

Coordinate with `data-architect` for:

- Data inventory and lawful basis documentation
- DSR workflows (access/delete) with engineering tickets
- DPIA triggers for new processing
- Cross-border transfer mechanisms (SCCs, etc.) as **documented** requirements—not legal advice

## When to load references

- **Scope and frameworks** → `references/framework_scoping.md`
- **Control mapping** → `references/control_mapping.md`
- **Evidence collectors** → `references/evidence_automation.md`
- **Drift and CCM** → `references/continuous_monitoring.md`
- **Audit prep** → `references/audit_readiness.md`
