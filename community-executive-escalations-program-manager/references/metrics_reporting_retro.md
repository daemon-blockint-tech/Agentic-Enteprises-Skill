# Metrics, Reporting, and Retrospective

## Program KPIs

| Metric | Definition | Target direction |
|--------|------------|------------------|
| Time to acknowledge | Intake → human ack | Down |
| Time to DRI | Intake → named owner | Down |
| Time to resolve | Intake → close per criteria | Down |
| SLA adherence | % cases within sev SLA | Up |
| Repeat escalation rate | Same account/issue within 90d | Down |
| Exec brief latency | E1 open → first brief | Down |
| Community first response | E1–E2 public → official reply | Down |
| Customer satisfaction post-close | Survey or explicit sign-off | Up |
| Playbook coverage | % cases matching known playbook | Up |

Segment by: exec vs community, severity, product area, region.

## Executive dashboard (monthly)

1. **Volume** — opened, closed, open by severity
2. **Aging** — cases past SLA; oldest open
3. **Themes** — top 5 root-cause categories
4. **Revenue exposure** — ARR at risk in open queue
5. **Public** — open community E1–E2 count
6. **Program health** — SLA trend, repeat rate, staffing gaps

## Weekly operational report

```markdown
## Escalation program — Week of [date]

**Open:** E1 n | E2 n | E3 n
**Closed this week:** n
**SLA misses:** [case IDs]
**Top themes:** 1. … 2. …
**Decisions needed:** [bullets]
**Next week focus:** …
```

## Case close record

```markdown
- Case ID, severity, channel (exec/community/both)
- Duration (open days)
- Root cause category
- Owning team for fix
- Customer/public outcome
- Playbook used? Y/N — delta if N
- Repeat risk: low/med/high
```

## Retrospective (within 5 business days of E1 close)

| Question | Output |
|----------|--------|
| What happened? | Timeline |
| What worked? | Keep |
| What failed? | Change |
| Where did we over/under-escalate? | Triage tweak |
| Playbook gap? | PR to reference doc |
| Metrics impact? | Dashboard note |

Blameless; focus on system fixes.

## Governance reviews

| Cadence | Audience | Use metrics for |
|---------|----------|-----------------|
| Weekly | Program + functional leads | Staffing, reds |
| Monthly | VP steering | Policy, SLA changes |
| Quarterly | Exec sponsor | Investment, tooling |

## Tooling hints

- CRM flag for exec escalation + link to war room channel
- Single dashboard (Sheets, BI) fed from case tracker
- Do not double-count tickets and program cases—link IDs

## Pair with TPM

Use `technical-program-manager` when escalation spawns multi-quarter remediation program; this skill owns **case program** until handoff.
