# Stories and Visual QA

## Storybook (or equivalent)

Each reusable component:

| Story | Purpose |
|---|---|
| Default | Baseline |
| Variants | primary / secondary / ghost |
| Sizes | sm / md / lg |
| States | disabled, loading |
| Edge | long text, many items |

Name stories to match design spec terms.

## PR checklist

- [ ] Storybook updated for changed components
- [ ] Screenshots: before/after for visual change
- [ ] Responsive: mobile + desktop capture
- [ ] States: error/empty if applicable
- [ ] No console errors in story and page
- [ ] Token compliance (no stray hex)

## Visual compare

| Method | Use |
|---|---|
| Figma side-by-side | Layout and spacing |
| Design review tag | `@design` in PR if org requires |
| Percy/Chromatic | If team has visual CI |

Log **known deltas** (font rendering, browser) in PR description.

## Regression

- Do not change shared component without checking **consumers**
- Run smoke on critical flows if touching layout shell

## Scope boundary

- E2E test authoring → QA or fullstack preference
- Unit test logic → team standard; UI engineer adds interaction tests when required
