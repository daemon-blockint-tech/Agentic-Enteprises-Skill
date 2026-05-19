# Supply chain security

## Table of contents

1. [SBOM requirements](#sbom-requirements)
2. [Artifact signing](#artifact-signing)
3. [Dependency policy](#dependency-policy)
4. [Third-party risk](#third-party-risk)
5. [SLSA orientation](#slsa-orientation)

## SBOM requirements

Generate on every release build (not only on request).

| Field | Why it matters |
|---|---|
| Component name + version | Trace to CVE |
| Package URL (purl) | Automated matching |
| Hash | Integrity verification |
| Dependency graph | Transitive risk |
| Supplier/license | Compliance |

**Tools:** Syft, CycloneDX CLI, GitHub dependency submission, build tools with native SBOM export.

Store SBOM alongside artifact in registry or artifact store; retain per release for audit window (typically 1–3 years).

## Artifact signing

| Artifact | Mechanism |
|---|---|
| Container images | cosign sign/verify with keyless (Sigstore) or KMS key |
| Helm charts | cosign OCI attach or provenance attestation |
| Generic binaries | Sigstore blob signing |

**Deploy gate pseudocode:**

```
build → push image@digest → sign digest → deploy only if verify(signature) == OK
```

## Dependency policy

| Rule | Enforcement |
|---|---|
| Lockfile required | CI fails if lockfile not updated with manifest change |
| No unpinned major jumps without review | CODEOWNERS on package manifests |
| Critical CVE | Block merge unless waiver |
| Unmaintained package (>2y no release) | Quarterly review queue |
| Typosquatting | Use private registry mirror + namespace allowlist |

**Reachability:** prefer scanners that mark CVEs as reachable/unreachable in the dependency graph to reduce noise.

## Third-party risk

Before adopting:

- GitHub Action: pinned SHA, org reputation, permissions requested
- Helm chart: verify publisher, scan chart templates, pin version
- Base image: official or distroless; scan and rebuild on CVE SLA
- SaaS CI integration: OAuth scopes, data residency, SOC 2 report

## SLSA orientation

| Level | Practical step |
|---|---|
| L1 | Scripted build, version control |
| L2 | Hosted build service, signed provenance |
| L3 | Hardened build platform, non-falsifiable provenance |

Most teams target **L2** with hosted CI + signed provenance; L3 requires dedicated build infrastructure.

**Provenance attestation (conceptual):** builder records source repo, commit, build command, materials; consumer policy checks attestation before deploy.
