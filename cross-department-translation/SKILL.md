---
name: Cross-Department Translation
description: |
  Reframes messages, requirements, metrics, and decisions for organizational audiences—engineering,
  product, finance, legal, compliance, sales, operations, actuarial, and executive—by detecting jargon,
  surfacing implicit assumptions, producing dual-audience briefs, RACI-aligned handoffs, owner-tagged
  meeting actions, technical-to-business and business-to-technical translation, and escalation summaries.
  Use when translating for engineering, explaining to finance, cross-department bridging, rewriting for
  executives, business-friendly versions, technical summaries for leadership, inter-team handoffs,
  department jargon, or dual-audience briefs—not external customer or brand copy (communication-lead),
  contract redlines (commercial-counsel), full multi-team program execution (technical-program-manager),
  human-language i18n/l10n product strings, or strategy-only consulting without audience reframing
  (business-consultant).
---

# Cross-Department Translation

## When to Use

- Reframe a message, spec, metric, or decision for a different internal audience
- Produce **dual-audience** briefs (e.g., engineering detail + executive summary on one page)
- Decode department jargon and unstated assumptions before handoff
- Convert meeting notes into **action items by owner** with RACI clarity
- Translate technical specs, incidents, or architecture for business stakeholders
- Translate business constraints, policy, or financial limits for engineering implementation
- Draft escalation summaries that each function can act on without re-interpretation
- Align vocabulary across product, finance, legal, compliance, sales, ops, and actuarial threads

## When NOT to Use

- Company-wide messaging strategy, launches, crisis **wording**, or brand voice → `communication-lead`
- Issue trees, business cases, operating models, or steerCo **analysis** without audience reframing → `business-consultant`
- Multi-team milestones, RAID ownership, dependency maps, launch **program** governance → `technical-program-manager`
- Contract, DPA, or legal **redlines** and negotiation positions → `commercial-counsel`
- Control mapping, audit evidence pipelines, or attestation **engineering** → `compliance-engineer`
- Actuarial engagement SOW, reserve opinions, or regulatory actuarial **deliverables** → `actuarial-consulting`
- Natural-language product localization (locale strings, RTL, cultural adaptation) → route to localization/l10n skills if present
- Deep technical modeling execution (pricing triangles, IBNR) → `actuary`

## Related skills

| Need | Skill |
|---|---|
| Org-wide narrative, launches, crisis message packs | `communication-lead` |
| Strategy, business case, issue trees, operating model | `business-consultant` |
| Program plan, RAID, milestones, cross-team delivery | `technical-program-manager` |
| Requirements, BRDs, process maps for build teams | `business-analyst` |
| UX scope and product journeys | `product-designer` |
| Technical controls and audit evidence | `compliance-engineer` |
| Actuarial engagement framing and stakeholder packs | `actuarial-consulting` |
| System architecture and ADRs | `senior-system-architecture` |
| Commercial terms in handoff documents | `commercial-counsel` |

## Core Workflows

### 1. Identify source and target audiences

1. **Source** — who wrote this; what they assume the reader knows
2. **Target** — who must understand, decide, or execute
3. **Decision or ask** — one sentence: what changes if they get it right
4. **Sensitivity** — legal, regulatory, financial materiality, security, personnel

Load `references/audience_profiles_and_register.md` for register, depth, and vocabulary norms.

### 2. Jargon and assumption pass

Before rewriting:

1. Highlight terms that are **department-local** or overloaded (e.g., "platform," "risk," "material")
2. List **implicit assumptions** (data exists, approval granted, timeline fixed)
3. Flag **ambiguous metrics** (gross vs net, ARR vs revenue, calendar vs fiscal)
4. Build a mini-glossary only for terms that appear in the artifact

**See `references/jargon_decoding_and_glossary.md`.**

### 3. Requirements and decision briefs

| Input | Typical outputs |
|---|---|
| Engineering spec / RFC | Business summary: outcome, constraints, timeline, cost/risk |
| Business policy / OKR | Engineering brief: acceptance criteria, non-goals, dependencies |
| Finance ask | Product/engineering impact: effort bands, trade-offs, measurement |
| Legal/compliance constraint | Implementation checklist: must/must-not, evidence needed |

Use pyramid structure for executives; appendices for specialists.

**See `references/requirements_and_decision_briefs.md`.**

### 4. Meeting notes and handoffs

1. Capture **decisions** (what was decided, not discussed)
2. Extract **actions** with one owner, due date, and definition of done
3. Separate **FYI** from **needs response**
4. Add **RACI** when multiple teams share work
5. Include **open questions** with who resolves them

**See `references/meeting_notes_and_handoffs.md`.**

### 5. Escalation and executive summaries

Escalations need: situation, impact, options, recommendation, asks by role, and what **not** to do yet.

Keep exec sections to one screen; link detail for operators.

**See `references/executive_and_escalation_summaries.md`.**

## Output standards

- Lead with **decision or ask** for executive readers; lead with **context and constraints** for implementers
- Define acronyms once; prefer plain language over metaphor
- Separate **facts**, **assumptions**, and **recommendations**
- Preserve numeric precision; never round material figures without stating basis
- Tag sections when dual-audience: `## Executive`, `## Engineering`, `## Finance`, etc.
- Flag `[LEGAL REVIEW]`, `[COMPLIANCE]`, `[FINANCE SIGN-OFF]` when content touches those domains

## When to load references

| Topic | Reference |
|---|---|
| Scope, boundaries, translation vs other skills | `references/cross_department_translation_scope.md` |
| Audience profiles, register, depth | `references/audience_profiles_and_register.md` |
| Jargon, glossaries, assumption surfacing | `references/jargon_decoding_and_glossary.md` |
| Specs, decisions, dual-audience briefs | `references/requirements_and_decision_briefs.md` |
| Notes, actions, RACI handoffs | `references/meeting_notes_and_handoffs.md` |
| Exec summaries and escalations | `references/executive_and_escalation_summaries.md` |
