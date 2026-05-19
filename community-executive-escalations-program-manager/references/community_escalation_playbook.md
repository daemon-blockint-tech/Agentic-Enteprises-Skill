# Community Escalation Playbook

## When this path applies

- High-reach negative posts (social, forum, GitHub, Discord, review sites)
- Coordinated feedback (many users same issue in 24h)
- Maintainer, champion, or influencer public criticism
- Misinformation about product, security, or pricing
- Community perceived as ignored after product incident

## Goals

1. **Understand** fast (facts, scope, sentiment)
2. **Stabilize** narrative without defensive tone
3. **Route** fix to correct owner (eng, product, docs, policy)
4. **Close the loop** publicly when appropriate

## Response principles

| Do | Don't |
|----|-------|
| Acknowledge quickly with empathy | Argue with users in thread |
| State what is known / unknown | Speculate on root cause |
| Point to status page or tracking issue when exists | Delete criticism without policy basis |
| Thank reporters of real bugs | Dismiss as "noise" |
| Single voice per channel | Multiple conflicting official replies |

## Severity-driven response

| Sev | Response |
|-----|----------|
| E1 | War room + comms/legal + status page; exec-aware brief |
| E2 | Official reply within SLA; engineering/product DRI assigned |
| E3 | Community manager reply + internal ticket |
| E4 | Monitor; batch for weekly community digest |

## Workflow

1. **Monitor** — alerts on keywords, GitHub labels, forum tags, NPS verbatims
2. **Triage** — severity, link to incident if any (`incident-management-engineer`)
3. **Fact sheet** — reproducible? known issue? workaround?
4. **Draft response** — community manager + comms review for E1–E2
5. **Publish** — forum post, GitHub comment, blog update, or status page
6. **Track** — engagement after reply; adjust if misinformation persists
7. **Retro** — playbook update if new failure mode

## Message templates (adapt; get approval)

**Acknowledgment:**
> We're aware of [issue] affecting [scope]. Our team is investigating. We'll update [here/status page] by [time]. Thanks to everyone who reported details.

**Known issue + workaround:**
> This is a known issue tracked in [link]. Workaround: [steps]. Fix targeted for [date/phase] if eng-approved.

**Resolution:**
> We've deployed a fix for [issue]. If you still see problems after [action], contact [support link]. We appreciate your patience.

## Moderation and legal

- Escalate to legal: defamation, threats, PII dumps, IP allegations
- Document moderation actions (hide, lock thread) with policy cite
- Never confirm individual customer data in public threads

## Champions and maintainers

- Separate **private** line for sensitive escalations
- Proactive outreach before public break when health signals red
- Recognize good-faith critics; separate bad-faith spam

## Metrics

- Time to first official response
- Thread sentiment trend (manual or tooling)
- Repeat mentions of same issue post-fix
- Contributor/champion churn signals

## Handoff

- Technical fix → support/engineering with public tracking ID
- Messaging → `communication-lead`
- Product prioritization → product leadership via program RAID
