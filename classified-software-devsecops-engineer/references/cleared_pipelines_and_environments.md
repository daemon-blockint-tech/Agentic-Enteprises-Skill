# Cleared Pipelines and Environments

## Purpose

Design CI/CD runners, source control, secrets, and networking for **cleared** or **high-side** software delivery where connectivity and tooling are constrained.

## Pipeline topology patterns

### Segregated build and deploy

```
[Source] → [Build job - untrusted] → [Artifact vault] → [Deploy job - trusted] → [Target env]
```

- Build jobs compile, test, scan; **cannot** push to production clusters
- Deploy jobs run only on protected branches/tags with environment approvals
- Separate service identities for build vs deploy; deploy identity has minimal blast radius

### Staged runners by trust

| Stage | Runner pool | Network | Typical jobs |
|-------|-------------|---------|--------------|
| Dev integration | Lower-trust pool | Dev enclave | Unit test, lint, fast SAST |
| Release build | Hardened pool | Build enclave | Full SAST/SCA, image build, sign |
| Promote | Trusted pool | Deploy enclave | Helm/K8s apply, config push |

### Air-gapped build loop (conceptual)

1. Approved dependency bundles enter the enclave on program-approved transfer
2. Build consumes only internal mirrors and lockfiles
3. Scans run against offline vulnerability data (synced on schedule)
4. Signed artifacts exit via one-way transfer to downstream stage
5. Document **verification** at receipt (hash, signature, manifest match)

## Source control hardening

- Protected default branch; required reviews and status checks
- No direct pushes; signed commits where program requires
- Branch policies tie merge to pipeline success on same commit SHA
- Submodule and large binary policies aligned with supply-chain vetting
- Audit log retention for clone, push, permission changes

## Secrets and credentials

| Pattern | Use | Avoid |
|---------|-----|-------|
| Short-lived OIDC to internal cloud/K8s | Deploy from trusted job | Long-lived access keys in variables |
| Vault / internal secrets manager | Build-time secrets, deploy tokens | Secrets in repo or container layers |
| Per-environment scopes | Staging vs prod separation | One credential for all environments |
| Rotation + break-glass | Documented, rare | Shared personal tokens in CI |

## Cleared developer workstation themes

- Builds may occur only on **approved** images with mandatory endpoint controls
- Local secrets prohibited or confined to hardware-backed stores per policy
- Dependency installs from internal mirrors; document offline workflow for travelers
- Pre-commit hooks optional; **authoritative** gates remain on server-side CI
- Screen capture, removable media, and remote access rules are personnel/IT—not defined here

## Runner hardening checklist

- [ ] OS baseline aligned to program STIG/CIS image (see infrastructure reference)
- [ ] Non-root job execution where supported
- [ ] Ephemeral workers or frequent rebuild to limit persistence
- [ ] No interactive shells on production-path runners
- [ ] Toolchain versions pinned; changes via change control
- [ ] Antivirus/EDR where required; logs forwarded to central store
- [ ] Time sync (NTP) for audit correlation

## Network placement

- Build runners in dedicated VLAN/subnet; egress allowlists only
- Artifact registry internal; TLS and auth required
- Package proxies vet upstream (where proxy exists)
- DAST scanners isolated; never pointed at production mission systems without approval

## Observability and audit

Log at minimum:

- Job ID, pipeline definition version, commit SHA, actor (service or human)
- Gate results per stage (pass/fail/waived)
- Artifact digest promoted
- Deploy target environment and approval record ID

Retention meets program and control family expectations; ISSO defines authoritative period.

## Failure modes

| Symptom | Likely cause | Response theme |
|---------|--------------|----------------|
| Builds fail only in enclave | Mirror lag or missing approved package | Request bundle refresh; do not bypass mirror |
| Scans time out | Offline DB stale | Schedule sync; temporary waiver via exception process |
| Deploy OIDC fails | Trust policy drift | Fix federation config; no static key fallback |
| Duplicate artifacts | Retag without rebuild | Enforce immutable tags; content-addressable storage |

## Related workflows

- Security gates and SBOM → `security_gates_and_supply_chain.md`
- Promotion across boundaries → `artifact_promotion_and_boundaries.md`
- Evidence packaging → `evidence_ato_and_operations.md`
