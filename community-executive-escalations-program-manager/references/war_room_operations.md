# War Room Operations

## When to open a war room

- E1–E2 exec or community escalation
- Cross-functional blocker with no single owner >1 business day
- Customer-imposed deadline within 72h
- Public + private escalation on same underlying issue

## War room charter (one slide)

```markdown
**Case ID:** — **DRI:** Program PM — **Customer/community:** —
**Objective:** Resolve [specific outcome] by [date]
**In scope:** — **Out of scope:** —
**Cadence:** Daily 30m at [time] until exit criteria met
**Participants:** [names/roles]
```

## Standing agenda (30 minutes)

| Min | Topic |
|-----|-------|
| 0–5 | Facts since last session (no debate) |
| 5–10 | Customer/community status and next touch |
| 10–20 | Blockers — owner and ETA per blocker |
| 20–25 | Decisions needed today |
| 25–30 | Actions recap; next meeting |

## Roles in session

| Role | Behavior |
|------|----------|
| Chair (Program PM) | Timebox; drive decisions; assign actions |
| Scribe | RAID updates live |
| Account/community DRI | Speaks for customer/public plan |
| Technical DRI | Facts only; no speculative ETAs |
| Exec sponsor | Decides trade-offs; joins only when needed |

## Decision log entry

```markdown
| Date | Decision | Rationale | Approver | Communicated to customer? |
```

## RAID linkage

| Type | Example |
|------|---------|
| Risk | Fix may miss renewal date |
| Action | Eng to ship patch by Friday |
| Issue | Legal reviewing public post |
| Dependency | Billing team must credit invoice |

## Exit criteria

- [ ] Customer sponsor accepts resolution OR documented impasse path
- [ ] Public thread plan executed (if applicable)
- [ ] No open E1–E2 blockers without owner and date
- [ ] Handoff to steady-state owner (CS, product, support)
- [ ] Retro scheduled within 5 business days

## Async norms between meetings

- Single Slack/Teams channel per case; no side DMs for decisions
- Status update at agreed cadence even if "no change"
- Escalate silent stakeholders after one missed update

## Anti-patterns

- War room without technical DRI
- Re-litigating severity each day
- Large audience without decision authority
- Continuing war room after exit criteria met
