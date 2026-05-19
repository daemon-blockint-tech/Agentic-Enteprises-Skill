# Front-end code review

## Table of contents

1. [Review rubric](#review-rubric)
2. [Severity guide](#severity-guide)

## Review rubric

| Area | Questions |
|---|---|
| Correctness | All states handled? Race on fast navigation? |
| A11y | Keyboard, labels, contrast, semantics? |
| Performance | New client bundle? Waterfall fetches? |
| Maintainability | Clear component API? Duplication? |
| Security | XSS from `dangerouslySetInnerHTML`? Secrets in client bundle? |
| Tests | Behavior covered for changed UX? |

## Severity guide

| Level | Example |
|---|---|
| Block | Missing auth on sensitive UI action exposed client-side only |
| Major | No keyboard access to modal; LCP regression >20% |
| Minor | Naming, optional a11y polish |
| Nit | Style preference with no functional impact |
