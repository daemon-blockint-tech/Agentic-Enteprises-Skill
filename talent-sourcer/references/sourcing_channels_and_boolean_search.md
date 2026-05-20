# Sourcing channels and boolean search

## Table of contents

1. [Boolean fundamentals](#boolean-fundamentals)
2. [LinkedIn sourcing](#linkedin-sourcing)
3. [X-ray and web search](#x-ray-and-web-search)
4. [GitHub and technical sourcing](#github-and-technical-sourcing)
5. [Communities and events](#communities-and-events)
6. [Boolean pattern library](#boolean-pattern-library)
7. [Quality and iteration](#quality-and-iteration)

## Boolean fundamentals

| Operator | Use |
|---|---|
| `AND` | Require all terms (often implicit) |
| `OR` | Synonyms, alternate titles |
| `NOT` / `-` | Exclude noise (use sparingly) |
| `"phrase"` | Exact match |
| `( )` | Group OR blocks |

**Rules:**

- Start broad, then narrow with `NOT` and filters
- Keep a **variant log** (v1, v2) with result counts
- Prefer title + skill + company over keyword soup
- Test synonyms: "kubernetes" OR "k8s"

## LinkedIn sourcing

Typical filter stack:

1. Title keywords (current + past)
2. Skills (required vs optional)
3. Geography + open to remote
4. Company (current/past) lists
5. Seniority / years of experience
6. Activity signals where available (open to work — use ethically)

**Recruiter-style strings** (adapt to platform syntax):

```
("staff engineer" OR "principal engineer") AND (rust OR golang)
NOT (recruiter OR "talent acquisition")
```

Save searches; re-run on cadence for new profiles.

## X-ray and web search

Find public profiles outside native recruiter UI:

```
site:linkedin.com/in ("distributed systems" OR "data platform")
("Acme Corp" OR "Beta Inc") -intitle:recruiter
```

```
site:github.com "location: San Francisco" language:Rust stars:>50
```

Respect robots.txt and terms of service; prefer official APIs where licensed.

## GitHub and technical sourcing

Signals for engineering ICs:

| Signal | Query idea |
|---|---|
| Language depth | `language:Go` org:target-org |
| Impact | stars, forks, contributor graphs |
| Domain | repo topics, README keywords |
| Activity | recent commits, release cadence |

Cross-link GitHub username to LinkedIn via public bio or search—do not assume identity without confirmation.

## Communities and events

| Source | Tactics |
|---|---|
| Slack/Discord guilds | Speaker lists, maintainers, help threads |
| Meetups / conferences | Agenda speakers, sponsors |
| Newsletters / podcasts | Guest lists |
| OSS foundations | Committers, TSC members |
| Alumni groups | School/company chapters (policy permitting) |

Engage **in community norms**—value-first, not spam.

## Boolean pattern library

**Backend IC (example):**

```
(title:"software engineer" OR title:"backend engineer" OR title:"SWE")
AND (python OR java OR go)
AND (microservices OR "distributed systems")
NOT (intern OR student OR recruiter)
```

**Product leader (example):**

```
(title:"product manager" OR title:"group product manager")
AND (B2B OR SaaS OR "enterprise")
AND (roadmap OR "go-to-market")
```

**Security (example):**

```
(title:"security engineer" OR title:"application security")
AND (OWASP OR "threat modeling" OR AppSec)
```

Customize per ICP; store winners in playbook.

## Quality and iteration

| Metric | Action if low |
|---|---|
| High views, low qualify | Tighten ICP or booleans |
| High qualify, low reply | Improve outreach hooks |
| High reply, low interest | Calibrate role pitch / comp |
| Duplicate rate high | Fix CRM merge rules |

Review boolean performance **weekly**; retire strings with <5% qualify rate after sufficient volume.
