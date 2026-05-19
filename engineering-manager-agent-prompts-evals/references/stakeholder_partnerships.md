# Stakeholder Partnerships

## Product management

| You provide | You need |
|---|---|
| Eval-based ship recommendations | Prioritized agents and dates |
| Clear limitations for GTM | Early prompt/tool scope lock |
| Pass-rate dashboards by slice | Acceptance of eval-driven delays |

## Applied AI architect

- Escalate new tool surfaces and multi-agent handoffs
- Do not bypass ADRs for tenant/data boundaries

## Risk and compliance

- Tier assignment before roadmap commit
- Waiver path for time pressure
- Policy updates → new refusal goldens within SLA

## Red team

- Schedule before Tier 1–2 GA
- Convert findings to **regression tags** in golden set
- Not a substitute for continuous CI

## AI lead ops

- Incidents caused by prompts: joint post-mortem
- Production judge sampling alignment
- Model version changes → re-baseline plan

## IC team (`prompt-engineer-agent-prompts-evals`)

EM protects **eval debt time**; ICs own technical depth.

## Status rhythm

| Forum | Frequency |
|---|---|
| Eval health review | Weekly |
| Launch readiness | Per milestone |
| Judge calibration | Monthly |

Anti-pattern: EM rewriting prompts in prod without IC review.
