# Reporting and Escalation

## Weekly status (delivery program)

1. **Headline RAG** and demand date confidence
2. **Burn-up** — kW and racks vs plan
3. **Critical path** — next 3 milestones and owners
4. **RAID top 5** — reds and ambers only in exec summary
5. **Decisions needed** — numbered with recommendation
6. **Budget** — spend vs forecast, contingency remaining

## RAG rules

| RAG | Capacity delivery |
|---|---|
| **Green** | ≤1 week slip vs baseline or recovered |
| **Amber** | 1–4 weeks slip; mitigation plan approved |
| **Red** | >4 weeks or no credible recovery; demand date at risk |

## Escalation matrix

| Trigger | Escalate to |
|---|---|
| Critical path slip >2 weeks | Portfolio lead + design lead |
| Budget overrun >contingency | Finance + steering |
| Utility or colo force majeure | Exec sponsor |
| Safety stop-work | Facilities exec + compliance |

## Steering vs portfolio

| Forum | Content |
|---|---|
| **Delivery weekly** | Tactical blockers |
| **Portfolio monthly** | Cross-site capacity, tradeoffs |
| **Steering** | Decisions, funding, date change |

## Integration with compute demand

When `data-center-compute-supply-efficiency` shows GPU queue pressure:

- Quantify MW/racks needed vs delivery plan
- Propose accelerate, partial delivery, or cloud bridge
- Do not promise workload-ready without gate sign-off

## Anti-patterns

- Reporting green while critical path items are red
- Separate schedules that do not link dependencies
- Declaring rack-ready without signed checklist
