# Validation and packaging

## Table of contents

1. [Single skill](#single-skill)
2. [Batch validate](#batch-validate)
3. [Package for distribution](#package-for-distribution)
4. [CI suggestion](#ci-suggestion)

## Single skill

```bash
python3 ~/.claude/skills/skill-creator/scripts/quick_validate.py path/to/skill-dir
```

Fix reported YAML, naming, or description issues before merge.

## Batch validate

From repo root:

```bash
bash ai-skill-manager/scripts/validate_all_skills.sh .
```

Or set `SKILL_VALIDATOR` if skill-creator lives elsewhere.

Exit non-zero if any skill fails — use in CI.

## Package for distribution

```bash
mkdir -p dist
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py path/to/skill-dir ./dist
```

Produces `dist/<skill-name>.skill` (zip). Package only after validation passes.

## CI suggestion

On pull requests that touch `*/SKILL.md`:

1. Run `validate_all_skills.sh`
2. Optional: diff grep for removed skill names → require cross-link updates

Do not package all skills on every PR unless releasing a bundle.
