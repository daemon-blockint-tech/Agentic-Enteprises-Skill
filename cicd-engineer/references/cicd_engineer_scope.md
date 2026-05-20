# CI/CD Engineer — scope

## Role definition

Own **continuous integration and delivery** for repositories that ship **Agent Skills** (folders with `SKILL.md`, `references/`, optional scripts)—not general application runtime unless skill packaging is in scope.

## In scope

| Area | Examples |
|---|---|
| Pipeline design | PR validate, release package, changed-path detection |
| GitHub Actions | Workflows, reusable workflows, environments, concurrency |
| Skill tooling | `quick_validate.py`, `package_skill.py`, `validate_all_skills.sh` |
| Artifacts | `.skill` zip bundles, release assets, checksums |
| Gates | Frontmatter, description ≤1024 chars, folder hygiene |
| Secrets | GitHub secrets, OIDC, no credentials in repo |
| Operations | Rollback, release runbooks, promotion to consumers |

## Out of scope (route elsewhere)

| Ask | Route to |
|---|---|
| App containers, K8s deploy, GitOps for services | `devops` |
| “Is this plan safe?” before building | `build-validator` |
| Developer portal, golden paths, scaffolders | `platform-engineer` |
| SLO/error budget program per service | `site-reliability-engineer` |
| Catalog overlap, split/merge skills, governance | `ai-skill-manager` |
| SBOM, SAST gates, signed artifacts policy | `devsecops` |
| Writing skill content and references only | skill-creator |

## Trigger phrases (description)

CI/CD, CI/CD engineer, pipeline design, GitHub Actions, skill validation CI, package skills, release pipeline, deploy skills, PR checks, continuous integration, skill release workflow.

## Success criteria

- Every merged change to `SKILL.md` or skill tree passed `quick_validate.py` (or documented exception)
- Releases produce reproducible `.skill` artifacts tied to git tag and commit
- Rollback path tested or documented; secrets never in git history
- Peer skills cross-linked in **When NOT to Use** and **Related skills**

## Engagement checklist

1. Confirm repo layout (monorepo of skills vs single skill)
2. Identify consumer (Cursor plugin, internal registry, manual install)
3. Choose PR vs release packaging cadence
4. Map required checks to existing scripts
5. Document owners for approve/promote/rollback
