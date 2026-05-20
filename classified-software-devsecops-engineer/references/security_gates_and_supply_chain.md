# Security Gates and Supply Chain

## Table of contents

1. [Gate philosophy](#gate-philosophy)
2. [Pipeline stage order](#pipeline-stage-order)
3. [Scan types and defaults](#scan-types-and-defaults)
4. [SBOM and signing](#sbom-and-signing)
5. [Dependency policy](#dependency-policy)
6. [Exceptions and waivers](#exceptions-and-waivers)
7. [Agentic CI considerations](#agentic-ci-considerations)

## Gate philosophy

- Gates on **protected branches** and **production deploy paths** are non-skippable
- Fail closed on secrets and critical exploitable issues unless documented exception
- Same commit SHA scanned in CI is what gets signed and promoted
- Waivers are time-bound, owned, and visible to ISSO via evidence index

## Pipeline stage order

```text
lint → unit test → SAST → SCA → build → IaC scan (if infra change) → image build →
container scan → SBOM → sign/provenance → staging deploy → smoke → [DAST] → prod promote
```

DAST only where policy allows; never default-scan production mission systems.

## Scan types and defaults

| Gate | Trigger | Default policy | Notes for classified |
|------|---------|----------------|----------------------|
| Secret scan | Every push/PR | Block on verified secret | Enable push protection on server |
| SAST | PR + default branch | Block new critical/high | Tune rules per language |
| SCA | PR + default branch | Block critical CVE with fix | Offline DB sync in air-gap |
| IaC scan | IaC/terraform changes | Block critical misconfig | Map to landing zone guardrails |
| Container scan | Before registry push | Block critical OS/app CVE | Scan **after** build, before sign |
| DAST | Staging only | Block only agreed findings | Scoped targets, rate limits |
| License policy | Release branch | Block deny-list licenses | Legal list from compliance |

### False positives

- Require tool + rule ID + file path in ticket
- Prefer global suppressions with expiry over silent ignores in repo
- Revisit suppressions quarterly or on major tool upgrade

## SBOM and signing

### SBOM (CycloneDX or SPDX)

Include per release:

- Component name, version, purl or coordinates
- Hash of deliverable artifact
- Relationship to parent image/bundle
- **No** embedded customer data or environment secrets

### Signing and provenance

| Artifact | Minimum | Stronger programs |
|----------|---------|-------------------|
| Container image | Digest pin + signature | SLSA-oriented attestations |
| Helm chart / manifest bundle | Signature on package | Policy controller verify at deploy |
| Generic binary | Code-signing cert from program CA | Timestamp + transparency log (if allowed) |

**Deploy verification:** admission controller or deploy job verifies signature before apply.

## Dependency policy

1. Lockfiles required; no floating versions on release branches
2. New dependencies need review ticket (purpose, license, maintainer health)
3. Internal mirrors are source of truth in disconnected enclaves
4. Block typosquat and unpinned Git URLs in manifests
5. Pin CI actions and base images by digest or immutable version

### Third-party CI actions

- Allowlist organizations/actions
- Fork and pin if vendor actions required
- Review agentic workflow plugins with same rigor as production code

## Exceptions and waivers

| Field | Required |
|-------|----------|
| Finding ID / CVE | Yes |
| Risk rationale | Yes |
| Compensating control | Yes |
| Owner | Yes |
| Expiry date | Yes |
| ISSO notification | Per program |

Expired waivers fail the pipeline until remediated or renewed.

## Agentic CI considerations

When AI coding agents run in CI (e.g., automated fix bots):

- Treat agent output as **untrusted** until scanned like developer commits
- Restrict agent permissions to least-privilege tokens
- Log prompts and actions where policy allows; never log secrets
- Block agents from modifying pipeline definitions or branch protections without human review
- Pair with `agentic-actions-auditor` patterns when installed for workflow review

## Evidence outputs per release

- Machine-readable scan reports (SARIF or vendor export)
- SBOM file stored with artifact
- Signature verification log
- Exception register snapshot
- Pipeline run URL/ID and commit SHA

## Related workflows

- Air-gapped toolchains → `cleared_pipelines_and_environments.md`
- Deploy verification → `infrastructure_hardening_and_deploy.md`
- ISSO handoff → `evidence_ato_and_operations.md`
