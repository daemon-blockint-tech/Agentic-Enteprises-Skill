---
name: business-model-researcher
description: |
  Guides business model research—Business Model Canvas and Lean Canvas, value proposition and
  customer segments, revenue and pricing models, unit economics (CAC, LTV, payback), market sizing
  (TAM/SAM/SOM), competitive business-model benchmarking, and evidence-backed synthesis for
  startups and product strategy.
  Use when researching how a company or idea makes money, comparing competitor monetization,
  sizing a market, stress-testing unit economics, drafting a canvas for a pitch, or documenting
  monetization hypotheses—for shipping pricing/packaging PRDs and paywalls use
  product-management-monetization—not for delivery BRDs (business-analyst), steerCo consulting engagements
  (business-consultant), GAAP revenue recognition (senior-revenue-accountant), internal BI SQL
  (bi-analyst), or technical architecture (senior-system-architecture).
---

# Business Model Researcher

## When to Use

- Map or critique a business model (canvas, lean canvas, value proposition)
- Research competitor revenue models, pricing, and packaging
- Estimate TAM/SAM/SOM with stated assumptions
- Model unit economics and sensitivity (CAC, LTV, margins, payback)
- Compare monetization options (subscription, usage, marketplace, ads)
- Synthesize public sources into a cited business-model brief

## When NOT to Use

- BRDs, user stories, process maps → `business-analyst`
- Issue trees, operating model, steerCo recommendation → `business-consultant`
- ASC 606, close, contract accounting → `senior-revenue-accountant`
- Warehouse metrics and dashboards → `bi-analyst`
- Long-form API docs or runbooks → `tech-writer-researcher`
- UX journeys and wireframes → `product-designer`
- Deal desk CPQ and order forms → `deal-operations-administrator`
- Monetization PRDs, paywalls, billing product requirements → `product-management-monetization`

## Related skills

| Need | Skill |
|---|---|
| Executive business case and roadmap | `business-consultant` |
| Build requirements from validated model | `business-analyst` |
| Research writing polish | `tech-writer-researcher` |
| Product discovery UX | `product-designer` |
| Pitch narrative (if deck-focused) | `business-consultant` references |

## Core Workflows

### 1. Define the research question

State explicitly:

- **Subject** — company, product line, or greenfield idea
- **Decision** — invest, pivot pricing, enter segment, fundraise narrative
- **Audience** — founder, product, investors, board
- **Depth** — snapshot (2–4h) vs diligence (multi-day)
- **Sources allowed** — public only vs internal data

List unknowns as hypotheses to validate or kill.

### 2. Map the current or proposed model

Fill canvas blocks with **evidence tags** `[source]` per claim:

| Block | Research focus |
|---|---|
| Customer segments | Who pays vs who uses; ICP |
| Value proposition | Job, pain, gain; differentiation |
| Channels | Acquisition and delivery |
| Relationships | Self-serve vs enterprise vs community |
| Revenue streams | Pricing model and packaging |
| Key resources / activities / partners | What enables the model |
| Cost structure | Fixed vs variable; COGS vs OpEx |

**See `references/canvas_frameworks.md`.**

### 3. Size the market (when needed)

Use **top-down** and **bottom-up**; reconcile or explain gap.

Document every assumption (penetration, ARPU, growth rate).

**See `references/market_sizing.md`.**

### 4. Unit economics

Build a simple model:

- Revenue per customer or unit
- Variable cost per unit (COGS, infra, support allocation)
- CAC and payback period
- LTV (state churn and gross margin assumptions)

Run sensitivity on churn, CAC, and price.

**See `references/unit_economics.md`.**

### 5. Competitive benchmarking

Compare 3–7 peers on:

| Dimension | Notes |
|---|---|
| Primary revenue model | Sub, usage, take rate, hybrid |
| Pricing tiers | Entry price, enterprise motion |
| GTM motion | PLG, sales-led, channel |
| Unit economics signals | Public filings, interviews, estimates |

Label **fact** vs **estimate** vs **unknown**.

**See `references/competitive_benchmarking.md`.**

### 6. Revenue model options (greenfield or pivot)

Shortlist 2–3 monetization patterns; score fit to segment and delivery cost.

**See `references/revenue_models.md`.**

### 7. Deliverable

Standard output structure:

```markdown
## Executive summary (≤ 10 bullets)
## Business model map (canvas table)
## Market size (if applicable) — assumptions table
## Unit economics — base case + sensitivity
## Competitive comparison table
## Risks and open questions
## Sources
```

Hand strategic recommendation and investment case to `business-consultant` when exec decision is next.

## When to load references

- **Canvas / VPC / lean** → `references/canvas_frameworks.md`
- **TAM SAM SOM** → `references/market_sizing.md`
- **CAC, LTV, payback** → `references/unit_economics.md`
- **Sub, marketplace, usage** → `references/revenue_models.md`
- **Peer comparison** → `references/competitive_benchmarking.md`
