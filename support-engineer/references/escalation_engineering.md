# Engineering escalation

## Table of contents

1. [Ticket quality bar](#ticket-quality-bar)
2. [Severity for engineering](#severity-for-engineering)

## Ticket quality bar

Engineering should not need to ask:

- [ ] Clear repro or explicit "cannot reproduce" with attempts listed
- [ ] Single owner on support side
- [ ] Customer impact quantified
- [ ] Regression yes/no and first seen version/date

Label: `customer-reported`, `repro-confirmed`, `regression`.

## Severity for engineering

| Label | Meaning |
|---|---|
| S0 | Active outage, many customers |
| S1 | Major broken path, workaround weak |
| S2 | Isolated bug |
| S3 | Minor / tech debt |

Match internal engineering severity if different from customer-facing P-level.
