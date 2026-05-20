---
name: enterprise-security-architect
description: |
  Guides enterprise-wide security architecture—reference architectures and domains (identity, data,
  application, network, endpoint), zero-trust and segmentation, framework mapping (NIST CSF, ISO
  27001, CIS), EA and risk alignment, architecture executive briefings, and BU/acquisition standards.
  Use for enterprise security reference models, zero-trust roadmaps, control catalogs, security ARB
  standards, or acquisition integration—not cloud landing zones (enterprise-cloud-architect), cloud
  IAM/terraform (cloud-security-engineer), control deployment/SIEM/EDR (information-security-engineer),
  product ADRs (senior-system-architecture), risk scoring (security-risk-analyst), GRC program
  (compliance-specialist), evidence automation (compliance-engineer), CI gates (devsecops), or CISO
  board program (chief-information-security-officer).
---

# Enterprise Security Architect

## When to Use

- Define **enterprise security reference architecture** — domains, layers, trust boundaries, patterns catalog
- Harmonize **security domains** — identity, data, application, network, endpoint, operations
- Design **zero-trust and segmentation** — identity-centric access, micro-segmentation, east-west controls
- Map **control frameworks** — NIST CSF, ISO 27001 Annex A, CIS, SOC 2 to architecture building blocks
- Integrate security with **enterprise architecture (EA)** — capability maps, standards, exception process
- Align architecture with **risk appetite** — control tiers, compensating controls, treatment themes
- Publish **BU and acquisition standards** — mandatory patterns, integration playbooks, sunset rules
- Run **security architecture review** — ARB criteria, threat-informed design gates, pattern exceptions
- Prepare **architecture executive briefings** — standards adoption, zero-trust roadmap, pattern gaps, acquisition integration (not CISO program KRIs)

## When NOT to Use

- Multi-BU cloud landing zones, CCoE, EA commits, regulated cloud placement, cloud guardrail catalog → `enterprise-cloud-architect`
- Single-product or single-account cloud target design → `cloud-architect`
- Implement SCPs, CSPM rules, cloud IAM policies, KMS wiring → `cloud-security-engineer`
- Deploy SSO connectors, SIEM pipelines, EDR, hardening runbooks → `information-security-engineer`
- Build risk registers, inherent/residual scoring, FAIR estimates → `security-risk-analyst`
- Entitlement modeling, access reviews, PAM vault configuration → `iam-specialist`
- GRC program scope, audit prep, questionnaire packs → `compliance-specialist`
- Automate control evidence from IdP, CI/CD, CSPM → `compliance-engineer`
- CI SAST/SBOM, pipeline scan gates, artifact signing only → `devsecops`
- Security program strategy, policies, vuln/IR program, pentest governance → `cybersecurity`
- Board program briefings, risk appetite, KRIs, crisis comms → `chief-information-security-officer`
- Product/service ADRs, C4 models, strangler migrations → `senior-system-architecture`
- Infrastructure capex portfolio and facility supply chain → `vp-of-infrastructure`

## Related skills

| Need | Skill |
|---|---|
| Enterprise cloud governance and landing zones | `enterprise-cloud-architect` |
| Product or account cloud architecture | `cloud-architect` |
| Cloud guardrails, CSPM, cloud IAM implementation | `cloud-security-engineer` |
| Control deployment, SIEM/EDR, secrets, hardening | `information-security-engineer` |
| Risk registers, scoring, treatment decisions | `security-risk-analyst` |
| IAM lifecycle, RBAC, federation, PAM detail | `iam-specialist` |
| GRC program, audits, framework scope | `compliance-specialist` |
| Technical control evidence automation | `compliance-engineer` |
| Secure SDLC pipeline implementation | `devsecops` |
| Security program strategy and policies | `cybersecurity` |
| CISO board narrative, risk appetite, program ops | `chief-information-security-officer` |
| Cross-service ADRs and integration architecture | `senior-system-architecture` |
| Infrastructure portfolio and executive infra narrative | `vp-of-infrastructure` |

## Core Workflows

### 1. Define scope and operating model

Clarify enterprise vs federated ownership, ARB authority, and mandatory vs recommended controls.

**See `references/enterprise_security_architect_scope.md`.**

### 2. Publish reference architecture

Layered model, domain map, pattern catalog, and integration points to EA.

**See `references/security_reference_architecture.md`.**

### 3. Design identity, data, and zero trust

Identity-centric access, data protection tiers, segmentation, and ZTNA/SASE alignment.

**See `references/identity_data_and_zero_trust.md`.**

### 4. Standardize application and integration security

Secure SDLC gates, API/B2B patterns, secrets, and third-party integration standards.

**See `references/application_and_integration_security.md`.**

### 5. Map governance, frameworks, and controls

Map frameworks to architecture blocks; define control tiers and exception lifecycle.

**See `references/governance_frameworks_and_controls.md`.**

### 6. Brief executives on architecture posture

Architecture packs for board/CISO: standards adoption, KPIs, investment cases, acquisition integration (program KRIs → `chief-information-security-officer`).

**See `references/executive_security_architecture_briefings.md`.**

### 7. Integrate acquisitions and new BUs

Apply assimilation playbook — identity, logging, segmentation, mandatory patterns by day 1/30/90.

**See `references/enterprise_security_architect_scope.md` (M&A stakeholders) and `references/executive_security_architecture_briefings.md` (acquisition summaries).**

## Outputs

- **Enterprise security reference architecture** — domains, layers, trust zones, pattern catalog
- **Zero-trust roadmap** — phases, dependencies, identity and segmentation milestones
- **Control-to-architecture matrix** — framework clauses mapped to building blocks and evidence owners
- **Security standards catalog** — mandatory, recommended, deprecated; BU adoption checklist
- **ARB/security review checklist** — threat-informed gates, exception template with expiry
- **Acquisition integration playbook** — identity, logging, data, network assimilation steps
- **Executive briefing deck outline** — posture, top gaps, investments, measurable outcomes

## Principles

- **Architecture before tooling** — patterns and control intent precede vendor selection
- **Identity is the perimeter** — authenticate, authorize, and continuously validate every access path
- **Defense in depth by domain** — no single control family carries the entire risk
- **Measurable standards** — every mandatory pattern has a validation method and owner
- **Federation with guardrails** — central standards, local delivery within approved patterns
- **Risk-informed exceptions** — time-bound, logged, tied to residual risk acceptance
- **Patterns before implementation** — `information-security-engineer` and `cloud-security-engineer` deploy; this skill defines intent and standards
