---
name: build-validator
description: |
  Validate plans, designs, and implementations before execution to prevent costly mistakes.
  Cover architecture review, security audit, scalability assessment, cost analysis, compliance check,
  and risk identification. Produce go/no-go decisions with specific remediation steps.
  Triggers on "review this plan", "validate architecture", "check for mistakes", "is this production ready",
  "audit this design", "what could go wrong", "pre-flight check", "build review",
  "quality gate", "risk assessment", "cost estimate", or "compliance check".
---

# Build Validator

## Overview

Validate plans, designs, and implementations before execution to prevent costly mistakes.
This skill acts as a quality gate across all domains — infrastructure, data architecture, ML models,
revenue accounting, customer operations, documentation, and AI systems. Produce go/no-go decisions
with specific remediation steps, not vague feedback.

## Features

- Architecture review: pattern validation, anti-pattern detection, dependency analysis
- Security audit: threat modeling, access control review, data protection assessment
- Scalability assessment: load testing plans, bottleneck identification, capacity planning
- Cost analysis: TCO estimation, waste identification, optimization recommendations
- Compliance check: regulatory alignment, audit readiness, documentation completeness
- Risk identification: single points of failure, vendor lock-in, technical debt, operational gaps

## Usage

1. Present the plan, design, or implementation to validate
2. Specify the domain (infrastructure, data, ML, revenue, customer ops, docs, AI)
3. Run the corresponding validation workflow below
4. Receive go/no-go decision with specific remediation steps

## Examples

- **User**: "Review this data lakehouse architecture"
  **Agent**: Runs Architecture Review workflow, checks partitioning strategy, governance model, cost estimates, identifies 3 anti-patterns, produces go/no-go with fixes

- **User**: "Is this ML model production ready?"
  **Agent**: Runs ML Validation workflow, checks training data quality, model monitoring plan, drift detection, rollback strategy, produces readiness scorecard

- **User**: "Check this revenue recognition setup"
  **Agent**: Runs Compliance Check workflow, validates ASC 606 five-step model, contract analysis completeness, audit trail, produces compliance report

## When to Use

- Before committing to a major architecture decision or technology choice
- Before deploying to production (infrastructure, data pipelines, ML models)
- Before signing vendor contracts or committing to long-term commitments
- Before launching customer-facing features or revenue-generating products
- When unsure if a design is production-ready or has hidden risks

## When NOT to Use

- Day-to-day coding decisions or minor refactoring → use code review tools
- Quick prototyping or proof-of-concept work → iterate fast, validate later
- Personal projects with no production or compliance requirements → use judgment
- Legal or regulatory interpretations requiring licensed professionals → consult counsel

## Core Workflows

### 1. Architecture Review

**Validation checklist:**

1. **Pattern validation**
   - Does the architecture follow established patterns for this domain?
   - Are there anti-patterns (tight coupling, single points of failure, over-engineering)?
   - Is the technology choice justified by requirements, not trends?

2. **Dependency analysis**
   - What are the critical dependencies? What happens if they fail?
   - Are there vendor lock-in risks? What's the exit strategy?
   - Is there a clear upgrade/migration path?

3. **Scalability check**
   - How does the system behave at 10x current load?
   - Where are the bottlenecks? How are they mitigated?
   - Is there a capacity planning process?

4. **Security review**
   - Are authentication and authorization properly designed?
   - Is data encrypted at rest and in transit?
   - Are there audit logs and monitoring?

**Decision output:** Go / Conditional Go (with fixes) / No Go (with reasons)

### 2. Security Audit

**Threat modeling workflow:**

1. **Identify assets**: What data, systems, or processes need protection?
2. **Map trust boundaries**: Where does data cross security boundaries?
3. **Enumerate threats**: STRIDE analysis (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)
4. **Assess risk**: Likelihood × Impact for each threat
5. **Define mitigations**: Technical controls, process controls, monitoring

**Common findings:**
- Missing input validation → injection risks
- Hardcoded secrets → credential exposure
- Overly permissive IAM → privilege escalation
- No audit trail → compliance failure
- Missing rate limiting → abuse/DoS

### 3. Cost Analysis

**TCO estimation framework:**

| Cost Category | Year 1 | Year 2 | Year 3 | Notes |
|---|---|---|---|---|
| Infrastructure |  |  |  | Compute, storage, network |
| Software licenses |  |  |  | Per-seat, per-usage, enterprise |
| Personnel |  |  |  | FTEs, contractors, training |
| Operations |  |  |  | Monitoring, support, incident response |
| Compliance |  |  |  | Audits, certifications, legal |
| **Total** |  |  |  |  |

**Optimization checks:**
- Are there over-provisioned resources?
- Can reserved instances or committed use discounts apply?
- Are there cheaper alternatives with equivalent capability?
- What's the cost of NOT building this?

### 4. Compliance Check

**Regulatory alignment assessment:**

1. **Identify applicable regulations**: GDPR, CCPA, SOC 2, HIPAA, PCI-DSS, ASC 606, etc.
2. **Map requirements to controls**: Which technical/process controls address each requirement?
3. **Gap analysis**: What's missing? What's partially implemented?
4. **Audit readiness**: Can you demonstrate compliance to an auditor today?

**Documentation checklist:**
- [ ] Architecture diagrams with data flows
- [ ] Access control policies and user lists
- [ ] Data retention and deletion procedures
- [ ] Incident response plan
- [ ] Business continuity and disaster recovery plan
- [ ] Vendor risk assessments
- [ ] Training records for staff

### 5. Risk Identification

**Risk register template:**

| Risk | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|
|  | High/Med/Low | High/Med/Low |  |  | Open/Mitigated/Accepted |

**Common risk categories:**
- **Technical**: Single points of failure, untested dependencies, technical debt
- **Operational**: No on-call coverage, missing runbooks, undocumented processes
- **Business**: Vendor lock-in, regulatory changes, market shifts
- **People**: Bus factor, skill gaps, turnover risk

### 6. Go/No-Go Decision Framework

**Scoring matrix:**

| Criteria | Weight | Score (1-5) | Weighted |
|---|---|---|---|
| Architecture soundness | 20% |  |  |
| Security posture | 20% |  |  |
| Scalability readiness | 15% |  |  |
| Cost efficiency | 15% |  |  |
| Compliance alignment | 15% |  |  |
| Operational readiness | 15% |  |  |
| **Total** | **100%** |  |  |

**Decision thresholds:**
- **4.0+**: Go — proceed with confidence
- **3.0-3.9**: Conditional Go — proceed after addressing specific findings
- **Below 3.0**: No Go — significant risks require redesign

**Output format:**
```
## Build Validation Report

**Overall Score:** X.X / 5.0
**Decision:** Go / Conditional Go / No Go

### Findings
1. [Finding] — [Severity] — [Remediation]
2. ...

### Risks
1. [Risk] — [Likelihood/Impact] — [Mitigation]
2. ...

### Next Steps
1. [Action item] — [Owner] — [Deadline]
2. ...
```
