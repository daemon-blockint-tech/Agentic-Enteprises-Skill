# Evidence, ATO, and Operations

## Purpose

Package **pipeline and delivery evidence** for RMF/ATO-style assessments without owning the system security plan (SSP). Support ISSO and assessors with traceable artifacts.

## DevSecOps vs ISSO boundary

| Activity | DevSecOps engineer | ISSO |
|----------|-------------------|------|
| Run scans in CI | R | I |
| Maintain SSP control text | C | R/A |
| POA&M entries | C (supply findings) | R/A |
| Authorization decision | I | C |
| Evidence storage location | R (pipeline store) | A (official package) |
| Significant change analysis | C (technical delta) | R/A |

## Control families commonly supported by pipeline evidence

High-level mapping themes (exact control IDs vary by baseline):

| Family | Pipeline evidence examples |
|--------|---------------------------|
| CM — Configuration management | IaC in git, approved merges, deploy logs |
| SA — System and services acquisition | SDLC gates, security requirements in CI |
| SI — System integrity | Signing, SBOM, integrity verification logs |
| RA — Risk assessment | Vulnerability scan exports, exception register |
| AU — Audit | Build/deploy audit logs, retention config |
| IA — Identification/authentication | OIDC federation config, service account inventory |

ISSO maps artifacts to control narratives; DevSecOps maintains **index and freshness**.

## Evidence index template

For each release or assessment period:

```markdown
## Release: <version> — <date>
- Pipeline run: <id>
- Commit: <sha>
- Artifact digest: <digest>
- SBOM: <path or ticket>
- Signatures: <verification log ref>
- SAST: <report ref>
- SCA: <report ref>
- Container scan: <report ref>
- IaC scan: <report ref if applicable>
- Exceptions: <ticket ids>
- Deploy record: <change id>
- Known open findings: <summary for POA&M consideration>
```

Store in program-approved repository; no classified payloads in shared trackers unless authorized.

## Continuous monitoring hooks

- Weekly: open critical/high in default branch vs production digest
- On dependency upgrade: diff SBOM and re-run full gate suite
- On runner image change: record in change system; attach scan
- On pipeline definition change: treat as significant change candidate for ISSO review

## Audit logging requirements

Capture and retain:

| Event | Fields |
|-------|--------|
| Pipeline start/end | actor, definition version, commit |
| Gate failure/waiver | rule, waiver ticket |
| Sign | key id (not private material), digest |
| Promote/deploy | environment, approver, manifest digest |
| Secret access | job, secret name class (not value) |

Correlate timestamps with central SIEM where integrated.

## Assessment support

When assessors request samples:

1. Confirm scope (time window, environments)
2. Export indexed artifacts—redact as required
3. Provide narrative of **how** gates enforce policy (not classified ops detail)
4. Escalate gaps to ISSO for POA&M, not informal waivers

## Operations cadence

| Cadence | Action |
|---------|--------|
| Daily | Monitor failed production-path pipelines |
| Weekly | Review exception expiry; dependency risk summary |
| Monthly | Runner image patch; tool version review |
| Quarterly | Gate threshold tune; suppression audit |
| Annually | Architecture review with ISSO for significant pipeline changes |

## Incident themes (pipeline compromise)

If pipeline or registry compromise suspected:

1. Freeze promotions and rotate CI/deploy credentials per IR playbook
2. Preserve logs and artifact manifests
3. Notify ISSO and classified cyber interfaces
4. Rebuild runners from gold images; re-verify all production digests
5. Do not execute destructive cleanup without IR coordination

Technical IR execution → `incident-responder`; governance → `classified-cyber-security-senior-manager`.

## Related workflows

- Gates and SBOM → `security_gates_and_supply_chain.md`
- Scope and RACI → `classified_devsecops_scope.md`
