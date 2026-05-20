---
name: software-assurance-formal-methods-specialist
description: |
  Software assurance and formal methods engineering—assurance cases (GSN/CAE), safety and security
  claims with evidence, requirements-to-verification traceability, hazard-analysis interfaces
  (FMEA, FTA) at evidence level, and high-level standards context (DO-178C, DO-333, IEC 61508,
  ISO 26262, Common Criteria, NIST SSDF). Formal methods—property specification, model checking
  vs theorem proving, abstraction and refinement, bounded model checking, contract/spec languages
  (ACSL, SPARK, TLA+, Alloy) at concept level, proof obligations and counterexamples, CI and
  release-gate integration. Use for software assurance, formal methods, model checking, theorem
  proving, assurance case, GSN, safety case, verification evidence, DO-178C, DO-333, proof
  obligations, TLA+, property verification, formal specification—not routine unit/integration
  tests only, hands-on pentest, enterprise GRC-only, ML adversarial robustness, or bare-metal
  firmware-only work.
---

# Software Assurance / Formal Methods Specialist

## When to Use

- Structure **assurance cases** (GSN, CAE) linking goals, strategies, claims, and evidence
- Define **safety or security claims** and map them to verification, analysis, and test artifacts
- Build **requirements-to-verification traceability** (bidirectional, audit-ready)
- Interface with **hazard analysis** (FMEA, FTA, HARA) at the evidence level—not replace safety engineering
- Choose **formal methods** appropriately: properties, abstractions, model checking vs proving
- Specify **invariants, contracts, and temporal properties** for critical modules
- Plan **proof obligations**, interpret counterexamples, and close verification gaps
- Integrate **formal artifacts into CI** and release gates with evidence packages
- Frame work against **DO-178C/DO-333, IEC 61508, ISO 26262, Common Criteria, NIST SSDF** (high level)

## When NOT to Use

- Routine unit/integration test authoring or test pyramid design only → `senior-software-engineer`
- Pre-execution plan/design go/no-go without assurance-case structure → `build-validator`
- Hands-on penetration testing, exploit development, or offensive findings → `penetration-tester`
- Enterprise GRC program, gap plans, audit questionnaires without verification engineering → `compliance-specialist`
- Technical control mapping and audit evidence automation without formal verification → `compliance-engineer`
- IAM, logging, and guardrail implementation without property-level assurance → `information-security-engineer`
- AI model risk tiers, model cards, and ML governance → `ai-risk-governance`
- ML adversarial robustness (evasion, poisoning, ASR) → `ai-adversarial-robustness-engineer`
- Mission-critical tiering, RTO/RPO, and release governance without verification claims → `mission-critical`
- HRO culture, stop-the-line, and defect-escape metrics without formal evidence → `zero-tolerance-for-failure`
- Bare-metal firmware, RTOS scheduling, and driver HAL only → `embedded-real-time-software-engineer`

## Related skills

| Need | Skill |
|---|---|
| Pre-flight architecture/security/cost validation | `build-validator` |
| Audit evidence pipelines and control automation | `compliance-engineer` |
| GRC scope, gap plans, audit coordination | `compliance-specialist` |
| Security control implementation (IAM, crypto, logging) | `information-security-engineer` |
| AI system risk tiers and model governance | `ai-risk-governance` |
| Production code quality, testing patterns, refactors | `senior-software-engineer` |
| Criticality tiering, RTO/RPO, release governance | `mission-critical` |
| HRO mindset, verification gates, fail-safe design | `zero-tolerance-for-failure` |
| Authorized pentest findings (input to assurance cases) | `penetration-tester` |
| CI/CD security gates and SSDF from pipelines | `devsecops` |

## Core Workflows

### 1. Scope and assurance posture

1. Identify **system context**—safety vs security vs mixed; SIL/ASIL/DAL target if known
2. List **top-level claims** (what must be believed about the software)
3. Classify **evidence types** already available vs gaps (analysis, proof, test, review, field data)
4. Record **assumptions** and **environment** boundaries explicitly

**See `references/software_assurance_scope.md`.**

### 2. Assurance case and claims

Decompose goals with GSN (or CAE): strategies, sub-goals, context, assumptions, and evidence nodes.

**See `references/assurance_cases_and_claims.md`.**

### 3. Formal methods selection

Match technique to property class, scale, and team skill; document why model checking vs proving vs abstract interpretation.

**See `references/formal_methods_landscape.md`.**

### 4. Specification and properties

Write requirements-linked properties: invariants, pre/post conditions, temporal specs, and trace IDs.

**See `references_specification_and_properties.md`.**

### 5. Verification integration

Wire tools into CI, define pass/fail gates, package evidence for release, and handle regressions.

**See `references/verification_integration.md`.**

### 6. Standards and safety/security context

Map artifacts to framework expectations without reproducing full standard text.

**See `references/standards_and_safety_security.md`.**

## Outputs

- **Assurance case** — GSN/CAE diagram or structured outline with claim–evidence links
- **Traceability matrix** — requirement ↔ property ↔ verification activity ↔ result
- **Property catalog** — invariants, contracts, temporal properties with status (proved / bounded / tested / open)
- **Verification plan** — techniques, tools, environments, proof obligations, acceptance criteria
- **Evidence package** — logs, reports, counterexample traces, review records, version pins
- **Gap and residual-risk memo** — open obligations, waived items with rationale and approver

## Principles

- **Claims before tools** — choose verification to support an explicit claim, not the reverse
- **Assumptions are first-class** — document and review them; bad assumptions invalidate proofs
- **Counterexamples are data** — treat failed proofs like test failures with reproduction artifacts
- **Proportionality** — depth of formality matches criticality, not enthusiasm
- **Do not attest** — produce engineering evidence; legal/regulatory sign-off stays with accountable roles
