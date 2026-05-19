# Quality standards

## Table of contents

1. [Frontmatter](#frontmatter)
2. [SKILL.md body](#skillmd-body)
3. [Bundled resources](#bundled-resources)
4. [Review checklist](#review-checklist)

## Frontmatter

Required YAML keys only: `name`, `description` (optional: `license`, `allowed-tools`, `metadata` per validator).

- `name`: hyphen-case, matches directory name, ≤64 characters
- `description`: multi-line `|` block; includes:
  - Capability summary
  - **Use when** — concrete triggers
  - **Not for** — peer skill names (routing)

Do not put "When to use" only in the body — agents read `description` before loading the body.

## SKILL.md body

- Imperative voice
- **When to Use** / **When NOT to Use** / **Related skills** table
- Core workflows numbered; link to `references/` for depth
- Target &lt;500 lines in body

## Bundled resources

| Dir | Purpose |
|---|---|
| `references/` | Load on demand |
| `scripts/` | Deterministic, tested ops |
| `assets/` | Templates not loaded into context |

Forbidden inside skill folder: `README.md`, `CHANGELOG.md`, install guides.

## Review checklist

- [ ] Validator passes
- [ ] No secrets or env-specific URLs
- [ ] Scripts run in clean shell (if present)
- [ ] Cross-links added to ≥2 related skills
- [ ] No duplicate of skill-creator content (point to skill-creator instead)
