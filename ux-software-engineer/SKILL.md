---
name: ux-software-engineer
description: |
  Guides UX software engineering—translating user flows into interaction specs and coded prototypes,
  heuristic UX reviews, information architecture in product, micro-interactions, usability fixes
  in the UI layer, and design-engineering handoff. Bridges discovery output and production UI.
  Use when prototyping flows in code, specifying interaction behavior for engineering, auditing UX
  in a live or staging app, fixing confusing flows, or defining states/edge cases for builders—not
  for research-only discovery (product-designer), pixel-perfect production implementation from
  final Figma (ui-software-engineer), senior FE performance/architecture
  (senior-frontend-software-engineer), or BRDs (business-analyst).
---

# UX Software Engineer

## When to Use

- Turn **user journeys** into flow diagrams and interaction specs
- Build **clickable or coded prototypes** to validate flows before production
- Run **heuristic UX audits** on existing product and prioritize fixes
- Define **interaction details**: validation timing, focus, undo, confirmations
- Improve **IA**: navigation, labeling, grouping, empty paths
- Write **UX acceptance criteria** for `ui-software-engineer` or fullstack
- Partner on **usability tests** (tasks, success metrics, synthesis to tickets)
- Refine **microcopy** in UI (labels, errors, empty states) with product voice

## When NOT to Use

- Greenfield discovery, wireframes without build intent → `product-designer`
- Final visual implementation and token-perfect screens → `ui-software-engineer`
- Core Web Vitals, bundle, RSC architecture → `senior-frontend-software-engineer`
- Formal requirements and process maps → `business-analyst`
- Marketing site copy → `tech-writer-researcher`

## Related skills

| Need | Skill |
|---|---|
| Product design and wireframes | `product-designer` |
| Production UI from specs | `ui-software-engineer` |
| Senior FE and a11y depth | `senior-frontend-software-engineer` |
| End-to-end feature delivery | `fullstack-software-engineer` |

## Core Workflows

### 1. Flows and interaction specs

Journey → screens → transitions → states.

**See `references/flows_interaction_specs.md`.**

### 2. Prototypes in code

When to prototype; fidelity levels; validation loops.

**See `references/prototypes_in_code.md`.**

### 3. Heuristic evaluation

Nielsen-style pass; severity; fix tickets.

**See `references/heuristic_evaluation.md`.**

### 4. Information architecture

Nav, taxonomy, findability in product.

**See `references/information_architecture.md`.**

### 5. UX handoff to engineering

Acceptance criteria, edge cases, open questions.

**See `references/ux_engineering_handoff.md`.**

### 6. Microcopy and content UX

Labels, errors, empty states, tone.

**See `references/microcopy_content_ux.md`.**

## Output standards

- Every flow documents **entry, success, error, and exit**
- Prototypes link to **test tasks** and assumptions
- Audit findings ranked **severity + effort**
- Handoff lists **interaction rules**, not only screenshots
- Escalate visual brand decisions to `product-designer`

## When to load references

- **Flows** → `references/flows_interaction_specs.md`
- **Prototypes** → `references/prototypes_in_code.md`
- **Heuristics** → `references/heuristic_evaluation.md`
- **IA** → `references/information_architecture.md`
- **Handoff** → `references/ux_engineering_handoff.md`
- **Copy** → `references/microcopy_content_ux.md`
