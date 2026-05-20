# Misleading visualization and ethics

## Table of contents

1. [Principles](#principles)
2. [Pre-publish checklist](#pre-publish-checklist)
3. [Truncated and manipulated axes](#truncated-and-manipulated-axes)
4. [Dual axes and indexing](#dual-axes-and-indexing)
5. [Cherry-picking and survivorship](#cherry-picking-and-survivorship)
6. [Aggregation traps](#aggregation-traps)
7. [Uncertainty and significance](#uncertainty-and-significance)
8. [Review workflow](#review-workflow)

## Principles

1. **Show the data** the audience needs for the stated decision—no more, no less
2. **Do not distort** perception through scale, cropping, or encoding tricks
3. **Disclose** filters, exclusions, transformations, and uncertainty
4. **Separate** exploration drafts from certified external views
5. **Escalate** when pressure requests cosmetic exaggeration—document and refuse

This is ethical communication guidance, not legal advice.

## Pre-publish checklist

- [ ] Title matches what the data actually shows
- [ ] Axis baselines and units correct; log/discontinuities labeled
- [ ] Comparisons use consistent definitions and periods
- [ ] Denominators shown for rates; exposure changes visible
- [ ] Outliers and one-time events called out
- [ ] Color does not imply unsubstantiated good/bad
- [ ] Sample size and suppression documented
- [ ] Source and as-of date on the visual
- [ ] No hidden filters or post-hoc segment cuts without disclosure

## Truncated and manipulated axes

| Issue | Risk | Fix |
|---|---|---|
| Y-axis not at zero on bars | Exaggerates delta | Start at zero or use slope/index chart |
| Broken axis | Hides continuity | Inset with clear break symbol + label |
| Cherry-picked y-range on lines | Drama | Show full range or add context panel |
| 3D effects | Area misread | Use 2D |

If truncation is required for readability, **flag prominently** in title or footnote.

## Dual axes and indexing

**Dual y-axis** (two scales): invites viewers to infer correlation between unrelated series.

Prefer:

- **Two panels** stacked with shared x-axis
- **Indexed lines** (rebase to 100 at start) with one y-axis
- **Scatter** if relationship is the claim

If dual axis is mandated by template:

- Label both scales clearly
- Do not imply causation in title
- Add correlation disclaimer in footnote

## Cherry-picking and survivorship

| Tactic | Detection | Response |
|---|---|---|
| Convenient date range | Compare to full history | Extend window or show inset |
| Excluded bad months | Read filter spec | List exclusions |
| Survivorship (only winners) | Check cohort entry | Show full cohort or label bias |
| Metric switching | Track definition versions | One primary metric per story |

Document **why** any subset was chosen.

## Aggregation traps

| Trap | Example | Mitigation |
|---|---|---|
| Simpson's paradox | Rate rises overall, falls in every segment | Show segments |
| Unequal weights | Avg of ratios ≠ ratio of sums | Use proper weighted aggregate |
| Geographic aggregation | Mix high/low exposure regions | Normalize by exposure |
| Calendar effects | 28- vs 31-day months | Use same-day compare or YoY |

Pair with `data-scientist` when statistical validity is in question.

## Uncertainty and significance

- Show **intervals** or **scenario bands** when estimates are noisy
- Avoid implying precision beyond measurement (four decimals on volatile KPIs)
- Do not use **chart icons** or **icons only** for material deltas
- For experiments, route design to `data-scientist`; viz shows CI, not just uplift arrow

## Review workflow

1. **Author** completes checklist above
2. **Peer** (analyst or actuary) verifies definitions and filters
3. **Stakeholder** sign-off for external/board packs
4. **Archive** spec + data snapshot ID with published chart

When asked to "make it look better" by distorting scale:

- Propose honest alternatives (context line, indexed view, annotation)
- Record request and response in ticket or memo
- Route narrative pressure to `storytelling` without bending axes
