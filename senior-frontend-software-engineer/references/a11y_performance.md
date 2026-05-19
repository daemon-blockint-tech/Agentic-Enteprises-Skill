# Accessibility and performance

## Table of contents

1. [A11y checklist](#a11y-checklist)
2. [Core Web Vitals](#core-web-vitals)

## A11y checklist

- [ ] Heading hierarchy logical
- [ ] Interactive elements keyboard reachable
- [ ] Focus visible; no focus trap without escape
- [ ] Form inputs have associated labels
- [ ] Color contrast AA for text and controls
- [ ] Images have alt text (decorative: alt="")
- [ ] Live regions for toasts/async status when needed

## Core Web Vitals

| Metric | Tactics |
|---|---|
| LCP | Priority image, server render hero, reduce TTFB |
| INP | Defer heavy JS, split handlers, virtualize long lists |
| CLS | Width/height on images, reserve ad/banner space |

Run Lighthouse on representative pages before claiming done.
