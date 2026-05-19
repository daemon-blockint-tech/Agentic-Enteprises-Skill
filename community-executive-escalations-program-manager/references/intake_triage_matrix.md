# Intake and Triage Matrix

## Two primary channels

| Channel | Examples | Primary risks |
|---------|----------|---------------|
| **Executive** | CEO email, board intro, strategic account exec call, churn threat from C-suite buyer | Revenue, relationship, contract |
| **Community** | Viral post, GitHub issue storm, forum backlash, influencer thread, champion revolt | Reputation, trust, adoption narrative |

Same incident may hit **both** — link cases; one program DRI.

## Intake fields (minimum)

```markdown
- ID / source (exec referral, CS, support, community monitor, legal)
- Customer or community entity (account ID, handle, forum thread URL)
- Reporter and relationship (role, influence)
- Summary (1–3 sentences, facts only)
- Customer impact (# users, ARR, segment)
- Public visibility (none / limited / viral)
- Product area / suspected component
- Desired date (customer or exec deadline)
- Attachments (ticket IDs, screenshots, links)
```

## Severity matrix

| Sev | Executive path | Community path |
|-----|----------------|----------------|
| **E1** | Imminent churn on flagship account; legal notice; active exec-to-exec | Viral negative; misinformation spreading; safety/legal allegation |
| **E2** | VP-level dissatisfaction; SLA miss on strategic; multi-week blocker | High-engagement thread; maintainer/champion public criticism |
| **E3** | Director-level concern; repeated issue on growth account | Moderate thread; confused messaging; doc gap |
| **E4** | Early signal; proactive outreach | Low reach; isolated feedback |

## Routing rules

| Signal | Route first | Also notify |
|--------|-------------|-------------|
| Technical repro needed | `support-engineer` path → eng | Program PM, CS |
| Product outage | `incident-management-engineer` | Program PM, comms |
| Public reply needed | `communication-lead` | Legal if defamation/PII |
| Contract/terms dispute | `commercial-counsel` | CS, deal ops |
| Billing/renewal | `customer-ops-specialist` | CS |
| Feature commitment question | Product DRI | Program PM, CS |

## SLA examples (tune per org)

| Sev | Acknowledge | Assign DRI | Exec/customer update |
|-----|-------------|------------|----------------------|
| E1 | 1h | 4h | 24h cadence until resolved |
| E2 | 4h | 1 business day | 48h |
| E3 | 1 business day | 2 business days | Weekly |
| E4 | 2 business days | As capacity | On change |

**Acknowledge** = human confirms receipt and next step—not auto-reply only.

## Downgrade / close criteria

- Customer confirms acceptance OR explicit written close from sponsor
- Public thread de-escalated (no new high-reach posts in 72h) with published resolution
- Tracking issue owned by product/engineering with committed date
- No open legal/comms blockers

## Triage checklist (first 30 minutes)

- [ ] Severity assigned with rationale
- [ ] Single DRI named
- [ ] Linked tickets/incidents
- [ ] Public? → comms/legal ping if E1–E2
- [ ] Exec sponsor identified if E1–E2 exec path
- [ ] War room scheduled if cross-team >2 days
