---
name: compliance-specialist
description: |
  Guides cross-functional GRC and compliance programs—framework selection and scope (SOC 2, ISO 27001,
  HIPAA, PCI, GDPR concepts), control mapping and gap assessments, policy and procedure outlines,
  audit and assessor coordination prep, vendor security questionnaire support, and continuous
  compliance program design with ownership and cadence.
  Use when standing up or maturing a compliance program, scoping attestations, running readiness
  gap analyses, drafting control matrices, preparing audit walkthroughs, responding to SIG/CAIQ-style
  questionnaires, or designing continuous compliance—not technical control implementation or evidence
  automation (compliance-engineer), cloud-only API evidence and residency packages
  (cloud-compliance-specialist), IAM/terraform guardrails (cloud-security-engineer,
  information-security-engineer), legal interpretation or contract redlines (commercial-counsel),
  security risk registers (security-risk-analyst), or pentest execution (penetration-tester).
---

# Compliance Specialist

## When to Use

- Select and **scope** frameworks (SOC 2 Type I/II, ISO 27001, HIPAA, PCI, GDPR-style privacy program)
- Build **control mapping** and gap assessments with remediation plans and owners
- Draft **policy and procedure outlines** aligned to in-scope controls (not legal advice)
- Prepare **audit and assessor coordination** — calendars, walkthrough agendas, request lists
- Support **vendor security questionnaires** (SIG, CAIQ, custom) with consistent answers and evidence pointers
- Design **continuous compliance** — control inventory, review cadence, exception register, metrics
- Align **GRC program** roles, RACI, and executive reporting before engineering evidence work

## When NOT to Use

- Automate evidence from IdP, CI/CD, CSPM, or build CCM pipelines → `compliance-engineer`
- Cloud API evidence, shared responsibility, FedRAMP/PCI in AWS/GCP/Azure → `cloud-compliance-specialist`
- Implement IAM, encryption, SCPs, or CSPM rules → `information-security-engineer`, `cloud-security-engineer`
- Interpret law, negotiate DPAs, or redline contracts → `commercial-counsel`
- Enterprise security strategy without audit/program lens → `cybersecurity`
- Inherent/residual risk scoring and risk register → `security-risk-analyst`
- Execute penetration tests → `penetration-tester`

## Related skills

| Need | Skill |
|---|---|
| Technical control mapping and evidence automation | `compliance-engineer` |
| Cloud framework evidence and residency packages | `cloud-compliance-specialist` |
| Security program strategy and IR | `cybersecurity` |
| Security risk register and treatment framing | `security-risk-analyst` |
| Contract, DPA, and legal terms | `commercial-counsel` |
| Cloud guardrails and misconfiguration remediation | `cloud-security-engineer` |
| Corp IdP, SIEM, EDR implementation | `information-security-engineer` |
| BCM/DRP artifacts, exercise records, high-level continuity mapping | `bcm-disaster-recovery-specialist` |

## Core Workflows

### 1. Program charter and framework selection

1. Document business drivers (customer contracts, sector, geography)
2. Inventory systems, data classes, and subprocessors
3. Select frameworks and trust criteria / Annex A scope
4. Define observation period, audit windows, and exclusions with risk acceptance
5. Assign program owner, control owners, and executive sponsor

**See `references/compliance_specialist_scope.md`.**

### 2. Control mapping and gap assessment

Map each in-scope requirement to policy, procedure, technical control, and evidence type. Classify gaps: missing, partial, implemented. Prioritize by audit date and customer impact.

**See `references/framework_scoping_and_mapping.md` and `references/gap_assessment_and_remediation_planning.md`.**

### 3. Policies, procedures, and evidence design

Draft outlines stakeholders can approve; define evidence **requirements** (what, who, cadence)—hand implementation collectors to `compliance-engineer`.

**See `references/policies_procedures_evidence.md`.**

### 4. Audit and assessor coordination

Prepare request lists, walkthrough scripts, point-of-contact roster, and exception register. Coordinate with engineering for live demos only when narratives need validation.

**See `references/audit_and_assessor_coordination.md`.**

### 5. Vendor and continuous compliance

Standardize questionnaire responses, tier vendors, and run periodic control reviews—not one-time audit cramming.

**See `references/vendor_and_continuous_compliance.md`.**

## Outputs

- **Compliance scope memo** — frameworks, systems, data, exclusions, calendar
- **Control matrix** — requirement ID, owner, policy/procedure, evidence type, status
- **Gap and remediation plan** — priority, due date, dependency on engineering/legal
- **Policy/procedure outlines** — sections ready for approval workflow
- **Audit prep pack** — agenda, FAQ, request tracker, exception log
- **Questionnaire response library** — approved answers with evidence links

## Principles

- **Program before tooling** — scope and owners before collectors
- **Separate GRC from build** — this skill defines *what* to prove; `compliance-engineer` automates *how*
- **No legal advice** — cite requirements; escalate interpretation to counsel
- **Evidence pointers, not screenshots hoards** — name systems of record and owners
- **Continuous cadence** — quarterly reviews beat pre-audit fire drills

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and program charter | `references/compliance_specialist_scope.md` |
| Framework selection and mapping | `references/framework_scoping_and_mapping.md` |
| Gap assessment and remediation | `references/gap_assessment_and_remediation_planning.md` |
| Policies, procedures, evidence | `references/policies_procedures_evidence.md` |
| Audit and assessor prep | `references/audit_and_assessor_coordination.md` |
| Vendor questionnaires and CCM | `references/vendor_and_continuous_compliance.md` |
