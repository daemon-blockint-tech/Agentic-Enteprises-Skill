# GitHub Actions and build

## Workflow layout

```
.github/workflows/
  skill-validate-pr.yml      # on pull_request
  skill-release.yml          # on push tags or workflow_dispatch
  reusable-validate.yml      # workflow_call
```

## Changed-skill detection

**Option A — paths filter (simple)**

```yaml
on:
  pull_request:
    paths:
      - '**/SKILL.md'
      - '**/references/**'
      - '**/scripts/**'
```

**Option B — dynamic list (monorepo)**

- Job lists directories containing `SKILL.md` at depth 1 (or 2)
- `git diff --name-only origin/main...` → map files to skill roots
- Output JSON array for matrix `skill: ${{ fromJson(needs.changes.outputs.skills) }}`

## Validate job pattern

```yaml
jobs:
  validate:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        skill: ${{ fromJson(needs.detect.outputs.skills) }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install validator deps
        run: pip install pyyaml
      - name: quick_validate
        run: |
          python3 ~/.claude/skills/skill-creator/scripts/quick_validate.py "${{ matrix.skill }}"
```

Pin skill-creator via submodule, copy script into repo, or install from known commit in CI.

## Reusable workflow

Expose inputs: `skill_path`, `python_version`. Call from PR and release workflows to avoid drift.

## Permissions (least privilege)

| Event | `contents` | `pull-requests` | `id-token` |
|---|---|---|---|
| PR validate | read | write (checks) | only if OIDC publish |
| Release | read + write if attaching assets | — | if cloud upload |

Avoid `permissions: write-all`.

## Fork safety

- Prefer `pull_request` over `pull_request_target` for untrusted forks
- Never expose org secrets to fork PR workflows
- For label-gated workflows on external contributors, use explicit `labeled` + CODEOWNERS review

## Caching

- Cache pip packages for PyYAML if validator needs it
- Do not cache `dist/*.skill` across release versions without content-addressed keys

## Secrets

| Secret | Use |
|---|---|
| `SKILL_REGISTRY_TOKEN` | Upload to internal registry |
| Cloud OIDC | Prefer over long-lived keys |

Document required secrets in repo `CONTRIBUTING` or internal runbook—not in skill folders.

## Build summary for PRs

Emit step summary markdown: skill name, pass/fail, validator message. Surfaces failures without digging logs.
