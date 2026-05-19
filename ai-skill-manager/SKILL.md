---
name: ai-skill-manager
description: |
  Guides management of an enterprise Agent Skills portfolio—inventory and catalog hygiene, naming
  and structure standards, overlap and routing deduplication, cross-linking between skills, validation
  and packaging at scale, lifecycle (split, merge, deprecate), and quality/security review before
  distribution.
  Use when curating a skills repo, auditing skill quality, fixing trigger overlap, maintaining a
  skill catalog, batch-validating or packaging skills, or governing who may publish skills—not for
  authoring a single new skill from scratch (follow skill-creator), implementing agents or RAG
  (ai-engineer), production LLM ops (ai-lead-ops), or writing prompts inside one skill (prompt-engineer).
---

# AI Skill Manager

## When to Use

- Inventory skills in a repo or org catalog; find gaps and duplicates
- Audit `description` frontmatter for clear triggers and routing
- Add or fix **When NOT to Use** and **Related skills** cross-links
- Run batch validation or package `.skill` bundles for distribution
- Split an overloaded skill or merge overlapping ones
- Deprecate or rename a skill without breaking consumers
- Define governance: review checklist, owners, publish cadence
- Triage security concerns in skill content (secrets, dangerous scripts)

## When NOT to Use

- Step-by-step creation of one new skill → use **skill-creator** (`init_skill.py`, `package_skill.py`)
- Design RAG, agents, eval harnesses → `ai-engineer`
- Model/prompt release ops and cost rituals → `ai-lead-ops`
- AI regulatory policy registers → `ai-risk-governance`
- Rewrite prompts inside a domain skill → `prompt-engineer`

## Related skills

| Need | Skill |
|---|---|
| Build and ship AI features | `ai-engineer` |
| Prompt and tool-schema craft | `prompt-engineer` |
| AI risk tiering and policies | `ai-risk-governance` |
| AI production ops cadence | `ai-lead-ops` |
| Token cost programs | `ai-token-improvement-plan-engineer` |
| Comms for rolling out new capabilities | `communication-lead` |

## Core Workflows

### 1. Portfolio inventory

For each skill directory with `SKILL.md`, record:

| Field | Source |
|---|---|
| `name` | YAML frontmatter |
| One-line purpose | First sentence of `description` |
| Primary triggers | `description` (not body) |
| References count | `references/*.md` |
| Has scripts/assets | optional dirs |

Flag: same trigger keywords in multiple `description` fields.

**See `references/catalog_inventory.md`.**

### 2. Quality gate (per skill)

Before merge or publish:

1. `name` matches folder name (hyphen-case, ≤64 chars)
2. `description` includes **what** + **when to use** + **when NOT** (peer skill names)
3. Body ≤ ~500 lines; deep detail in `references/`
4. No README/CHANGELOG inside skill folder
5. Run validator (below)

**See `references/quality_standards.md`.**

### 3. Routing and overlap

When two skills trigger on the same user phrase:

1. Pick **primary** owner of the workflow
2. Move triggers into primary `description`; add explicit negation in the other
3. Add reciprocal **Related skills** rows
4. If overlap >30% of workflows, plan **split** or **merge**

**See `references/routing_and_overlap.md`.**

### 4. Lifecycle

| Action | When |
|---|---|
| **Create** | New domain with ≥3 repeatable workflows → skill-creator |
| **Split** | SKILL.md or references too large; distinct audiences |
| **Merge** | Two skills always loaded together; duplicate triggers |
| **Deprecate** | Superseded; keep folder 1 release with redirect text in `description` |

**See `references/skill_lifecycle.md`.**

### 5. Validate and package

Single skill:

```bash
python3 ~/.claude/skills/skill-creator/scripts/quick_validate.py <path/to/skill-dir>
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py <path/to/skill-dir> ./dist
```

Entire repo (this skill bundle):

```bash
bash ai-skill-manager/scripts/validate_all_skills.sh /path/to/Agentic-Enteprises-Skill
```

**See `references/validation_packaging.md`.**

### 6. Security and supply chain

Review before org-wide install:

- No secrets, API keys, or customer data in skills
- Scripts: least privilege; no `curl | bash` patterns
- `description` must not instruct bypassing safety or compliance
- Third-party skills: same checklist + license note

**See `references/portfolio_governance.md`.**

## Output standards

- Inventory as table: name, purpose, triggers, overlap risk, last reviewed
- Change proposals: what moves, which skills get updated cross-links
- Deprecation notice: replacement skill name and migration sentence for `description`

## When to load references

- **Inventory and catalog** → `references/catalog_inventory.md`
- **Review checklist** → `references/quality_standards.md`
- **Dedup and routing** → `references/routing_and_overlap.md`
- **Split/merge/deprecate** → `references/skill_lifecycle.md`
- **validate/package commands** → `references/validation_packaging.md`
- **RACI and publish policy** → `references/portfolio_governance.md`
