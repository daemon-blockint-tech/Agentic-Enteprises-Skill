# Testing gates and quality

## Gate stack (skills repo)

| Order | Gate | Blocks merge |
|---|---|---|
| 1 | `quick_validate.py` per changed skill | Yes |
| 2 | Optional full repo `validate_all_skills.sh` | Yes on main/nightly |
| 3 | Secret scan (gitleaks, trufflehog) | Yes |
| 4 | Description overlap grep (custom) | Warn or yes per policy |
| 5 | Human review (CODEOWNERS) | Yes |

## quick_validate expectations

- `SKILL.md` exists with valid YAML frontmatter
- Only allowed frontmatter keys (per skill-creator): `name`, `description`, `license`, `allowed-tools`, `metadata`
- `description` ≤ 1024 characters; no angle brackets
- `name` conventions per org policy (many repos use hyphen-case folder name)

Treat validator exit code non-zero as **hard fail**.

## Batch validation

From repo root:

```bash
bash ai-skill-manager/scripts/validate_all_skills.sh .
```

Use on:

- Nightly schedule
- Before major release tag
- After bulk import or rename

Shard by alphabet or top-level folder if runtime exceeds CI budget.

## PR policy

- Require status check `skill-validate` (or matrix aggregate)
- Require up-to-date branch with main before merge
- Block force-push to main without admin exception

## Quality beyond validator

| Check | Method |
|---|---|
| **When NOT to Use** present | Lint script or review checklist |
| **Related skills** table | Grep broken `skill` backtick names |
| Reference files exist | CI lists paths from SKILL.md |
| No README in skill dir | Filesystem glob fail |
| Scripts executable safety | Review + optional `shellcheck` |

## Test data and fixtures

- Keep minimal fixture skill under `tests/fixtures/valid-skill/` for workflow integration tests
- Do not commit real API keys in fixture skills

## Flake management

- Validator should be deterministic; if flaky, fix script not retry blindly
- Network calls in CI for packaging uploads: retry with backoff only on 5xx

## Reporting metrics (optional)

Track per week: PR validate duration, fail rate by skill, release count, rollback count.
