# Design principles and accessibility

## Table of contents

1. [Visual hierarchy](#visual-hierarchy)
2. [Axes, scales, and units](#axes-scales-and-units)
3. [Color](#color)
4. [Typography and labels](#typography-and-labels)
5. [Small multiples](#small-multiples)
6. [Accessibility checklist](#accessibility-checklist)
7. [Alt text and long descriptions](#alt-text-and-long-descriptions)
8. [Export and print](#export-and-print)

## Visual hierarchy

1. **Most important** metric or chart top-left (LTR layouts)
2. Use **size** and **weight** before extra color
3. Limit dashboard to **5–7** primary elements per screen
4. De-emphasize gridlines and borders; emphasize data ink
5. One **accent color** for the story metric; neutrals elsewhere

## Axes, scales, and units

| Rule | Application |
|---|---|
| Label units | %, USD, claims count, per 1,000 exposure |
| Zero baseline | Bar charts comparing magnitude; not required for all line contexts if disclosed |
| Tick density | ~5–7 ticks; avoid label overlap |
| Log scale | Label explicitly; explain why |
| Dual axis | Avoid; see `misleading_viz_and_ethics.md` |
| Rounding | Match audience (exec: fewer digits; ops: more precision) |

Annotate **events** (launch, rate change, storm) sparingly on time series.

## Color

### Semantic use

| Role | Guidance |
|---|---|
| Positive / negative | Green/red only if culturally appropriate; add +/- labels |
| Categories | Distinct hues; max ~8 before grouping "Other" |
| Sequential | Light → dark for magnitude |
| Diverging | Center at meaningful midpoint (0, target, median) |

### Colorblind-safe palettes

Prefer:

- **Okabe–Ito** or **ColorBrewer** qualitative sets
- Test with deuteranopia/protanopia simulators
- Redundant encoding: shape, pattern, labels, position

Avoid:

- Rainbow scales for continuous data
- Red-green only pair for critical distinction

### Contrast

- Text on background: target **WCAG AA** (4.5:1 body, 3:1 large text)
- Chart lines thick enough for projection rooms (≥2px at slide scale)

## Typography and labels

- **Titles** state insight: "Loss ratio rose 3pt YoY driven by CAT" not "Loss ratio chart"
- **Subtitles** carry definition or filter: "US P&C, accident year 2024, ex reserve releases"
- **Direct labels** on final series when ≤4 lines; legend only when necessary
- **Footnotes**: source, refresh, suppression, FX basis
- Avoid rotated axis labels when horizontal bar or transpose fixes readability

## Small multiples

Use when:

- Same chart type, same scale, different segments (region, LOB, product)
- Comparing shape of distribution or trend across groups

Rules:

- Shared axes across panels when comparison is goal
- Consistent ordering of categories in every panel
- Panel titles = segment name; super-title = overall message

## Accessibility checklist

- [ ] Color is not the only differentiator (shape, label, pattern)
- [ ] Palette checked for colorblind safety
- [ ] Contrast sufficient for text, lines, and UI controls
- [ ] Interactive tooltips have keyboard path or static fallback
- [ ] Motion/autoplay disabled or user-controlled
- [ ] Alt text or long description provided for static images
- [ ] Data table available for screen-reader users when feasible

## Alt text and long descriptions

**Alt text** (short): chart type + main trend + key number.

Example: "Line chart: monthly active users rose from 1.2M to 1.8M Jan–Dec 2025."

**Long description** (report appendix): axes, filters, outliers, and caveats in prose.

For dashboards, link to **accessible table export** or documented filter state.

## Export and print

- Slide exports: minimum font **18–24pt** for axis labels at 16:9
- Print: test grayscale legibility
- Embed fonts or outline text when brand requires
- Include **as-of** timestamp on operational PDFs
