---
name: cicd-engineer
description: |
  Guides CI/CD for agent skills repositories and skill packages—pipeline design (build, test,
  validate, package), GitHub Actions for PR checks and release promotion, environment gates,
  secrets hygiene (no secrets in repo), skill-creator integration (quick_validate.py,
  package_skill.py), .skill artifact strategy, rollback, and operational runbooks for skill releases.
  Use when the user mentions CI/CD, CI/CD engineer, pipeline design, GitHub Actions, skill validation CI,
  package skills, release pipeline, deploy skills, PR checks, continuous integration, or skill release
  workflow—not application-only CI without skill packaging (devops), pre-flight plan go/no-go
  (build-validator), IDP or golden paths (platform-engineer), org-wide SLO and error-budget programs
  without pipeline ownership (site-reliability-engineer), or portfolio catalog governance without
  pipeline YAML (ai-skill-manager).
---

# CI/CD Engineer

## When to Use

- Design or implement CI/CD for a **skills monorepo** (validate on PR, package on release)
- Add or fix **GitHub Actions** workflows for skill folders, changed-path detection, and matrix validation
- Wire **skill-creator** scripts (`quick_validate.py`, `package_skill.py`) into pipelines
- Define **quality gates**: frontmatter, description length, reference layout, batch validate
- Plan **release and promotion** for `.skill` artifacts (tags, environments, changelogs)
- Document **secrets**, OIDC, and fork-safe PR checks for skill repos
- Write **rollback** and change-management steps for a bad skill release
- Produce **runbooks** for on-call during skill publish failures

## When NOT to Use

- Application/service CI only (containers, K8s deploy, app test suites) without skill packaging → `devops`
- Pre-flight architecture or build go/no-go before execution → `build-validator`
- Internal developer platform, golden paths, Backstage, paved-road templates → `platform-engineer`
- SLI/SLO programs, error budgets, burn-rate alerting, PRR without pipeline work → `site-reliability-engineer`
- Skill catalog inventory, overlap dedup, deprecate/split governance without CI YAML → `ai-skill-manager`
- Security gates (SBOM, SAST policy, supply-chain signing) as the primary task → `devsecops`
- Author a single new skill from scratch (content only) → skill-creator / `init_skill.py`

## Related skills

| Need | Skill |
|---|---|
| General app CI/CD, GitOps, container delivery | `devops` |
| Go/no-go validation before major changes | `build-validator` |
| IDP, golden paths, developer portal | `platform-engineer` |
| SLOs, reliability metrics, incident reliability | `site-reliability-engineer` |
| Batch validate script, portfolio standards | `ai-skill-manager` |
| Pipeline and artifact security gates | `devsecops` |
| Release cutover tiers and change windows | `deployment-strategist` |

## Core Workflows

### 1. Pipeline topology for skills repos

**Standard stage order:**

```
checkout → detect changed skills → validate (quick_validate) → optional lint/scripts → package on release tag → publish artifact → notify
```

**Checklist:**

- [ ] Pipeline as code under `.github/workflows/`; versioned with repo
- [ ] PR jobs run on changed skill directories only when possible
- [ ] `quick_validate.py` gates merge; fail closed on invalid frontmatter
- [ ] Release job runs `package_skill.py` only after validation passes
- [ ] Artifacts immutable (tag + commit SHA in name or metadata)
- [ ] Manual or environment approval before org-wide distribution

**See `references/pipeline_design_and_workflow.md`.**

### 2. GitHub Actions implementation

1. Use `paths` / `paths-filter` for `**/SKILL.md` and `references/**`
2. Matrix or loop per changed skill directory
3. Cache nothing sensitive; use `GITHUB_TOKEN` with least scope
4. Fork PRs: read-only checks; no secrets on `pull_request_target` without hardening
5. Reusable workflow (`workflow_call`) for validate + package jobs

**See `references/github_actions_and_build.md`.**

### 3. Testing and quality gates

| Gate | Tool / check |
|---|---|
| Structure + YAML | `quick_validate.py` |
| Batch regression | `ai-skill-manager/scripts/validate_all_skills.sh` |
| Description triggers | Human review + grep for duplicate keywords |
| Scripts in skill dirs | Lint + no network exfil patterns |

**See `references/testing_gates_and_quality.md`.**

### 4. Skill validation and packaging CI

```bash
python3 ~/.claude/skills/skill-creator/scripts/quick_validate.py path/to/skill-dir
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py path/to/skill-dir ./dist
```

- PR: validate changed skills only
- Release: package validated skills; attach `.skill` to GitHub Release or internal registry
- Do not package every skill on every PR unless releasing a bundle

**See `references/skill_validation_and_packaging_ci.md`.**

### 5. Deployment, promotion, and operations

1. **Dev/staging**: auto-validate on PR merge to main
2. **Release**: tag `skill-v*` or calendar version; package and publish
3. **Promotion**: copy artifacts to consumer paths (plugin cache, internal registry) with checksum
4. **Rollback**: re-publish previous tag artifacts; document superseded skill `description` if needed
5. **Runbook**: who approves, how to verify install, comms for broken bundle

**See `references/deployment_promotion_and_operations.md`.**

### 6. Scope and boundaries

Confirm the ask is **skills-repo CI/CD**, not generic platform ops. Load `references/cicd_engineer_scope.md` when routing or scoping engagements.

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and triggers | `references/cicd_engineer_scope.md` |
| Pipeline stages, branching, artifacts | `references/pipeline_design_and_workflow.md` |
| GitHub Actions patterns | `references/github_actions_and_build.md` |
| Gates, batch validate, PR policy | `references/testing_gates_and_quality.md` |
| quick_validate / package_skill in CI | `references/skill_validation_and_packaging_ci.md` |
| Release, promotion, rollback, runbooks | `references/deployment_promotion_and_operations.md` |
