# Skill lifecycle

## Table of contents

1. [Create](#create)
2. [Iterate](#iterate)
3. [Split](#split)
4. [Merge](#merge)
5. [Deprecate](#deprecate)

## Create

Use **skill-creator** process:

```bash
python3 ~/.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path <repo-root>
```

Then: references → SKILL.md → validate → cross-link peers → optional package.

Only create a new skill when an existing one cannot absorb workflows without bloating triggers.

## Iterate

After real usage:

1. Move verbose content from SKILL.md → `references/`
2. Tighten `description` if misfires reported
3. Re-run validator and batch script

## Split

When:

- Multiple frameworks (e.g. AWS vs Azure) each &gt;100 lines
- Distinct audiences with different triggers

Steps:

1. Create new skill with focused `description`
2. Move reference files to new folder
3. Shorten original; add **When NOT** → new skill
4. Update cross-links across repo (grep skill name)

## Merge

When:

- Duplicate triggers cause wrong skill &gt;20% of time
- Maintenance burden exceeds value

Steps:

1. Pick surviving `name`
2. Fold references; dedupe headings
3. Union `description` triggers (carefully)
4. Deprecate removed skill (below)

## Deprecate

1. Add to old skill `description`: `Deprecated—use <new-name> for ...`
2. Remove old skill from install bundles after one release
3. Grep repo for backtick references; update tables
4. Keep directory one cycle for git history, then delete if policy allows
