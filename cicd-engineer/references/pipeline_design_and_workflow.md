# Pipeline design and workflow

## Recommended stages

### Pull request (continuous integration)

1. **Checkout** — full history if versioning or path filters need base comparison
2. **Discover changes** — list skill directories touched (`SKILL.md`, `references/`, `scripts/`)
3. **Validate** — `quick_validate.py` per changed skill (fail job on first error or matrix all)
4. **Optional** — run skill-local scripts tests, markdown lint, secret scan
5. **Report** — PR check summary with skill names and validator output

### Main branch (integration)

- Nightly or on-merge: `validate_all_skills.sh` for full-repo regression when cheap enough
- Skip full matrix if repo is huge; sample or shard by top-level directory

### Release (continuous delivery)

1. **Trigger** — tag push (`v*`, `skill-*`) or manual `workflow_dispatch`
2. **Validate** — all skills in release set (never package unvalidated trees)
3. **Package** — `package_skill.py` → `dist/<name>.skill`
4. **Publish** — GitHub Release assets, internal blob store, or artifact registry
5. **Record** — changelog entry, commit SHA, artifact digest

## Branching

| Model | Fit for skills repos |
|---|---|
| Trunk + PR | Default: main protected, all changes via PR checks |
| Release branches | Periodic bundled drops to enterprises |
| Tags only | Package exclusively on annotated tags |

## Artifact strategy

| Artifact | When | Retention |
|---|---|---|
| Validator log | Every PR | 30–90 days |
| `.skill` zip | Release tag | Long-term; immutable |
| Manifest (JSON) | Optional | Lists skill name, version, sha256 |

Name artifacts with **skill folder name + version + short SHA** to avoid overwrites.

## Environment gates

| Environment | Typical gate |
|---|---|
| `ci` | Automatic on PR |
| `staging` | Merge to main + optional manual approve |
| `production` | Release tag + required reviewer |

Use GitHub **environments** for approval on org-wide skill distribution, not for every PR validate job.

## Idempotency and concurrency

- `concurrency: group: release-${{ github.ref }}` cancel-in-progress false for releases
- PR jobs: cancel superseded runs on same branch
- Re-running release workflow must not mutate prior release assets (new tag or version suffix)

## Failure handling

| Failure | Action |
|---|---|
| Validator fail on PR | Block merge; fix frontmatter or structure |
| Package fail on release | Do not publish partial bundle; fix and re-tag |
| Bad release in field | Rollback job publishes previous tag artifacts (see deployment reference) |
