# Deployment, promotion, and operations

## Promotion model

```
PR validate → merge main → (optional) staging registry → release tag → production registry / plugin channel
```

| Stage | Audience | Mechanism |
|---|---|---|
| CI | Authors | GitHub Checks |
| Staging | Early adopters | Pre-release asset or internal bucket |
| Production | All users | GitHub Release, plugin update, or config pull |

## Release versioning

- **Calendar**: `2025.05.1` for monthly skill bundles
- **Semver**: `skill-catalog-v2.3.0` when breaking routing or folder moves
- **Per-skill tags**: `cicd-engineer-v1.0.0` when releasing skills independently

Document scheme in release notes; consumers pin versions.

## Rollback

1. Identify last good release tag and artifact checksums
2. Re-publish previous `dist/*.skill` assets to production channel (do not rebuild from old commit unless reproducibility required)
3. If bad skill content already merged: revert git commit or publish patch release with fixed `description`/body
4. Post-incident: add CI gate that would have caught the issue

**Time target:** rollback artifact promotion < 15 minutes; git revert separate.

## Change management

| Change type | Approval |
|---|---|
| New workflow only | Platform + repo maintainer |
| New required check | Announce; grace period with `continue-on-error` |
| Breaking folder rename | Major version + migration note in `ai-skill-manager` |

## Operational runbook (skill release failed)

### Symptoms

- Release workflow red after tag push
- Users report missing or corrupt `.skill` install
- Validator passed locally but failed in CI

### Triage

1. Open failed workflow run; read `quick_validate` vs `package_skill` step
2. Confirm tag points to intended commit (`git rev-parse $TAG`)
3. List artifacts uploaded; verify checksums

### Mitigate

- Re-run workflow with fixed commit (new patch tag)
- Or rollback promotion to previous release assets
- Disable auto-update channel if bad bundle propagated

### Communicate

- Internal: #skills-platform with tag, failing skill names, ETA
- External: minimal notice if consumer-facing plugin broke

### Follow-up

- Add test fixture or gate
- Update runbook with new failure mode

## Secrets rotation

- Rotate registry tokens on schedule; update GitHub secrets
- Re-run dry-run release without publishing to verify OIDC

## Observability

- Alert on: release workflow failure, validate main failure, artifact upload 4xx/5xx
- Dashboard: validate duration p95, skills packaged per release

## Boundaries

Promotion to **Kubernetes clusters** or **cloud runtimes** is `devops` / `cloud-engineer`. This reference covers **skill artifact** promotion only.
