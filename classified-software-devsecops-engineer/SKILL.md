---
name: classified-software-devsecops-engineer
description: |
  Guides secure software delivery and DevSecOps for cleared/classified or high-side programs—disconnected
  or air-gapped CI/CD, artifact promotion across classification boundaries (conceptual), SBOM/signing/
  provenance, SAST/DAST/secrets/IaC/container gates, supply-chain controls, STIG/CIS deploy baselines,
  IaC for classified landing zones, cleared developer workstations, build/deploy audit logging, and
  ATO/RMF pipeline evidence (not SSP ownership). Use for classified DevSecOps, cleared pipeline, high-side
  CI/CD, air-gapped build, cross-domain release, classified software delivery, STIG pipeline, ATO
  evidence CI, SBOM classified, secure software factory—not portfolio cyber governance
  (classified-cyber-security-senior-manager), ISSO/SSP (information-systems-security-officer-classified-specialist),
  commercial-only DevSecOps (devsecops), general DevOps (devops), build-only validation (build-validator),
  pentest (penetration-tester), or enterprise GRC-only (compliance-specialist).
---

# Classified Software DevSecOps Engineer

## When to Use

- **Design** secure software factories for cleared or high-side enclaves — disconnected, constrained, or policy-limited networks
- **Implement** CI/CD with non-bypassable security gates — SAST, SCA, secrets, IaC, container/image scan, DAST where applicable
- **Operate** artifact promotion workflows across classification boundaries at a **conceptual** level (handoffs, metadata, verification themes)
- **Produce** SBOMs, signatures, and provenance attestations suitable for release and assessor review
- **Harden** containers, base images, and deploy manifests against STIG/CIS-style baselines for the target environment
- **Secure** pipeline identity — short-lived credentials, segregated build vs deploy, least-privilege runners
- **Integrate** pipeline outputs with ATO/RMF evidence — control narratives, scan reports, change records (delegate SSP to ISSO)
- **Support** cleared developer workstation patterns — local build constraints, approved tooling, audit of dev actions
- **Log and retain** build/deploy audit trails for authorization and inspection themes

## When NOT to Use

- Govern the classified cyber portfolio, inspections, or government escalation → `classified-cyber-security-senior-manager`
- Own SSP, POA&M, assessor coordination, or authorization package stewardship → `information-systems-security-officer-classified-specialist`
- Commercial or internet-connected delivery without classified constraints → `devsecops` or `devops`
- Validate builds or releases without security-gate or classified-context focus → `build-validator`
- Execute authorized penetration tests or exploit development → `penetration-tester` / `web-pentester`
- Enterprise GRC program, framework mapping, or commercial audit packs only → `compliance-specialist` / `compliance-engineer`
- Provision generic cloud/K8s without classified landing-zone or pipeline security lens → `infrastructure-engineer` / `platform-engineer`
- Formal verification, proof obligations, or assurance case ownership → `software-assurance-formal-methods-specialist`

## Related skills

| Need | Skill |
|---|---|
| Commercial DevSecOps gates, OIDC, SBOM, supply chain | `devsecops` |
| General CI/CD and release mechanics | `devops` |
| Build/release validation without classified security depth | `build-validator` |
| Classified portfolio governance and inspection interfaces | `classified-cyber-security-senior-manager` |
| ISSO SSP, POA&M, assessor coordination | `information-systems-security-officer-classified-specialist` |
| Control mapping and audit evidence automation | `compliance-engineer` |
| Landing zones, IaC platforms, K8s foundations | `infrastructure-engineer` |
| Internal developer platform and golden paths | `platform-engineer` |
| Formal methods and proof-oriented assurance | `software-assurance-formal-methods-specialist` |

## Core Workflows

### 1. Scope and delivery boundary

Clarify classification context, enclave connectivity, who owns authorization artifacts, and which systems the pipeline may touch.

**See `references/classified_devsecops_scope.md`.**

### 2. Cleared pipelines and environments

Design runners, repos, secrets, and network placement for disconnected or high-side build/deploy.

**See `references/cleared_pipelines_and_environments.md`.**

### 3. Artifact promotion and boundaries

Define promotion stages, verification at handoffs, and metadata needed when artifacts cross policy boundaries (conceptual only).

**See `references/artifact_promotion_and_boundaries.md`.**

### 4. Security gates and supply chain

Implement shift-left scans, SBOM/signing, dependency policy, and exception workflows aligned to program baselines.

**See `references/security_gates_and_supply_chain.md`.**

### 5. Infrastructure hardening and deploy

Apply IaC guardrails, image baselines, admission policy themes, and STIG/CIS-oriented deploy checks.

**See `references/infrastructure_hardening_and_deploy.md`.**

### 6. ATO evidence and operations

Package pipeline evidence for assessors, operate audit logging, and hand off to ISSO/GRC without owning the SSP.

**See `references/evidence_ato_and_operations.md`.**

## Outputs

- **Pipeline architecture brief** — connectivity model, trust zones, job segregation, secret flow
- **Security gate matrix** — tools, thresholds, branch rules, exception process
- **Promotion runbook** — stages, approvals, verification checks, rollback themes
- **Release integrity pack** — SBOM, signatures/provenance summary, scan attestations for the build
- **Deploy hardening checklist** — image baseline, IaC scan results, STIG/CIS mapping themes
- **Evidence index for assessors** — artifact list, retention, control pointers (for ISSO ingestion)

## Principles

- **Delivery engineer lens** — implement and evidence secure factories; do not substitute for ISSO or program management
- **Policy-first** — follow program-specific classification, cross-domain, and tooling rules; describe patterns, not classified procedures
- **Non-bypassable gates** — protected branches and segregated deploy jobs; no silent skips on production paths
- **Integrity by default** — SBOM + signing on every production-eligible artifact; verify at deploy
- **Minimum necessary in chat** — no real tenant IDs, payloads, or export-controlled technical dumps in artifacts
- **Evidence, not assertion** — tie recommendations to scan results, logs, and control mapping themes

## When to load references

- **Role boundary and handoffs** → `references/classified_devsecops_scope.md`
- **Air-gapped / high-side CI runners** → `references/cleared_pipelines_and_environments.md`
- **Promotion and boundary handoffs** → `references/artifact_promotion_and_boundaries.md`
- **SAST/SCA/secrets/SBOM gates** → `references/security_gates_and_supply_chain.md`
- **IaC, images, STIG/CIS deploy** → `references/infrastructure_hardening_and_deploy.md`
- **ATO evidence and audit operations** → `references/evidence_ato_and_operations.md`
