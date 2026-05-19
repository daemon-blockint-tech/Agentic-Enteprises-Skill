# Portfolio governance

## Table of contents

1. [Roles](#roles)
2. [Publish workflow](#publish-workflow)
3. [Security review](#security-review)
4. [Versioning](#versioning)

## Roles

| Role | Accountable for |
|---|---|
| Skill owner (domain) | Accuracy, triggers, references |
| AI skill manager | Catalog, overlap, validation gate |
| Security | Scripts, external fetch, data handling |
| Platform / IT | Install path, agent allowlists |

## Publish workflow

1. Author opens PR with skill or delta
2. Owner + skill manager review checklist (`quality_standards.md`)
3. `validate_all_skills.sh` green
4. Cross-links updated in peer skills
5. Merge; tag release if distributing `.skill` bundles
6. Announce via `communication-lead` if org-wide behavior changes

## Security review

Block publish if skill contains:

- Credentials, tokens, private URLs, customer examples
- Scripts that disable safeguards or exfiltrate data
- Instructions to ignore legal, export, or compliance rules
- Unsigned third-party scripts without review

Prefer references to public docs over copying restricted internal policy text.

## Versioning

- Git tags on repo for catalog snapshots (e.g. `skills-2026.05`)
- Per-skill breaking change: note in PR; update deprecated skill `description`
- Agent installs: pin tag or hash; document upgrade path for teams

Align with [Agent Skills open format](https://agentskills.io) when integrating external tooling.
