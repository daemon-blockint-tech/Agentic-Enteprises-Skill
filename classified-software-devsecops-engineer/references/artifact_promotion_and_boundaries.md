# Artifact Promotion and Boundaries

## Purpose

Describe **conceptual** patterns for promoting software artifacts when classification, connectivity, or policy boundaries separate build from consumption—without reproducing program-specific transfer procedures.

## Promotion model

### Immutable artifacts

- Every release build produces a **content-addressed** or digest-pinned artifact (container image, package bundle, firmware image)
- Tags are pointers; rollback = promote prior digest, not rebuild old tag in place
- Manifest lists all constituent images/packages with digests

### Promotion stages (example)

| Stage | Entry criteria | Exit artifact |
|-------|----------------|---------------|
| CI build | Gates pass on commit | Unsigned or dev-signed build |
| Release candidate | Full scan + review | Signed artifact + SBOM |
| Staging deploy | Ops approval | Deploy record + config version |
| Production-eligible | Change board / ISSO themes | Promotion manifest |
| Downstream enclave | Boundary verification | Receipt attestation (program form) |

Adjust names to program vocabulary; keep criteria testable.

## Boundary handoff themes

When artifacts cross a **classification** or **connectivity** boundary:

1. **Manifest** — digests, versions, build provenance reference, SBOM location
2. **Verification** — signature check, hash match, optional human dual-control per policy
3. **Labeling** — security marking metadata per program rules (not invented in chat)
4. **Receipt** — downstream logs acceptance; breaks chain if mismatch
5. **Separation** — build metadata that must not transit is stripped or summarized

Do **not** document operational steps for cross-domain solutions (CDS), guards, or couriers—route to program engineers and security officers.

## Metadata minimums

| Field | Why |
|-------|-----|
| `artifact_digest` | Integrity |
| `build_id` / `pipeline_run` | Traceability |
| `commit_sha` | Source linkage |
| `sbom_ref` | Supply-chain audit |
| `signature_ref` | Non-repudiation |
| `baseline_version` | STIG/image lineage |
| `classification_label` | Handling (program-defined) |
| `vulnerability_summary` | Risk visibility at handoff |

## Dual-control and approvals

- Production promotion may require two approvers from separate roles
- Waivers for failed gates require named owner, expiry, compensating control
- Emergency break-glass documented in change system with retrospective review

## Rollback

- Keep **N** prior production digests warm in registry
- Rollback deploy references prior manifest; re-run smoke tests
- If rollback crosses boundary, same verification as forward promotion
- Incident linkage if rollback due to security defect

## Anti-patterns

- Rebuilding "the same version" on the far side without provenance link
- Promoting `:latest` without digest pin
- Passing source code archives when policy requires binary-only transfer
- Omitting SBOM at boundary because "downstream trusts us"
- Storing customer or mission data inside artifact bundles

## Interface with ISSO

At each boundary crossing, ISSO may require:

- Evidence that verification occurred
- Significant change record if artifact type or data flow changed
- Updated architecture diagram reference in SSP (ISSO-owned narrative)

DevSecOps supplies **artifacts and logs**; ISSO maintains authorization package.

## Diagram (logical)

```text
[Build enclave] --signed bundle+SBOM--> [Transfer zone] --verified receipt--> [Consume enclave]
                      |                              |
                 audit log                      audit log
```

## Related workflows

- Cleared runners → `cleared_pipelines_and_environments.md`
- Signing and SBOM → `security_gates_and_supply_chain.md`
- Deploy baselines → `infrastructure_hardening_and_deploy.md`
