# Outreach and engagement sequences

## Table of contents

1. [Principles](#principles)
2. [Personalization framework](#personalization-framework)
3. [First-touch templates](#first-touch-templates)
4. [Multi-touch sequences](#multi-touch-sequences)
5. [Channel-specific guidance](#channel-specific-guidance)
6. [Compliance and opt-out](#compliance-and-opt-out)
7. [Measurement](#measurement)

## Principles

- **Relevant**: Tie message to public work (talk, repo, post)—one specific detail
- **Concise**: Mobile-readable; respect senior candidates' time
- **Honest**: Real role, real company; no bait-and-switch
- **Low friction**: Clear CTA (15-min chat, not "apply to 12 steps")
- **Persistent but polite**: 3–4 touches max for cold; stop on decline

## Personalization framework

| Token | Source (public) |
|---|---|
| `{hook}` | Recent talk, blog, OSS release |
| `{skill_match}` | Overlap between their work and req |
| `{company_pitch}` | 1 sentence why your company matters |
| `{role_hook}` | Problem the team solves |
| `{cta}` | Calendar link or reply ask |

Avoid: marital status, age cues, political views, health, unrelated personal data.

## First-touch templates

**Engineering (LinkedIn/InMail):**

```
Hi {name} — I saw your work on {hook} and thought it lined up with
{skill_match}. We're hiring a {title} to {role_hook} at {company}.
Open to a 20-min intro? No pressure if timing's off.
```

**Executive (shorter):**

```
{name}, your track record in {domain} at {company} stood out. We're
building {company_pitch} and looking for a {title}. Worth a brief
conversation?
```

**Referral intro:**

```
{name}, {referrer} suggested I reach out regarding {title} at
{company}. {one_line_pitch}. Happy to share more if relevant.
```

Customize every send; templates are scaffolding only.

## Multi-touch sequences

Example **cold sequence** (business days):

| Day | Channel | Purpose |
|-----|---------|---------|
| 0 | LinkedIn / email | First touch + CTA |
| 3 | Email | Add detail: team, stack, impact |
| 7 | LinkedIn | Short bump; new angle (e.g., podcast they did) |
| 14 | Email | Final; offer to close loop |

Rules:

- Vary subject lines; never "just following up" alone
- If open but no reply, try different channel once
- Move to nurture pool if interested but timing bad (6-month revisit)

## Channel-specific guidance

| Channel | Notes |
|---|---|
| LinkedIn | Connection note <300 chars; InMail for closed profiles |
| Email | Verified work email preferred; avoid personal unless public |
| GitHub | Issue/PR comments only when contextually appropriate—usually avoid cold |
| Community | DM only after genuine participation |

## Compliance and opt-out

- Include **opt-out** language where required by org policy
- Honor global unsubscribe and CRM suppression lists
- Do not re-add candidates who declined within cooling period
- Document consent basis per privacy team for EU/UK candidates

## Measurement

Track per sequence variant:

| Metric | Definition |
|---|---|
| Send volume | Messages sent |
| Open rate | If available (email) |
| Reply rate | Any human reply |
| Positive rate | Interested in conversation |
| Handoff rate | Accepted by recruiter for screen |

Review weekly; pause variants with reply rate <10% after 50+ sends without testing new hooks.
