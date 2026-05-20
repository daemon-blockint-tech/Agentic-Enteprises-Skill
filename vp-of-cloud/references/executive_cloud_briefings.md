# Executive cloud briefings

## Table of contents

1. [Audience and format](#audience-and-format)
2. [SteerCo pack](#steerco-pack)
3. [CFO and finance](#cfo-and-finance)
4. [Board and audit](#board-and-audit)
5. [Investment asks](#investment-asks)
6. [Crisis and escalation](#crisis-and-escalation)

## Audience and format

| Audience | Focus | Length |
|----------|-------|--------|
| Cloud SteerCo | Portfolio, blockers, decisions | 5–8 slides |
| CFO / finance | Envelope, forecast, EA, ROI | 3–5 slides + appendix |
| CTO / engineering | Adoption, standards, migration | Narrative + metrics |
| Board / audit committee | Material risk, spend trend, bets | 2–3 slides in infra/cloud section |
| CISO | Risk themes, exceptions, investment | Joint pack — do not duplicate |

Use **decision-first** structure: decision needed → options → recommendation → ask.

## SteerCo pack

Monthly template:

1. **Headline** — on track / at risk / off track (one sentence)
2. **Metrics** — adoption, spend vs plan, commit util, open exceptions
3. **Portfolio** — wave status, stage-gate completions, slips
4. **Decisions** — 2–3 items with owner and date
5. **Risks** — top 5 with mitigation and escalation path
6. **Appendix** — detail for delegates

VP presents; TPM owns RAID appendix; architects own technical depth offline.

## CFO and finance

Lead with **money and accountability**:

| Slide | Content |
|-------|---------|
| Run-rate | Actual vs envelope; forecast rest of year |
| Drivers | Migration dual-run, AI/GPU, region, new products |
| EA | Utilization, true-up risk, renegotiation timeline |
| Efficiency | Waste removed, commit coverage, unit cost trend |
| Ask | Funding, headcount, or envelope change |

Pair every cost increase with **plan to absorb** or **benefit timing**.

`cloud-economist` supports scenarios; VP owns narrative.

## Board and audit

Materiality filter — board cares when:

- Cloud spend is **large %** of OpEx or growing >X% YoY
- **Regulatory** or customer audit finding in cloud
- **Multi-year EA** or vendor concentration risk
- **Major migration** affects revenue or availability
- **Security incident** with cloud root cause

Include: trend chart, top risks, management actions, no jargon (no service acronyms without gloss).

Coordinate with `vp-of-infrastructure` if **single infra section** — split cloud vs DC clearly.

## Investment asks

Structure asks:

| Element | Detail |
|---------|--------|
| Problem | Cost, risk, or speed constraint |
| Options | Do nothing, partial, full program |
| Recommendation | One clear choice |
| Cost | 3-year TCO; year-1 cash |
| Benefits | Quantified where possible |
| Metrics | How success measured in 4 quarters |

Tie to **strategic theme** from cloud strategy doc.

## Crisis and escalation

Brief executives within **24h** for:

- Region-wide outage affecting revenue
- Data exposure in cloud workload
- EA true-up surprise >material threshold
- Migration rollback affecting customers

Template: timeline, customer impact, root cause (facts), immediate actions, decision needed.

Delegate technical war room to `cloud-engineer`, `site-reliability-engineer`, `cloud-security-engineer`.

VP owns **external narrative** alignment with `communication-lead`.
