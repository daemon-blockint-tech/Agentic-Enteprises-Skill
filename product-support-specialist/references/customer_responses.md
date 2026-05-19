# Customer Responses

## Response structure

```markdown
1. **Direct answer** (1–2 sentences)
2. **Steps** (numbered, current UI labels)
3. **Context** (plan limit, expected behavior, link)
4. **Next steps** (what you will do / what they should send)
5. **Close** (invite reply if unresolved)
```

## Tone

| Do | Don't |
|----|-------|
| Acknowledge effort | Blame user for misconfiguration |
| Be specific | "We're looking into it" only |
| Admit known issues | Speculate on root cause |
| Match formality to customer | Over-apologize for design limits |

## Macro building blocks

**Acknowledge + answer:**
> You can export reports from **Settings → Reports → Export**. CSV includes all columns visible in the table.

**Known issue:**
> We're aware that [issue] affects [scope]. Engineering is tracking [TICKET]. Workaround: [steps] until fix ships.

**Works as designed:**
> [Feature] is available on [plan]. On your current plan, [alternative]. Details: [KB link].

**Need more info:**
> To help quickly, please send: (1) screenshot of [screen], (2) approximate time of error, (3) browser version.

**Handoff:**
> I'm connecting you with our technical team who can investigate logs. You'll hear from [queue] within [SLA]. Reference: [ticket ID].

## Localization and accessibility

- Plain language; define acronyms once
- Describe UI elements consistently with product
- Offer async-friendly steps (no "call now" unless tier includes phone)

## Sensitive situations

| Situation | Approach |
|-----------|----------|
| Angry customer | Stay factual; escalate severity if abusive |
| Data loss fear | Confirm what is/isn't deleted; escalate P1 |
| Competitor mention | No disparagement; focus on enablement |
| Security concern | Do not ask for passwords; route per security policy |

## Quality check before send

- [ ] Steps tested or verified in docs in last 90 days
- [ ] Plan/limit mentioned if relevant
- [ ] No promise of date without eng confirmation
- [ ] KB link works
- [ ] Internal notes updated for next agent
