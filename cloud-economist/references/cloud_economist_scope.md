# Cloud economist scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Questions economists answer](#questions-economists-answer)
3. [Inputs and outputs](#inputs-and-outputs)
4. [Handoffs](#handoffs)

## Role boundary

| cloud-economist | Partner |
|---|---|
| 3–5y TCO, NPV, option compare | `finops-analyst` — monthly actuals, waste, CUR |
| Economic memo for ADR | `cloud-architect` — technical design |
| EA $ structure modeling | `enterprise-cloud-architect` — program design |
| Journal entries | `compute-accounting-manager` |
| General strategy | `business-consultant` |

Economist **models**; does not own billing consoles or terraform.

## Questions economists answer

- Should we migrate workload X to cloud vs extend colo?
- What is NPV of a 3-year all-upfront commit vs pay-as-you-go?
- Which region minimizes TCO given latency constraints?
- How does gross margin change if egress doubles?
- What commit coverage maximizes risk-adjusted savings?
- Is multi-cloud worth +$Y/year for portability?

## Inputs and outputs

**Inputs:**

- Usage forecasts (from product, FinOps history, architecture)
- List prices and discount schedules (EA, private offers)
- Labor rates (run vs build), migration one-time costs
- SLO and residency constraints from architecture

**Outputs:**

- Spreadsheet or notebook model with documented assumptions
- Executive summary with recommendation and risks
- Feeds ADRs, board decks, negotiation targets

## Handoffs

| After decision | Owner |
|---|---|
| Tagging, budgets, rightsizing | `finops-analyst` |
| Landing zone / service choice | `cloud-architect` |
| Purchase commit / EA signature | Finance + `enterprise-cloud-architect` |
| GL treatment of prepaids | `compute-accounting-manager` |
