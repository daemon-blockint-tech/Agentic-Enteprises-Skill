---
name: talent-sourcer
description: |
  This skill should be used when the user asks to talent sourcer, source candidates, define a
  sourcing strategy, run boolean search or X-ray search, conduct LinkedIn sourcing, find passive
  candidates, build a talent map or talent pool, build a recruiting pipeline, draft recruiting
  outreach, produce a candidate list, or follow a sourcer playbook for proactive recruiting.
  Guides role intake and search strategy, platform sourcing (LinkedIn, GitHub, communities),
  talent mapping and market scans, personalized outreach at scale, pipeline hygiene and CRM notes,
  diversity sourcing, competitor talent pool analysis, and handoff to recruiters—not interview loop
  design (interview-prep, interview-system-designer), offer letters (draft-offer), comp bands
  (comp-analysis), HR policy or employee relations (hr-business-partner), generic B2B prospecting
  (lead-researcher, account-research, enrich-lead unless explicitly recruiting), employer branding
  campaigns (cmo-advisor), or end-to-end recruiting ops (talent-acquisition).
---

# Talent Sourcer

## When to Use

- Intake a requisition and translate it into **search strategy**, channels, and boolean strings
- Run **boolean**, **X-ray**, and platform-native searches (LinkedIn, GitHub, communities)
- Build a **talent map**, market scan, or **talent pool** for a role or company
- Identify and qualify **passive candidates** with evidence-backed fit notes
- Draft **recruiting outreach** and multi-touch engagement sequences at scale
- Maintain **pipeline hygiene**—CRM stages, notes, tags, and duplicate handling
- Apply **diversity sourcing** considerations without tokenism or biased filters
- Analyze **competitor** and target-company talent pools for mapping and poachability
- Prepare **handoff packages** for recruiters and hiring managers with clear next steps

## When NOT to Use

- Design interview loops, scorecards, or calibration → `interview-system-designer`, `interview-prep`
- Draft offer letters or total comp packages → `draft-offer`, `comp-analysis`
- HR policy, ER cases, workforce planning, or org design → `hr-business-partner`
- Generic B2B sales prospecting or account research → `lead-researcher`, `account-research`, `enrich-lead` (unless explicitly recruiting)
- Sales call prep for non-hiring conversations → `call-prep`
- Full recruiting program design, employer brand campaigns, or TA strategy → `talent-acquisition`, `cmo-advisor`
- Track reqs across hiring stages without sourcing work → `recruiting-pipeline` (coordination only)

## Related skills

| Need | Skill |
|---|---|
| Recruiting strategy, employer brand, hiring funnel design | `talent-acquisition` |
| Pipeline stages, req tracking, hiring status | `recruiting-pipeline` |
| Interview plans, questions, scorecards | `interview-prep`, `interview-system-designer` |
| HR programs, policy, workforce planning | `hr-business-partner` |
| B2B account or contact research (non-recruiting) | `lead-researcher`, `account-research` |
| Contact enrichment for outreach lists | `enrich-lead` |
| Compensation benchmarking and bands | `comp-analysis` |
| Sales or customer meeting prep | `call-prep` |

## Core Workflows

### 1. Role intake and search strategy

1. Confirm must-haves vs nice-to-haves, level, location, work model, and comp band (directional only)
2. Define **ideal candidate profile** (ICP): titles, skills, companies, tenure patterns, exclusions
3. Choose primary channels and backup channels by persona (e.g., IC eng → GitHub + LinkedIn)
4. Set weekly sourcing targets and quality bar for handoff
5. Document **search strings** and platform-specific filters in a reusable playbook block

**See `references/role_intake_and_search_strategy.md`.**

### 2. Sourcing execution

1. Run boolean / X-ray searches per channel; log variants and result quality
2. Screen profiles against ICP; tag **fit tier** (A/B/C) with one-line rationale
3. De-duplicate against CRM and prior outreach; respect do-not-contact lists
4. Capture **evidence** (profile URL, snippet, project link) for each qualified lead
5. Batch-add to pipeline with consistent field mapping

**See `references/sourcing_channels_and_boolean_search.md`.**

### 3. Talent mapping and market research

1. Map target companies, teams, and alumni flows for the role family
2. Estimate pool size and competition (open roles, funding, layoffs)
3. Identify warm paths: referrals, communities, conference speakers, OSS maintainers
4. Produce a **talent map** artifact: segments, names (where appropriate), and gaps
5. Refresh map on cadence aligned to req urgency

**See `references/talent_mapping_and_market_research.md`.**

### 4. Outreach and engagement

1. Personalize first touch from **public** signals (talks, repos, posts)—no creepy inference
2. Sequence follow-ups with channel-appropriate spacing; stop on opt-out
3. A/B test subject lines and hooks where volume warrants it
4. Track reply rate, interested rate, and conversion to screen
5. Escalate warm leads to recruiter with context package

**See `references/outreach_and_engagement_sequences.md`.**

### 5. Pipeline hygiene and handoff

1. Enforce stage definitions: sourced → contacted → replied → interested → handed off
2. Write CRM notes that answer: why fit, risk flags, outreach history, next action
3. Hand off A-tier candidates with profile summary and suggested pitch to HM
4. Report sourcing metrics weekly; flag blockers (low pool, low reply, bad JD)

**See `references/pipeline_handoff_and_sourcing_metrics.md`.**

## When to load references

- **Scope and boundaries** → `references/talent_sourcer_scope.md`
- **Intake and strategy** → `references/role_intake_and_search_strategy.md`
- **Channels and boolean** → `references/sourcing_channels_and_boolean_search.md`
- **Mapping and market** → `references/talent_mapping_and_market_research.md`
- **Outreach** → `references/outreach_and_engagement_sequences.md`
- **Handoff and metrics** → `references/pipeline_handoff_and_sourcing_metrics.md`
