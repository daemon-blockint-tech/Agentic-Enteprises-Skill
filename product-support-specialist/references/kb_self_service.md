# Knowledge Base and Self-Service

## When to create or update KB

| Trigger | Action |
|---------|--------|
| Same question 3+ times in 30 days | New or merge article |
| Release changes UI | Update screenshots/steps |
| Macro >200 words | Consider article + short macro |
| Known issue with workaround | Known-issue article + link in status |
| Plan change | Update limit tables |

Deep API reference → `tech-writer-researcher`; support KB focuses on **tasks**.

## Article structure

```markdown
# Title: Task-oriented (How to export a report)

**Applies to:** plans, roles
**Time:** ~5 min

## Before you begin
## Steps
## Troubleshooting
## Related articles
```

## Deflection without deflecting

- Link KB **after** summarizing answer in ticket (not only link)
- Confirm article solved: "Did this help?"
- If article wrong, fix same day and note ticket

## Search and taxonomy

| Practice | Why |
|----------|-----|
| Consistent product area tags | Reporting |
| Synonyms in intro | Search hit rate |
| Avoid internal codenames | Customer-facing |

## Macros ↔ KB

| Macro | KB |
|-------|-----|
| Short pointer | Link + one-line summary |
| Long procedure | KB only; macro is link |

## Quality metrics

- Article views after ticket deflection
- CSAT on article
- Tickets reopened after KB send (quality signal)
- Time on page (too long = rewrite)

## Gaps report (weekly)

```markdown
| Theme | Ticket count | KB exists? | Owner |
```

Share with docs and product support lead.

## Community and forums

For public answers:

- No private data
- Align with `community_escalation_playbook` tone if in `community-executive-escalations-program-manager`
- Link official KB over ad-hoc replies when possible

## Anti-patterns

- Stale screenshots after redesign
- "Contact support" as only step
- Duplicate articles competing in search
