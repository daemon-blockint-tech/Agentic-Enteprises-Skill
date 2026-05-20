# Skill validation and packaging CI

## Tooling paths

| Script | Purpose |
|---|---|
| `~/.claude/skills/skill-creator/scripts/quick_validate.py` | Structure and frontmatter gate |
| `~/.claude/skills/skill-creator/scripts/package_skill.py` | Build `.skill` distribution zip |
| `ai-skill-manager/scripts/validate_all_skills.sh` | Batch validate entire repo |

In CI, vendor scripts into `tools/skill-creator/` or pin a container image if `~/.claude` is unavailable.

## PR workflow contract

**Inputs:** changed skill directory paths  
**Outputs:** pass/fail per skill; logs archived as workflow artifacts  

**Rules:**

1. Every path with edited `SKILL.md` must run `quick_validate.py` on that directory
2. If only `references/` changed, still validate owning skill root
3. Do not run `package_skill.py` on PR unless testing packaging explicitly (slow, noisy)

## Release workflow contract

**Inputs:** tag, optional skill list (default: all skills or tag changelog)  
**Steps:**

```bash
mkdir -p dist
for skill_dir in skills/*/; do
  python3 tools/skill-creator/quick_validate.py "$skill_dir"
  python3 tools/skill-creator/package_skill.py "$skill_dir" dist/
done
```

**Outputs:**

- `dist/<skill-name>.skill` per packaged skill
- Optional `dist/manifest.json` with `{ name, path, sha256, git_sha, tag }`

## When to package

| Event | Package? |
|---|---|
| PR | No (validate only) |
| Merge to main | Optional nightly bundle |
| Release tag | Yes |
| Hotfix branch | Yes, with patch tag |

## Artifact integrity

- Compute `sha256sum dist/*.skill` → attach `checksums.txt` to Release
- Upload artifacts with `actions/upload-artifact` and `softprops/action-gh-release`
- Consumers verify hash before org-wide push

## Integration with skill-creator init

- `init_skill.py` scaffolds folders; CI should fail if example scripts/assets remain in merged skills (policy-dependent)
- Enforce deletion of `scripts/example.py`, `assets/example_asset.txt` via lint or CODEOWNERS review

## Parallelism

Matrix over skill folders; cap `max-parallel` to avoid runner starvation on large monorepos.

## Failure messages

Surface validator message verbatim in PR comment or check summary—speeds fix for frontmatter typos.

## Coordination with ai-skill-manager

- **ai-skill-manager**: catalog, overlap, lifecycle governance
- **cicd-engineer**: wires validation into automation and release mechanics

Both may reference the same scripts; avoid duplicating validator logic in custom bash—call upstream scripts.
