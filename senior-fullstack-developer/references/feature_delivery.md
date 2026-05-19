# Feature delivery

## Table of contents

1. [Vertical slice checklist](#vertical-slice-checklist)
2. [PR description template](#pr-description-template)

## Vertical slice checklist

- [ ] Acceptance criteria met
- [ ] API contract documented or OpenAPI updated
- [ ] Authz on all new routes
- [ ] UI states: loading, empty, error
- [ ] Tests for happy path + main failure
- [ ] Feature flag if gradual rollout
- [ ] Rollback steps in PR or release notes

## PR description template

```markdown
## What
## Why
## How to test
## Risks / rollback
## Screenshots (if UI)
```
